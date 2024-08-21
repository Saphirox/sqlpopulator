
## SQL tuning 

## Context
- note: I used 8M row records due to limitation of a computer
- Database has 8M records of users
- 12 virtual cpu docker
- 1 Gi swap on docker
- 8 Gi RAM
- 64 GI of SSD 

# Write

Write performance using following variables
- innodb_flush_log_at_trx_commit 
- innodb_buffer_pool_size


The test makes 10 bulks insert with batches of 10 000 users

| innodb_buffer_pool_size | innodb_flush_log_at_trx_commit | Bulk insert time | 
|-------------------------|--------------------------------|------------------|
| 16MB                    | 0                              | 9.5 seconds      |
| 16MB                    | 1                              | 10 seconds       |
| 16MB                    | 2                              | 8.6 seconds      |
| 1Gi                     | 0                              | 2 seconds     |
| 1Gi                     | 1                              | 2.43 seconds     |
| 1Gi                     | 2                              | 2.74 seconds     |


# Read
```sql
SELECT *
FROM users
WHERE birth_date BETWEEN DATE_SUB(CURDATE(), INTERVAL 25 YEAR) AND DATE_SUB(CURDATE(), INTERVAL 18 YEAR)
LIMIT 1000000;
```

In query we search age of users between 18 and 25. (Users are distributed uniformely from 18 to 60)

| has index | Read time        | Query cost | 
|-----------|------------------|------------|
| Yes       | 13.3 seconds     | 900 000    |
| No        | 2.208 seconds   | 744 963    |




