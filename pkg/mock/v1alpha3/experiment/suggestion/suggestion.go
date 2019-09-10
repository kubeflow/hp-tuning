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

// CreateSuggestion mocks base method
func (m *MockSuggestion) CreateSuggestion(arg0 *v1alpha3.Experiment, arg1 int32) error {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "CreateSuggestion", arg0, arg1)
	ret0, _ := ret[0].(error)
	return ret0
}

// CreateSuggestion indicates an expected call of CreateSuggestion
func (mr *MockSuggestionMockRecorder) CreateSuggestion(arg0, arg1 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "CreateSuggestion", reflect.TypeOf((*MockSuggestion)(nil).CreateSuggestion), arg0, arg1)
}

// GetSuggestions mocks base method
func (m *MockSuggestion) GetSuggestions(arg0 *v1alpha30.Suggestion) []v1alpha30.TrialAssignment {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "GetSuggestions", arg0)
	ret0, _ := ret[0].([]v1alpha30.TrialAssignment)
	return ret0
}

// GetSuggestions indicates an expected call of GetSuggestions
func (mr *MockSuggestionMockRecorder) GetSuggestions(arg0 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "GetSuggestions", reflect.TypeOf((*MockSuggestion)(nil).GetSuggestions), arg0)
}

// UpdateSuggestion mocks base method
func (m *MockSuggestion) UpdateSuggestion(arg0 *v1alpha30.Suggestion, arg1 int32) error {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "UpdateSuggestion", arg0, arg1)
	ret0, _ := ret[0].(error)
	return ret0
}

// UpdateSuggestion indicates an expected call of UpdateSuggestion
func (mr *MockSuggestionMockRecorder) UpdateSuggestion(arg0, arg1 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "UpdateSuggestion", reflect.TypeOf((*MockSuggestion)(nil).UpdateSuggestion), arg0, arg1)
}
