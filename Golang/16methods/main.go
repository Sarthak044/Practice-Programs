package main

import "fmt"

func main() {
	fmt.Println("Welcome to Methods in golang")
	sk := User{"Sarthak", 18, "sar@gmail.com"}
	fmt.Println("User is:", sk)
	fmt.Printf("User is: %+v\n", sk)
	sk.GetAge()
}

type User struct {
	Name  string
	Age   int
	Email string
}

// first we create a object of the struct then import struct and then use
// that object to call the entites inside the struct
func (u User) GetAge() {
	fmt.Println("User age is:", u.Age)
}
