package main

import "fmt"

func main() {
	fmt.Println("Welcome to Loops in Golang")

	days := []string{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}

	fmt.Println(days)

	// for  i:=0;i<len(days);i++{
	// 	fmt.Println(days[i])
	// }

	// for i := range days {
	// 	fmt.Println(days[i])
	// }

	// for i,day :=range days{
	// 	fmt.Printf("Index is %v and value is %v\n",i,day)
	// }

	rogueValue := 1

	for rogueValue<10{

		if rogueValue == 2 {
			goto local	
		}
		if rogueValue == 5 {
			break	
		}

		fmt.Println("Value is", rogueValue)
		rogueValue++ 
	}

	local:
		fmt.Println("Jumping to local")
}
