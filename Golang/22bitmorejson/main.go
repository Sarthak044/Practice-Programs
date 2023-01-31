package main

import (
	"encoding/json"
	"fmt"
)

type course struct {
	Name     string `json:"coursename"`
	Price    int
	Platform string   `json:"website"`
	Password string   `json:"-"`
	Tags     []string `json:"tags,omitempty"` //if value is nil dont refelct it omitemplty
}

func main() {
	fmt.Println("Welcome to JSON")
	//EncodeJson()
	DecodeJson()
}

func EncodeJson() {
	courses := []course{
		{"Reacjs Bootcamp", 299, "Learncodeonline.in", "abc123", []string{"web-dev", "js"}},
		{"MERN Bootcamp", 599, "Learncodeonline.in", "bcd123", []string{"full-stack", "js"}},
		{"Angular Bootcamp", 199, "Learncodeonline.in", "tyu123", nil},
	}

	//package this data as JSON data

	finalJson, err := json.MarshalIndent(courses, "", "\t")
	if err != nil {
		panic(err)
	}
	fmt.Printf("%s\n", finalJson)
}

func DecodeJson() {
	jsonData := []byte(`
		
		{
			"coursename": "Reacjs Bootcamp",
			"Price": 299,
			"website": "Learncodeonline.in",
			"tags": ["web-dev","js"]
		}
	`)

	var lcocourse course
	checkValid := json.Valid(jsonData)

	if checkValid{
		fmt.Println("JSON was valid")
		json.Unmarshal(jsonData, &lcocourse)
		fmt.Printf("%#v\n", lcocourse)
	}else{
		fmt.Println("JSON NOT VALID")
	}

	// some cases where you just want to add data to key value

	var myOnlineData map[string]interface{}
	json.Unmarshal(jsonData, &myOnlineData)
	fmt.Printf("%#v\n", myOnlineData)

	for k,v := range myOnlineData {
		fmt.Printf("Key is %v and value is %v and type is: %T\n",k,v,v)
	}
}
