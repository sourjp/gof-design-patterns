package composite

import "strconv"

type entry interface {
	getName() string
	getSize() int
	PrintList(prefix string) string
	Add(entry entry)
}

type baseEntry struct {
	entry
	name string
}

func (be *baseEntry) getName() string {
	return be.name
}

func (be *baseEntry) toString(e entry) string {
	return e.getName() + " (" + strconv.Itoa(e.getSize()) + ")" + "\n"
}

type file struct {
	*baseEntry
	size int
}

func (f *file) getSize() int {
	return f.size
}

func (f *file) PrintList(prefix string) string {
	return prefix + "/" + f.toString(f)
}

type directory struct {
	*baseEntry
	directory []entry
}

func (d *directory) getSize() int {
	size := 0
	for _, entry := range d.directory {
		size += entry.getSize()
	}
	return size
}

func (d *directory) PrintList(prefix string) string {
	list := prefix + "/" + d.toString(d)
	for _, entry := range d.directory {
		list += entry.PrintList(prefix + "/" + d.getName())
	}
	return list
}

func (d *directory) Add(entry entry) {
	d.directory = append(d.directory, entry)
}

func NewFile(name string, size int) *file {
	return &file{
		baseEntry: &baseEntry{name: name},
		size:      size,
	}
}

func NewDirectory(name string) *directory {
	return &directory{baseEntry: &baseEntry{name: name}}
}
