package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	readFile("./part1-test.txt")
}

func readFile(filename string) string {
	reader := strings.NewReader(filename)
	dat, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println(err)
	}
	text := string(dat)
	fmt.Println(text)
	return text
}
