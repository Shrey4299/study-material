const tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const numberOfWorkers = 4;

function divideTasks(tasks, numberOfWorkers) {
  const result = Array.from({ length: numberOfWorkers }, () => []);

  for (let i = 0; i < tasks.length; i++) {
    result[i % numberOfWorkers].push(tasks[i]);
  }

  return result;
}

const dividedTasks = divideTasks(tasks, numberOfWorkers);
console.log(dividedTasks);
