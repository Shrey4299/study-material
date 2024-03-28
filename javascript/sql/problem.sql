-- Active: 1694601173563@@127.0.0.1@3306@sampledb

CREATE TABLE
    customer (
        customer_id INT PRIMARY KEY,
        customer_name VARCHAR(32) NOT NULL,
        password VARCHAR(32),
        city VARCHAR(32),
        state VARCHAR(32),
        zip INT,
        country VARCHAR(32)
    );

-- Create the 'toy' table
CREATE TABLE
    toy (
        toy_id INT PRIMARY KEY,
        toy_name VARCHAR(32) NOT NULL,
        toy_type VARCHAR(32) NOT NULL,
        min_age INT CHECK (
            min_age BETWEEN 0 AND 12
        ),
        max_age INT,
        price DECIMAL(9, 2) CHECK (price > 0),
        quantity DECIMAL(9, 2) CHECK (quantity > 0),
        rental_amount DECIMAL(9, 2) CHECK (rental_amount > 0)
    );

CREATE TABLE
    toy_rental (
        rental_id INT PRIMARY KEY,
        customer_id INT,
        toy_id INT,
        rental_start_date DATE NOT NULL,
        rental_end_date DATE NOT NULL,
        rental_amount_per_day DECIMAL(9, 2) NOT NULL,
        total_amount DECIMAL(9, 2),
        fine DECIMAL(9, 2),
        status VARCHAR(32),
        FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
        FOREIGN KEY (toy_id) REFERENCES toy(toy_id)
    );

INSERT INTO customer
VALUES (
        1001,
        'Kanishk',
        'Welcome@123',
        'Chennai',
        'TamilNadu',
        600075,
        'India'
    );

INSERT INTO customer
VALUES (
        1002,
        'Krithick',
        'Krithi@321',
        'Bangalore',
        'Karnataka',
        560001,
        'India'
    );

INSERT INTO customer
VALUES (
        1003,
        'Chandrav',
        'Chand@423',
        'Mumbai',
        'Maharastra',
        400001,
        'India'
    );

INSERT INTO customer
VALUES (
        1004,
        'John',
        'Joh@36',
        'New Delhi',
        'Delhi',
        110001,
        'India'
    );

INSERT INTO customer
VALUES (
        1005,
        'Raj',
        'Kri@356',
        'Hyderabad',
        'Telangana',
        500001,
        'India'
    );

INSERT INTO customer
VALUES (
        1006,
        'Kishore',
        'Shore@78',
        'Chennai',
        'TamilNadu',
        600075,
        'India'
    );

INSERT INTO customer
VALUES (
        1007,
        'Malik',
        'alik@28',
        'Mumbai',
        'Maharastra',
        400001,
        'India'
    );

INSERT INTO customer
VALUES (
        1008,
        'Christina',
        'tina@763',
        'Delhi',
        'Delhi',
        110001,
        'India'
    );

INSERT INTO customer
VALUES (
        1009,
        'Kenson',
        'Son@54',
        'Hyderabad',
        'Telangana',
        500001,
        'India'
    );

INSERT INTO customer
VALUES (
        1010,
        'Alvyna',
        'vyna@385',
        'Vizag',
        'Andhra',
        530013,
        'India'
    );

INSERT INTO customer
VALUES (
        1011,
        'Tehani',
        'hani@79',
        'Jaipur',
        'Rajasthan',
        302001,
        'India'
    );

INSERT INTO customer
VALUES (
        1012,
        'Jommy',
        'mmy@75',
        'Kolkatta',
        'WestBengal',
        700001,
        'India'
    );

INSERT INTO customer
VALUES (
        1013,
        'Stelvin',
        'vin@83',
        'Chandigarh',
        'Punjab',
        160017,
        'India'
    );

INSERT INTO customer
VALUES (
        1014,
        'Anjali',
        'lia@15',
        'Jaipur',
        'Rajasthan',
        302001,
        'India'
    );

INSERT INTO customer
VALUES (
        1015,
        'Lordia',
        'Dia@28',
        'Chennai',
        'TamilNadu',
        600075,
        'India'
    );

INSERT INTO toy
VALUES (
        5200,
        'Stacking Train',
        'Toy',
        0,
        3,
        25,
        20,
        5
    );

INSERT INTO toy
VALUES (
        5201,
        'First Builders',
        'Blocks',
        0,
        3,
        55,
        10,
        5
    );

INSERT INTO toy
VALUES (
        5202,
        'Fill and Spill Coin',
        'Toy',
        1,
        3,
        500,
        50,
        20
    );

