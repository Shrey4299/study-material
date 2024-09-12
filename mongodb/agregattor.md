db.teachers.find().limit(1)
db.teachers.find().sort({ teacher_id: -1 }).limit(3)
