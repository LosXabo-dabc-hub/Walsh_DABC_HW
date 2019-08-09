SELECT e.emp_no, e.last_name, e.first_name, e.gender, s.salary FROM employees e JOIN salaries s ON (e.emp_no=s.emp_no);
SELECT * FROM employees WHERE hire_date >= '1986-01-01' AND hire_date < '1987-01-01' ORDER BY hire_date ASC;
SELECT m.dept_no, d.dept_name, m.emp_no, e.last_name, e.first_name, m.dept_mgr_from_date, m.dept_mgr_from_date FROM dept_mgr m JOIN departments d ON m.dept_no=d.dept_no JOIN employees e ON m.emp_no=e.emp_no ORDER BY m.emp_no
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name FROM employees e JOIN dept_emp de ON e.emp_no=de.emp_no JOIN departments d ON de.dept_no=d.dept_no ORDER BY e.emp_no
SELECT e.first_name, e.last_name FROM employees e WHERE e.first_name='Hercules' AND e.last_name like 'B%' ORDER BY e.last_name
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name FROM employees e JOIN dept_emp de ON e.emp_no=de.emp_no JOIN departments d ON de.dept_no=d.dept_no WHERE d.dept_name='Sales' ORDER BY e.emp_no
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name FROM employees e JOIN dept_emp de ON e.emp_no=de.emp_no JOIN departments d ON de.dept_no=d.dept_no WHERE d.dept_name='Sales' OR d.dept_name='Development' ORDER BY e.emp_no
SELECT e.last_name, COUNT(*) FROM employees e GROUP BY e.last_name ORDER BY COUNT(*) DESC;

SELECT * FROM employees WHERE emp_no = 499942

