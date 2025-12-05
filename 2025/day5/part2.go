//go:build part2
// +build part2

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

func parseRanges(lines []string) []Range {
	var ranges []Range

	// Parse ranges until we hit the blank line
	for _, line := range lines {
		if strings.TrimSpace(line) == "" {
			break
		}
		parts := strings.Split(line, "-")
		start, _ := strconv.Atoi(parts[0])
		end, _ := strconv.Atoi(parts[1])
		ranges = append(ranges, Range{start: start, end: end})
	}

	return ranges
}

func mergeRanges(ranges []Range) []Range {
	if len(ranges) == 0 {
		return ranges
	}

	// Sort ranges by start position
	// Simple bubble sort for clarity
	for i := 0; i < len(ranges); i++ {
		for j := i + 1; j < len(ranges); j++ {
			if ranges[i].start > ranges[j].start {
				ranges[i], ranges[j] = ranges[j], ranges[i]
			}
		}
	}

	// Merge overlapping or adjacent ranges
	merged := []Range{ranges[0]}

	for i := 1; i < len(ranges); i++ {
		current := ranges[i]
		last := &merged[len(merged)-1]

		// If current range overlaps or is adjacent to the last merged range
		if current.start <= last.end+1 {
			// Extend the last merged range
			if current.end > last.end {
				last.end = current.end
			}
		} else {
			// No overlap, add as new range
			merged = append(merged, current)
		}
	}

	return merged
}

func countFreshIDs(ranges []Range) int {
	// Merge overlapping ranges first to avoid counting duplicates
	merged := mergeRanges(ranges)

	// Count total IDs in all merged ranges
	total := 0
	for _, r := range merged {
		// Number of IDs in range [start, end] is (end - start + 1)
		total += r.end - r.start + 1
	}

	return total
}

func main() {
	lines := readFile()
	ranges := parseRanges(lines)

	freshCount := countFreshIDs(ranges)

	fmt.Printf("Total ingredient IDs considered fresh: %d\n", freshCount)
}
