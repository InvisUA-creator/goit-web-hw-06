SELECT t.first_name, t.last_name, AVG(g.grade) AS avg_grade
FROM teachers t
JOIN subjects sj ON t.id = sj.teacher_id
JOIN grades g ON sj.id = g.subject_id
GROUP BY t.first_name, t.last_name
HAVING t.first_name = 'John' AND t.last_name = 'Jonson';