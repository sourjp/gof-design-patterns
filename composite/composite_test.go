package composite

import (
	"testing"
)

func TestComposite(t *testing.T) {
	rootDir := NewDirectory("root")
	binDir := NewDirectory("bin")
	tmpDir := NewDirectory("tmp")
	usrDir := NewDirectory("usr")

	rootDir.Add(binDir)
	rootDir.Add(tmpDir)
	rootDir.Add(usrDir)

	binDir.Add(NewFile("vi", 10000))
	binDir.Add(NewFile("latex", 20000))

	got := rootDir.PrintList("")
	want := "/root (30000)\n" +
		"/root/bin (30000)\n" +
		"/root/bin/vi (10000)\n" +
		"/root/bin/latex (20000)\n" +
		"/root/tmp (0)\n" +
		"/root/usr (0)\n"

	if got != want {
		t.Errorf("expect %v, but gtot %v", want, got)
	}
}
