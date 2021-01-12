package builder

import "fmt"

type builder interface {
	makeTitle(string)
	makeString(string)
	makeItems([]string)
	close()
}

type Director struct {
	builder builder
}

func (d *Director) Construct() {
	d.builder.makeTitle("Title")
	d.builder.makeString("String1")
	d.builder.makeItems([]string{"Item1", "Item2"})
	d.builder.makeString("String2")
	d.builder.makeItems([]string{"Item1", "Item2", "Item3"})
	d.builder.close()
}

type TextBuilder struct {
	buffer string
}

func (tb *TextBuilder) makeTitle(title string) {
	tb.buffer += fmt.Sprintf("=====\n「%v」\n\n", title)
}

func (tb *TextBuilder) makeString(str string) {
	tb.buffer += fmt.Sprintf("*%v\n\n", str)
}

func (tb *TextBuilder) makeItems(items []string) {
	for _, item := range items {
		tb.buffer += fmt.Sprintf("・%v\n", item)
	}
}

func (tb *TextBuilder) close() {
	tb.buffer += fmt.Sprintf("=====\n")
}

func (tb *TextBuilder) GetString() string {
	return tb.buffer
}
