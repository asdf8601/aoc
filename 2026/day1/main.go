package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

var code_test = `
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
`

func readFile() []string {
	data, err := os.ReadFile("day1/input.txt")
	if err != nil {
		panic(err)
	}
	return strings.Split(strings.TrimSpace(string(data)), "\n")
}

type Dial struct {
	value      int
	maxValue   int
	startValue int
	countZero  int
}

func (d *Dial) rotate(dir int) int {
	d.value += dir
	if d.value > d.maxValue {
		d.value = 0
	}
	if d.value < 0 {
		d.value = d.maxValue
	}
	if d.value == 0 {
		d.countZero += 1
	}
	return d.value
}

func test1() {
	dial := Dial{value: 50, maxValue: 99, startValue: 50, countZero: 0}

	lines := readFile()
	for _, line := range lines {
		dir := 1
		if string(line[0]) == "L" {
			dir = -1
		}
		clicks, _ := strconv.Atoi(line[1:])

		for i := 0; i < clicks; i++ {
			dial.rotate(dir)
		}
	}

	fmt.Printf("Password: %d\n", dial.countZero)
}

func main() {
	test1()
}
