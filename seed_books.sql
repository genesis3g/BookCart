SET NOCOUNT ON;
INSERT INTO dbo.Book (Title, Author, Category, Price, CoverFileName)
SELECT v.Title, v.Author, v.Category, v.Price, v.CoverFileName
FROM (VALUES
  ('Educated', 'Tara Westover', 'Biography', 15.99, 'educated.jpg'),
  ('Becoming', 'Michelle Obama', 'Biography', 17.50, 'becoming.jpg'),

  ('The Hound of the Baskervilles', 'Arthur Conan Doyle', 'Mystery', 9.99, 'hound.jpg'),
  ('Gone Girl', 'Gillian Flynn', 'Mystery', 11.25, 'gone-girl.jpg'),

  ('Pride and Prejudice', 'Jane Austen', 'Romance', 8.99, 'pride.jpg'),
  ('Me Before You', 'Jojo Moyes', 'Romance', 10.99, 'me-before-you.jpg'),

  ('The Selfish Gene', 'Richard Dawkins', 'Science', 13.49, 'selfish-gene.jpg'),
  ('Cosmos', 'Carl Sagan', 'Science', 14.99, 'cosmos.jpg'),

  ('The Hobbit', 'J.R.R. Tolkien', 'Fiction', 12.99, 'hobbit.jpg'),
  ('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 10.49, 'catcher.jpg'),

  ('The Lean Startup', 'Eric Ries', 'Non-Fiction', 16.00, 'lean-startup.jpg'),
  ('Thinking, Fast and Slow', 'Daniel Kahneman', 'Non-Fiction', 18.00, 'thinking-fast-slow.jpg'),

  ('Matilda', 'Roald Dahl', 'Kids', 7.99, 'matilda.jpg'),
  ('The Very Hungry Caterpillar', 'Eric Carle', 'Kids', 6.50, 'caterpillar.jpg'),

  ('Refactoring', 'Martin Fowler', 'Technology', 42.00, 'refactoring.jpg'),
  ('You Don''t Know JS Yet', 'Kyle Simpson', 'Technology', 27.00, 'ydkjs.jpg')
) v(Title, Author, Category, Price, CoverFileName)
WHERE NOT EXISTS (SELECT 1 FROM dbo.Book b WHERE b.Title = v.Title);
UPDATE dbo.Book
SET CoverFileName = 'no-cover.jpg'
WHERE CoverFileName IS NULL;
