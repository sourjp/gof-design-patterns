package template

import "testing"

func TestCharDisplay(t *testing.T) {
	cd := CharDisplay{Char: "H"}
	want := "<<<HHHHH>>>"
	result := cd.Display(cd)
	if result != want {
		t.Errorf("expect %v, but got %v", want, result)
	}
}

func TestStringDisplay(t *testing.T) {
	sd := StringDisplay{String: "Hello World!"}
	want := "+------------+\n" +
		"|Hello World!|\n" +
		"|Hello World!|\n" +
		"|Hello World!|\n" +
		"|Hello World!|\n" +
		"|Hello World!|\n" +
		"+------------+\n"
	result := sd.Display(sd)
	if result != want {
		t.Errorf("expect %v, but got %v", want, result)
	}
}
