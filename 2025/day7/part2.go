//go:build part2
// +build part2

package main

import (
	"fmt"
	"os"
	"strings"
)

func readFile(filename string) []string {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	out := strings.Split(strings.Trim(string(data), "\n"), "\n")
	return out
}

func solve(grid []string) int {
	rows := len(grid)
	cols := len(grid[0])

	// Find starting position S
	startCol := -1
	for c := 0; c < cols; c++ {
		if grid[0][c] == 'S' {
			startCol = c
			break
		}
	}

	// Track number of timelines at each column position
	// Key: column, Value: number of timelines that have a particle at that column
	timelines := make(map[int]int)
	timelines[startCol] = 1

	for row := 1; row < rows && len(timelines) > 0; row++ {
		nextTimelines := make(map[int]int)

		for col, count := range timelines {
			if col < 0 || col >= cols {
				continue // out of bounds
			}

			cell := grid[row][col]
			if cell == '^' {
				// Splitter: each timeline splits into 2
				// One goes left, one goes right
				if col-1 >= 0 {
					nextTimelines[col-1] += count
				}
				if col+1 < cols {
					nextTimelines[col+1] += count
				}
			} else {
				// Continue downward, timelines unchanged
				nextTimelines[col] += count
			}
		}

		timelines = nextTimelines
	}

	total := 0
	for _, count := range timelines {
		total += count
	}

	return total
}

func main() {
	testGrid := readFile("day7/input-test.txt")
	testResult := solve(testGrid)
	fmt.Printf("Test: %d (expected: 40)\n", testResult)

	grid := readFile("day7/input.txt")
	result := solve(grid)
	fmt.Printf("Result: %d\n", result)
}
