package adapter

type Banner struct {
	Message string
}

func (b Banner) ShowWithParen() string {
	return "(" + b.Message + ")"
}

func (b Banner) ShowWithAstr() string {
	return "*" + b.Message + "*"
}

type Print interface {
	PrintWeak() string
	PrintStrong() string
}

type PrintBanner struct {
	Banner Banner
}

func NewPrintBanner(msg string) Print {
	return PrintBanner{Banner: Banner{Message: msg}}
}

func (pb PrintBanner) PrintWeak() string {
	return pb.Banner.ShowWithParen()
}

func (pb PrintBanner) PrintStrong() string {
	return pb.Banner.ShowWithAstr()
}
