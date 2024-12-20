numbers = [1,2,3,4,5]

sqaure_num = numbers.map((num) => num * num * num)

console.log(sqaure_num); // [1, 4, 9, 16, 25]

multi_3 = numbers.filter((num) => num % 3 === 0);

console.log(multi_3); // [3, 6, 9]


addition = numbers.reduce((sum, num) => sum + num, 0);

console.log(addition); // 45


Array.prototype.myMap = function (callback) {
    const result = [];
    for (let i = 0; i < this.length; i++) {
        if (true) {
            result.push(callback(this[i], i, this));
        }
    }
    return result;
};

// Example usage:
const numbers2 = [1, 2, 3];
const doubled = numbers2.myMap(num => num * 2);
console.log(doubled); // Output: [2, 4, 6]


Array.prototype.myFilter = function (callback) {
    const result = [];
    for (let i = 0; i < this.length; i++) {
        if (this.hasOwnProperty(i) && callback(this[i], i, this)) {
            result.push(this[i]);
        }
    }
    return result;
};

// Example usage:
const numbers3 = [1, 2, 3, 4];
const even = numbers3.myFilter(num => num % 2 === 0);
console.log(even); // Output: [2, 4]


Array.prototype.myReduce = function (callback, initialValue) {
    let accumulator = initialValue !== undefined ? initialValue : this[0];
    let startIndex = initialValue !== undefined ? 0 : 1;

    for (let i = startIndex; i < this.length; i++) {
        if (this.hasOwnProperty(i)) {
            accumulator = callback(accumulator, this[i], i, this);
        }
    }
    return accumulator;
};

// Example usage:
const numbers4 = [1, 2, 3, 4];
const sum4 = numbers4.myReduce((acc, num) => acc + num, 0);
console.log(sum4); // Output: 10


let nums = [1, 2, 2, 4, 5, 6, 4];
let ans = []

let dict = {};

// Use a Set to store unique values
let different = new Set(nums);

for (let i = 0 ; i < nums.length; i++) {

    if (dict[nums[i]] == 1){
        ans.push(nums[i])
    }
    dict[nums[i]] = (dict[nums[i]] || 0) + 1;
}

// Count the occurrences in nums
for (let i = 0; i < nums.length; i++) {
    dict[nums[i]] = (dict[nums[i]] || 0) + 1;
}

// Log the counts
for (const [key, value] of Object.entries(dict)) {
    console.log(`${key}: ${value}`);
}


console.log("Unique values:", different);
console.log(ans)

function twoSum(nums, target) {
    const map = new Map(); // To store the difference and its index
    let ans = []

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i]; // Calculate complement
        if (map.has(complement)) {
            ans.push([nums[map.get(complement)], nums[i]]); // Return indices
        }
        map.set(nums[i], i); // Store number and its index in the map
    }

    return ans; // If no solution exists
}

// Example Usage
const nums2 = [2, 4, 5, 7, 11, 15];
const target = 9;
const result = twoSum(nums2, target);
console.log(result); // Output: [0, 1]

console.log(nums2.slice(1, 3)); // Output: [4, 5]

numbers.sort((a, b) => a - b);
const newArray = [...arr];
console.log(numbers);

db.models.find(
    {
        $or: [
            { name: "shrey" },
            { age: { $gte: 20, $lte: 30 } }
        ]
    },
    { _id: 0, name: 1, country: 1 }
)
.sort({ name: -1 })
.limit(100)
.skip(20)

Foo.findAll(
  {
    where: {
      rank: {
        [Op.gt]: 23,
      }
    }
  }
)

const foosWithOperatorExample = await Foo.find({
  $or: [
    {
      rank: {
        $lt: 1000,
        $eq: null,
      },
    },
    {
      $or: [{ title: { $regex: /^Boat/ } }, { description: { $regex: /boat/ } }],
    },
  ],
});

// SELECT students.name, classes.class_name
// FROM students
// JOIN classes
// ON students.class_id = classes.class_id;
