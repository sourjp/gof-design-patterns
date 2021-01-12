package prototype

import (
	"testing"
)

func TestProtoType(t *testing.T) {
	tests := []struct {
		input string
		want  string
	}{
		{input: "test1", want: "|test1|"},
		{input: "test2", want: "*test2*"},
	}

	manager := NewManager()
	mbox1 := MessageBox{DecoChar: "|"}
	mbox2 := MessageBox{DecoChar: "*"}

	manager.Register("m1", mbox1)
	manager.Register("m2", mbox2)

	m1 := manager.Create("m1")
	m2 := manager.Create("m2")
	if m1.Use(tests[0].input) != tests[0].want {
		t.Errorf("expect %v, but got %v", tests[0].want, tests[0].input)
	}
	if m2.Use(tests[1].input) != tests[1].want {
		t.Errorf("expect %v, but got %v", tests[1].want, tests[1].input)
	}
	if &m1 == &m2 {
		t.Errorf("expect to be false, but got &m1=%p &m2=%p", &m1, &m2)
	}
}
