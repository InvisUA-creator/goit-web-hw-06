SELECT s.first_name, s.last_name, g.grade, g.date
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.group_id = 'group1' AND g.subject_id = 'subject1';