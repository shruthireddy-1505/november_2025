# Write your MySQL query statement below

SELECT pd.product_name, s.year, s.price FROM Sales AS s JOIN Product AS pd ON s.product_id=pd.product_id;