select 
	count(*) as Count,
	max(salary),
	min(salary),
	round(avg(salary),2) 
from 
	salaries;
	
alter table 
	salaries 
add 
	salary_range varchar;

update
	salaries
set
	salary_range = case
		when salary >= 40000 and salary < 50000 then '[40000-50000)'
		when salary >= 50000 and salary < 60000 then '[50000-60000)'
		when salary >= 60000 and salary < 70000 then '[60000-70000)'
		when salary >= 70000 and salary < 80000 then '[70000-80000)'
		when salary >= 80000 and salary < 90000 then '[80000-90000)'
		when salary >= 90000 and salary < 100000 then '[90000-100000)'
		when salary >= 100000 and salary < 110000 then '[100000-110000)'
		when salary >= 110000 and salary < 120000 then '[110000-120000)'
		when salary >= 120000 and salary < 130000 then '[120000-130000)'
	else 'Unknown'
end;

select * from salaries;

drop view salary_counts;

create view 
	salary_counts as
		select salary_range,count(salary_range) as Count
		from salaries
		group by salary_range
		order by Count desc;
		
select * from salary_counts;

drop view avg_salary;

create view 
	avg_salary as 
		select round(avg(s.salary),2) as avg_salary,t.title
		from salaries s
		inner join titles t on t.emp_no = s.emp_no
		group by t.title
		order by avg_salary desc;
		
		
select * from avg_salary;