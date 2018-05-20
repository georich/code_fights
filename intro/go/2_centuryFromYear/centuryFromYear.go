package main

import "fmt"

func centuryFromYear(year int) int {
	if year%100 == 0 {
		return year / 100
	}
	return (year / 100) + 1
}

func main() {
	fmt.Printf("The year 2045 is in the %dt century.\n", centuryFromYear(2045))
}
