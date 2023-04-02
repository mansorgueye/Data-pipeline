# 2.Première partie 

SELECT date, SUM(prod_qty*prod_price) as ventes
FROM TRANSACTION 
WHERE CONVERT(DATETIME, date, 3) BETWEEN "2019-01-01" AND "2019-12-31"
GROUP BY  date 
ORDER BY date ASC;




# 3. Seconde partie

SELECT client_id, 
SUM( if ( product_type="MEUBLE", prod_qty*prod_price, 0 ) ) as ventes_meuble, 
SUM( if ( product_type="DECO", prod_qty*prod_price, 0 ) ) as ventes_deco, 
FROM TRANSACTIONS t
LEFT JOIN PRODUCT_NOMENCLATURE p
ON t.prod_id=p.product_id
WHERE CONVERT(DATETIME, date, 3) BETWEEN "2019-01-01" AND "2019-12-31"
GROUP BY  client_id
