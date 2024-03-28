// Creating a Date Object
const currentDate = new Date();
console.log("Current Date:", currentDate);

const specificDate = new Date(2023, 0, 1, 12, 0, 0, 0);
console.log("Specific Date:", specificDate);

// Getting Date Components
const year = currentDate.getFullYear();
const month = currentDate.getMonth(); // Returns 0-11
const day = currentDate.getDate();
console.log("Year:", year, "Month:", month + 1, "Day:", day);

// Getting Time Components
const hours = currentDate.getHours();
const minutes = currentDate.getMinutes();
const seconds = currentDate.getSeconds();
const milliseconds = currentDate.getMilliseconds();
console.log(
  "Hours:",
  hours,
  "Minutes:",
  minutes,
  "Seconds:",
  seconds,
  "Milliseconds:",
  milliseconds
);

// Setting Date and Time Components
currentDate.setFullYear(2024);
currentDate.setMonth(6); // Sets July (months are 0-11)
currentDate.setDate(15);
console.log("Updated Date:", currentDate);

// Formatting Dates
const dateString = currentDate.toDateString();
const timeString = currentDate.toTimeString();
console.log("Date String:", dateString);
console.log("Time String:", timeString);

// Parsing Dates
const timestamp = Date.parse("2023-01-01T12:00:00Z");
console.log("Timestamp:", timestamp);

// Comparing Dates
const date1 = new Date("2023-01-01T12:00:00Z");
const date2 = new Date("2023-02-01T12:00:00Z");
console.log("Comparison:", date1 < date2);

// Given date (year, month - 1 because months are zero-based, day)
const givenDate = new Date(2023, 0, 1);

// Current date

// Calculate the difference in milliseconds
const timeDifferenceInMilliseconds = givenDate - currentDate;

// Convert milliseconds to days, hours, minutes, seconds, and milliseconds
const daysDifference = Math.floor(
  timeDifferenceInMilliseconds / (1000 * 60 * 60 * 24)
);
const hoursDifference = Math.floor(
  (timeDifferenceInMilliseconds % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
);
const minutesDifference = Math.floor(
  (timeDifferenceInMilliseconds % (1000 * 60 * 60)) / (1000 * 60)
);
const secondsDifference = Math.floor(
  (timeDifferenceInMilliseconds % (1000 * 60)) / 1000
);
const millisecondsDifference = timeDifferenceInMilliseconds % 1000;

// Display the differences
console.log("Days Difference:", daysDifference);
console.log("Hours Difference:", hoursDifference);
console.log("Minutes Difference:", minutesDifference);
console.log("Seconds Difference:", secondsDifference);
console.log("Milliseconds Difference:", millisecondsDifference);
