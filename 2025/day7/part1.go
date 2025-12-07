//go:build part1
// +build part1

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

	// Track active beams at each column (using a set)
	// Each beam moves downward from a column position
	activeBeams := make(map[int]bool)
	activeBeams[startCol] = true

	splitCount := 0

	// Process row by row
	for row := 1; row < rows && len(activeBeams) > 0; row++ {
		// Collect new beams for next iteration
		nextBeams := make(map[int]bool)

		for col := range activeBeams {
			if col < 0 || col >= cols {
				continue // beam went out of bounds
			}

			cell := grid[row][col]
			if cell == '^' {
				// Beam hits a splitter - it splits
				splitCount++
				// New beams go left and right from the splitter
				if col-1 >= 0 {
					nextBeams[col-1] = true
				}
				if col+1 < cols {
					nextBeams[col+1] = true
				}
			} else {
				// Beam continues downward
				nextBeams[col] = true
			}
		}

		activeBeams = nextBeams
	}

	return splitCount
}

func main() {
	testGrid := readFile("day7/input-test.txt")
	testResult := solve(testGrid)
	fmt.Printf("Test result: %d (expected: 21)\n", testResult)

	grid := readFile("day7/input.txt")
	result := solve(grid)
	fmt.Printf("Part 1 result: %d\n", result)
}
