//go:build part1
// +build part1

package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Range struct {
	start int
	end   int
}

func readFile() []string {
	// data, err := os.ReadFile("day5/input-test.txt")
	data, err := os.ReadFile("day5/input.txt")
	if err != nil {
		panic(err)
	}
	out := strings.Split(strings.TrimSpace(string(data)), "\n")
	return out
}

func parseInput(lines []string) ([]Range, []int) {
	var ranges []Range
	var ingredientIDs []int
	
	// Find the blank line that separates ranges from ingredient IDs
	blankLineIndex := -1
	for i, line := range lines {
		if strings.TrimSpace(line) == "" {
			blankLineIndex = i
			break
		}
	}
	
	// Parse ranges (before the blank line)
	for i := 0; i < blankLineIndex; i++ {
		parts := strings.Split(lines[i], "-")
		start, _ := strconv.Atoi(parts[0])
		end, _ := strconv.Atoi(parts[1])
		ranges = append(ranges, Range{start: start, end: end})
	}
	
	// Parse ingredient IDs (after the blank line)
	for i := blankLineIndex + 1; i < len(lines); i++ {
		if strings.TrimSpace(lines[i]) != "" {
			id, _ := strconv.Atoi(strings.TrimSpace(lines[i]))
			ingredientIDs = append(ingredientIDs, id)
		}
	}
	
	return ranges, ingredientIDs
}

func isFresh(id int, ranges []Range) bool {
	for _, r := range ranges {
		if id >= r.start && id <= r.end {
			return true
		}
	}
	return false
}

func main() {
	lines := readFile()
	ranges, ingredientIDs := parseInput(lines)
	
	freshCount := 0
	for _, id := range ingredientIDs {
		if isFresh(id, ranges) {
			freshCount++
		}
	}
	
	fmt.Printf("Number of fresh ingredient IDs: %d\n", freshCount)
}
