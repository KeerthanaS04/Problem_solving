SELECT DISTINCT CITY
FROM STATION AS S
WHERE RIGHT(CITY,1) IN ('a','e','i','o','u')
/*
'AS' is not necessary here, without that also this code will run successfully
*/
