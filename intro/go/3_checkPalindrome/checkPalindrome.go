package main

import "fmt"

func checkPalindrome(inputString string) bool {
	middle := len(inputString) / 2
	end := len(inputString) - 1
	for i := 0; i < middle; i++ {
		if inputString[i] != inputString[end-i] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Printf("Is 'aabaa' a palindrome? %t.\n", checkPalindrome("aabaa"))
}
