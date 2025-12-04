//go:build part1
// +build part1

package main

import (
	"fmt"
	"os"
	"strings"
)

func readFile() []string {
	// data, err := os.ReadFile("day4/input-test.txt")
	data, err := os.ReadFile("day4/input.txt")
	if err != nil {
		panic(err)
	}
	out := strings.Split(strings.TrimSpace(string(data)), "\n")
	return out
}

func countAdjacentRolls(grid []string, row, col int) int {
	// Define the 8 adjacent directions
	directions := [][2]int{
		{-1, -1}, {-1, 0}, {-1, 1}, // top-left, top, top-right
		{0, -1}, {0, 1}, // left, right
		{1, -1}, {1, 0}, {1, 1}, // bottom-left, bottom, bottom-right
	}

	count := 0
	rows := len(grid)
	cols := len(grid[0])

	for _, dir := range directions {
		newRow := row + dir[0]
		newCol := col + dir[1]

		// Check if the position is within bounds
		if newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols {
			if grid[newRow][newCol] == '@' {
				count++
			}
		}
	}

	return count
}

func main() {
	grid := readFile()

	accessibleCount := 0

	// Iterate through each position in the grid
	for row := 0; row < len(grid); row++ {
		for col := 0; col < len(grid[row]); col++ {
			// Check if current position is a roll of paper
			if grid[row][col] == '@' {
				adjacentRolls := countAdjacentRolls(grid, row, col)
				// A roll is accessible if it has fewer than 4 adjacent rolls
				if adjacentRolls < 4 {
					accessibleCount++
				}
			}
		}
	}

	fmt.Printf("%d\n", accessibleCount)
}
