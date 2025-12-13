//go:build part1
// +build part1

package main

import (
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Point struct {
	x, y, z int
}

type Edge struct {
	i, j int
	dist float64
}

// Union-Find data structure
type UnionFind struct {
	parent []int
	rank   []int
	size   []int
}

func NewUnionFind(n int) *UnionFind {
	uf := &UnionFind{
		parent: make([]int, n),
		rank:   make([]int, n),
		size:   make([]int, n),
	}
	for i := 0; i < n; i++ {
		uf.parent[i] = i
		uf.size[i] = 1
	}
	return uf
}

func (uf *UnionFind) Find(x int) int {
	if uf.parent[x] != x {
		uf.parent[x] = uf.Find(uf.parent[x]) // path compression
	}
	return uf.parent[x]
}

func (uf *UnionFind) Union(x, y int) bool {
	rootX, rootY := uf.Find(x), uf.Find(y)
	if rootX == rootY {
		return false // already in same set
	}
	// union by rank
	if uf.rank[rootX] < uf.rank[rootY] {
		rootX, rootY = rootY, rootX
	}
	uf.parent[rootY] = rootX
	uf.size[rootX] += uf.size[rootY]
	if uf.rank[rootX] == uf.rank[rootY] {
		uf.rank[rootX]++
	}
	return true
}

func (uf *UnionFind) Size(x int) int {
	return uf.size[uf.Find(x)]
}

func readFile(filename string) []string {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	out := strings.Split(strings.Trim(string(data), "\n"), "\n")
	return out
}

func parsePoints(lines []string) []Point {
	points := make([]Point, 0, len(lines))
	for _, line := range lines {
		if line == "" {
			continue
		}
		parts := strings.Split(line, ",")
		x, _ := strconv.Atoi(parts[0])
		y, _ := strconv.Atoi(parts[1])
		z, _ := strconv.Atoi(parts[2])
		points = append(points, Point{x, y, z})
	}
	return points
}

func distance(a, b Point) float64 {
	dx := float64(a.x - b.x)
	dy := float64(a.y - b.y)
	dz := float64(a.z - b.z)
	return math.Sqrt(dx*dx + dy*dy + dz*dz)
}

func solve(lines []string, numConnections int) int {
	points := parsePoints(lines)
	n := len(points)

	// Generate all edges with distances
	edges := make([]Edge, 0, n*(n-1)/2)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			edges = append(edges, Edge{i, j, distance(points[i], points[j])})
		}
	}

	// Sort by distance
	sort.Slice(edges, func(a, b int) bool {
		return edges[a].dist < edges[b].dist
	})

	// Union-Find to connect pairs
	uf := NewUnionFind(n)
	connections := 0

	for _, e := range edges {
		if connections >= numConnections {
			break
		}
		// Always count as a connection attempt, even if already connected
		connections++
		uf.Union(e.i, e.j)
	}

	// Find sizes of all circuits
	circuitSizes := make(map[int]int)
	for i := 0; i < n; i++ {
		root := uf.Find(i)
		circuitSizes[root] = uf.Size(root)
	}

	// Get unique sizes and find top 3
	sizes := make([]int, 0, len(circuitSizes))
	for _, size := range circuitSizes {
		sizes = append(sizes, size)
	}
	sort.Sort(sort.Reverse(sort.IntSlice(sizes)))

	// Multiply top 3
	result := 1
	for i := 0; i < 3 && i < len(sizes); i++ {
		result *= sizes[i]
	}

	return result
}

func main() {
	testLines := readFile("day8/input-test.txt")
	testResult := solve(testLines, 10)
	fmt.Printf("Test result: %d (expected: 40)\n", testResult)

	lines := readFile("day8/input.txt")
	result := solve(lines, 1000)
	fmt.Printf("Part 1 result: %d\n", result)
}
