/*
Now, you need to figure out how to pilot this thing.

It seems like the submarine can take a series of commands like forward 1, down
2, or up 3:

forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.

Note that since you're on a submarine, down and up affect your depth, and so
they have the opposite result of what you might expect.

The submarine seems to already have a planned course (your puzzle input). You
should probably figure out where it's going. For example:

forward 5
down 5
forward 8
up 3
down 8
forward 2

Your horizontal position and depth both start at 0. The steps above would then
modify them as follows:

- forward 5 adds 5 to your horizontal position, a total of 5.
- down 5 adds 5 to your depth, resulting in a value of 5.
- forward 8 adds 8 to your horizontal position, a total of 13.
- up 3 decreases your depth by 3, resulting in a value of 2.
- down 8 adds 8 to your depth, resulting in a value of 10.
- forward 2 adds 2 to your horizontal position, a total of 15.


After following these instructions, you would have a horizontal position of 15
and a depth of 10. (Multiplying these together produces 150.)


Calculate the horizontal position and depth you would have after following the
planned course. What do you get if you multiply your final horizontal position
by your final depth?

*/

package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
	// "reflect"
)


var DEBUG bool = false

func readFile(fname string) (nums []string, err error) {
    // read file

    b, err := ioutil.ReadFile(fname)
    if err != nil { return nil, err }

    lines := strings.Split(strings.Trim(string(b), "\n"), "\n")

    return  lines, err
}



type Ship struct {
    horizontal int
    depth int
    aim int
}


func (s *Ship) move(movement string) {
    // split and convert movement string into int.

    order_split := strings.Fields(movement)
    dir_str := order_split[0]
    mod_str := order_split[1]
    x, _ := strconv.Atoi(mod_str)

    switch dir_str {

    case "forward":
        s.move_horizontal(x)
        s.move_depth(s.aim * x)
    case "down":
        s.move_aim(x)
    case "up":
        s.move_aim(-x)
    }

}

func (s *Ship) move_horizontal(x int) {
    // Move over horizontal
    (*s).horizontal += x
}

func (s *Ship) move_aim(x int) {
    // Move over horizontal
    (*s).aim += x
}

func (s *Ship) move_depth(x int) {
    // Move over horizontal
    (*s).depth += x
}

func (s *Ship) multiply() int {
    return (*s).depth * (*s).horizontal
}


func main() {

    ship := Ship{}
    // order_list, _ := readFile("sample") // multiply = 900
    order_list, _ := readFile("input")

    for idx, order := range order_list {

        if DEBUG { fmt.Println(idx, order) }

        ship.move(order)

        if DEBUG { fmt.Println(ship) }
    }

    fmt.Println(ship)
    fmt.Println(ship.multiply())
}
