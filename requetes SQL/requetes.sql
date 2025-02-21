# 2.Première partie (BigQuery)

SELECT date, SUM(prod_qty*prod_price) as ventes
FROM TRANSACTION 
WHERE date BETWEEN "2019-01-01" AND "2019-12-31"
GROUP BY  date 
ORDER BY date;




# 3. Seconde partie (BigQuery)

SELECT t.client_id as client_id, 
SUM( if ( p.product_type="MEUBLE", t.prod_qty*t.prod_price, 0 ) ) as ventes_meuble, 
SUM( if ( p.product_type="DECO", t.prod_qty*t.prod_price, 0 ) ) as ventes_deco, 
FROM TRANSACTIONS t
LEFT JOIN PRODUCT_NOMENCLATURE p
ON t.prod_id=p.product_id
WHERE t.date BETWEEN "2019-01-01" AND "2019-12-31"
GROUP BY  t.client_id
