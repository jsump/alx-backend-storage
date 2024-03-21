-- List all bands with Glam rock as their main style
-- ranked by longetivity
SELECT band_name,
	DATEDIFF(2022, IFNULL(split, 2022)) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
