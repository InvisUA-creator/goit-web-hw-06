SELECT groups.name AVG(grades.grade) AS avg_grade
FROM groups
JOIN students ON groups.id = students.group_id
JOIN grades ON students.id = grades.student_id
JOIN subject ON grades.subject_id = subject.id
WHERE subject.name = 'Math'
GROUP BY group.id