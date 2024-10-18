SELECT m.symbol AS metal, n.symbol AS nonmetal
FROM Elements m
JOIN Elements n
ON m.type = 'Metal' AND n.type = 'Nonmetal';