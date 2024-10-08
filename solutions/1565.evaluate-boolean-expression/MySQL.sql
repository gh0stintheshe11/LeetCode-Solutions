SELECT e.left_operand, 
       e.operator, 
       e.right_operand,
       CASE WHEN e.operator = '<' AND lv.value < rv.value THEN 'true'
            WHEN e.operator = '<' AND lv.value >= rv.value THEN 'false'
            WHEN e.operator = '>' AND lv.value > rv.value THEN 'true'
            WHEN e.operator = '>' AND lv.value <= rv.value THEN 'false'
            WHEN e.operator = '=' AND lv.value = rv.value THEN 'true'
            WHEN e.operator = '=' AND lv.value <> rv.value THEN 'false'
       END as value
FROM Expressions e
JOIN Variables lv ON e.left_operand = lv.name
JOIN Variables rv ON e.right_operand = rv.name;