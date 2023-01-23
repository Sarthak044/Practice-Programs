package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

const url = "https://lco.dev"

func main() {
	fmt.Println("Welcome to Web Request")
	response, err := http.Get(url)
	if err != nil {
		panic(err)
	}

	fmt.Printf("Response of Type: %T\n", response)
	fmt.Println("Response is:", response)
	defer response.Body.Close()

	data, err := ioutil.ReadAll(response.Body)
	if err != nil {
		panic(err)
	}

	content := string(data)
	fmt.Println("Content is:", content)
}
