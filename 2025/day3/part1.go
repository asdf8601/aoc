//go:build part1
// +build part1

package main

import (
	"fmt"
	"os"
	"strings"
)

func readFile() []string {
	// data, err := os.ReadFile("day3/test.txt")
	data, err := os.ReadFile("day3/input.txt")
	if err != nil {
		panic(err)
	}
	out := strings.Split(strings.TrimSpace(string(data)), "\n")
	return out
}

func maxBank(s string) int {
	best := -1

	// Iterate through every possible first digit
	for i := 0; i < len(s)-1; i++ {
		d1 := int(s[i] - '0')
		if d1 < 1 || d1 > 9 {
			continue
		}

		// Iterate through every possible second digit that comes after
		for j := i + 1; j < len(s); j++ {
			d2 := int(s[j] - '0')
			if d2 < 1 || d2 > 9 {
				continue
			}

			val := d1*10 + d2
			if val > best {
				best = val
			}
		}
	}

	return best
}

func main() {
	lines := readFile()
	total := 0

	for _, line := range lines {
		total += maxBank(line)
	}

	fmt.Println(total)
}
