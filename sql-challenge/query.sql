-- List the following details of each employee: employee number, last name, first name, gender, and salary.

select e.emp_no,e.last_name,e.first_name,e.gender,s.salary
from employees e
inner join salaries s on s.emp_no = e.emp_no;

-- List employees who were hired in 1986.

select emp_no,last_name,first_name,hire_date 
from employees 
where hire_date between '1986-01-01' and '1986-12-31';

-- List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.

select d.dept_no,d.dept_name,e.emp_no,e.last_name,e.first_name,dm.from_date,dm.to_date
from departments d
inner join dept_manager dm on d.dept_no = dm.dept_no
inner join employees e on e.emp_no = dm.emp_no;

-- List the department of each employee with the following information: employee number, last name, first name, and department name.

select e.emp_no,e.last_name,e.first_name,d.dept_name
from departments d
inner join dept_manager dm on d.dept_no = dm.dept_no
inner join employees e on e.emp_no = dm.emp_no;

-- List all employees whose first name is "Hercules" and last names begin with "B."

select * 
from employees e 
where e.first_name = 'Hercules' and e.last_name like 'B%';

-- List all employees in the Sales department, including their employee number, last name, first name, and department name.

select e.emp_no,e.last_name,e.first_name,d.dept_name
from departments d
inner join dept_manager dm on d.dept_no = dm.dept_no
inner join employees e on e.emp_no = dm.emp_no
where d.dept_name = 'Sales';

-- List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

select e.emp_no,e.last_name,e.first_name,d.dept_name
from departments d
inner join dept_manager dm on d.dept_no = dm.dept_no
inner join employees e on e.emp_no = dm.emp_no
where d.dept_name = 'Sales' or d.dept_name = 'Development';

-- In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

select e2.last_name,count(e.last_name)
from employees e
inner join employees e2 on e2.last_name = e.last_name
group by e2.last_name
order by e.last_name desc;
