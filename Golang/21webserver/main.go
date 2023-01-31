package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
	"strings"
)

func main() {
	fmt.Println("Welcome to webserver reqs")
	//PerformPostRequest()
	//PerformGetRequest()
	//PerformPostformRequest()
}

func PerformGetRequest() {
	const myurl = "http://localhost:8000/get"

	response, err := http.Get(myurl)
	if err != nil {
		panic(err)
	}
	defer response.Body.Close()

	fmt.Println("Status code:", response.StatusCode)
	fmt.Println("Content Length:", response.ContentLength)
	var responseString strings.Builder
	content, _ := ioutil.ReadAll(response.Body) //content is in byte format
	byteCount, _ := responseString.Write(content)
	fmt.Println("Byte count is:", byteCount)
	fmt.Println(responseString.String())

	//fmt.Println(string(content))
}

func PerformPostRequest() {
	const myurl = "http://localhost:8000/post"

	//fake json payload

	requestBody := strings.NewReader(`
	{
		"coursename":"lets go with golang",
		"price":0,
		"platform":"lco"
	}
	`)

	response, err := http.Post(myurl, "application/json", requestBody)
	if err != nil {
		panic(err)
	}

	defer response.Body.Close()

	var responseString strings.Builder
	content, _ := ioutil.ReadAll(response.Body)
	responseString.Write(content)
	fmt.Println(responseString.String())

}

func PerformPostformRequest() {
	const myurl = "http://localhost:8000/postform"

	//formdata

	data := url.Values{}
	data.Add("firstname", "sar")
	data.Add("lastname", "kul")
	data.Add("email", "sarkul@gmail.com")

	response, err := http.PostForm(myurl, data)
	if err != nil {
		panic(err)
	}
	defer response.Body.Close()
	var responseString strings.Builder

	content, _ := ioutil.ReadAll(response.Body)
	responseString.Write(content)
	fmt.Println(responseString.String())

}