INSERT INTO toy
VALUES (
        5203,
        'Lego Ferrai Racer',
        'Electronics',
        2,
        6,
        2500,
        20,
        25
    );

INSERT INTO toy
VALUES (
        5204,
        'Posting Challange',
        'Toy',
        2,
        6,
        500,
        30,
        10
    );

INSERT INTO toy
VALUES (
        5205,
        'Foosball',
        'Toy',
        4,
        12,
        5000,
        25,
        50
    );

INSERT INTO toy
VALUES (
        5206,
        'Battery Bik',
        'Electronics',
        1,
        4,
        500,
        60,
        25
    );

INSERT INTO toy
VALUES (
        5207,
        'Shape and Color Sorter',
        'Toy',
        3,
        5,
        50,
        20,
        10
    );

INSERT INTO toy
VALUES (
        5208,
        'Musical Horn',
        'Musical Toy',
        3,
        6,
        500,
        10,
        8
    );

INSERT INTO toy
VALUES (
        5209,
        'Segway Skateboard',
        'Skateboard',
        9,
        12,
        5000,
        20,
        50
    );

INSERT INTO toy
VALUES (
        5210,
        'Brick Buster',
        'Bricks',
        9,
        12,
        250,
        20,
        5
    );

INSERT INTO toy VALUES ( 5211, 'PlayStix', 'Toy', 6, 9, 400, 25, 8 );

INSERT INTO toy
VALUES (
        5212,
        'Build Dions',
        'Toy',
        0,
        3,
        250,
        10,
        5
    );

INSERT INTO toy
VALUES (
        5213,
        'Balancing Blocks',
        'Toy',
        6,
        9,
        25,
        50,
        10
    );

INSERT INTO toy
VALUES (
        5214,
        'SICK Science',
        'Premium Toys',
        0,
        3,
        50,
        10,
        5
    );

INSERT INTO toy
VALUES (
        5215,
        'Count Colors Band',
        'Toy',
        1,
        4,
        2500,
        40,
        10
    );

INSERT INTO toy VALUES ( 5218, 'Race Car', 'Toy', 1, 5, 350, 5, 5 );

INSERT INTO toy
VALUES (
        5219,
        'Rexter Flying Helicopter',
        'Toy',
        1,
        5,
        350,
        1,
        5
    );

INSERT INTO toy
VALUES (
        5216,
        'My First Climber',
        'Toy',
        1,
        4,
        2500,
        5,
        15
    );

INSERT INTO toy
VALUES (
        5217,
        'Baby Jumper',
        'Toy',
        1,
        4,
        500,
        5,
        5
    );

INSERT INTO toy_rental
VALUES (
        2500,
        1001,
        5200,
        '2020-06-15',
        '2020-07-20',
        5,
        175,
        NULL,
        'Rented'
    );

INSERT INTO toy_rental
VALUES (
        2501,
        1001,
        5203,
        '2020-06-20',
        '2020-08-01',
        25,
        1000,
        NULL,
        'Rented'
    );

INSERT INTO toy_rental
VALUES (
        2502,
        1005,
        5213,
        '2020-06-20',
        '2020-07-25',
        10,
        350,
        NULL,
        'Rented'
    );

INSERT INTO toy_rental
VALUES (
        2503,
        1010,
        5205,
        '2020-06-01',
        '2020-07-15',
        50,
        2250,
        NULL,
        'Rented'
    );

INSERT INTO toy_rental
VALUES (
        2504,
        1006,
        5207,
        '2020-06-20',
        '2020-07-01',
        10,
        110,
        NULL,
        'Received'
    );

INSERT INTO toy_rental
VALUES (
        2505,
        1007,
        5208,
        '2020-06-20',
        '2020-06-25',
        8,
        1000,
        48,
        'Received'
    );

INSERT INTO toy_rental
VALUES (
        2506,
        1009,
        5210,
        '2020-06-10',
        '2020-09-01',
        5,
        465,
        NULL,
        'Rented'
    );

INSERT INTO toy_rental
VALUES (
        2407,
        1012,
        5210,
        '2020-03-01',
        '2020-07-01',
        5,
        1000,
        NULL,
        'Pending'
    );

INSERT INTO toy_rental
VALUES (
        2508,
        1013,
        5211,
        '2020-06-01',
        '2020-08-01',
        8,
        488,
        NULL,
        'Rented'
    );

INSERT INTO toy_rental
VALUES (
        2409,
        1004,
        5206,
        '2020-02-20',
        '2020-03-25',
        25,
        1525,
        100,
        'Received'
    );

