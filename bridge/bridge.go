package bridge

import (
	"strings"
)

type DefaultDisplay struct {
	impl displayImpl
}

func (d *DefaultDisplay) open() string {
	return d.impl.rawOpen()
}

func (d *DefaultDisplay) print() string {
	return d.impl.rawPrint()
}

func (d *DefaultDisplay) close() string {
	return d.impl.rawClose()
}

func (d *DefaultDisplay) Display() string {
	return d.impl.rawOpen() + d.impl.rawPrint() + d.impl.rawClose()
}

type CountDisplay struct {
	*DefaultDisplay
}

func (cd *CountDisplay) MultiDisplay(times int) string {
	var sb strings.Builder
	sb.WriteString(cd.open())
	sb.WriteString(strings.Repeat(cd.print(), times))
	sb.WriteString(cd.close())
	return sb.String()
}

type displayImpl interface {
	rawOpen() string
	rawPrint() string
	rawClose() string
}

type StringDisplayImpl struct {
	str string
}

func (sd *StringDisplayImpl) rawOpen() string {
	return sd.printLine()
}

func (sd *StringDisplayImpl) rawPrint() string {
	return "|" + sd.str + "|"
}

func (sd *StringDisplayImpl) rawClose() string {
	return sd.printLine()
}

func (sd *StringDisplayImpl) printLine() string {
	repeatNum := len([]rune(sd.str))
	boarder := strings.Repeat("-", repeatNum)
	return "+" + boarder + "+"
}

type CharDisplayImpl struct {
	head, str, bottom string
	call              int
}

func (cd *CharDisplayImpl) rawOpen() string {
	return cd.head
}

func (cd *CharDisplayImpl) rawPrint() string {
	out := strings.Repeat(cd.str, cd.call)
	cd.call++
	return out
}

func (cd *CharDisplayImpl) rawClose() string {
	return cd.bottom
}
