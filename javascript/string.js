// String Declaration
let singleQuotes = "Hello, World!";
let doubleQuotes = "Hello, World!";
let backticks = `Hello, World!`;

// String Properties and Methods
let str = "Hello";
console.log(str.length); // Outputs: 5
console.log(str.toUpperCase()); // Outputs: HELLO
console.log(str.toLowerCase()); // Outputs: hello

// String Concatenation
let str1 = "Hello";
let str2 = "World";
let result = str1 + ", " + str2; // "Hello, World"

// String Template Literals
let name = "John";
let greeting = `Hello, ${name}!`; // "Hello, John!"

// String Escape Characters
let escapedString = "This is a line\nNew line";

// String Methods (Partial List)
console.log(str.charAt(0)); // Outputs: H
console.log(str.indexOf("lo")); // Outputs: 3
console.log(str.slice(1, 4)); // Outputs: ell
console.log(str.replace("Hello", "Hi")); // Outputs: Hi
console.log(str.replaceAll("Hello", "Hi")); // Outputs: Hi
console.log("   trim me   ".trim()); // Outputs: trim me
console.log(str.split("")); // Outputs: ["H", "e", "l", "l", "o"]

// String Immutability
// Strings are immutable; operations create new strings
let immutableStr = "Immutable";
let newStr = immutableStr.slice(0, 5) + "able"; // "Immuatable"

// String Conversion
let num = 42;
let strNum = String(num);

// Unicode and UTF-16
let unicodeChar = "😊";

// String Comparison
let strA = "apple";
let strB = "banana";
console.log(strA.localeCompare(strB)); // Outputs: -1 (strA comes before strB)

// Regular Expressions (Regex)
let regexPattern = /pattern/;
let testString = "This is a pattern test.";
console.log(testString.match(regexPattern));

// String Iteration
let iterableStr = "JavaScript";
// Iterate using a for loop
for (let i = 0; i < iterableStr.length; i++) {
  console.log(iterableStr[i]);
}
// Iterate using forEach method
Array.from(iterableStr).forEach((char) => console.log(char));


let remainder = 10;
console.log(String.fromCharCode(65 + remainder));

let charCode = "K".charCodeAt(0);
let remainder2 = charCode - 65;
console.log(remainder2); // Output: 10


const characters = ["a", "f", "h", "m", "o"];
const asciiValues = characters.map((char) => char.charCodeAt(0));

console.log(asciiValues);

