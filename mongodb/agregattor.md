db.teachers.find().limit(1)
db.teachers.find().sort({ teacher_id: -1 }).limit(3)

db.teachers.aggregate([
  { $unwind: "$students" },  // Unwind the students array so each student becomes a separate document
  { $match: { "students.total_marks": { $gt: 243 } } },  // Match students where total_marks is greater than 243
  { $sort: { "students.total_marks": -1 } },  // Sort students by total_marks in descending order
  { $limit: 2 },  // Limit the result to 2 students
  { $project: { 
      "teacher_id": 1,  // Include teacher_id
      "name": 1,        // Include teacher name
      "students.name": 1,        // Include student name
      "students.total_marks": 1  // Include student total_marks
  }}
])

db.teachers.aggregate([
  {
    $lookup: {
      from: "schools",           // The collection to join (schools)
      localField: "school_id",   // The field from the teachers collection
      foreignField: "school_id", // The field from the schools collection
      as: "school_details"       // Output array field with the joined data
    }
  },
  { 
    $unwind: "$school_details"   // Unwind to flatten the array and get individual documents
  },
  { 
    $sort: { "teacher_id": 1 }   // Sort the results by teacher_id in ascending order
  },
  { 
    $limit: 2                    // Limit the result to 2 documents
  },
  { 
    $project: {                  // Project (select) specific fields to include in the output
      "teacher_id": 1,
      "name": 1,
      "school_details.school_name": 1  // Include the school name from the joined collection
    }
  }
])





Example:

    pipeline = [
        {"$match": {"programdata.startTime": {"$regex": f"^{date_str}T"}}},
        {
            "$project": {
                "_id": 0,
                "tivo_station_id": 1,
                "hsa_station_id": 1,
                "programdata": {
                    "$filter": {
                        "input": "$programdata",
                        "as": "pd",
                        "cond": {
                            "$regexMatch": {
                                "input": "$$pd.startTime",
                                "regex": f"^{date_str}T",
                            }
                        },
                    }
                },
            }
        },
    ]




Example:

db.teachers.aggregate([
  {
    $project: {
        _id: 0,
      teacher_id: 1,  // Include teacher_id
      name: 1,        // Include teacher name
      students: {
        $filter: {
          input: "$students",  // The original students array
          as: "student",       // The variable to refer to each student
          cond: { 
            $gt: ["$$student.total_marks", 243] // Condition to filter students with total_marks > 243
          }
        }
      }
    }
  },
  { $match: { "students.0": { $exists: true } } }, // Match only teachers with at least one student who passed the filter
  { $limit: 2 } // Optional: Limit to the first 2 results
])


Example:

db.teachers.aggregate([
  {
    $project: {
      _id: 0,
      teacher_id: 1,  // Include teacher_id
      name: 1,        // Include teacher name
      highest_student: { // Field for the highest student
        $arrayElemAt: [
          {
            $filter: {
              input: {
                $sortArray: {   // Sort the students array by total_marks in descending order
                  input: "$students",
                  sortBy: { total_marks: -1 }
                }
              },
              as: "student",
              cond: { 
                $gt: ["$$student.total_marks", 243] // Condition to filter students with total_marks > 243
              }
            }
          },
          0 // Get the first element of the filtered array
        ]
      }
    }
  },
  { $match: { "highest_student": { $exists: true } } } // Match only teachers with at least one qualifying student
])


examples:

db.station_schedule07.aggregate([
    { "$match": { "programdata.programData.id": "10691781524" } },  // Corrected the boolean value to true
    {
        "$project": {
            "_id": 0,
            "tivo_station_id": 1,
            "hsa_station_id": 1,
            "programdata": {
                "$filter": {
                    "input": "$programdata",
                    "as": "pd",
                    "cond": { 
                        "$eq": ["$$pd.programData.id", "10691781524"]  // Changed to use $$pd for the filter
                    }
                }
            }
        }
    },
    { "$limit": 5 }
])



examples:


db.station_schedule07.aggregate([
    {
        "$match": {
            "programdata.programData.id": "10691781524"
        }
    },
    {
        "$project": {
            "_id": 0,
            "tivo_station_id": 1,
            "hsa_station_id": 1,
            "programdata": {
                "$filter": {
                    "input": "$programdata",
                    "as": "pd",
                    "cond": {
                        "$gt": [
                            {
                                "$size": {
                                    "$filter": {
                                        "input": "$$pd.programData",
                                        "as": "p",
                                        "cond": { "$eq": ["$$p.id", "10691781524"] }
                                    }
                                }
                            },
                            0
                        ]
                    }
                }
            }
        }
    },
    { "$limit": 5 }
])


$filter: This operator filters the programData array ($$pd.programData) to include only those objects where the id matches "10691781524".
$size: This operator calculates the size (number of elements) of the filtered array.
$gt: Finally, it checks if the size of the filtered array is greater than zero.