package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

func main() {
	fmt.Println("Hello mod in golang")
	greeter()
	r := mux.NewRouter()
	r.HandleFunc("/", serveHome).Methods("GET")

	log.Fatal(http.ListenAndServe(":4000", r))
}

func greeter() {
	fmt.Println("Hey there mod users")
}

func serveHome(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("<h1>Welcome to golang series</h1>"))
}

//NOTES
/* go mod tidy : tidies up the mod files
go mod graph : pulls up the graph for the modules depedencies
go mod list : pulls up the list for modules
go mod list -all : pulls up more or detailed list
go mod why <package name> : tells you why this module is being used
go mod list -m -all
go mod list -m -versions <package name> : gives the versions available for each package
go mod edit : edit go mod file [flags : -go(version change), -module(change module name)]
go mod vendor : pushing it to production grade
go run -mod=vendor main.go : goes to cache first and pulls up from there
*/
