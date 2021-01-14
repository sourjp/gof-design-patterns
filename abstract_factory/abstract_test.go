package abstract

import (
	"testing"
)

func TestAbstractFactory(t *testing.T) {

	factory := ListFactory{}

	linkGoogle := factory.CreateLink("Google!", "https://google.com")
	linkYahoo := factory.CreateLink("Yahoo!", "http://yahoo.com")

	tray := factory.CreateTray("Search Engine")
	tray.Add(linkGoogle)
	tray.Add(linkYahoo)

	page := factory.CreatePage("Title", "Author")
	page.Add(tray)

	output := page.Output()

	expect := "<html><head><title>Title</title></head>\n" +
		"<body>\n<h1>Title</h1>\n<ul>\n<li>\nSearch Engine\n" +
		"<ul><li><a href=\"https://google.com\">\"Google!\"</a></li>\n" +
		"<li><a href=\"http://yahoo.com\">\"Yahoo!\"</a></li>\n" +
		"</ul>\n</li>\n</ul>\n<hr><address>Author</address></body></html>\n"

	if output != expect {
		t.Errorf("Expect %s, but got %s\n", expect, output)
	}

}
