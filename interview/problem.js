console.log("Ennoventure Blr");
function fetchData() {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log("We Process your code");
      resolve("Data received");
    }, 2000);
  });
}
async function processData() {
  console.log("Welcome in the code block");
  const dataPromise = fetchData();
  console.log("Your task is done. Thank You.");
  const result = await dataPromise;
  console.log("You finished your task as per Requirement");
  console.log("You are amazing", result);
}
console.log("Thank You");
processData();
console.log("Ennovengers");

// Thank You
// console.log("Ennovengers");
// Welcome in the code block
// Your task is done. Thank You.
// You finished your task as per Requirement
// We Process your code