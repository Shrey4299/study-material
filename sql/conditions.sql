SELECT
  CASE
    WHEN A + B > C AND B + C > A AND A + C > B THEN
      CASE
        WHEN A = B AND B = C THEN 'Equilateral'
        WHEN A = B OR B = C OR A = C THEN 'Isosceles'
        ELSE 'Scalene'
      END
    ELSE
      'Not A Triangle'
  END AS TriangleType
FROM
  TRIANGLES;

-- The COALESCE function takes two or more arguments and returns the first non-NULL value.

SELECT t.emp_id, 
        COALESCE(jc.job_release_code, tjc.job_release_code) AS job_release_code,
        COALESCE(jc.job_division, tjc.job_division) AS job_division,
        COALESCE(jc.job_code_id, tjc.job_code) AS job_code_id,
        jc.is_all_temp_updated,
        CONCAT(e.first_name, 
                CASE 
                    WHEN e.middle_name IS NOT NULL AND e.middle_name <> '' 
                    THEN CONCAT(' ', e.middle_name) 
                    ELSE '' 
                END, 
                ' ', e.last_name) AS name
    FROM timesheet_v2 t
    LEFT JOIN public.job_codes jc ON t.division = jc.job_code_id
    LEFT JOIN public.temp_job_codes_v2 tjc ON t.division = tjc.job_code
    JOIN public.employee e ON t.emp_id = e.emp_id
WHERE emp_check_in_time >= '{lower_bound.rstrip("Z")}'::TIMESTAMP 
AND emp_check_in_time <= '{upper_bound.rstrip("Z")}'::TIMESTAMP
AND timesheet_status = 'SUBMITTED';