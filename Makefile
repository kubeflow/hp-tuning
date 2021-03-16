HAS_LINT := $(shell command -v golint;)
COMMIT := $(shell git rev-parse --short=7 HEAD)

# Run tests
.PHONY: test
test:
	go test ./pkg/... ./cmd/... -coverprofile coverage.out

check: generate fmt vet lint

fmt:
	hack/verify-gofmt.sh

lint:
ifndef HAS_LINT
	go get -u golang.org/x/lint/golint
	echo "installing golint"
endif
	hack/verify-golint.sh

vet:
	go vet ./pkg/... ./cmd/...

update:
	hack/update-gofmt.sh

# Deploy Katib v1beta1 manifests using Kustomize into a k8s cluster.
deploy:
	bash scripts/v1beta1/deploy.sh

# Undeploy Katib v1beta1 manifests using Kustomize from a k8s cluster
undeploy:
	bash scripts/v1beta1/undeploy.sh

# Generate deepcopy, clientset, listers, informers, open-api and python SDK for APIs.
# Run this if you update any existing controller APIs.
generate:
ifndef GOPATH
	$(error GOPATH not defined, please define GOPATH. Run "go help gopath" to learn more about GOPATH)
endif
	go generate ./pkg/... ./cmd/...
	hack/gen-python-sdk/gen-sdk.sh

# Build images for the Katib v1beta1 components.
build: generate
ifeq ($(and $(REGISTRY),$(COMMIT_TAG),$(RELEASE_TAG)),)
	$(error REGISTRY, COMMIT_TAG and RELEASE_TAG must be set. Usage: make build REGISTRY=<registry> COMMIT_TAG=<commit-tag> RELEASE_TAG=<release-tag>)
endif
	bash scripts/v1beta1/build.sh $(REGISTRY) $(COMMIT_TAG) $(RELEASE_TAG)

# Build and push Katib images from the latest master commit.
push-latest:
	bash scripts/v1beta1/push.sh docker.io/kubeflowkatib v1beta1-$(COMMIT) latest

# Build and push Katib images for the given tag.
push-tag:
ifeq ($(TAG),)
	$(error TAG must be set. Usage: make push-tag TAG=<release-tag>)
endif
	bash scripts/v1beta1/push.sh docker.io/kubeflowkatib v1beta1-$(COMMIT) $(TAG)

# Release a new version of Katib.
release:
ifeq ($(and $(BRANCH),$(TAG)),)
	$(error BRANCH and TAG must be set. Usage: make release BRANCH=<branch> TAG=<tag>)
endif
	bash scripts/v1beta1/release.sh $(BRANCH) $(TAG)

# Prettier UI format check for Katib v1beta1.
prettier-check:
	npm run format:check --prefix pkg/ui/v1beta1/frontend
