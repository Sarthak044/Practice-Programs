package main

import "fmt"

func main() {
	fmt.Println("Welcome to Pointers")

	// var pointer *int
	// fmt.Println("Value of pointer is,", pointer)

	myNumber := 23
	var pointer1 = &myNumber //referencing we use & and while creating a pointer we use *
	fmt.Println("Memory address of myNumber is:", pointer1)
	fmt.Println("Value of actual pointer is:", *pointer1)
	
	// When we want to know what is inside the pointer we print *var 
	// When we want to know what the memory address does that pointer point to we just print the pointer as it is without any *

	*pointer1 = *pointer1 *2
	fmt.Println("New Value of the pointer is:",  myNumber)

}
