WITH user_platform_usage AS (
    SELECT spend_date, 
           user_id,
           CASE WHEN COUNT(DISTINCT platform) = 2 THEN 'both'
                ELSE MIN(platform)
           END AS platform,
           SUM(amount) AS amount
    FROM Spending
    GROUP BY spend_date, user_id
),
platform_aggregation AS (
    SELECT spend_date, 
           platform,
           SUM(amount) AS total_amount,
           COUNT(DISTINCT user_id) AS total_users
    FROM user_platform_usage
    GROUP BY spend_date, platform
),
complete_dates AS (
    SELECT DISTINCT spend_date
    FROM Spending
),
all_platform_combinations AS (
    SELECT spend_date, 'desktop' AS platform FROM complete_dates
    UNION ALL
    SELECT spend_date, 'mobile' AS platform FROM complete_dates
    UNION ALL
    SELECT spend_date, 'both' AS platform FROM complete_dates
)
SELECT ap.spend_date, ap.platform, 
       COALESCE(pa.total_amount, 0) AS total_amount, 
       COALESCE(pa.total_users, 0) AS total_users
FROM all_platform_combinations ap
LEFT JOIN platform_aggregation pa
ON ap.spend_date = pa.spend_date AND ap.platform = pa.platform
ORDER BY ap.spend_date, ap.platform;