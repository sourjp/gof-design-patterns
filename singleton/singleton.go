package singleton

// privateにして他パッケージから直接作れないように保証
type singleton struct {
	input int
}

// Global変数として一つであることを保証
var instance *singleton

// GetInstance 一つであるglobal変数を返すように実装
func GetInstance() *singleton {
	if instance == nil {
		instance = &singleton{}
	}
	return instance
}
