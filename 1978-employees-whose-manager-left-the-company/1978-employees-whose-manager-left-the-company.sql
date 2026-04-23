Select
    employee_id
from employees
where salary<30000
    and 
    manager_id NOT IN(SELECT employee_id from employees)
order by employee_id;