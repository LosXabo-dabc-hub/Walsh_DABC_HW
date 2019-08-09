-- CREATE TABLES --

-->>>> EMPLOYEES TABLE <<<<
	-- Drop employees table	
	DROP TABLE employees;

	-- Create table for Employees.csv data	
	CREATE TABLE employees (
		emp_no INT PRIMARY KEY,
		birth_date DATE NOT NULL,
		first_name VARCHAR(255),
		last_name VARCHAR(255),
		gender VARCHAR(10),
		hire_date DATE NOT NULL
	);
	-- Display content of employees table
	SELECT * FROM employees

-->>>> SALARIES TABLE <<<<
	-- Drop salaries table
	DROP TABLE salaries;

	-- Create salaries table for Salaries.csv data
	CREATE TABLE salaries (
		emp_no INT NOT NULL PRIMARY KEY,
		salary INT NOT NULL,
		sal_from_date DATE NOT NULL,
		sal_to_date DATE NOT NULL,
		FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
	);

	-- Display content of salaries table
	SELECT * FROM salaries

-->>>> TITLES TABLE <<<<
	-- Drop titles table
	DROP TABLE titles;

	-- Create table for Titles.csv data
	CREATE TABLE titles (
		emp_no INT NOT NULL,
		title VARCHAR(255) NOT NULL,
		title_from_date DATE NOT NULL,
		title_to_date DATE NOT NULL,
		PRIMARY KEY (emp_no,title_from_date),
		FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
	);

	-- Display content of salaries table
	SELECT * FROM titles

-->>>> DEPT_MANAGERS TABLE <<<<
	-- Drop dept_mgr table
	DROP TABLE dept_mgr;

	-- Create table for dept_manager.csv data
	CREATE TABLE dept_mgr (
		dept_no VARCHAR NOT NULL,
		emp_no INT NOT NULL PRIMARY KEY,
		dept_mgr_from_date DATE NOT NULL,
		dept_mgr_to_date DATE NOT NULL,
		FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
	);

	-- Display content of dept_manager table
	SELECT * FROM dept_mgr

-->>>> DEPT_EMPLOYEES TABLE <<<<
	-- Drop dept_emp table	
	DROP TABLE dept_emp;

	-- Create table for dept_emp.csv data
	CREATE TABLE dept_emp (
		emp_no INT NOT NULL,
		dept_no VARCHAR NOT NULL,
		dept_emp_from_date DATE NOT NULL,
		dept_emp_to_date DATE NOT NULL,
		PRIMARY KEY (emp_no,dept_no),
		FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
	);

	-- Display content of dept_emp table
	SELECT * FROM dept_emp

-->>>> DEPARTMENTS TABLE <<<<
	-- Drop departments table
	DROP TABLE departments;

	-- Create table for Departments.csv data
	CREATE TABLE departments (
		dept_no VARCHAR NOT NULL PRIMARY KEY,
		dept_name VARCHAR(50) NOT NULL
	);

	-- Display content of departments table
	SELECT * FROM departments


-- QUERY REQUESTED DATA --
	-- Once you have a complete database, do the following: 
	
	-- QUERY_1: List the following details of each employee: employee number, last name, first name, 
	--		gender, and salary.
	SELECT e.emp_no, e.last_name, e.first_name, e.gender, s.salary
	FROM employees e
	JOIN salaries s
	ON (e.emp_no=s.emp_no);

	-- QUERY_2: List employees who were hired in 1986.
	SELECT * FROM employees 
	WHERE hire_date >= '1986-01-01'
	AND hire_date < '1987-01-01'
	ORDER BY hire_date ASC;

	-- QUERY_3: List the manager of each department with the following information: department number, 
	-- department name, the manager's employee number, last name, first name, and start and 
	-- end employment dates.
	SELECT m.dept_no, d.dept_name, m.emp_no, e.last_name, e.first_name, m.dept_mgr_from_date, 
		m.dept_mgr_from_date
	FROM dept_mgr m
	JOIN departments d ON m.dept_no=d.dept_no
	JOIN employees e ON m.emp_no=e.emp_no
	ORDER BY m.emp_no

	-- QUERY_4: List the department of each employee with the following information: employee number, 
	--	last name, first name, and department name.
	SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
	FROM employees e
	JOIN dept_emp de ON e.emp_no=de.emp_no
	JOIN departments d ON de.dept_no=d.dept_no
	ORDER BY e.emp_no

	-- QUERY_5: List all employees whose first name is "Hercules" and last names begin with "B."
	SELECT e.first_name, e.last_name
	FROM employees e
	WHERE e.first_name='Hercules'
	AND e.last_name like 'B%'
	ORDER BY e.last_name

	-- QUERY_6: List all employees in the Sales department, including their employee number, 
	--	last name, first name, and department name.
	SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
	FROM employees e
	JOIN dept_emp de ON e.emp_no=de.emp_no
	JOIN departments d ON de.dept_no=d.dept_no
	WHERE d.dept_name='Sales'
	ORDER BY e.emp_no

	-- QUERY_7: List all employees in the Sales and Development departments, including 
	--	their employee number, last name, first name, and department name.
	SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
	FROM employees e
	JOIN dept_emp de ON e.emp_no=de.emp_no
	JOIN departments d ON de.dept_no=d.dept_no
	WHERE d.dept_name='Sales'
	OR d.dept_name='Development'
	ORDER BY e.emp_no

	-- QUERY_8: In descending order, list the frequency count of employee last names, i.e., how 
	--	many employees share each last name.
	SELECT e.last_name, COUNT(*)
	FROM employees e
	GROUP BY e.last_name
	ORDER BY COUNT(*) DESC;


-- BONUS: Using Pandas, create a bar chart of average salary by title
	-- DROP TABLE if existing
	DROP TABLE bonus_newtable

	-- Create new table
	SELECT t.title, s.salary, e.*
	INTO bonus_newtable
	FROM employees e
	JOIN titles t ON t.emp_no=e.emp_no
	JOIN salaries s ON s.emp_no=e.emp_no
	ORDER BY e.emp_no

	SELECT * FROM bonus_newtable

	SELECT * FROM bonus_newtable
	WHERE emp_no = 499942
-- OUTPUT: "Technique Leader"	40000	499942	"1963-01-10"	"April"	"Foolsday"	"F"	"1997-02-10"




-- *********************
-- *********************
-- TEST CODE
SELECT emp_no, COUNT(*)
FROM employees
GROUP BY emp_no
HAVING COUNT(*) > 1

