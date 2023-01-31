package main

import (
	"fmt"
)

func main() {
	fmt.Println("Welcome to functions")
	result := adder(3,5)
	fmt.Println("Result is:", result)

	proresult := proAdder(2,5,6,77,112,66)
	fmt.Println("Pro result:",proresult)

}

 
func proAdder(values ...int)int{
	sum := 0

	for _, i :=range values{
		sum+= i
	}
	return sum
}

func adder(x int , y int) int{
	return x+y
}