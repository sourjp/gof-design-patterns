package strategy

import (
	"math/rand"
	"strconv"
	"time"
)

const (
	handValueGuu int = iota
	handValueCho
	handValuePaa
)

var (
	hands []*hand
)

func init() {
	hands = []*hand{
		&hand{handValueGuu},
		&hand{handValueCho},
		&hand{handValuePaa},
	}
	rand.Seed(time.Now().UnixNano())
}

type hand struct {
	handValue int
}

func GetHand(handValue int) *hand {
	return hands[handValue]
}

func (self *hand) IsStrongerThan(h *hand) bool {
	return self.fight(h) == 1
}

func (self *hand) IsWeakerThan(h *hand) bool {
	return self.fight(h) == -1
}

func (self *hand) fight(h *hand) int {
	if self == h {
		return 0
	} else if (self.handValue+1)%3 == h.handValue {
		return 1
	} else {
		return -1
	}
}

type strategy interface {
	nextHand() *hand
	study(bool)
}

type WinningStrategy struct {
	won      bool
	prevHand *hand
}

func (ws *WinningStrategy) nextHand() *hand {
	if !ws.won {
		ws.prevHand = GetHand(rand.Intn(3))
	}
	return ws.prevHand
}

func (ws *WinningStrategy) study(win bool) {
	ws.won = win
}

type Player struct {
	Name                           string
	Strategy                       strategy
	wincount, losecount, gamecount int
}

func (p *Player) NextHand() *hand {
	return p.Strategy.nextHand()
}

func (p *Player) Win() {
	p.Strategy.study(true)
	p.wincount++
	p.gamecount++
}

func (p *Player) Lose() {
	p.Strategy.study(false)
	p.losecount++
	p.gamecount++
}

func (p *Player) Even() {
	p.gamecount++
}

func (p *Player) Finish() string {
	return "[" + p.Name + ":" +
		strconv.Itoa(p.gamecount) + " games, " +
		strconv.Itoa(p.wincount) + " win, " +
		strconv.Itoa(p.losecount) + " lose]"
}
