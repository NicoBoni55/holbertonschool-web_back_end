-- ranks country origins of bands
SELECT
    band_name,
    COALESCE(split, 2024) - formed as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
