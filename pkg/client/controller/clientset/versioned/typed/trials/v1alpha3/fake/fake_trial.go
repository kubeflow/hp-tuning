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
// Code generated by client-gen. DO NOT EDIT.

package fake

import (
	v1alpha3 "github.com/kubeflow/katib/pkg/apis/controller/trials/v1alpha3"
	v1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	labels "k8s.io/apimachinery/pkg/labels"
	schema "k8s.io/apimachinery/pkg/runtime/schema"
	types "k8s.io/apimachinery/pkg/types"
	watch "k8s.io/apimachinery/pkg/watch"
	testing "k8s.io/client-go/testing"
)

// FakeTrials implements TrialInterface
type FakeTrials struct {
	Fake *FakeTrialV1alpha3
	ns   string
}

var trialsResource = schema.GroupVersionResource{Group: "trial.kubeflow.org", Version: "v1alpha3", Resource: "trials"}

var trialsKind = schema.GroupVersionKind{Group: "trial.kubeflow.org", Version: "v1alpha3", Kind: "Trial"}

// Get takes name of the trial, and returns the corresponding trial object, and an error if there is any.
func (c *FakeTrials) Get(name string, options v1.GetOptions) (result *v1alpha3.Trial, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewGetAction(trialsResource, c.ns, name), &v1alpha3.Trial{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1alpha3.Trial), err
}

// List takes label and field selectors, and returns the list of Trials that match those selectors.
func (c *FakeTrials) List(opts v1.ListOptions) (result *v1alpha3.TrialList, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewListAction(trialsResource, trialsKind, c.ns, opts), &v1alpha3.TrialList{})

	if obj == nil {
		return nil, err
	}

	label, _, _ := testing.ExtractFromListOptions(opts)
	if label == nil {
		label = labels.Everything()
	}
	list := &v1alpha3.TrialList{ListMeta: obj.(*v1alpha3.TrialList).ListMeta}
	for _, item := range obj.(*v1alpha3.TrialList).Items {
		if label.Matches(labels.Set(item.Labels)) {
			list.Items = append(list.Items, item)
		}
	}
	return list, err
}

// Watch returns a watch.Interface that watches the requested trials.
func (c *FakeTrials) Watch(opts v1.ListOptions) (watch.Interface, error) {
	return c.Fake.
		InvokesWatch(testing.NewWatchAction(trialsResource, c.ns, opts))

}

// Create takes the representation of a trial and creates it.  Returns the server's representation of the trial, and an error, if there is any.
func (c *FakeTrials) Create(trial *v1alpha3.Trial) (result *v1alpha3.Trial, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewCreateAction(trialsResource, c.ns, trial), &v1alpha3.Trial{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1alpha3.Trial), err
}

// Update takes the representation of a trial and updates it. Returns the server's representation of the trial, and an error, if there is any.
func (c *FakeTrials) Update(trial *v1alpha3.Trial) (result *v1alpha3.Trial, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewUpdateAction(trialsResource, c.ns, trial), &v1alpha3.Trial{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1alpha3.Trial), err
}

// UpdateStatus was generated because the type contains a Status member.
// Add a +genclient:noStatus comment above the type to avoid generating UpdateStatus().
func (c *FakeTrials) UpdateStatus(trial *v1alpha3.Trial) (*v1alpha3.Trial, error) {
	obj, err := c.Fake.
		Invokes(testing.NewUpdateSubresourceAction(trialsResource, "status", c.ns, trial), &v1alpha3.Trial{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1alpha3.Trial), err
}

// Delete takes name of the trial and deletes it. Returns an error if one occurs.
func (c *FakeTrials) Delete(name string, options *v1.DeleteOptions) error {
	_, err := c.Fake.
		Invokes(testing.NewDeleteAction(trialsResource, c.ns, name), &v1alpha3.Trial{})

	return err
}

// DeleteCollection deletes a collection of objects.
func (c *FakeTrials) DeleteCollection(options *v1.DeleteOptions, listOptions v1.ListOptions) error {
	action := testing.NewDeleteCollectionAction(trialsResource, c.ns, listOptions)

	_, err := c.Fake.Invokes(action, &v1alpha3.TrialList{})
	return err
}

// Patch applies the patch and returns the patched trial.
func (c *FakeTrials) Patch(name string, pt types.PatchType, data []byte, subresources ...string) (result *v1alpha3.Trial, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewPatchSubresourceAction(trialsResource, c.ns, name, data, subresources...), &v1alpha3.Trial{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1alpha3.Trial), err
}
