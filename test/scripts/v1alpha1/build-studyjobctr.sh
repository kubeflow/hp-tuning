#!/bin/bash

# Copyright 2018 The Kubeflow Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This shell script is used to build an image from our argo workflow

set -o errexit
set -o nounset
set -o pipefail

export PATH=${GOPATH}/bin:/usr/local/go/bin:${PATH}
REGISTRY="${GCP_REGISTRY}"
PROJECT="${GCP_PROJECT}"
GO_DIR=${GOPATH}/src/github.com/${REPO_OWNER}/${REPO_NAME}-studyjob-controller
VERSION=$(git describe --tags --always --dirty)

echo "Activating service-account"
gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

echo "Copy source to GOPATH"
mkdir -p ${GO_DIR}
cp -r cmd ${GO_DIR}/cmd
cp -r pkg ${GO_DIR}/pkg
cp -r vendor ${GO_DIR}/vendor

cd ${GO_DIR}
cp cmd/katib-controller/v1alpha1/Dockerfile .
gcloud builds submit . --tag=${REGISTRY}/${REPO_NAME}/v1alpha1/studyjob-controller:${VERSION} --project=${PROJECT}
gcloud container images add-tag --quiet ${REGISTRY}/${REPO_NAME}/v1alpha1/studyjob-controller:${VERSION} ${REGISTRY}/${REPO_NAME}/studyjob-controller:latest --verbosity=info

cd ${GO_DIR}
cp cmd/metricscollector/v1alpha1/Dockerfile .
gcloud builds submit . --tag=${REGISTRY}/${REPO_NAME}/v1alpha1/metrics-collector:${VERSION} --project=${PROJECT}
gcloud container images add-tag --quiet ${REGISTRY}/${REPO_NAME}/v1alpha1/metrics-collector:${VERSION} ${REGISTRY}/${REPO_NAME}/metrics-collector:latest --verbosity=info

cd ${GO_DIR}
cp cmd/tfevent-metricscollector/v1alpha1/Dockerfile .
gcloud builds submit . --tag=${REGISTRY}/${REPO_NAME}/v1alpha1/tfevent-metrics-collector:${VERSION} --project=${PROJECT}
gcloud container images add-tag --quiet ${REGISTRY}/${REPO_NAME}/v1alpha1/tfevent-metrics-collector:${VERSION} ${REGISTRY}/${REPO_NAME}/tfevent-metrics-collector:latest --verbosity=info
