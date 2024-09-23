SELECT students.name, AVG(grades.grade) AS avg_grade
FROM students
JOIN grades ON student_id = grades.student_id
JOIN subject ON grades.subject_id = subject_id
WHERE subject.name = 'Math'
GROUP BY avg_grade DESC
LIMIT 1;