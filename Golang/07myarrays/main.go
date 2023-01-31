package main

import (
	"fmt"
)

func main() {
	fmt.Println("Welcome to the arrays")

	var fruitList [4]string

	fruitList[0] = "Apple"
	fruitList[1] = "Orange"
	// fruitList[2]
	fruitList[3] = "Strawberry"
	fmt.Println("Fruit list :", fruitList)
	fmt.Println("Fruit list :", len(fruitList))
	var vegList = [5]string{"potato", "beans", "mushroom"}
	fmt.Println("Veggie List:", vegList)
	fmt.Println("Veggie List:", len(vegList))
}
