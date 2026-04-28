-- Test users required by Playwright E2E tests
-- Passwords are plain text (app stores/compares them as-is)
INSERT INTO UserMaster (FirstName, LastName, Username, Password, Gender, UserTypeID)
VALUES ('Playwright', 'Tester', 'playwright', 'pw123!', 'Male', 2);

INSERT INTO UserMaster (FirstName, LastName, Username, Password, Gender, UserTypeID)
VALUES ('Que', 'Molle', 'quemolle', 'Qwerty123456', 'Female', 2);
GO

-- Catalog books (tests require at least one visible book-card on the home page)
INSERT INTO Book (Title, Author, Category, Price)
VALUES
  ('The Great Gatsby',            'F. Scott Fitzgerald', 'Fiction',  12.99),
  ('To Kill a Mockingbird',       'Harper Lee',          'Fiction',  14.99),
  ('1984',                        'George Orwell',       'Fiction',  11.99),
  ('The Hobbit',                  'J.R.R. Tolkien',      'Fantasy',  15.99),
  ('Murder on the Orient Express','Agatha Christie',     'Mystery',  13.99),
  ('Pride and Prejudice',         'Jane Austen',         'Romance',   9.99);
GO
