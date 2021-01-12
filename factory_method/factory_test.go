package factory

import "testing"

func TestFactoryMethod(t *testing.T) {
	wants := []string{"A", "B", "C"}
	factory := &IDCardFactory{}
	products := []Product{
		factory.Create(factory, wants[0]),
		factory.Create(factory, wants[1]),
		factory.Create(factory, wants[2]),
	}

	for i, product := range products {
		if owner := product.Use(); owner != wants[i] {
			t.Errorf("expect %v, but got %v", owner, wants[i])
		}
	}
}
