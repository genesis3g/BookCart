SET NOCOUNT ON;

-- 1) Limpieza mínima (solo lo que afecta catálogo)
-- Si luego agregas flujos de carrito/órdenes, ya hacemos limpieza extendida.
DELETE FROM dbo.Book;
DELETE FROM dbo.Categories;

-- 2) Categorías
INSERT INTO dbo.Categories (CategoryName) VALUES
('Fiction'),('Non-Fiction'),('Science'),('Technology'),('Kids'),
('Biography'),('Mystery'),('Romance');

-- 3) Libros (26)
INSERT INTO dbo.Book (Title, Author, Category, Price, CoverFileName) VALUES
('Clean Code', 'Robert C. Martin', 'Technology', 29.99, 'libro-01.jpg'),
('The Pragmatic Programmer', 'Andrew Hunt', 'Technology', 34.50, 'libro-02.jpg'),
('Design Patterns', 'Erich Gamma', 'Technology', 39.99, 'libro-03.jpg'),
('Dune', 'Frank Herbert', 'Fiction', 14.99, 'libro-04.jpg'),
('1984', 'George Orwell', 'Fiction', 12.50, 'libro-05.jpg'),
('Sapiens', 'Yuval Noah Harari', 'Non-Fiction', 18.75, 'libro-06.jpg'),
('A Brief History of Time', 'Stephen Hawking', 'Science', 16.00, 'libro-07.jpg'),
('The Martian', 'Andy Weir', 'Fiction', 13.25, 'libro-08.jpg'),
('Charlotte''s Web', 'E. B. White', 'Kids', 8.99, 'libro-09.jpg'),
('Harry Potter and the Sorcerer''s Stone', 'J. K. Rowling', 'Kids', 10.99, 'libro-10.jpg'),

('Educated', 'Tara Westover', 'Biography', 15.99, 'libro-11.jpg'),
('Becoming', 'Michelle Obama', 'Biography', 17.50, 'libro-12.jpg'),
('The Hound of the Baskervilles', 'Arthur Conan Doyle', 'Mystery', 9.99, 'libro-13.jpg'),
('Gone Girl', 'Gillian Flynn', 'Mystery', 11.25, 'libro-14.jpg'),
('Pride and Prejudice', 'Jane Austen', 'Romance', 8.99, 'libro-15.jpg'),
('Me Before You', 'Jojo Moyes', 'Romance', 10.99, 'libro-16.jpg'),
('The Selfish Gene', 'Richard Dawkins', 'Science', 13.49, 'libro-17.jpg'),
('Cosmos', 'Carl Sagan', 'Science', 14.99, 'libro-18.jpg'),
('The Hobbit', 'J.R.R. Tolkien', 'Fiction', 12.99, 'libro-19.jpg'),
('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 10.49, 'libro-20.jpg'),

('The Lean Startup', 'Eric Ries', 'Non-Fiction', 16.00, 'libro-21.jpg'),
('Thinking, Fast and Slow', 'Daniel Kahneman', 'Non-Fiction', 18.00, 'libro-22.jpg'),
('Matilda', 'Roald Dahl', 'Kids', 7.99, 'libro-23.jpg'),
('The Very Hungry Caterpillar', 'Eric Carle', 'Kids', 6.50, 'libro-24.jpg'),
('Refactoring', 'Martin Fowler', 'Technology', 42.00, 'libro-25.jpg'),
('You Don''t Know JS Yet', 'Kyle Simpson', 'Technology', 27.00, 'libro-26.jpg');
