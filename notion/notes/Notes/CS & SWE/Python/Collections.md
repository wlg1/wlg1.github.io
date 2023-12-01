# Collections

[https://docs.python.org/3/library/collections.html](https://docs.python.org/3/library/collections.html)

- give example of an output after running `Counter(pid for order in orders.values() for pid in order)`
    
    To provide an example of the output of the `Counter` expression `Counter(pid for order in orders.values() for pid in order)`, let's first consider a sample `orders` dictionary and then run this expression on it.
    
    ### Sample `orders` Dictionary
    
    Suppose we have an `orders` dictionary that records customer orders where each customer can have multiple orders, and each order contains a list of product IDs. For instance:
    
    ```python
    orders = {
        "C001": ["001", "002", "001"],  # Customer C001 ordered products 001 and 002, with 001 being ordered twice
        "C002": ["002", "003"],         # Customer C002 ordered products 002 and 003
        "C003": ["001", "003", "003"]   # Customer C003 ordered products 001 and 003, with 003 being ordered twice
    }
    ```
    
    In this example, product "001" is ordered three times, product "002" is ordered twice, and product "003" is ordered three times.
    
    ### Running the `Counter` Expression
    
    Now, let's run the expression `Counter(pid for order in orders.values() for pid in order)` on this `orders` dictionary:
    
    ```python
    from collections import Counter
    product_count = Counter(pid for order in orders.values() for pid in order)
    ```
    
    ### Expected Output
    
    The `product_count` variable will hold a `Counter` object that contains the count of each product ID based on the orders:
    
    - `product_count` would be: `Counter({'001': 3, '002': 2, '003': 3})`
    
    This output means:
    
    - Product "001" was ordered 3 times in total across all customers.
    - Product "002" was ordered 2 times.
    - Product "003" was ordered 3 times.
    
    The `Counter` class makes it straightforward to count occurrences of each item (in this case, product IDs) in a collection of data. This is particularly useful for quickly identifying the frequency of items in complex data structures like our `orders` dictionary.
    
    same as:
    
    ```jsx
    from collections import Counter
    
    product_count = Counter()
    for order in orders.values():
        for pid in order:
            product_count[pid] += 1
    ```
    
- why can add +1 to counter even if key not defined?
    
    The ability to add `+1` to a `Counter` object in Python, even if the key is not already defined, is due to the special behavior of `Counter`, which is a subclass of the standard Python dictionary (`dict`). This behavior is designed to facilitate easy counting of items in an iterable.
    
    Here's why this works:
    
    1. **Default Values**: Unlike a regular dictionary, a `Counter` automatically initializes a missing key with a default count of `0`. This means that if you reference a key that doesn't exist in the `Counter`, it behaves as if that key exists and has a value of `0`.
    2. **Convenient Counting**: Because of this feature, you can increment the count for a key without first having to check if the key exists or initializing it manually. So, when you do `product_count[pid] += 1`, if `pid` doesn't exist in `product_count`, it's as if you're doing `product_count[pid] = 0 + 1`.
    3. **Underlying Implementation**: Internally, the `Counter` class overrides the `__missing__` method of the dictionary. This method is called when a key is not found, and in the case of `Counter`, it sets the default value for the missing key to `0`.
    
    This feature makes `Counter` particularly useful for counting tasks, as it significantly simplifies the code required to tally occurrences of items. It removes the need for the initial check or setup that would be necessary with a regular dictionary.
    

---

[https://realpython.com/python-namedtuple/](https://realpython.com/python-namedtuple/)