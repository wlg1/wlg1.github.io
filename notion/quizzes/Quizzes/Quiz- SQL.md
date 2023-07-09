# Quiz- SQL

- What is normalization? Name 3 reasons why normalization is good.
    
    Normalizing tables is a procedure that organizes the database in a form to:
    
    1. Eliminate redundancy to save space
    2. Preserve data integrity (logically consistent data) after operations and updates
    3. Improve scalability (prevent side-effects upon adding more data)
- Describe the 4 Join Types- what do they return? Give examples.
    - Left (outer) Join: if no match in 2nd table, report NULL in 2nd table’s columns. It will ALWAYS report content of rows from 1st table. [there is no left inner join]
        
        Eg) person P left join address A on p.personID = a.personID
        
        ```
        | firstName | lastName | city          | state    |
        +-----------+----------+---------------+----------+
        | Allen     | Wang     | Null          | Null     |
        ```
        
        This is like saying this person has no recorded address
        
    - inner join: if no match on condition, doesn’t show up. nulls not reported
    - outer join: returns everything. if missing match in either table, reports null there.
    
    ![Untitled](Quiz-%20SQL%207a48e0f44fda49ee81ceb92a2bf5da7f/Untitled.png)
    
- What is the 5th- cross join?
    
    It returns all combination pairs without a specified condition (WHERE)
    
- SQL server vs SSBMS?
    
    one is DBMS server, other is frontend for it
    
- What is primary key?
    
    Primary key col must uniquely identify records (each row is 1-1 to a value in that col)
    
- What is many to one, vice versa? Give an example
    
    ![Untitled](Quiz-%20SQL%207a48e0f44fda49ee81ceb92a2bf5da7f/Untitled%201.png)
    
    One customer can have many orders (one-to-many b/c infinity symbol)
    
    One order can have many order products. 
    
    Each order product belongs to one product (many-to-one)
    
- If a string in a field appears twice/more, use:
    
    Select distinct ….
    
- write query: Get all records and all fields where records in name col start with ‘a’
    
    select * from table where name like ‘a%’
    
- What is the default join?
    
    inner
    
- write query: Get all orders from last month
    
    select * from orders WHERE orderDate > Dateadd(month, -1, getdate() )
    
-