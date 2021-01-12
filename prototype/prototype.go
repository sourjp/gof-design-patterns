package prototype

type Manager struct {
	ShowCase map[string]Producter
}

func NewManager() *Manager {
	return &Manager{ShowCase: make(map[string]Producter)}
}

func (m *Manager) Register(name string, proto Producter) {
	m.ShowCase[name] = proto
}

func (m *Manager) Create(name string) Producter {
	return m.ShowCase[name].createClone()
}

type Producter interface {
	Use(string) string
	createClone() Producter
}

type MessageBox struct {
	DecoChar string
}

func (mbox MessageBox) Use(msg string) string {
	return mbox.DecoChar + msg + mbox.DecoChar
}

// 値渡しで返すことで別のインスタンスにする
func (mbox MessageBox) createClone() Producter {
	return mbox
}
