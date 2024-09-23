SELECT s.first_name, s.last_name, sj.name AS subject_name, t.first_name AS teacher_first_name, t.last_name AS teacher_last_name
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sj ON g.subject_id = sj.id
JOIN teachers t ON sj.teacher_id = t.id
WHERE s.first_name = 'John' AND s.last_name = 'Smith' AND t.first_name = 'John' AND t.last_name = 'Jonson';