--  lists all bands with Glam rock
SELECT band_name, (IFNULL(formed, '2023') - split) AS lifespan
    FROM metal_bands
    WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
    ORDER BY lifespan DESC;
