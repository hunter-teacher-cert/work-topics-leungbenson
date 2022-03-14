# Benson Leung

# Homework
Homework Assignment: Write a SQL query that retrieves the following records: https://drive.google.com/file/d/1Vy6VDlqOZy8aV7zceGFSJNbbpFH06z1G/view?usp=sharing

Your SQL JOIN query will retrieve from the tables shared with you the records of all of the unexcused period attendance absences in the school for the week of 1-24-22 sorted by student last name ascending. You will use the resulting table of results, which you can call allCuts, in the async assignment. Consider a cut to be any instance of a student scanning into the building and being marked absent in a class. You will retrieve only the first name, last name, student ID, grade, scanTime, status, date, courseSection, attendance, period, and teacher.

```sql

#Practice your homework query here.
#Please save it to your repository.
#It is necessary to complete the homework before the asynchronous work.

sql_query_string = """

SELECT s.*,p.date,p.coursesection, p.attendance,p.teacher,p.period
FROM scan AS s
INNER JOIN periodAtt as p
ON s.studentID=p.studentID AND SUBSTR(s.scantime, 1, instr(s.scantime,' ') - 1)=p.date AND p.attendance = "A"
ORDER BY s.last ASC

"""
 
#Execute the SQL query
result_df = sql_query_to_pd(sql_query_string, db_name='default.db')
result_df
```







