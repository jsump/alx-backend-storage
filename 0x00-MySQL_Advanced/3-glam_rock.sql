-- List all bands with Glam rock as their main style
-- ranked by longetivity
SELECT band_name,
	IFNULL(
		CASE
			WHEN split IS NOT NULL THEN split - formed
			ELSE YEAR(NOW()) - formed
		END,
		0
	) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
