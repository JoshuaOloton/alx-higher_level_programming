-- Displays average temperature of cities in
-- descending order of temperature.
SELECT `city`, AVG(`temp`) as `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;