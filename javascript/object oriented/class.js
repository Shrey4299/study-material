class Student {
  constructor(name, marks) {
    this.name = name; // Use `this` to set instance properties
    this.marks = marks;
  }

  getName() {
    return this.name;
  }

  setName(name) {
    this.name = name;
  }

  getMarks() {
    return this.marks;
  }

  setMarks(marks) {
    if (marks < 0 || marks > 100) {
      console.log("Invalid Marks");
    } else {
      this.marks = marks;
    }
  }
}

var stud = new Student("dev", 78);
// stud.setName("John");
// stud.setMarks(-3); // alert() invokes
console.log(stud.getName() + " " + stud.getMarks());
