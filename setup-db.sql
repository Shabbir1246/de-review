-- CREATE INTITIAL DATABASE

DROP DATABASE IF EXISTS nc_sells_fridges_og;
CREATE DATABASE nc_sells_fridges_og;

\c nc_sells_fridges_og

CREATE TABLE items (
    item_name VARCHAR PRIMARY KEY,
    features VARCHAR[],
    department VARCHAR,
    amount_in_stock INT
);

CREATE TABLE staff (
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    department VARCHAR
);

CREATE TABLE sales (
    sale_code VARCHAR PRIMARY KEY,
    item_name VARCHAR,
    salesperson VARCHAR,
    price DECIMAL,
    quantity INT,
    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO items
(item_name, features, department, amount_in_stock)
VALUES
('Louboutin Flip Flops', ARRAY['Designer', 'Faux-Faux-Leather'], 'Footwear', 50),
('Eau de Fromage', ARRAY['Fragrance', 'Designer'], 'Beauty', 20),
('Space Raiders', ARRAY['Classic'], 'Grocery', 50),
('Bags be gone', ARRAY['Roller-Application', 'Multipack'], 'Beauty', 10),
('Croc Martins', ARRAY['Designer', 'Breezy'], 'Footwear', 80),
('1up', ARRAY['Restorative'], 'Health', 75),
('Backpack', ARRAY['Faux-Faux-Leather', 'Multi-coloured', 'Functional'], 'Kids', 5),
('Shrek Complete Collection', ARRAY['Classic'], 'Movies', 10),
('Phillipe Fellope', ARRAY['Unique', 'Designer'], 'Footwear', 12),
('Faux SheepSkin Rug', ARRAY['Fluffy'], 'Home', 37),
('Mario Party', ARRAY['Fun-for-all-the-family', 'Friendship-killer'], 'Games', 28),
('Car seat', ARRAY['Safe'], 'Baby', 68),
('Bucket of sparks', ARRAY['Rare'], 'Tools', 23),
('Bath robe', ARRAY['Fluffy'], 'Baby', 12),
('Drum Kit', ARRAY['Drum-sticks', 'Stool'], 'Music', 4),
('Guess Who', ARRAY['2-player'], 'Games', 5),
('A long weight', ARRAY['Variable-weight'], 'Sports', 16),
('Chain link bracelet', ARRAY['Designer', 'Mirror-finish'], 'Jewelry', 36),
('Rattan Furniture', ARRAY['Classic'], 'Garden', 84),
('Chocolate Fireguard', ARRAY['Functional'], 'Home', 24),
('Croydon Facelift', ARRAY['Designer', 'DIY kit'], 'Beauty', 34),
('Rebooks', ARRAY['Straps', 'Designer'], 'Footwear', 31),
('Unlabelled VHS', ARRAY['Scary', 'Immersive-experience'], 'Movies', 13),
('Tartan Paint', ARRAY['Rare', 'Unique', 'Designer'], 'Tools', 9),
('Spirit Level Bubble', ARRAY['Balanced'], 'Tools', 5);


INSERT INTO staff
(first_name, last_name, department)
VALUES
('Danika', 'Crawley', 'Beauty'),
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
(sale_code, item_name, salesperson, price, quantity, created_at)
VALUES
('guiiljnevn', 'Louboutin Flip Flops', 'Danika Crawley', 14.95, 2, '2023-01-08 04:05:06'),
('48yv929f0w', 'Eau de Fromage', 'Danika Crawley', 29.95, 1, '2023-01-18 05:09:34'),
('4opsvio2to', 'Space Raiders', 'Sutherlan Housbey', 23.47, 26, '2023-01-27 14:10:36'),
('tvazcdxoup', 'Bags be gone', 'Vincents Guille', 43.53, 19, '2023-01-07 09:27:43'),
('5w7nzlxgy8', 'Croc Martins', 'Cat Hoang', 59.08, 18, '2023-01-03 10:34:56'),
('br699za07t', '1up', 'Lesli Probet', 94.16, 30, '2023-01-14 08:05:23'),
('gu5s1fy667', 'Backpack', 'Cat Hoang', 9.12, 6, '2023-01-27 14:10:36'),
('mf3egrah5w', 'Shrek Complete Collection', 'Erastus Vaines', 69.54, 19, '2023-01-08 04:05:06'),
('m1xetg7sbi', 'Phillipe Fellope', 'Marlo Stidworthy', 82.87, 11, '2023-01-27 04:05:06'),
('jajw3w6c0s', 'Faux SheepSkin Rug', 'Phillipp Zanini', 15.83, 14,'2023-01-03 10:34:56'),
('tripa7kcsr', 'Mario Party', 'Kirbee Abrahamovitz', 37.48, 27, '2023-01-03 10:34:56'),
('9wihbmw8s5', 'Car seat', 'Danika Archell', 45.12, 17, '2023-01-03 10:34:56'),
('cjzkxoqkkh', 'Bucket of sparks', 'Danika Crawley', 71.08, 9, '2023-01-03 10:34:56'),
('xj9jqf09v6', 'Bath robe', 'Christie Whitland', 2.18, 25, '2023-01-27 14:10:36'),
('kf949ghsn8', 'Drum Kit', 'Seline Meekings', 84.13, 5, '2023-01-03 10:34:56'),
('jlbokqyw4k', 'Guess Who', 'Ailyn Laxen', 54.56, 16, '2023-01-27 14:10:36'),
('r2mye6nrcb', 'A long weight', 'Riley Hopkynson', 82.52, 4, '2023-01-03 10:34:56'),
('k2w4bcie0b', 'Chain link bracelet', 'Anastasie Mordan', 90.41, 13, '2023-01-27 14:10:36'),
('r9wpdoz3oe', 'Rattan Furniture', 'Anastasie Mordan', 13.44, 22, '2023-01-27 14:10:36'),
('xraz3oyoed', 'Chocolate Fireguard', 'Stefanie Dartan', 48.44, 26, '2023-01-03 10:34:56'),
('xr5md8nwzz', 'Rebooks', 'Tannie Whiteland', 57.14, 29, '2023-01-27 14:10:36'),
('hy1sla3hhc', 'Tartan Paint', 'Tannie Whiteland', 88.44, 5, '2023-01-03 10:34:56');

-- CREATE NEW DATABASE

DROP DATABASE IF EXISTS nc_sells_fridges_new;
CREATE DATABASE nc_sells_fridges_new;

\c nc_sells_fridges_new


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
    stock_id INT REFERENCES dim_stock(stock_id),
    feature_id INT REFERENCES dim_features(feature_id)
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
    item_id INT REFERENCES dim_stock(stock_id),
    salesperson INT REFERENCES dim_staff(staff_id),
    price DECIMAL,
    quantity INT,
    created_at TIMESTAMP DEFAULT NOW()
);
