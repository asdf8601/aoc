// filepath: day3/part2.go
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
	// data, err := os.ReadFile("day3/test.txt")
	data, err := os.ReadFile("day3/input.txt")
	if err != nil {
		panic(err)
	}
	out := strings.Split(strings.TrimSpace(string(data)), "\n")
	return out
}

func maxBankPart2(s string) int64 {
	k := 12

	// Filter valid digits first to simplify index math
	digits := make([]byte, 0, len(s))
	for i := 0; i < len(s); i++ {
		if s[i] >= '1' && s[i] <= '9' {
			digits = append(digits, s[i])
		}
	}

	n := len(digits)
	if n < k {
		return 0
	}

	stack := make([]byte, 0, k)

	for i := 0; i < n; i++ {
		c := digits[i]
		// While stack is not empty, top is smaller than current,
		// and we have enough remaining digits to fill the stack to size k
		for len(stack) > 0 && stack[len(stack)-1] < c && (len(stack)-1+(n-i)) >= k {
			stack = stack[:len(stack)-1]
		}
		if len(stack) < k {
			stack = append(stack, c)
		}
	}

	resStr := string(stack)
	val, err := strconv.ParseInt(resStr, 10, 64)
	if err != nil {
		panic(err)
	}
	return val
}

func main() {
	lines := readFile()
	var total int64 = 0

	for _, line := range lines {
		total += maxBankPart2(line)
	}

	fmt.Println(total)
}
