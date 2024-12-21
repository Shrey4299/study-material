const myPromise = new Promise((resolve, reject) => {
  let success = true;

  setTimeout(() => {
    if (success) {
      resolve("Promise resolved successfully!");
    } else {
      reject("Promise rejected!");
    }
  }, 1000);
});

myPromise
  .then((result) => {
    console.log(result); // "Promise resolved successfully!"
  })
  .catch((error) => {
    console.error(error);
  })
  .finally(() => {
    console.log("Promise has been settled.");
  });


  function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
     console.log("Fetching data...");
      resolve("2");
    }, 0);
  });
}

async function fetchAndLogData() {
  console.log("1");
  const data = await fetchData(); // Waits for fetchData to resolve
  console.log(data); // Logs: "1"
  console.log(3); // Logs: "Data fetched successfully!"
}

fetchAndLogData();
console.log("out")