const persons = ["John", "Doe", "Bad"];
const numbers = [3, 2, 5, 6, 7, 8, 9, 10, 3, 2];
let seen = new Array(5).fill(0);

console.log(seen)
// adding and removing data from the back
persons.push("Jane");
persons.push("Doe");
persons.pop();
console.log("After poping Doe", persons);

// adding and removing data from the front
persons.unshift("NewPerson");
console.log("After adding to the front:", persons);
const removedPerson = persons.shift();
console.log("Removed person:", removedPerson);
console.log("After removing from the front:", persons);

// Add and Remove an element at a particular position
persons.splice(2, 0, "Lemon", "Jane");
// The first parameter (2) defines the position where new elements should be added (spliced in).
// The second parameter (0) defines how many elements should be removed.
console.log("After adding at position:", persons);
persons.splice(0, 1);
// The first parameter (0) defines the position where new elements should be added (spliced in).
// The second parameter (1) defines how many elements should be removed.
console.log("After removing at position:", persons);

console.log(persons.slice(3,6))

// concat two Array
const arr1 = ["Cecilie", "Lone"];
const arr2 = ["Emil", "Tobias", "Linus"];
const arr3 = ["Robin", "Morgan"];
const myChildren = arr1.concat(arr2, arr3);
console.log(myChildren);

// all iterating method for array
for (const person of persons) {
  console.log(person);
}

for (let i = 0; i < persons.length; i++) {
  console.log(`Person at index ${i}: ${persons[i]}`);
}

persons.forEach((person, index) => {
  console.log(`Person at index ${index}: ${person}`);
});

for (const [index, person] of persons.entries()) {
  console.log(`Person at index ${index}: ${person}`);
}

// javascript array functions

console.log(persons.length);
console.log(persons.sort());
console.log(persons.toString);
console.log(persons.includes("apple"));
console.log(persons.join("->"));
console.log(persons.reverse());
console.log(persons.indexOf("Jane"));
console.log(persons.lastIndexOf("Jane"));
console.log(
  numbers.sort( (a, b) => {
    return a - b;
  })
);
console.log(Math.max.apply(null, numbers));
console.log(Math.min.apply(null, numbers));
console.log(...new Set(numbers));

// copy one array into another
const arr = [].concat(numbers);
const newArray = [...arr];

const myArray = [1, 2, 3, 4, 4, 5, 6, 6];
const mySet = new Set(myArray);

// Get a random integer between 1 and 10
const min = 1;
const max = 11;
const randomNum = Math.floor(Math.random() * (max - min)) + min;

console.log(randomNum);

const double_arr = arr.map((item) => {
  return item * 2;
});
const even = arr.filter((item) => {
  return item % 2 === 0;
});
const reduce = arr.reduce((acc, item) => acc + item);

console.log(double_arr);
console.log(even);
console.log(reduce);