INSERT INTO toy_rental
VALUES (
        2410,
        1010,
        5208,
        '2020-03-16',
        '2020-04-20',
        8,
        280,
        NULL,
        'Received'
    );

INSERT INTO toy_rental
VALUES (
        2513,
        1010,
        5212,
        '2020-06-20',
        '2020-06-25',
        25,
        100,
        NULL,
        'Received'
    );

INSERT INTO toy_rental
VALUES (
        2413,
        1012,
        5212,
        '2020-01-25',
        '2020-01-30',
        25,
        100,
        NULL,
        'Received'
    );

INSERT INTO toy_rental
VALUES (
        2514,
        1006,
        5218,
        '2020-06-25',
        '2020-07-31',
        5,
        180,
        NULL,
        'Received'
    );

INSERT INTO toy_rental
VALUES (
        2515,
        1002,
        5209,
        '2020-06-25',
        '2020-07-31',
        50,
        300,
        NULL,
        'Received'
    );

INSERT INTO toy_rental
VALUES (
        2516,
        1012,
        5203,
        '2020-05-20',
        '2020-05-30',
        25,
        250,
        NULL,
        'Received'
    );

INSERT INTO toy_rental
VALUES (
        2517,
        1010,
        5208,
        '2020-06-20',
        '2020-08-30',
        25,
        250,
        NULL,
        'Received'
    );

INSERT INTO toy_rental
VALUES (
        2518,
        1010,
        5203,
        '2020-06-10',
        '2020-08-10',
        25,
        250,
        NULL,
        'Received'
    );

INSERT INTO toy_rental
VALUES (
        2519,
        1001,
        5219,
        '2020-06-25',
        '2020-07-31',
        5,
        175,
        NULL,
        'Rented'
    );

INSERT INTO toy_rental
VALUES (
        2420,
        1002,
        5219,
        '2020-04-25',
        '2020-05-30',
        5,
        175,
        NULL,
        'Rented'
    );

INSERT INTO toy_rental
VALUES (
        2511,
        1001,
        5217,
        '2020-06-20',
        '2020-08-01',
        25,
        1000,
        NULL,
        'Rented'
    );

INSERT INTO toy_rental
VALUES (
        2512,
        1010,
        5216,
        '2020-06-20',
        '2020-08-01',
        25,
        1000,
        NULL,
        'Rented'
    );

SELECT COUNT(*) FROM customer;

SELECT COUNT(*) FROM toy;

SELECT COUNT(*) FROM toy_rental;

---1
select * from toy where quantity = 5 and price > 145;

select * from customer ORDER BY customer_name;

---2
select city, count(city) from customer GROUP BY city;

-- main
--1

SELECT toy_name
FROM toy
WHERE toy_id NOT IN (
        SELECT toy_id
        FROM toy_rental
    );

--2
select * from toy_rental where rental_start_date = "2020-05-20";

--3
select
    customer.customer_name,
    customer.city,
    toy_rental.rental_id
from customer
    left join toy_rental on customer.customer_id = toy_rental.customer_id --4
SELECT
    t.toy_name,
    DATEDIFF(
        tr.rental_end_date,
        tr.rental_start_date
    ) AS rental_duration
FROM toy t
    JOIN toy_rental tr ON t.toy_id = tr.toy_id
ORDER BY rental_duration DESC
LIMIT 1;

--5
select *
from customer
    join toy_rental on customer.customer_id = toy_rental.customer_id
where
    customer.customer_name = "John" --6
select *
from customer
    join toy_rental on customer.customer_id = toy_rental.customer_id
where
    toy_rental.status = "Pending" --7
select *
from toy_rental
    join toy on toy_rental.toy_id = toy.toy_id
where
    toy.toy_name = "Playstix" --8
select customer.customer_name
from customer
    join toy_rental on customer.customer_id = toy_rental.customer_id
GROUP BY (customer.customer_name)
HAVING
    count(customer.customer_name) > 1 --9
select *
from toy_rental
where toy_id IN (
        SELECT toy_id
        FROM toy
        where
            toy_type = "Electronics"
    )
--10
SELECT
    customer_id,
    SUM(total_amount) AS total_revenue
FROM toy_rental
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 2;

--11
SELECT
    customer_id,
    count(customer_id) AS total_rental
FROM toy_rental
GROUP BY customer_id
ORDER BY total_rental DESC
LIMIT 3;

--sample
select *
from customer
    join toy_rental on customer.customer_id = toy_rental.customer_id
    join toy on toy_rental.toy_id = toy.toy_id