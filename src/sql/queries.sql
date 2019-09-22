-- Setup
set schema 'elevate';
SELECT postgis_full_version();

-- Create a geography column to find by location
ALTER TABLE customers ADD COLUMN geog geography(Point,4326);
UPDATE customers SET geog = ST_MakePoint(longitude, latitude);

s0belect count(cid) from customers;

-- Break down the TD customers by age group
select case
	when age < 18 then '<18'
	when age >= 18 and age < 25 then '18-24'
	when age >= 25 and age < 35 then '25-34'
	when age >= 35 and age < 45 then '35-44'
	when age >= 45 and age < 55 then '45-54'
	when age >= 55 and age < 65 then '55-64'
	else '65 and above'
end as agegroup, count(cid) from customers
where cid in (select distinct customerid from accounts)
group by agegroup;

-- Show the TD customers whose account information I have loaded up so far
select count(distinct customerid) from accounts;

-- Find people in the 55+ age bracket with the highest bank account balance
select c.givenname, c.surname, c.age, c.latitude, c.longitude, sum(a.balance), c.cid from accounts a
join customers c on c.cid = a.customerid
where c.age >= 55
group by 1, 2, 3, 4, 5, 7
having sum(a.balance) >= 50000
order by 6 desc, 3 desc, 2 asc;

-- Given a customer ID, find the top 50 people who live the closest 25 or younger - within 10km radius
SELECT c.*, ST_Distance(c.geog, poi)/1000 AS distance_km
FROM customers c,
  (select geog as poi from customers where cid = '218e4191-c5f3-4887-9192-691fc58c14bf') as poi
WHERE ST_DWithin(c.geog, poi, 10000)
  and c.age <= 25
  and coalesce(c.totalincome,0) <= 50000
ORDER BY ST_Distance(c.geog, poi)
limit 50;
