# Write your MySQL query statement below
Select p.project_id,
        ROUND(
            AVG(
                    Coalesce(e.experience_years,0)
                ),2
        ) as average_years


from project p left join employee e
on p.employee_id=e.employee_id
group by p.project_id;
