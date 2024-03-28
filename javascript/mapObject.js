const nums = [1, 3, 6, 7, 8, 3, 9, 10, 11];
  const numIndices = new Map();

  for (let i = 0; i < nums.length; i++) {
    if (numIndices.has(nums[i])) {
      numIndices.set(nums[i], numIndices.get(nums[i]) + 1);
    } else {
      numIndices.set(nums[i], 1);
    }
  }

  // numIndices.set(nums[i], (numIndices.get(nums[i]) || 0) + 1);
  //  map.set(sum, (map.get(sum) || 0) + 1);

  console.log(numIndices);

  // Convert the map to an array of key-value pairs and sort it
  const sortedNumIndicesArray = Array.from(numIndices.entries()).sort(
    (a, b) => b[1] - a[1]
  );

  // Convert the sorted array back to a map
  const sortedNumIndices = new Map(sortedNumIndicesArray);

  console.log(sortedNumIndices);

  // for (const [key, value] of numIndices) {
  //   if (value === 1) {
  //     console.log(`Key: ${key}, Value: ${value}`);
  //     ans.push(key);
  //   }
  // }

  for (var i = 0; i < k; i++) {
    ans.push(sortedNumIndicesArray[i][0]);
  }


console.log(sortedNumIndices);

for (const [key, value] of numIndices) {
  if (value === 1) {
    console.log(`Key: ${key}, Value: ${value}`);
    ans.push(key);
  }
}

console.log(ans);

/**
 * Example of using a Map in JavaScript
 */

// Create a new Map

// 1. Add key-value pairs to the map using set
// numIndices.set("apple", 0);
// numIndices.set("banana", 1);
// numIndices.set("orange", 2);

// // 2. Retrieve values using get
// const bananaIndex = numIndices.get("banana");
// console.log("Index of banana:", bananaIndex);

// // 3. Check if a key exists using has
// const hasOrange = numIndices.has("orange");
// console.log("Does the map have 'orange'?", hasOrange);

// // 4. Delete a key-value pair using delete
// numIndices.delete("apple");
// console.log("Map after deleting 'apple':", numIndices);

// // 5. Clear all key-value pairs using clear
// numIndices.clear();
// console.log("Map after clearing:", numIndices);

// // 6. Use size to get the number of key-value pairs
// console.log("Size of the map:", numIndices.size);

// // 7. Use keys to get an iterator over keys
// const keysIterator = numIndices.keys();
// console.log("Keys in the map:", Array.from(keysIterator));

// // 8. Use values to get an iterator over values
// const valuesIterator = numIndices.values();
// console.log("Values in the map:", Array.from(valuesIterator));

// // 9. Use entries to get an iterator over key-value pairs
// numIndices.set("grape", 3);
// const entriesIterator = numIndices.entries();
// console.log("Entries in the map:", Array.from(entriesIterator));
