package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	fmt.Println("Welcome to Switch Case in Golang")
	fmt.Println("A Dice Game")

	rand.Seed(time.Now().UnixNano())
	diceNumber := rand.Intn(6) + 1
	fmt.Println("Value of dice is :", diceNumber)

	switch diceNumber{
	case 1:
		fmt.Println("Dice Value is 1 you can Open")
	case 2:
		fmt.Println("Move 2 spot")
	case 3:
		fmt.Println("Move 3 spot")
	case 4:
		fmt.Println("Move 4 spot")
	case 5:
		fmt.Println("Move 5 spot")
	case 6:
		fmt.Println("Move 6 spot and roll the dice again")
	default:
		fmt.Println("Enter a value between 1-6")
	}
}
