package main

import (
	"context"
	"log"
	"time"

	"github.com/kubeflow/katib/pkg/api"
	"google.golang.org/grpc"
)

const (
	manager = "192.168.99.100:30678"
)

var studyConfig = api.StudyConfig{
	Name:                          "grid-demo",
	Owner:                         "katib",
	OptimizationType:              api.OptimizationType_MAXIMIZE,
	OptimizationGoal:              0.99,
	DefaultSuggestionAlgorithm:    "grid",
	DefaultEarlyStoppingAlgorithm: "medianstopping",
	ObjectiveValueName:            "Validation-accuracy",
	Metrics: []string{
		"accuracy",
	},
	ParameterConfigs: &api.StudyConfig_ParameterConfigs{
		Configs: []*api.ParameterConfig{
			&api.ParameterConfig{
				Name:          "--lr",
				ParameterType: api.ParameterType_DOUBLE,
				Feasible: &api.FeasibleSpace{
					Min: "0.03",
					Max: "0.07",
				},
			},
		},
	},
}

var workerConfig = api.WorkerConfig{
	Image: "mxnet/python",
	Command: []string{
		"python",
		"/mxnet/example/image-classification/train_mnist.py",
		"--batch-size=64",
	},
	Gpu:       0,
	Scheduler: "default-scheduler",
}

var gridConfig = []*api.SuggestionParameter{
	&api.SuggestionParameter{
		Name:  "DefaultGrid",
		Value: "2",
	},
	&api.SuggestionParameter{
		Name:  "--lr",
		Value: "4",
	},
}

func main() {
	conn, err := grpc.Dial(manager, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("could not connect: %v", err)
	}
	defer conn.Close()
	ctx := context.Background()
	c := api.NewManagerClient(conn)
	createStudyreq := &api.CreateStudyRequest{
		StudyConfig: &studyConfig,
	}
	createStudyreply, err := c.CreateStudy(ctx, createStudyreq)
	if err != nil {
		log.Fatalf("StudyConfig Error %v", err)
	}
	studyId := createStudyreply.StudyId
	log.Printf("Study ID %s", studyId)
	getStudyreq := &api.GetStudyRequest{
		StudyId: studyId,
	}
	getStudyReply, err := c.GetStudy(ctx, getStudyreq)
	if err != nil {
		log.Fatalf("GetConfig Error %v", err)
	}
	log.Printf("Study ID %s StudyConf%v", studyId, getStudyReply.StudyConfig)
	setSuggesitonParameterRequest := &api.SetSuggestionParametersRequest{
		StudyId:              studyId,
		SuggestionAlgorithm:  "grid",
		SuggestionParameters: gridConfig,
	}
	setSuggesitonParameterReply, err := c.SetSuggestionParameters(ctx, setSuggesitonParameterRequest)
	if err != nil {
		log.Fatalf("SetConfig Error %v", err)
	}
	log.Printf("Grid Prameter ID %s", setSuggesitonParameterReply.ParamId)
	getGridSuggestRequest := &api.GetSuggestionsRequest{
		StudyId:             studyId,
		SuggestionAlgorithm: "grid",
		RequestNumber:       0,
		//RequestNumber=0 means get all grids.
		ParamId: setSuggesitonParameterReply.ParamId,
	}
	getGridSuggestReply, err := c.GetSuggestions(ctx, getGridSuggestRequest)
	if err != nil {
		log.Fatalf("GetSuggestion Error %v", err)
	}
	log.Println("Get Grid Suggestions:")
	for _, t := range getGridSuggestReply.Trials {
		log.Printf("%v", t)
	}
	workerIds := make([]string, len(getGridSuggestReply.Trials))
	workerParameter := make(map[string][]*api.Parameter)
	for i, t := range getGridSuggestReply.Trials {
		wc := workerConfig
		rtr := &api.RunTrialRequest{
			StudyId:      studyId,
			TrialId:      t.TrialId,
			Runtime:      "kubernetes",
			WorkerConfig: &wc,
		}
		for _, p := range t.ParameterSet {
			rtr.WorkerConfig.Command = append(rtr.WorkerConfig.Command, p.Name)
			rtr.WorkerConfig.Command = append(rtr.WorkerConfig.Command, p.Value)
		}
		workerReply, err := c.RunTrial(ctx, rtr)
		if err != nil {
			log.Fatalf("RunTrial Error %v", err)
		}
		workerIds[i] = workerReply.WorkerId
		workerParameter[workerReply.WorkerId] = t.ParameterSet
		saveModelRequest := &api.SaveModelRequest{
			Model: &api.ModelInfo{
				StudyName:  studyConfig.Name,
				WorkerId:   workerReply.WorkerId,
				Parameters: t.ParameterSet,
				Metrics:    []*api.Metrics{},
				ModelPath:  "pvc:/Path/to/Model",
			},
			DataSet: &api.DataSetInfo{
				Name: "Mnist",
				Path: "/path/to/data",
			},
		}
		_, err = c.SaveModel(ctx, saveModelRequest)
		if err != nil {
			log.Fatalf("SaveModel Error %v", err)
		}
		log.Printf("WorkerID %s start\n", workerReply.WorkerId)
	}
	for true {
		time.Sleep(10 * time.Second)
		getMetricsRequest := &api.GetMetricsRequest{
			StudyId:   studyId,
			WorkerIds: workerIds,
		}
		getMetricsReply, err := c.GetMetrics(ctx, getMetricsRequest)
		if err != nil {
			log.Printf("GetMetErr %v", err)
			continue
		}
		for _, mls := range getMetricsReply.MetricsLogSets {
			if len(mls.MetricsLogs) > 0 {
				log.Printf("WorkerID %s :", mls.WorkerId)
				//Only Metrics can be updated.
				saveModelRequest := &api.SaveModelRequest{
					Model: &api.ModelInfo{
						StudyName: studyConfig.Name,
						WorkerId:  mls.WorkerId,
						Metrics:   []*api.Metrics{},
					},
				}
				for _, ml := range mls.MetricsLogs {
					if len(ml.Values) > 0 {
						log.Printf("\t Metrics Name %s Value %v", ml.Name, ml.Values[len(ml.Values)-1])
						saveModelRequest.Model.Metrics = append(saveModelRequest.Model.Metrics, &api.Metrics{Name: ml.Name, Value: ml.Values[len(ml.Values)-1]})
					}
				}
				_, err = c.SaveModel(ctx, saveModelRequest)
				if err != nil {
					log.Fatalf("SaveModel Error %v", err)
				}
			}
		}
		getWorkerRequest := &api.GetWorkersRequest{StudyId: studyId}
		getWorkerReply, err := c.GetWorkers(ctx, getWorkerRequest)
		if err != nil {
			log.Fatalf("GetWorker Error %v", err)
		}
		completeCount := 0
		for _, w := range getWorkerReply.Workers {
			if w.Status == api.State_COMPLETED {
				completeCount++
			}
		}
		if completeCount == len(getWorkerReply.Workers) {
			log.Printf("All Worker Completed!")
			break
		}
	}
}
