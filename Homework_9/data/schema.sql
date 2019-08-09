DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS salaries;
DROP TABLE IF EXISTS titles;
DROP TABLE IF EXISTS dept_mgr;
DROP TABLE IF EXISTS dept_emp;
DROP TABLE IF EXISTS departments;

CREATE TABLE employees (
	emp_no INT PRIMARY KEY,
	birth_date DATE NOT NULL,
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	gender VARCHAR(10),
	hire_date DATE NOT NULL
);

CREATE TABLE salaries (
	emp_no INT NOT NULL PRIMARY KEY,
	salary INT NOT NULL,
	sal_from_date DATE NOT NULL,
	sal_to_date DATE NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
);

CREATE TABLE titles (
	emp_no INT NOT NULL,
	title VARCHAR(255) NOT NULL,
	title_from_date DATE NOT NULL,
	title_to_date DATE NOT NULL,
	PRIMARY KEY (emp_no,title_from_date),
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
);

CREATE TABLE dept_mgr (
	dept_no VARCHAR NOT NULL,
	emp_no INT NOT NULL PRIMARY KEY,
	dept_mgr_from_date DATE NOT NULL,
	dept_mgr_to_date DATE NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
);

CREATE TABLE dept_emp (
	emp_no INT NOT NULL,
	dept_no VARCHAR NOT NULL,
	dept_emp_from_date DATE NOT NULL,
	dept_emp_to_date DATE NOT NULL,
	PRIMARY KEY (emp_no,dept_no),
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
);

CREATE TABLE departments (
	dept_no VARCHAR NOT NULL PRIMARY KEY,
	dept_name VARCHAR(50) NOT NULL
);

-- BONUS: Table for bar plot
SELECT t.title, s.salary, e.*
	INTO bonus_newtable
	FROM employees e
	JOIN titles t ON t.emp_no=e.emp_no
	JOIN salaries s ON s.emp_no=e.emp_no
	ORDER BY e.emp_no