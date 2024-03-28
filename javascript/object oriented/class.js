class Student {
  constructor() {
    var name;
    var marks;
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
var stud = new Student();
stud.setName("John");
stud.setMarks(10); //alert() invokes
console.log(stud.getName() + " " + stud.getMarks());
