-- ranks country origins of bands
SELECT
    band_name,
    CASE
        WHEN split IS NULL THEN YEAR(CURDATE()) - formed
        ELSE split - formed
    END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
