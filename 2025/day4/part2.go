//go:build part2
// +build part2

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

func findAccessibleRolls(grid []string) [][2]int {
	accessible := [][2]int{}
	
	for row := 0; row < len(grid); row++ {
		for col := 0; col < len(grid[row]); col++ {
			if grid[row][col] == '@' {
				adjacentRolls := countAdjacentRolls(grid, row, col)
				if adjacentRolls < 4 {
					accessible = append(accessible, [2]int{row, col})
				}
			}
		}
	}
	
	return accessible
}

func removeRoll(grid []string, row, col int) {
	// Convert string to rune slice for modification
	line := []rune(grid[row])
	line[col] = '.'
	grid[row] = string(line)
}

func main() {
	grid := readFile()

	totalRemoved := 0
	
	// Keep removing rolls until no more are accessible
	for {
		accessible := findAccessibleRolls(grid)
		
		if len(accessible) == 0 {
			break
		}
		
		// Remove all accessible rolls in this iteration
		for _, pos := range accessible {
			removeRoll(grid, pos[0], pos[1])
			totalRemoved++
		}
	}

	fmt.Printf("%d\n", totalRemoved)
}
