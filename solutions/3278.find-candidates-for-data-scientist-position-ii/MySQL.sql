WITH CandidateScores AS (
    SELECT 
        p.project_id,
        c.candidate_id,
        SUM(CASE 
            WHEN c.proficiency > p.importance THEN 10 
            WHEN c.proficiency < p.importance THEN -5 
            ELSE 0 
        END) + 100 AS score,
        COUNT(p.skill) AS skill_count
    FROM 
        Projects p
    JOIN 
        Candidates c ON p.skill = c.skill
    GROUP BY 
        p.project_id, c.candidate_id
),
ValidCandidates AS (
    SELECT 
        cs.project_id,
        cs.candidate_id,
        cs.score,
        cs.skill_count
    FROM 
        CandidateScores cs
    JOIN 
        (SELECT 
            project_id, COUNT(skill) AS required_skill_count 
         FROM 
            Projects 
         GROUP BY 
            project_id) p
    ON 
        cs.project_id = p.project_id
    WHERE 
        cs.skill_count = p.required_skill_count
),
RankedCandidates AS (
    SELECT 
        vc.project_id,
        vc.candidate_id,
        vc.score,
        ROW_NUMBER() OVER (PARTITION BY vc.project_id ORDER BY vc.score DESC, vc.candidate_id ASC) AS rn
    FROM 
        ValidCandidates vc
)
SELECT 
    project_id,
    candidate_id,
    score
FROM 
    RankedCandidates
WHERE 
    rn = 1
ORDER BY 
    project_id;