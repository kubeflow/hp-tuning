package manifest

import (
	"bytes"
	"errors"
	"text/template"

	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"

	experimentsv1alpha2 "github.com/kubeflow/katib/pkg/api/operators/apis/experiment/v1alpha2"
	apiv1alpha2 "github.com/kubeflow/katib/pkg/api/v1alpha2"
	"github.com/kubeflow/katib/pkg/util/v1alpha2/katibclient"
	"sigs.k8s.io/controller-runtime/pkg/client"
)

// Producer is the type for manifests producer.
type Producer interface {
	GetRunSpec(e *experimentsv1alpha2.Experiment, experiment, trial, namespace string) (string, error)
	GetRunSpecWithHyperParameters(e *experimentsv1alpha2.Experiment, experiment, trial, namespace string, hps []*apiv1alpha2.ParameterAssignment) (string, error)
}

// General is the default implementation of Producer.
type General struct {
	client *katibclient.KatibClient
}

// New creates a new Producer.
func New() (Producer, error) {
	katibClient, err := katibclient.NewClient(client.Options{})
	if err != nil {
		return nil, err
	}
	return &General{
		client: katibClient,
	}, nil
}

// GetRunSpec get the specification for trial.
func (g *General) GetRunSpec(e *experimentsv1alpha2.Experiment, experiment, trial, namespace string) (string, error) {
	params := trialTemplateParams{
		Experiment: experiment,
		Trial:      trial,
		NameSpace:  namespace,
	}
	return g.getRunSpec(e, params)
}

// GetRunSpecWithHyperParameters get the specification for trial with hyperparameters.
func (g *General) GetRunSpecWithHyperParameters(e *experimentsv1alpha2.Experiment, experiment, trial, namespace string, hps []*apiv1alpha2.ParameterAssignment) (string, error) {
	params := trialTemplateParams{
		Experiment:      experiment,
		Trial:           trial,
		NameSpace:       namespace,
		HyperParameters: hps,
	}
	return g.getRunSpec(e, params)
}

func (g *General) getRunSpec(e *experimentsv1alpha2.Experiment, params trialTemplateParams) (string, error) {
	var buf bytes.Buffer
	trialTemplate, err := g.getTrialTemplate(e)
	if err != nil {
		return "", err
	}
	if err := trialTemplate.Execute(&buf, params); err != nil {
		return "", err
	}
	return buf.String(), nil
}

func (g *General) getTrialTemplate(instance *experimentsv1alpha2.Experiment) (*template.Template, error) {
	var err error
	var tpl *template.Template = nil

	trialTemplate := instance.Spec.TrialTemplate
	if trialTemplate.GoTemplate.RawTemplate != "" {
		tpl, err = template.New("Trial").Parse(trialTemplate.GoTemplate.RawTemplate)
		if err != nil {
			return nil, err
		}
	} else {
		templateSpec := trialTemplate.GoTemplate.TemplateSpec
		configMapNS := templateSpec.ConfigMapNamespace
		configMapName := templateSpec.ConfigMapName
		templatePath := templateSpec.TemplatePath

		configMap, err := g.client.GetConfigMap(configMapName, configMapNS)
		if err != nil {
			return nil, err
		}

		if configMapTemplate, ok := configMap[templatePath]; !ok {
			err = errors.New(string(metav1.StatusReasonNotFound))
			return nil, err
		} else {
			tpl, err = template.New("Trial").Parse(configMapTemplate)
			if err != nil {
				return nil, err
			}
		}
	}

	return tpl, nil
}

type trialTemplateParams struct {
	Experiment      string
	Trial           string
	NameSpace       string
	HyperParameters []*apiv1alpha2.ParameterAssignment
}
