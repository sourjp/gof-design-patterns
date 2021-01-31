package visitor

import "strconv"

type visitor interface {
	visitFile(f *file) string
	visitDir(d *directory) string
}

type element interface {
	Accept(v visitor) string
}

type entry interface {
	element
	getName() string
	getSize() int
	Add(e entry)
}

type defaultEntry struct {
	entry
	name string
}

func (e *defaultEntry) getName() string { return e.name }

func (e *defaultEntry) print(inEntry entry) string {
	return inEntry.getName() + "(" + strconv.Itoa(inEntry.getSize()) + ")\n"
}

type file struct {
	*defaultEntry
	size int
}

func (f *file) getSize() int { return f.size }

func (f *file) Add(e entry) {}

func (f *file) Accept(v visitor) string { return v.visitFile((f)) }

type directory struct {
	*defaultEntry
	dir []entry
}

func (d *directory) getSize() int {
	size := 0
	for _, f := range d.dir {
		size += f.getSize()
	}
	return size
}

func (d *directory) Add(e entry) { d.dir = append(d.dir, e) }

func (d *directory) Accept(v visitor) string { return v.visitDir((d)) }

type listVisitor struct {
	currentDir string
}

func (v *listVisitor) visitFile(f *file) string {
	return v.currentDir + "/" + f.print(f)
}

func (v *listVisitor) visitDir(d *directory) string {
	saveDir := v.currentDir
	listedDir := v.currentDir + "/" + d.print(d)
	v.currentDir += "/" + d.getName()
	for _, dir := range d.dir {
		listedDir += dir.Accept(v)
	}
	v.currentDir = saveDir
	return listedDir
}

func NewFile(name string, size int) *file {
	return &file{
		defaultEntry: &defaultEntry{name: name},
		size:         size,
	}
}

func NewDirectory(name string) *directory {
	return &directory{defaultEntry: &defaultEntry{name: name}}
}
