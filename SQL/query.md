# Managers with atleast 5 direct reports

Find managers with at least five direct reports.

Example 1:

Input: 
Employee table:
| id  | name  | department | managerId |
|-----|-------|------------|-----------|
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |

Output: 

| name |
|------|
| John |


```sql
    -- with view
    with managers as (
        select managerid
        from employee
        group by managerid
        having count(*) >= 5
    )

    select name from employee 
    where id in (select managerid from managers);

    -- with view and join
    WITH managers AS (
        SELECT managerId
        FROM Employee
        GROUP by managerid
        HAVING count(*) >= 5
    )

    SELECT name 
    FROM Employee e
    INNER JOIN managers ON e.id = managers.managerId 

    -- with only join
    SELECT 
      e.name as name 
    from 
      Employee e 
      left join Employee m on e.id = m.managerId 
    group by 
      e.name, 
      e.id 
    having 
      count(m.id) >= 5;
```

# date with higher temperatures compared to yesterday

Example

| id | recordDate | temperature |
| -- | ---------- | ----------- |
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |


| id |
------
| 2  |
| 4  |


```sql
    -- selecting twice from the same table
    select 
        W1.Id 
    from 
        Weather as W1, 
        Weather as W2 
    where 
        W1.recordDate - interval '1 day' = W2.recordDate 
        and W1.temperature > W2.temperature
```

# Average time of process per machine

Example 

| machine_id | process_id | activity_type | timestamp |
| ---------- | ---------- | ------------- | --------- |
| 0          | 0          | start         | 0.712     |
| 0          | 0          | end           | 1.520     |
| 0          | 1          | start         | 3.140     |
| 0          | 1          | end           | 4.120     |
| 1          | 0          | start         | 0.550     |
| 1          | 0          | end           | 1.550     |
| 1          | 1          | start         | 0.430     |
| 1          | 1          | end           | 1.420     |
| 2          | 0          | start         | 4.100     |
| 2          | 0          | end           | 4.512     |
| 2          | 1          | start         | 2.500     |
| 2          | 1          | end           | 5.000     |

Output

| machine_id | processing_time |
| ---------- | --------------- |
| 0          | 0.894           |
| 2          | 1.456           |
| 1          | 0.995           |

There are 3 machines running 2 processes each.
- Machine 0's average time is ((1.520 - 0.712) + (4.120 - 3.140)) / 2 = 0.894
- Machine 1's average time is ((1.550 - 0.550) + (1.420 - 0.430)) / 2 = 0.995
- Machine 2's average time is ((4.512 - 4.100) + (5.000 - 2.500)) / 2 = 1.456

```sql
    SELECT 
        machine_id,
        ROUND(AVG(timestamp_diff)::numeric, 3) AS processing_time

    FROM (
        SELECT 
            machine_id,
            process_id,
            -- this works since we group by process id 
            -- and each (machine_id, process_id) combo has exactly one stop time and exactly one start time
            MAX(timestamp) - MIN(timestamp) AS timestamp_diff

        FROM Activity

        GROUP BY machine_id, process_id
    ) AS process_times

    -- as we want the final average wrt machine_id
    GROUP BY machine_id;
```

# Average Selling Price

Prices 

| product_id | start_date | end_date   | price |
| ---------- | ---------- | ---------- | ----- |
| 1          | 2019-02-17 | 2019-02-28 | 5     |
| 1          | 2019-03-01 | 2019-03-22 | 20    |
| 2          | 2019-02-01 | 2019-02-20 | 15    |
| 2          | 2019-02-21 | 2019-03-31 | 30    |
| 3          | 2019-02-21 | 2019-03-31 | 30    |

Units Sold

| product_id | purchase_date | units |
| ---------- | ------------- | ----- |
| 1          | 2019-02-25    | 100   |
| 1          | 2019-03-01    | 15    |
| 2          | 2019-02-10    | 200   |
| 2          | 2019-03-22    | 30    |

```sql
    -- Better solution
    SELECT 
        p.product_id, 
        COALESCE(ROUND
        (
            SUM(p.price * u.units) * 1.0 / SUM(u.units), 2
        ), 
        0) AS average_price

    FROM prices p

    LEFT JOIN UnitsSold u
    ON p.product_id = u.product_id AND purchase_date BETWEEN start_date AND end_date

    GROUP BY p.product_id;

    -- What I did Using Views
    WITH actual_price AS (
        SELECT 
            product_id, 
            units,
            units * (
                SELECT price 
                FROM prices 
                WHERE product_id = unitsSold.product_id 
                  AND purchase_date::DATE >= start_date::DATE 
                  AND purchase_date::DATE <= end_date::DATE
            ) AS total_price
        FROM unitsSold
    )

    SELECT 
        p.product_id, 
        COALESCE(ROUND(SUM(ap.total_price)::NUMERIC / SUM(ap.units)::NUMERIC, 2), 0) AS average_price 

    FROM prices AS p 

    LEFT JOIN actual_price AS ap
        ON p.product_id = ap.product_id

    GROUP BY p.product_id;

```


