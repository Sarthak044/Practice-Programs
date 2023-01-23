package main

import (
	"fmt"
	"io/ioutil"
	"log"

	"gopkg.in/yaml.v2"
)

type Test struct {
	courses     string `yaml:"Courses"`
	another_adv string `yaml:"Advance"`
}

func (c *Test) Parse(data []byte) error {
	return yaml.Unmarshal(data, c)
}
func main() {
	fmt.Println("TEST  FOR YAML INTEGRATION")
	data, err := ioutil.ReadFile("E:/Sarthak/Coding/YAML/first.yaml")
	if err != nil {
		log.Fatal(err)
	}
	var config Test
	if err := config.Parse(data); err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%+v\n", config)
}

//func yaml_api() {

//}
