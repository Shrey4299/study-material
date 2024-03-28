// Using var
function exampleVar() {
  if (true) {
    var x = 10; // Function-scoped
    console.log(x); // Outputs 10
  }
  console.log(x); // Outputs 10
}

// Using let
function exampleLet() {
  if (true) {
    let y = 20; // Block-scoped
    console.log(y); // Outputs 20
  }
  // console.log(y); // Error: y is not defined (commented out to prevent an error)
}

// Using const
function exampleConst() {
  const z = 30; // Block-scoped
  // z = 40; // Error: Assignment to a constant variable (commented out to prevent an error)
  if (true) {
    const z = 40; // Different variable z, block-scoped
    console.log(z); // Outputs 40
  }
  console.log(z); // Outputs 30
}

// Run examples
exampleVar();
exampleLet();
exampleConst();
