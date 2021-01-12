package iterator

import (
	"testing"
)

func TestIterator(t *testing.T) {
	wants := []Book{
		Book{"Programming Language Go"},
		Book{"Web API The Good Parts"},
		Book{"Mastering TCP/IP"},
	}
	bookshelf := NewBookShelf()
	for _, book := range wants {
		b := book
		bookshelf.AppendBook(&b)
	}

	i := 0
	for iterator := bookshelf.Iterator(); iterator.HasNext(); {
		if book := iterator.Next(); book.Name != wants[i].Name {
			t.Errorf("expect %v, but get %v", wants[i].Name, book.Name)
		}
		i++
	}
}
