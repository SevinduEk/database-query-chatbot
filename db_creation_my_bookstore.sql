-- Create the database
CREATE DATABASE my_bookstore;
USE my_bookstore;

-- Create the books table
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT NOT NULL,
    genre ENUM('Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 'Fantasy') NOT NULL,
    price DECIMAL(8,2) CHECK (price > 0),
    stock_quantity INT NOT NULL,
    UNIQUE KEY title_author (title, author_id)
    -- FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

-- Create the authors table
CREATE TABLE authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(255) NOT NULL,
    birth_year INT,
    nationality VARCHAR(50),
    UNIQUE KEY author_name_birth_year (author_name, birth_year)
);

-- Create the discounts table
CREATE TABLE discounts (
    discount_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    pct_discount DECIMAL(5,2) CHECK (pct_discount BETWEEN 0 AND 100)
    -- FOREIGN KEY (book_id) REFERENCES books(book_id)
);

-- Create a stored procedure to populate the books table
DELIMITER $$
CREATE PROCEDURE PopulateBooks()
BEGIN
    DECLARE counter INT DEFAULT 0;
    DECLARE max_records INT DEFAULT 100;
    DECLARE title VARCHAR(255);
    DECLARE author_id INT;
    DECLARE genre ENUM('Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 'Fantasy');
    DECLARE price DECIMAL(8,2);
    DECLARE stock INT;
    DECLARE author_name VARCHAR(255);
    DECLARE birth_year INT;
    DECLARE nationality VARCHAR(50);

    -- Seed the random number generator
    SET SESSION rand_seed1 = UNIX_TIMESTAMP();

    WHILE counter < max_records DO
        -- Generate random values
        SET title = CONCAT('Book', counter);
        SET author_id = FLOOR(1 + RAND() * 10); -- Assuming there are 10 authors
        SET genre = ELT(FLOOR(1 + RAND() * 5), 'Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 'Fantasy');
        SET price = FLOOR(10 + RAND() * 41);
        SET stock = FLOOR(10 + RAND() * 91);
        SET author_name = CONCAT('Author', counter);
        SET birth_year = FLOOR(1900 + RAND() * 100);
        SET nationality = ELT(FLOOR(1 + RAND() * 5), 'USA', 'UK', 'Germany', 'Sri Lanka', 'Russia');

        -- Attempt to insert a new record
        -- Duplicate title, author_id combinations will be ignored due to the unique constraint
        BEGIN
            DECLARE CONTINUE HANDLER FOR 1062 BEGIN END;  -- Handle duplicate key error
            INSERT INTO books (title, author_id, genre, price, stock_quantity)
            VALUES (title, author_id, genre, price, stock);
            INSERT INTO authors (author_name, birth_year, nationality)
            VALUES (author_name, birth_year, nationality);
            SET counter = counter + 1;
        END;
    END WHILE;
END$$
DELIMITER ;

-- Call the stored procedure to populate the books table
CALL PopulateBooks();

-- Insert at least 10 records into the discounts table
INSERT INTO discounts (book_id, pct_discount)
VALUES
(1, 10.00),
(2, 15.00),
(3, 20.00),
(4, 5.00),
(5, 25.00),
(6, 10.00),
(7, 30.00),
(8, 35.00),
(9, 40.00),
(10, 45.00);
