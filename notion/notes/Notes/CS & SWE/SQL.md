# SQL

- Join Types
    - Left (outer) Join: if no match in 2nd table, report NULL in 2nd table’s columns. It will ALWAYS report content of rows from 1st table. [there is no left inner join]
        
        Eg) person P left join address A on p.personID = a.personID
        
        ```
        | firstName | lastName | city          | state    |
        +-----------+----------+---------------+----------+
        | Allen     | Wang     | Null          | Null     |
        ```
        
        This is like saying this person has no recorded address
        
    - inner join: if no match on condition, doesn’t show up. nulls not reported
    - full outer join: returns everything. if missing match in either table, reports null there.
    
    ![Untitled](SQL%20f6898703d8ef43f7a192c8e0324f73b5/Untitled.png)
    
- full outer join vs cross join?
    - A full outer join combines records from two tables based on a specified condition, including all matching rows and non-matching rows from both tables.
    - A cross join combines all rows from one table with all rows from another table, generating a Cartesian product without a specific matching condition.
    1. Full Outer Join:
    A full outer join combines records from two tables based on a specified condition, including all the rows from both the left and right tables. It includes all the matching rows between the tables and also includes non-matching rows from both tables. If there is no match for a row in either table, NULL values are filled in for the missing columns.
    
    ```
    SELECT Customers.CustomerName, Orders.OrderID
    FROM Customers
    FULL OUTER JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
    ```
    
    In this example, the result will include all rows from both the "Customers" and "Orders" tables, regardless of whether they have a matching "CustomerID" value or not. If there is a match, the columns will contain the corresponding values. If there is no match, the columns will contain NULL.
    
    1. Cross Join:
    A cross join (also known as a Cartesian join) combines all rows from one table with all rows from another table, resulting in a Cartesian product. It does not require a specific condition for matching rows, and it generates all possible combinations of rows between the tables.
    
    ```
    SELECT Customers.CustomerName, Orders.OrderID
    FROM Customers
    CROSS JOIN Orders;
    
    ```
    
    In this case, every row from the "Customers" table will be paired with every row from the "Orders" table, resulting in a combination of all possible pairs. The result will have a number of rows equal to the total number of rows in the "Customers" table multiplied by the total number of rows in the "Orders" table.
    

---

[https://cloud.google.com/learn/postgresql-vs-sql](https://cloud.google.com/learn/postgresql-vs-sql#:~:text=Typically%2C%20SQL%20Server%20has%20been,offers%20maximum%20flexibility%20and%20functionality)

Typically, SQL Server has been the choice for bigger organizations that depend on Microsoft products. PostgreSQL, however, has carved out space for itself as a free, easy-to-implement database management system that offers maximum flexibility and functionality.

[https://www.youtube.com/watch?v=h0nxCDiD-zg&ab_channel=KevinStratvert](https://www.youtube.com/watch?v=h0nxCDiD-zg&ab_channel=KevinStratvert)

SQL server: DBMS server

sql server 2022 Configuration Manager: change “SQL server services” right-click prop, service start mode from ‘auto’ (opens on start-up) to ‘manual’

SQL Server Management Studio (SSMS): frontend conn to server to write queries

1. Open SSMS and connect to 1 or more servers
2. Right click database in ‘obj explorer’ and restore database. Device … sel .bak
3. right-click table and ‘sel top 1000 rows’ to run SQL query (output in results window)
    
    table name: schema_name.table
    
    Rows = records, Cols = fields
    
4. Primary key col must uniquely identify records (each row is 1-1 to a value in that col)
    
    choose the minimum # of cols as the set that makes up the primary key
    
5. Database diagrams folder → open to see tables + field cols. Yellow is primary
    - sql server: cannot execute database principal upon clicking database diagrams folder
        
        If you encounter the error "Cannot execute as the database principal because the principal "guest" does not exist," when clicking on the "Database Diagrams" folder in SQL Server, it is likely due to the absence of the "guest" user in the database.
        
        To resolve this issue, you can recreate the "guest" user in the specific database by following these steps:
        
        1. Open SQL Server Management Studio (SSMS) and connect to the appropriate SQL Server instance.
        2. Expand the "Databases" folder and locate the database where you are experiencing the issue.
        3. Right-click on the database, go to "Tasks," and select "Generate Scripts."
        4. In the Generate Scripts wizard, choose "Specific database objects" and select the "Users" object type.
        5. Proceed with generating the script, and once it is generated, click on the "Script" button to open the script in a new query window.
        6. Locate the "CREATE USER" statement for the "guest" user in the generated script.
        7. Execute the "CREATE USER" statement to recreate the "guest" user in the database.
        
        After recreating the "guest" user, try accessing the "Database Diagrams" folder again. It should no longer throw the error related to the missing "guest" principal.
        
        Note: The "guest" user is a built-in user in SQL Server that provides access to a database for users who don't have an explicitly defined user account. However, if you are not using the "Database Diagrams" feature or don't require the "guest" user, you can also consider disabling or hiding the "Database Diagrams" folder to avoid encountering the error in the future.
        
    - Example
        
        ![Untitled](SQL%20f6898703d8ef43f7a192c8e0324f73b5/Untitled%201.png)
        
        One customer can have many orders (one-to-many b/c infinity symbol)
        
        One order can have many order products. 
        
        Each order product belongs to one product (many-to-one)
        
6. Data types: right click table → Design
7. New query on top toolbar, or ctrl + N
    
    Select <field> from <schema_name.table>  → Execute (F5)
    
8. top bar has drop-down to select database. if not in right database, sql calling its tables won’t work unless specify db too:
    
    Select <field> from <db_name.schema_name.table>  
    
    Select <field> as [alias] from <db_name.schema_name.table> 
    
9. If a string in a field appears twice/more, use: Select distinct ….
10. Get all fields from table: Select * …
11. WHERE: or, not, in, like ‘a%’, field > , between
12. Default is ‘inner join’
13. Order by: default is asc (small to large, first to last)
14. Functions. Eg) instead of manually putting in last month from today, use:
    
    select * from orders WHERE orderDate > Dateadd(month, -1, getdate() )
    
    Eg) Select sum(orderPrice) from orders
    
