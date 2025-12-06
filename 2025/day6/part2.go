//go:build part2
// +build part2

package main

import (
	"os"
	"strconv"
	"strings"
	"unicode"
)

func readFile() []string {
	// data, err := os.ReadFile("day6/input-test.txt")
	data, err := os.ReadFile("day6/input.txt")
	if err != nil {
		panic(err)
	}
	out := strings.Split(strings.Trim(string(data), "\n"), "\n")
	return out
}

func solve(lines []string) int {
	if len(lines) == 0 {
		return 0
	}

	// Pad lines to max length
	maxLen := 0
	for _, line := range lines {
		if len(line) > maxLen {
			maxLen = len(line)
		}
	}
	grid := make([]string, len(lines))
	for i, line := range lines {
		grid[i] = line + strings.Repeat(" ", maxLen-len(line))
	}

	total := 0
	startCol := 0
	for col := 0; col < maxLen; col++ {
		// Check if this column is a separator (all spaces)
		isSeparator := true
		for _, row := range grid {
			if row[col] != ' ' {
				isSeparator = false
				break
			}
		}

		if isSeparator {
			if col > startCol {
				total += processBlock(grid, startCol, col)
			}
			startCol = col + 1
		}
	}
	// Process last block
	if startCol < maxLen {
		total += processBlock(grid, startCol, maxLen)
	}

	return total
}

func processBlock(grid []string, startCol, endCol int) int {
	var nums []int
	var operator string

	// Find operator
	// Scan the block to find the operator. It's usually at the bottom.
	// We can just scan all characters.
	for r := 0; r < len(grid); r++ {
		lineSlice := grid[r][startCol:endCol]
		if strings.Contains(lineSlice, "+") {
			operator = "+"
		} else if strings.Contains(lineSlice, "*") {
			operator = "*"
		}
	}

	// Iterate columns Right to Left
	for c := endCol - 1; c >= startCol; c-- {
		var digitStr strings.Builder
		for r := 0; r < len(grid); r++ {
			char := rune(grid[r][c])
			if unicode.IsDigit(char) {
				digitStr.WriteRune(char)
			}
		}
		if digitStr.Len() > 0 {
			val, err := strconv.Atoi(digitStr.String())
			if err == nil {
				nums = append(nums, val)
			}
		}
	}

	if len(nums) == 0 {
		return 0
	}

	res := nums[0]
	if operator == "+" {
		for i := 1; i < len(nums); i++ {
			res += nums[i]
		}
	} else if operator == "*" {
		for i := 1; i < len(nums); i++ {
			res *= nums[i]
		}
	}
	return res
}

func main() {
	lines := readFile()
	result := solve(lines)
	println(result)
}
