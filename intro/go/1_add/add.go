package main

import "fmt"

func add(param1, param2 int) int {
	return param1 + param2
}

func main() {
	fmt.Println(add(3, 4))
}
