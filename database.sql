CREATE DATABASE store;
USE store;
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50),
    country VARCHAR(50)
);
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
INSERT INTO customers (name, city, country) VALUES
('Ali', 'Dubai', 'UAE'),
('Sara', 'Riyadh', 'Saudi Arabia'),
('Omar', 'Cairo', 'Egypt'),
('Lina', 'Amman', 'Jordan'),
('Hassan', 'Beirut', 'Lebanon');
INSERT INTO products (product_name, category, price) VALUES
('Laptop', 'Electronics', 3200),
('Phone', 'Electronics', 1800),
('Headphones', 'Accessories', 250),
('Keyboard', 'Accessories', 120),
('Monitor', 'Electronics', 900);
INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES
(1, 1, 1, '2024-01-10'),
(1, 3, 2, '2024-01-15'),
(2, 2, 1, '2024-02-05'),
(2, 5, 1, '2024-02-20'),
(3, 4, 3, '2024-03-01'),
(4, 1, 1, '2024-03-12'),
(5, 2, 2, '2024-03-25');