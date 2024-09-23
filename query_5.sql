SELECT subjects.name
FROM subjects
JOIN teachers ON subjects.teacher_id = teacher.id
WHERE teachers.name = 'John Jonson';
