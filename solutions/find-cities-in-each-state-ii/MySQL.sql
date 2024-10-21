WITH sca AS (
  SELECT 
    state,
    GROUP_CONCAT(city ORDER BY city ASC SEPARATOR ', ') AS cities,
    COUNT(*) AS city_count,
    SUM(CASE WHEN LEFT(city, 1) = LEFT(state, 1) THEN 1 ELSE 0 END) AS matching_letter_count
  FROM cities
  GROUP BY state
  HAVING city_count >= 3 AND matching_letter_count > 0
)
SELECT state, cities, matching_letter_count FROM sca
ORDER BY matching_letter_count DESC, state ASC