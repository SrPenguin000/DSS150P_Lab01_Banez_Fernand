CREATE SCHEMA IF NOT EXISTS lab;

DROP TABLE IF EXISTS lab.customers;

CREATE TABLE lab.customers (
    customer_id VARCHAR(50) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255),
    city VARCHAR(100),
    signup_date DATE,
    customer_segment VARCHAR(50),
    
    CONSTRAINT ck_signup_date_valid CHECK (signup_date >= '2000-01-01')
);