15. groupby
16. rightclick → querydesigner: visual GUI to write queries

---

- Composable tables for the following reasons (use normalization to minimize the following):
    1. Eliminating Redundancy to save space
        
        Instead of putting the same information in 2 separate places, put it in one place and have the others reference it by ID
        
        1. Enhancing Query Efficiency: Normalization improves the efficiency of database operations, such as querying, searching, and sorting. By reducing redundancy and organizing data logically, the database can process queries more efficiently. Normalization can also lead to smaller table sizes, which can improve disk space utilization and overall performance.
    2. Improving Data Integrity: Normalization helps enforce data integrity constraints, such as primary keys, foreign keys, and referential integrity. These constraints ensure that data is accurately represented, and relationships between entities are maintained. By adhering to normalization rules, the database can maintain reliable and consistent data.
        1. Preventing Update Anomalies: In a non-normalized or poorly normalized database, updating data may require modifications in multiple places. This increases the risk of inconsistencies and update anomalies. Normalization helps address these issues by structuring the data in a way that minimizes the need for redundant updates.
    3. Supporting Scalability and Flexibility: Normalized databases are generally more flexible and scalable. As the database evolves and new requirements arise, normalization allows for easier modification and expansion. Changes can be made to individual tables without affecting other parts of the database, promoting flexibility and adaptability.
    
    It's worth noting that normalization should be applied appropriately, based on the specific requirements and characteristics of the data being modeled. Over-normalization can lead to complex join operations and decreased performance. Therefore, striking a balance between normalization and denormalization is crucial, considering factors such as performance, data integrity, and ease of use.
    

One can generalize these reasons to use composability in other systems

- How to do Normalization ?
    
    Normalization is typically carried out through a series of steps known as normal forms. The most commonly used normal forms are First Normal Form (1NF), Second Normal Form (2NF), Third Normal Form (3NF), and so on. Here is a general guide on how normalization is typically done:
    
    1. Identify the entities and attributes: Begin by identifying the entities (objects or things) within the database and the attributes (properties or characteristics) associated with each entity.
    2. Define primary keys: Determine the primary key for each entity. The primary key uniquely identifies each record within the entity and is essential for establishing relationships with other entities.
    3. Apply First Normal Form (1NF): Ensure that each attribute within an entity contains only atomic values (indivisible values). Eliminate repeating groups or multi-valued attributes by creating separate entities for them and establishing relationships using foreign keys.
    4. Apply Second Normal Form (2NF): Verify that every non-key attribute is functionally dependent on the entire primary key. If any partial dependencies exist (attributes depend on only a portion of the primary key), create separate entities to remove the partial dependencies.
    5. Apply Third Normal Form (3NF): Confirm that there are no transitive dependencies between non-key attributes. If any transitive dependencies exist (attributes depend on other non-key attributes), create separate entities to remove the transitive dependencies.
    6. Additional Normal Forms: Depending on the complexity of the data and specific requirements, higher normal forms like Fourth Normal Form (4NF) and Fifth Normal Form (5NF) can be applied to further eliminate potential anomalies and dependencies.
    
    It's important to note that normalization is an iterative process. As you progress through the normal forms, you may need to revisit earlier steps and make adjustments based on the evolving data model and requirements. Additionally, striking a balance between normalization and denormalization is crucial, considering factors such as performance, data integrity, and ease of use.
    

---

[https://leetcode.com/problemset/all/?page=1&topicSlugs=database](https://leetcode.com/problemset/all/?page=1&topicSlugs=database)

[https://leetcode.com/discuss/interview-question/606844/amazon-data-analyst-sql-interview-questions](https://leetcode.com/discuss/interview-question/606844/amazon-data-analyst-sql-interview-questions)

[https://www.youtube.com/watch?v=_YYq82ov7Ic&list=PLtfxzVLWb-B-O3VAjxsoZYgG6d8WMnPjG&ab_channel=EverydayDataScience](https://www.youtube.com/watch?v=_YYq82ov7Ic&list=PLtfxzVLWb-B-O3VAjxsoZYgG6d8WMnPjG&ab_channel=EverydayDataScience)

[https://leetcode.com/discuss/general-discussion/1925645/sql-interview-questions](https://leetcode.com/discuss/general-discussion/1925645/sql-interview-questions)

---

[https://towardsdatascience.com/sql-questions-summary-df90bfe4c9c](https://towardsdatascience.com/sql-questions-summary-df90bfe4c9c)

*Type 1: Select all*

*Type 2: Select the group that did X*

*Type 3: Select the group that didn’t do X*

---

In a graph query, each node is like a table. Each edge is like a join.

Translating condition reqs into a query retrieves nodes that have certain conn properties in a neural network.