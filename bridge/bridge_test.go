package bridge

import (
	"testing"
)

func TestBridge(t *testing.T) {
	dd := DefaultDisplay{impl: &StringDisplayImpl{str: "Hello, Japan."}}
	out := dd.Display()
	want := "+-------------+|Hello, Japan.|+-------------+"
	if out != want {
		t.Errorf("expect %v, but got %v", want, out)
	}

	dd = DefaultDisplay{impl: &StringDisplayImpl{str: "Hello, Japan."}}
	cd := CountDisplay{&dd}
	out = cd.MultiDisplay(2)
	want = "+-------------+|Hello, Japan.||Hello, Japan.|+-------------+"
	if out != want {
		t.Errorf("expect %v, but got %v", want, out)
	}

	dd = DefaultDisplay{impl: &CharDisplayImpl{head: "<", str: "*", bottom: ">"}}
	out = dd.Display()
	out = dd.Display()
	out = dd.Display()
	want = "<**>"
	if out != want {
		t.Errorf("expect %v, but got %v", want, out)
	}
}
