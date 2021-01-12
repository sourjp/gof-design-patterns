package adapter

import "testing"

func TestPrintBanner(t *testing.T) {
	TestMessage := "Hello"
	wants := []string{
		"(" + TestMessage + ")",
		"*" + TestMessage + "*",
	}

	pb := NewPrintBanner(TestMessage)
	if wants[0] != pb.PrintWeak() {
		t.Errorf("expect %v, but got %v", wants[0], pb.PrintWeak())
	}
	if wants[1] != pb.PrintStrong() {
		t.Errorf("expect %v, but got %v", wants[1], pb.PrintStrong())
	}
}
