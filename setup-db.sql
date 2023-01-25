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
('Space Raiders', ARRAY['Classic'], 'Grocery'),
('Bags be gone', ARRAY['Roller Application', 'Multipack'],'Beauty'),
('Croc Martins',ARRAY['Designer', 'Breezy'],'Footwear'),
('1up',ARRAY['Restorative'],'Health'),
('Backpack', ARRAY['Faux-Faux-Leather', 'Multi coloured','Functional'],'Kids'),
('Shrek Complete Collection', ARRAY['Classic'],'Movies'),
('Phillipe Fellope', ARRAY['Unique', 'Designer'],'Footwear'),
('Faux SheepSkin Rug', ARRAY['Fluffy'],'Home'),
('Mario Party', ARRAY['Fun for all the family', 'Friendship-killer'],'Games'),
('Car seat',ARRAY['Safe'],'Baby'),
('Bucket of sparks', ARRAY['Rare'],'Tools'),
('Bath robe', ARRAY['Fluffy'],'Baby'),
('Drum Kit', ARRAY['Drum sticks', 'Stool'],'Music'),
('Guess Who',ARRAY['2 player'],'Games'),
('A long weight',ARRAY['Variable weight'],'Sports'),
('Chain link bracelet',ARRAY['Designer','Mirror finish'],'Jewelry'),
('Rattan Furniture', ARRAY['Classic'],'Garden'),
('Chocolate Fireguard',ARRAY['Functional'],'Home'),
('Croydon Facelift', ARRAY['Designer', 'DIY kit'],'Beauty'),
('Rebooks', ARRAY['Straps', 'Designer'],'Footwear'),
('Unlabelled VHS',ARRAY['Scary', 'Immersive experience'],'Movies'),
('Tartan Paint',ARRAY['Rare', 'Unique', 'Designer'],'Tools'),
('Spirit Level Bubble',ARRAY['Balanced'],'Tools');


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