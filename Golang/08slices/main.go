package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println("Welcome to slices")

	var fruitList = []string{"apple", "tomato", "peach"}
	fmt.Printf("type of fruitlist is: %T \n", fruitList)

	fruitList = append(fruitList, "Mango", "Banana")
	fmt.Println("FRUITLIST IS:", fruitList)

	fruitList = fruitList[1:]
	fmt.Println("\n", fruitList)

	highScores := make([]int, 4)
	highScores[0] = 234
	highScores[1] = 945
	highScores[2] = 465
	highScores[3] = 867
	//highScores[4] = 442 This will not work as the default allocation of range is 4

	//whereas if we use append method we can add more values than the default allocation of the slice

	highScores = append(highScores, 555, 727, 999)
	fmt.Println(highScores)
	sort.Ints(highScores) //sorts the int value in increasing order
	fmt.Println("Sorted value of the Slice:", highScores)

}
