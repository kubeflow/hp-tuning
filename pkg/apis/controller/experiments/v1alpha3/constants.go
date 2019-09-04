/*
Copyright 2019 The Kubernetes Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
package v1alpha3

const (
	// Default value of Spec.ParallelTrialCount
	DefaultTrialParallelCount = 3

	// Default value of Spec.ConfigMapName for Trial template
	DefaultTrialConfigMapName = "trial-template"

	// Default env name of katib namespace
	DefaultKatibNamespaceEnvName = "KATIB_CORE_NAMESPACE"

	// Default value of Spec.TemplatePath
	DefaultTrialTemplatePath = "defaultTrialTemplate.yaml"

	// Default value of Spec.ConfigMapName for Metrics Collector template
	DefaultMetricsCollectorConfigMapName = "metrics-collector-template"

	// Configmap name which includes Katib's configuration
	KatibConfigMapName = "katib-config"
)
