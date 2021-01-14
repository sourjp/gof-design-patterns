package abstract

import (
	"fmt"
	"strings"
)

// スーパークラス
type item interface {
	makeHTML() string
}

type link interface {
	item
}

type tray interface {
	item
	Add(item item)
}

type page interface {
	Add(item item)
	Output() string
}

type baseTray struct {
	trays []item
}

func (bt *baseTray) Add(item item) {
	bt.trays = append(bt.trays, item)
}

type basePage struct {
	contents []item
}

func (bp *basePage) Add(item item) {
	bp.contents = append(bp.contents, item)
}

type factory interface {
	CreateLink(caption, url string) link
	CreateTray(caption string) tray
	CreatePage(title, author string) page
}

type listLink struct {
	caption, url string
}

func (ll *listLink) makeHTML() string {
	return fmt.Sprintf("<li><a href=\"%v\">\"%v\"</a></li>\n", ll.url, ll.caption)
}

type listTray struct {
	baseTray
	caption string
}

func (lt *listTray) makeHTML() string {
	var sb strings.Builder
	sb.WriteString(fmt.Sprintf("<li>\n%v\n<ul>", lt.caption))
	for _, tray := range lt.trays {
		sb.WriteString(tray.makeHTML())
	}
	sb.WriteString("</ul>\n</li>\n")
	return sb.String()
}

type listPage struct {
	basePage
	title, author string
}

func (lp *listPage) Output() string {
	var sb strings.Builder
	sb.WriteString(fmt.Sprintf("<html><head><title>%v</title></head>\n"+
		"<body>\n"+
		"<h1>%v</h1>\n"+
		"<ul>\n", lp.title, lp.title))
	for _, content := range lp.contents {
		sb.WriteString(content.makeHTML())
	}
	sb.WriteString(fmt.Sprintf("</ul>\n"+
		"<hr><address>%v</address></body></html>\n", lp.author))
	return sb.String()
}

type ListFactory struct{}

func (lf *ListFactory) CreateLink(caption, url string) link {
	return &listLink{caption, url}
}
func (lf *ListFactory) CreateTray(caption string) tray {
	return &listTray{caption: caption}
}
func (lf *ListFactory) CreatePage(title, author string) page {
	return &listPage{title: title, author: author}
}
