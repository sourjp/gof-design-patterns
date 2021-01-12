package builder

import (
	"testing"
)

func TestBuilder(t *testing.T) {
	want := "=====\n「Title」\n\n*String1\n\n・Item1\n・Item2\n" +
		"*String2\n\n・Item1\n・Item2\n・Item3\n=====\n"

	tb := &TextBuilder{}
	director := Director{builder: tb}
	director.Construct()
	result := tb.GetString()
	if result != want {
		t.Errorf("expect %v, but got %v", want, result)
	}
}
