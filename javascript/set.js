// Creating a Set
const mySet = new Set();

// Adding elements to the Set
mySet.add(1);
mySet.add("Hello");
mySet.add({ key: "value" });

// Checking if an element is in the Set
console.log(mySet.has(1)); // true
console.log(mySet.has("World")); // false

// Deleting an element from the Set
mySet.delete("Hello");

// Iterating through the Set
console.log("Iterating through the Set:");
for (let item of mySet) {
  console.log(item);
}

// Converting Set to Array
const myArray = Array.from(mySet);
console.log("Set converted to Array:", myArray);

// Initializing a Set with values
const initializedSet = new Set([1, 2, 3, 4, 5]);

// Chaining Methods - Corrected version
initializedSet.add(6);
initializedSet.delete(1);
initializedSet.add(7);

// Iterating through the initialized Set
console.log("Iterating through the Initialized Set:");
for (let value of initializedSet) {
  console.log(value);
}

// Converting Initialized Set to Array
const initializedArray = [...initializedSet];
console.log("Initialized Set converted to Array:", initializedArray);

// Other Set Methods
console.log(entries + " this is entries");
console.log("Using entries() method:");
for (let entry of entries) {
  console.log(entry);
}
