package main

import "fmt"

func main() {
	fmt.Println("Welcome to Structs in GOLANG")

	//There is no inhertance in golang, there is also no super class or parent class
	// classes do not exist
	// in golang we make first letter capital to make sure that it is public
	// and can be used in the entire code
	sarthak := User{"Sarthak", "sarthak@gmail.com", true, 16}
	fmt.Println(sarthak)
	fmt.Printf("sarthak details are:\n %+v\n ", sarthak) // %+v gives more details for the struct
	fmt.Printf("Name is: %v and email is %v", sarthak.Name,sarthak.Email)


}

type User struct {
	Name   string
	Email  string
	Status bool
	Age    int
}
