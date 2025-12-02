//go:build part2
// +build part2

package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readFile() []string {
	// data, err := os.ReadFile("day2/test.txt")
	data, err := os.ReadFile("day2/input.txt")
	if err != nil {
		panic(err)
	}
	out := strings.Split(strings.TrimSpace(string(data)), ",")
	return out
}

func compareByDigit(numberStr string, offset int) bool {
	numLen := len(numberStr)
	equal := true
	a := numberStr[0:offset]
	for i := 0; i+offset <= numLen && equal; i=i+offset {
		b := numberStr[i:i+offset]
		if a != b {
			equal = false
		}
		a = b
	}
	return equal
}

func checkInvalid(number int) bool {
	numberStr := fmt.Sprintf("%d", number)
	numLen := len(numberStr)
	if numLen < 2 {
		return false
	}

	if numLen%2 == 0 {
		a := numberStr[:numLen/2]
		b := numberStr[numLen/2:]
		if a == b {
			return true
		}
	}

	equal := false
	for digits := 1; (numLen/digits >= 2 && !equal); digits++ {
		if numLen % digits == 0 {
			equal = compareByDigit(numberStr, digits)
		}
	}
	return equal
}

func buildRange(line string, total *int) {
	numbers := strings.Split(line, "-")
	a, _ := strconv.Atoi(numbers[0])
	b, _ := strconv.Atoi(numbers[1])

	for i := a; i <= b; i++ {
		if checkInvalid(i) {
			fmt.Println("invalid:", line, i)
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
