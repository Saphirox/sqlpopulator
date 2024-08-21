
-- query under test for read
SELECT *
FROM users
WHERE birth_date BETWEEN DATE_SUB(CURDATE(), INTERVAL 30 YEAR) AND DATE_SUB(CURDATE(), INTERVAL 18 YEAR)
LIMIT 1000000;

CREATE INDEX idx_birth_date ON users(birth_date)
DROP INDEX idx_birth_date ON users;