// Code generated by MockGen. DO NOT EDIT.
// Source: github.com/kubeflow/katib/pkg/controller.v1beta1/suggestion/suggestionclient (interfaces: SuggestionClient)

// Package mock is a generated GoMock package.
package mock

import (
	gomock "github.com/golang/mock/gomock"
	v1beta1 "github.com/kubeflow/katib/pkg/apis/controller/experiments/v1beta1"
	v1beta10 "github.com/kubeflow/katib/pkg/apis/controller/suggestions/v1beta1"
	v1beta11 "github.com/kubeflow/katib/pkg/apis/controller/trials/v1beta1"
	reflect "reflect"
)

// MockSuggestionClient is a mock of SuggestionClient interface
type MockSuggestionClient struct {
	ctrl     *gomock.Controller
	recorder *MockSuggestionClientMockRecorder
}

// MockSuggestionClientMockRecorder is the mock recorder for MockSuggestionClient
type MockSuggestionClientMockRecorder struct {
	mock *MockSuggestionClient
}

// NewMockSuggestionClient creates a new mock instance
func NewMockSuggestionClient(ctrl *gomock.Controller) *MockSuggestionClient {
	mock := &MockSuggestionClient{ctrl: ctrl}
	mock.recorder = &MockSuggestionClientMockRecorder{mock}
	return mock
}

// EXPECT returns an object that allows the caller to indicate expected use
func (m *MockSuggestionClient) EXPECT() *MockSuggestionClientMockRecorder {
	return m.recorder
}

// SyncAssignments mocks base method
func (m *MockSuggestionClient) SyncAssignments(arg0 *v1beta10.Suggestion, arg1 *v1beta1.Experiment, arg2 []v1beta11.Trial) error {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "SyncAssignments", arg0, arg1, arg2)
	ret0, _ := ret[0].(error)
	return ret0
}

// SyncAssignments indicates an expected call of SyncAssignments
func (mr *MockSuggestionClientMockRecorder) SyncAssignments(arg0, arg1, arg2 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "SyncAssignments", reflect.TypeOf((*MockSuggestionClient)(nil).SyncAssignments), arg0, arg1, arg2)
}

// ValidateAlgorithmSettings mocks base method
func (m *MockSuggestionClient) ValidateAlgorithmSettings(arg0 *v1beta10.Suggestion, arg1 *v1beta1.Experiment) error {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "ValidateAlgorithmSettings", arg0, arg1)
	ret0, _ := ret[0].(error)
	return ret0
}

// ValidateAlgorithmSettings indicates an expected call of ValidateAlgorithmSettings
func (mr *MockSuggestionClientMockRecorder) ValidateAlgorithmSettings(arg0, arg1 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "ValidateAlgorithmSettings", reflect.TypeOf((*MockSuggestionClient)(nil).ValidateAlgorithmSettings), arg0, arg1)
}