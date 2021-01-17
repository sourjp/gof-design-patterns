package strategy

import (
	"fmt"
	"testing"
)

func TestStrategy(t *testing.T) {
	p1 := Player{Name: "player1", Strategy: &WinningStrategy{}}
	p2 := Player{Name: "player2", Strategy: &WinningStrategy{}}

	for i := 0; i < 10; i++ {
		nh1 := p1.NextHand()
		nh2 := p2.NextHand()

		if nh1.IsStrongerThan(nh2) {
			fmt.Printf("win: %v\n", p1.Name)
			p1.Win()
			p2.Lose()
		} else if nh1.IsWeakerThan(nh2) {
			fmt.Printf("win: %v\n", p2.Name)
			p1.Lose()
			p2.Win()
		} else {
			fmt.Println("even...")
			p1.Even()
			p2.Even()
		}
	}

	fmt.Println(p1.Finish())
	fmt.Println(p2.Finish())
}
