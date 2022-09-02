-- Displays average temperature of cities in
-- descending order of temperature.
SELECT `city`, AVG(`value`) as `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;