const nums = [1, 3, 6, 7,7,7,7, 8, 3, 9, 10, 10, 10, 11, 11];
const numIndices = new Map();

for (let i = 0; i < nums.length; i++) {
  if (numIndices.has(nums[i])) {
    numIndices.set(nums[i], numIndices.get(nums[i]) + 1);
  } else {
    numIndices.set(nums[i], 1);
  }
}

console.log(numIndices);

let max_val = 0;
let max_key = 0;

for (const [key, value] of numIndices) {
  if (value > max_val) {
    max_val = Math.max(max_val, value);
    console.log(`Key: ${key} and ${value}`);
    max_key = key;
  }
}

console.log(max_key);
