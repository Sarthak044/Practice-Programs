package main

import (
	"fmt"
	"net/url"
)

const myurl string = "https://lco.dev:3000/learn?coursename=reactjs&paymentid=hghgjjsa"

func main() {
	fmt.Println("Welcome to the urls in golang")
	fmt.Println(myurl)

	//parsing
	result, _ := url.Parse(myurl)
	// fmt.Println(result.Scheme)
	// fmt.Println(result.Host)
	// fmt.Println(result.Path)
	// fmt.Println(result.Port())
	//fmt.Println(result.RawQuery)

	qparams := result.Query()
	fmt.Printf("The type of query is: %T\n", qparams)

	fmt.Println(qparams["coursename"])
	fmt.Println(qparams["paymentid"])

	for _, val := range qparams{
		fmt.Println("Param is:", val)
	}

	partofurl := &url.URL{
		Scheme: "https",
		Host: "lco.dev",
		Path: "/tutcss",
		RawQuery: "user=hitesh",
	}
	anotherurl := partofurl.String()
	fmt.Println(anotherurl)
}
