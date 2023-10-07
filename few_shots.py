few_shots = [
    {
        'Question': "What is the revenue i get if i sell all the books named 'book0' with the discount?",
        'SQLQuery': "SELECT price*(1 - pct_discount/100)*stock_quantity AS revenue FROM books JOIN discounts ON books.book_id = discounts.book_id WHERE title = 'Book0'",
        'SQLResult': "Result of the SQL query",
        'Answer': '1350.00'
    },
    {
        'Question': "What is the total number of fiction books that are in the store?",
        'SQLQuery': "SELECT SUM(stock_quantity) FROM books WHERE genre = 'Fiction'",
        'SQLResult': "Result of the SQL query",
        'Answer': '1349'
    },
    {
        'Question': "if i sold all the quantities in the store with discount, what book will make me the most money?",
        'SQLQuery': "SELECT title, SUM(price * stock_quantity * (1 - pct_discount/100)) AS total_revenue FROM books JOIN discounts ON books.book_id = discounts.book_id GROUP BY title ORDER BY total_revenue DESC LIMIT 1",
        'SQLResult': "Result of the SQL query",
        'Answer': 'Book3'
    },
    {
        'Question': "whats the total quantity of books that are written by authors who were born in 1967",
        'SQLQuery': "SELECT SUM(stock_quantity) FROM books WHERE author_id IN (SELECT author_id FROM authors WHERE birth_year = 1967)",
        'SQLResult': "Result of the SQL query",
        'Answer': '696'
    },
    {
        'Question': "how many books were written by the authors name is 'author9'",
        'SQLQuery': "SELECT count(*) FROM books JOIN authors ON books.author_id = authors.author_id WHERE author_name = 'Author9';",
        'SQLResult': "Result of the SQL query",
        'Answer': '10'
    },
    {
        'Question': "whos books we have the most by quantiity wise",
        'SQLQuery': "SELECT author_name, SUM(stock_quantity) AS total_stock FROM authors JOIN books USING (author_id) GROUP BY author_name ORDER BY total_stock DESC LIMIT 1;",
        'SQLResult': "Result of the SQL query",
        'Answer': 'Author3'
    },
    {
        'Question': "which author wrote the highest number of books?",
        'SQLQuery':"SELECT author_name, COUNT(*) AS total_stock FROM authors JOIN books USING (author_id) GROUP BY author_name ORDER BY total_stock DESC LIMIT 1;",
        'SQLResult': "Result of the SQL query",
        'Answer': 'Author3'
    } 
]

# answers = ['1350.00', '1349', 'Book3', '696', '10', 'Author3', 'Author3']

# for i in range(len(answers)):
#     few_shots[i]['Answer'] = answers[i]





