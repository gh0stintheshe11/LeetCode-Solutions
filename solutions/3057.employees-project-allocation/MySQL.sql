SELECT 
    p.employee_id, 
    p.project_id, 
    e.name AS employee_name, 
    p.workload AS project_workload
FROM 
    Project p
JOIN 
    Employees e ON p.employee_id = e.employee_id
JOIN 
    (SELECT 
        team, 
        AVG(workload) AS avg_workload
     FROM 
        Project p2
     JOIN 
        Employees e2 ON p2.employee_id = e2.employee_id
     GROUP BY 
        team) AS team_avg ON e.team = team_avg.team
WHERE 
    p.workload > team_avg.avg_workload
ORDER BY 
    p.employee_id, 
    p.project_id;