/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
  if (matrix.length === 0 || matrix[0].length === 0) {
    return false;
  }

  const flattenedArray = matrix.reduce((acc, row) => acc.concat(row), []);

  let left = 0;
  let right = flattenedArray.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const midValue = flattenedArray[mid];

    if (midValue === target) {
      return true;
    } else if (midValue < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return false;
};
