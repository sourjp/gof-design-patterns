package singleton

import (
	"reflect"
	"testing"
)

func TestSingleton(t *testing.T) {
	s1 := GetInstance()
	s2 := GetInstance()
	s1.input = 10
	if !reflect.DeepEqual(s1, s2) {
		t.Errorf("expect to be equal, but got s1=%+v s2=%+v", s1, s2)
	}
}
