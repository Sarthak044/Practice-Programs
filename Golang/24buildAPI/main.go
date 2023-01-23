package main

import "net/http"

//Model for course - file
type Course struct {
	CourseID    string  `json:"courseid"`
	CourseName  string  `json:"coursename"`
	CoursePrice int     `json:"price"`
	Author      *Author `json:"author"`
}

type Author struct {
	Fullname string `json:"fullname"`
	Website  string `json:"website"`
}

//fake DB

var course []Course

//middleware or helper - they usually go in seperate file

func (c *Course) IsEmpty() bool {
	return c.CourseID == "" && c.CourseName == ""
}

func main() {
	/* main motive/action plan of api would be:
	1.  get the courses
	2.  create new courses
	3.  delete the courses
	4.  update the courses
	5.  way to see if there is a unique ID or not
	we will use slice as the database
	*/



}

//controllers - file 

// serve home route
func serveHome(w http.ResponseWriter,r *http.Request){
	w.Write([]byte(<h1>Welcome to API by ME</h1>))

}

func getAllCourses(w http.ResponseWriter,r *http.Request){
	fmt.Println("Get all courses")
	w.Header().Set("Content-type", "application/json")
	json.NewEncoder(w).Encode(courses)
}
