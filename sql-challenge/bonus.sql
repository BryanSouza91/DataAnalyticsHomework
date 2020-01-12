SELECT count(*) AS Count,
         max(salary),
         min(salary),
         round(avg(salary),
        2)
FROM salaries; 


ALTER TABLE salaries 
	ADD salary_range varchar;

UPDATE salaries 
SET salary_range = CASE
    WHEN salary >= 40000
        AND salary < 50000 THEN
    '[40000-50000)'
    WHEN salary >= 50000
        AND salary < 60000 THEN
    '[50000-60000)'
    WHEN salary >= 60000
        AND salary < 70000 THEN
    '[60000-70000)'
    WHEN salary >= 70000
        AND salary < 80000 THEN
    '[70000-80000)'
    WHEN salary >= 80000
        AND salary < 90000 THEN
    '[80000-90000)'
    WHEN salary >= 90000
        AND salary < 100000 THEN
    '[90000-100000)'
    WHEN salary >= 100000
        AND salary < 110000 THEN
    '[100000-110000)'
    WHEN salary >= 110000
        AND salary < 120000 THEN
    '[110000-120000)'
    WHEN salary >= 120000
        AND salary < 130000 THEN
    '[120000-130000)'
    ELSE 'Unknown' end;
	
SELECT *
FROM salaries;

DROP VIEW salary_counts;

CREATE VIEW	 salary_counts AS SELECT salary_range,
        count(salary_range) AS Count
FROM salaries
GROUP BY  salary_range
ORDER BY  Count desc;

SELECT *
FROM salary_counts; 


DROP VIEW avg_salary;

CREATE VIEW avg_salary AS SELECT t.title,
        round(avg(s.salary),
        2) AS avg_salary
FROM salaries s
INNER JOIN titles t
    ON t.emp_no = s.emp_no
GROUP BY  t.title
ORDER BY  avg_salary desc;

SELECT *
FROM avg_salary; 