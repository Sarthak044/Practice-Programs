package main

import "fmt"

func main() {
	fmt.Println("How to remove a value from slices based on index")

	var courses = []string{"reactjs", "java","Swift","python", "ruby"}
	fmt.Println(courses)

	var index int = 2
	courses = append(courses[:index], courses[index+1:]...)
	fmt.Println(courses)
}