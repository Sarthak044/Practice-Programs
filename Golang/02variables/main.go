package main

import "fmt"

func main() {
	var username string = "sarthak"
	fmt.Println(username)
	fmt.Printf("Variable is of type : %T \n", username)

	var isLoggedin bool = true
	fmt.Println(isLoggedin)
	fmt.Printf("Variable is of type : %T \n", isLoggedin)

	var smallValue int = 255
	fmt.Println(smallValue)
	fmt.Printf("Variable is of type : %T \n", smallValue)

	var smallFloat float32 = 255.9984456554
	var longVal float64 = 255.9984456554
	fmt.Println(smallFloat)
	fmt.Printf("Variable is of type : %T \n", smallFloat)
	fmt.Println(longVal)
	fmt.Printf("Variable is of type : %T \n", longVal)

	// Default values and some aliases 
	var anothervariable int 
	fmt.Println(anothervariable)
	fmt.Printf("Variable is of type : %T \n", anothervariable)

	//implicit type
	var website = "learncodeonline.in"
	fmt.Println(website)

	// no var style
	
	numberUsers := 300000
	fmt.Println(numberUsers) 


}
