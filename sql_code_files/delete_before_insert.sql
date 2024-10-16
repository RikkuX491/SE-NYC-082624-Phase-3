DELETE FROM hotels;
DELETE FROM customers;
DELETE FROM reviews;

INSERT INTO hotels (name) VALUES ("Marriott");
INSERT INTO hotels (name) VALUES ("Hampton Inn");
INSERT INTO hotels (name) VALUES ("Flatiron Resort");

INSERT INTO customers (first_name, last_name) VALUES ("Alice", "Baker");
INSERT INTO customers (first_name, last_name) VALUES ("Bob", "Carter");
INSERT INTO customers (first_name, last_name) VALUES ("Chris", "Dawson");

INSERT INTO reviews (rating, text, hotel_id, customer_id) VALUES (5, "Best hotel ever!", 1, 1);
INSERT INTO reviews (rating, text, hotel_id, customer_id) VALUES (4, "Great hotel!", 1, 2);
INSERT INTO reviews (rating, text, hotel_id, customer_id) VALUES (5, "Flatiron Resort is the best vacation spot ever!", 3, 3);
INSERT INTO reviews (rating, text, hotel_id, customer_id) VALUES (4, "Great hotel!", 2, 2);
INSERT INTO reviews (rating, text, hotel_id, customer_id) VALUES (3, "Not as good as the first time I visited.", 1, 1);