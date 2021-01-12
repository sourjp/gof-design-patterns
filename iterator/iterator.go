package iterator

type Book struct {
	Name string
}

type BookShelf struct {
	Books []*Book
}

type Aggregate interface {
	Iterator() Iterator
	AppendBook(*Book)
}

func NewBookShelf() Aggregate {
	return &BookShelf{}
}

func (bs *BookShelf) Iterator() Iterator {
	return &BookShelfIterator{BookShelf: bs}
}

func (bs *BookShelf) AppendBook(book *Book) {
	bs.Books = append(bs.Books, book)
}

type Iterator interface {
	HasNext() bool
	Next() *Book
}

type BookShelfIterator struct {
	BookShelf *BookShelf
	index     int
}

func (bsi *BookShelfIterator) HasNext() bool {
	if bsi.index < len(bsi.BookShelf.Books) {
		return true
	}
	return false
}

func (bsi *BookShelfIterator) Next() *Book {
	book := bsi.BookShelf.Books[bsi.index]
	bsi.index++
	return book
}
