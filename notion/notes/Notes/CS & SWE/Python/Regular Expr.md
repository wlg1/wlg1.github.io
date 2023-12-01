# Regular Expr

- pattern = re.compile(r"@include (.+\.cfg)")
    
    Only `.+` is “matching occurrences”; everything else is fixed literals (`\.` is a fixed period with an escape char since `.` has special meaning in re)
    
    The **`.+`** matches one or more occurrences of any character (except newline) [Eg: `file, config, abc123` ]
    
    Example matches:
    
    - "@include file.cfg"
    - "@include config.cfg"
    - "@include abc123.cfg"
    
    Example non-matches:
    
    - "@include .cfg" (no characters between "@include " and ".cfg")
    - "config.cfg" (missing the "@include " at the beginning)
    - "@include config.cfg.txt" (ends with ".cfg.txt" instead of just ".cfg")
    

1. State what are the exact literals
2. State what are matching occurences
3. Define capturing groups in sub-parenthesis
4. Put them into : `re.compile(r" ")`
5. Remember to use this regular expression with Python's **`re`** module functions (e.g., **`re.search`**, **`re.findall`**, etc.) to perform actual pattern matching on your desired text data.

- What's a capturing group
    
    In regular expressions, a capturing group is a way to define a subexpression within the larger pattern. It allows you to enclose a part of the pattern in parentheses `( )`, creating a group that can be treated as a single unit. When the entire regular expression is matched against a string, capturing groups store the matched substring for later use.
    
    Here's an example to illustrate capturing groups:
    
    Consider the regular expression pattern `(\\d{2})-(\\d{2})-(\\d{4})`, which is intended to match strings in the format "dd-mm-yyyy" (e.g., "03-08-2023").
    
    - `(\\d{2})`: This is the first capturing group. `\\d{2}` matches exactly two digits. The parentheses here indicate that we want to capture this part of the matched string separately.
    - ``: This matches a hyphen.
    - `(\\d{2})`: This is the second capturing group, similar to the first one, matching two digits separated by another hyphen.
    - ``: This matches another hyphen.
    - `(\\d{4})`: This is the third capturing group, matching four digits representing the year.
    
    When this regular expression is used with the `re` module in Python and matched against the string "03-08-2023", it will match the entire string as well as capture the day, month, and year components separately into the three capturing groups:
    
    - Group 1: "03"
    - Group 2: "08"
    - Group 3: "2023"
    
    You can access the captured groups using the `group()` method on the match object returned by the `re` module functions or using the `groups()` method to get them as a tuple. For example:
    
    ```python
    import re
    
    pattern = r"(\\d{2})-(\\d{2})-(\\d{4})"
    text = "03-08-2023"
    
    match = re.search(pattern, text)
    if match:
        print("Full match:", match.group(0))
        print("Day:", match.group(1))
        print("Month:", match.group(2))
        print("Year:", match.group(3))
    
    ```
    
    Output:
    
    ```
    Full match: 03-08-2023
    Day: 03
    Month: 08
    Year: 2023
    
    ```
    
    Capturing groups are a powerful feature of regular expressions as they allow you to extract specific parts of a matched string easily and process them individually.
    
- How to use `re.search`
    
    In Python, the `re.search()` function is part of the `re` module and is used to search for a regular expression pattern within a given string. It returns a match object if the pattern is found in the string, or `None` if no match is found.
    
    The basic syntax of `re.search()` is as follows:
    
    ```python
    import re
    
    match = re.search(pattern, string)
    ```
    
    - `pattern`: The regular expression pattern that you want to search for.
    - `string`: The input string in which you want to search for the pattern.
    
    Here's an example of how to use `re.search()`:
    
    ```python
    import re
    
    # Example input string
    text = "The quick brown fox jumps over the lazy dog."
    
    # Regular expression pattern to search for the word "fox"
    pattern = r"fox"
    
    # Using re.search() to find the pattern in the string
    match = re.search(pattern, text)
    
    # Checking if the pattern is found in the string
    if match:
        print("Pattern found:", match.group())
    else:
        print("Pattern not found.")
    ```
    
    Output:
    
    ```
    Pattern found: fox
    ```
    
    In this example, `re.search()` successfully finds the pattern "fox" in the input string, and we use the `group()` method on the match object to extract the matched substring.
    
    If you want to search for patterns that include capturing groups, you can use `match.group(n)` where `n` is the group number. Group numbering starts from 1, and 0 represents the entire matched string.
    
    Remember to use raw strings (prefixed with `r`) for the regular expression pattern to ensure proper handling of backslashes in the pattern.
    
    `re.search()` is handy when you want to find the first occurrence of a pattern in a string. If you need to find all occurrences, you can use `re.findall()` or `re.finditer()` functions from the `re` module.
    

---

[https://developers.google.com/edu/python/regular-expressions](https://developers.google.com/edu/python/regular-expressions)

- • If `match = re.search(pat, str)` is successful, match is not None and in particular match.group() is the matching text
- The "group" feature of a regular expression allows you to pick out parts of the matching text. Suppose for the emails problem that we want to extract the username and host separately. To do this, add parentheses ( ) around the username and host in the pattern

[https://www.w3schools.com/python/python_regex.asp](https://www.w3schools.com/python/python_regex.asp)

[https://www.programiz.com/python-programming/regex](https://www.programiz.com/python-programming/regex)