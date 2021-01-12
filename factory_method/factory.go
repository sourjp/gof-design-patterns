package factory

type Product interface {
	Use() string
}

type factoryCreater interface {
	createProduct(owner string) Product
	registerProduct(Product)
}

type Factory struct{}

func (f *Factory) Create(creater factoryCreater, owner string) Product {
	p := creater.createProduct(owner)
	creater.registerProduct(p)
	return p
}

type IDCard struct {
	owner string
}

func (idc *IDCard) Use() string {
	return idc.owner
}

type IDCardFactory struct {
	*Factory
	owners []*string
}

func (idcf *IDCardFactory) createProduct(owner string) Product {
	return &IDCard{owner}
}

func (idcf *IDCardFactory) registerProduct(p Product) {
	owner := p.Use()
	idcf.owners = append(idcf.owners, &owner)
}
