-- WE CREATE FIRST MESSY DB FOR THEM

DROP DATABASE IF EXISTS nc_sells_fridges;
CREATE DATABASE nc_sells_fridges;

\c nc_sells_fridges

CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR,
    features VARCHAR[],
    department VARCHAR
);

CREATE TABLE staff (
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    department VARCHAR
);

CREATE TABLE sales (
    sales_id SERIAL PRIMARY KEY,
    item_id INT REFERENCES items(item_id),
    salesperson INT REFERENCES staff(staff_id),
    price DECIMAL,
    quantity INT,
    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO items
(item_name, features, department)
VALUES
('Louboutin Flip Flops', ARRAY['Designer', 'Faux-Faux-Leather'], 'Footwear'),
('Eau de Fromage', ARRAY['Fragrance', 'Designer'], 'Beauty'),
('Space Raiders', ARRAY['Classic'], 'Grocery');

INSERT INTO staff
(first_name, last_name, department)
VALUES
('Duncan', 'Crawley', 'Beauty'),
('Cat', 'Hoang', 'Footwear');

INSERT INTO sales
(item_id, salesperson, price, quantity)
VALUES
(2, 1, 14.95, 2),
(1, 1, 29.95, 1);


SELECT * FROM items;

SELECT * FROM staff;

SELECT * FROM sales;