package template

import (
	"strings"
)

type printer interface {
	open() string
	close() string
	print() string
}

type AbstractDisplay struct{}

func (ab *AbstractDisplay) Display(printer printer) string {
	var sb strings.Builder
	sb.WriteString(printer.open())
	for i := 0; i < 5; i++ {
		sb.WriteString(printer.print())
	}
	sb.WriteString(printer.close())
	return sb.String()
}

type CharDisplay struct {
	*AbstractDisplay
	Char string
}

func (cd CharDisplay) open() string {
	return "<<<"
}

func (cd CharDisplay) close() string {
	return ">>>"
}

func (cd CharDisplay) print() string {
	return cd.Char
}

type StringDisplay struct {
	*AbstractDisplay
	String string
}

func (sd StringDisplay) open() string {
	return sd.printLine()
}

func (sd StringDisplay) close() string {
	return sd.printLine()
}

func (sd StringDisplay) print() string {
	return "|" + sd.String + "|\n"
}

func (sd StringDisplay) printLine() string {
	var sb strings.Builder
	sb.WriteString("+")
	sb.WriteString(strings.Repeat("-", len(sd.String)))
	sb.WriteString("+\n")
	return sb.String()
}
