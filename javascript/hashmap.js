// Using an Object as a HashMap
const hashMap = {};

hashMap["key1"] = "value1";
hashMap["key2"] = "value2";
hashMap["key3"] = 42;

console.log(hashMap["key1"]); // "value1"
console.log("key2" in hashMap); // true
console.log(hashMap.hasOwnProperty("key1") + "property"); // true

delete hashMap["key2"];

// Iterating over key-value pairs in the object
for (const key in hashMap) {
  const value = hashMap[key];
  console.log(`Object HashMap: ${key}: ${value}`);
}

// Using the Map object
const myMap = new Map();

myMap.set("key1", "value1");
myMap.set("key2", "value2");
myMap.set("key3", 42);

console.log(myMap.get("key1")); // "value1"
console.log(myMap.has("key2")); // true

myMap.delete("key2");

// Iterating over key-value pairs in the Map
for (const [key, value] of myMap) {
  console.log(`Map: ${key}: ${value}`);
}

// converting objects to array
const obj = { a: 1, b: 2, c: 3 };
const entries = Object.entries(obj);
console.log(entries);
entries.forEach(([key, value]) => {
  console.log(`Key: ${key}, Value: ${value}`);
});

// converting array to object
const entries2 = [
  ["a", 1],
  ["b", 2],
  ["c", 3],
];
const obj2 = Object.fromEntries(entries2);
console.log(obj2);
const dynamicEntries = Object.entries(obj2);
console.log(dynamicEntries);

const alltypes = ["HOT_LEAD", "WARM_LEAD", "COLD_LEAD", "NOT_CONNECTED"];
const initialTypeCounts = Object.fromEntries(alltypes.map((type) => [type, 0]));

// For copying one object into another

// shallow copy

const originalObject = { x: 1, y: 2 };
const copiedObject = { ...originalObject };

copiedObject.x = 7;
console.log(originalObject) // Output: { x: 1, y: 2 }
console.log(copiedObject); // Output: { x: 7, y: 2 }

// deep copy

const originalObject2 = { x: 1, y: { z: 3 } };
const copiedObject2 = JSON.parse(JSON.stringify(originalObject2));

console.log(copiedObject2); // Output: { x: 1, y: { z: 3 } }




