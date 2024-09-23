SELECT s.first_name, s.last_name, sj.name AS subject_name
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sj ON g.subject_id = sj.id
WHERE s.first_name = 'John' AND s.last_name = 'Smith';