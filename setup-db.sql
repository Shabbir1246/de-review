-- WE CREATE FIRST MESSY DB FOR THEM

DROP DATABASE IF EXISTS nc_sells_fridges_draft;
CREATE DATABASE nc_sells_fridges_draft;

\c nc_sells_fridges_draft

CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR,
    features VARCHAR[],
    department VARCHAR,
    amount_in_stock INT
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
(item_name, features, department, amount_in_stock)
VALUES
('Louboutin Flip Flops', ARRAY['Designer', 'Faux-Faux-Leather'], 'Footwear', 50),
('Eau de Fromage', ARRAY['Fragrance', 'Designer'], 'Beauty', 50),
('Space Raiders', ARRAY['Classic'], 'Grocery', 50),
('Bags be gone', ARRAY['Roller-Application', 'Multipack'],'Beauty', 50),
('Croc Martins',ARRAY['Designer', 'Breezy'],'Footwear', 50),
('1up',ARRAY['Restorative'],'Health', 50),
('Backpack', ARRAY['Faux-Faux-Leather', 'Multi-coloured','Functional'],'Kids', 50),
('Shrek Complete Collection', ARRAY['Classic'],'Movies', 50),
('Phillipe Fellope', ARRAY['Unique', 'Designer'],'Footwear', 50),
('Faux SheepSkin Rug', ARRAY['Fluffy'],'Home', 50),
('Mario Party', ARRAY['Fun-for-all-the-family', 'Friendship-killer'],'Games', 50),
('Car seat',ARRAY['Safe'],'Baby', 50),
('Bucket of sparks', ARRAY['Rare'],'Tools', 50),
('Bath robe', ARRAY['Fluffy'],'Baby', 50),
('Drum Kit', ARRAY['Drum-sticks', 'Stool'],'Music', 50),
('Guess Who',ARRAY['2-player'],'Games', 50),
('A long weight',ARRAY['Variable-weight'],'Sports', 50),
('Chain link bracelet',ARRAY['Designer','Mirror-finish'],'Jewelry', 50),
('Rattan Furniture', ARRAY['Classic'],'Garden', 50),
('Chocolate Fireguard',ARRAY['Functional'],'Home', 50),
('Croydon Facelift', ARRAY['Designer', 'DIY kit'],'Beauty', 50),
('Rebooks', ARRAY['Straps', 'Designer'],'Footwear', 50),
('Unlabelled VHS',ARRAY['Scary', 'Immersive-experience'],'Movies', 50),
('Tartan Paint',ARRAY['Rare', 'Unique', 'Designer'],'Tools', 50),
('Spirit Level Bubble',ARRAY['Balanced'],'Tools', 50);


INSERT INTO staff
(first_name, last_name, department)
VALUES
('Duncan', 'Crawley', 'Beauty'),
('Cat', 'Hoang', 'Footwear'),
('Vincents', 'Guille', 'Health'),
('Marlo', 'Stidworthy', 'Kids'),
('Lesli', 'Probet', 'Movies'),
('Sutherlan', 'Housbey', 'Footwear'),
('Erastus', 'Vaines', 'Home'),
('Phillipp', 'Zanini', 'Games'),
('Kirbee', 'Abrahamovitz', 'Baby'),
('Danika', 'Archell', 'Tools'),
('Christie', 'Whitland', 'Baby'),
('Seline', 'Meekings', 'Music'),
('Ailyn', 'Laxen', 'Games'),
('Riley', 'Hopkynson', 'Sports'),
('Anastasie', 'Mordan', 'Jewelry'),
('Stefanie', 'Dartan', 'Garden'),
('Tannie', 'Whiteland', 'Home');

INSERT INTO sales
(item_id, salesperson, price, quantity)
VALUES
(2, 1, 14.95, 2),
(1, 1, 29.95, 1),
(15, 6, 23.47, 26),
(1, 10, 43.53, 19),
(11, 2, 59.08, 18),
(10, 7, 94.16, 30),
(14, 2, 9.12, 6),
(7, 17, 69.54, 19),
(6, 14, 82.87, 11),
(7, 5, 15.83, 14),
(6, 3, 37.48, 27),
(10, 16, 45.12, 17),
(4, 1, 71.08, 9),
(10, 5, 2.18, 25),
(12, 3, 84.13, 5),
(10, 12, 54.56, 16),
(1, 11, 82.52, 4),
(4, 3, 90.41, 13),
(11, 3, 13.44, 22),
(12, 9, 48.44, 26),
(2, 10, 57.14, 29),
(12, 16, 88.44, 5);


SELECT * FROM items;

SELECT * FROM staff;

SELECT * FROM sales;


DROP DATABASE IF EXISTS nc_sells_fridges;
CREATE DATABASE nc_sells_fridges;

\c nc_sells_fridges


CREATE TABLE dim_features (
    feature_id SERIAL PRIMARY KEY,
    feature_name VARCHAR
);

CREATE TABLE dim_stock (
    stock_id SERIAL PRIMARY KEY,
    item_name VARCHAR,
    amount_in_stock INT
);

CREATE TABLE stock_feature_junc (
    stock_feature_id SERIAL PRIMARY KEY,
    feature_id INT REFERENCES dim_features(feature_id),
    stock_id INT REFERENCES dim_stock(stock_id)
);

CREATE TABLE dim_date (
    date_id TIMESTAMP,
    day_of_week VARCHAR,
    month VARCHAR,
    year INT
);

CREATE TABLE dim_department (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR
);

CREATE TABLE dim_staff (
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    department_id INT REFERENCES dim_department(department_id)
);

CREATE TABLE fact_sales (
    sales_id SERIAL PRIMARY KEY,
    item_id INT REFERENCES dim_stock(stock_id)
);
