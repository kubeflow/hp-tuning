// Code generated by MockGen. DO NOT EDIT.
// Source: github.com/kubeflow/katib/pkg/controller.v1alpha3/experiment/suggestion (interfaces: Suggestion)

// Package mock is a generated GoMock package.
package mock

import (
	gomock "github.com/golang/mock/gomock"
	v1alpha3 "github.com/kubeflow/katib/pkg/apis/controller/experiments/v1alpha3"
	v1alpha30 "github.com/kubeflow/katib/pkg/apis/controller/suggestions/v1alpha3"
	reflect "reflect"
)

// MockSuggestion is a mock of Suggestion interface
type MockSuggestion struct {
	ctrl     *gomock.Controller
	recorder *MockSuggestionMockRecorder
}

// MockSuggestionMockRecorder is the mock recorder for MockSuggestion
type MockSuggestionMockRecorder struct {
	mock *MockSuggestion
}

// NewMockSuggestion creates a new mock instance
func NewMockSuggestion(ctrl *gomock.Controller) *MockSuggestion {
	mock := &MockSuggestion{ctrl: ctrl}
	mock.recorder = &MockSuggestionMockRecorder{mock}
	return mock
}

// EXPECT returns an object that allows the caller to indicate expected use
func (m *MockSuggestion) EXPECT() *MockSuggestionMockRecorder {
	return m.recorder
}

// GetOrCreateSuggestion mocks base method
func (m *MockSuggestion) GetOrCreateSuggestion(arg0 *v1alpha3.Experiment, arg1 int32) (*v1alpha30.Suggestion, error) {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "GetOrCreateSuggestion", arg0, arg1)
	ret0, _ := ret[0].(*v1alpha30.Suggestion)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// GetOrCreateSuggestion indicates an expected call of GetOrCreateSuggestion
func (mr *MockSuggestionMockRecorder) GetOrCreateSuggestion(arg0, arg1 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "GetOrCreateSuggestion", reflect.TypeOf((*MockSuggestion)(nil).GetOrCreateSuggestion), arg0, arg1)
}

// UpdateSuggestion mocks base method
func (m *MockSuggestion) UpdateSuggestion(arg0 *v1alpha30.Suggestion) error {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "UpdateSuggestion", arg0)
	ret0, _ := ret[0].(error)
	return ret0
}

// UpdateSuggestion indicates an expected call of UpdateSuggestion
func (mr *MockSuggestionMockRecorder) UpdateSuggestion(arg0 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "UpdateSuggestion", reflect.TypeOf((*MockSuggestion)(nil).UpdateSuggestion), arg0)
}

// UpdateSuggestionStatus mocks base method
func (m *MockSuggestion) UpdateSuggestionStatus(arg0 *v1alpha30.Suggestion) error {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "UpdateSuggestionStatus", arg0)
	ret0, _ := ret[0].(error)
	return ret0
}

// UpdateSuggestionStatus indicates an expected call of UpdateSuggestionStatus
func (mr *MockSuggestionMockRecorder) UpdateSuggestionStatus(arg0 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "UpdateSuggestionStatus", reflect.TypeOf((*MockSuggestion)(nil).UpdateSuggestionStatus), arg0)
}
