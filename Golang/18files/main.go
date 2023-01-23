package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"os"
)

func main() {
	fmt.Println("Welcome to the Files in golang")
	content := "This needs to go into the file - yello!"

	file, err := os.Create("./mygofile.txt")

	if err != nil {
		panic(err)
	} else {
		length, err := io.WriteString(file, content)
		if err != nil {
			panic(err)
		} else {
			fmt.Println("lenght is:", length)
			defer file.Close()
			readFile("./mygofile.txt")
		}
	}
}

func readFile(filename string) {
	databyte, err := ioutil.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	fmt.Println("Text Data inside the file is:", string(databyte))

}
