//go:build part1
// +build part1
package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readFile() []string {
	data, err := os.ReadFile("day2/input.txt")
	// data, err := os.ReadFile("day2/test.txt")
	if err != nil {
		panic(err)
	}
	out := strings.Split(strings.TrimSpace(string(data)), ",")
	return out
}

func checkInvalid(number int) bool {
	numberStr := fmt.Sprintf("%d", number)
	len := len(numberStr)
	if len%2 != 0 {
		return false
	}
	a := numberStr[:len/2]
	b := numberStr[len/2:]
	return a == b
}


func buildRange(line string, total *int) {
	numbers := strings.Split(line, "-")
	a, _ := strconv.Atoi(numbers[0])
	b, _ := strconv.Atoi(numbers[1])

	store := make([]int, 100)

	for i := a; i <= b; i++ {
		if checkInvalid(i) {
			fmt.Println("invalid:", i)
			store = append(store, i)
			*total += i
		}
	}
}

func main() {
	ranges := readFile()
	total := 0
	for _, line := range ranges {
		buildRange(line, &total)
	}
	fmt.Println("Total", total)
}
