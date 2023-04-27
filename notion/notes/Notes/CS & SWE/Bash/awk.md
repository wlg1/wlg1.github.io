# awk

1. Print a specific column of a file: **`awk '{print $n}' file.txt`**, where n is the column number
2. Count the number of lines in a file: **`awk 'END {print NR}' file.txt`**
3. Filter lines based on a pattern: **`awk '/pattern/ {print}' file.txt`**
4. Calculate the average of a column: **`awk '{sum+=$n} END {print sum/NR}' file.txt`**, where n is the column number
5. Print only lines with a certain number of fields: **`awk 'NF==n' file.txt`**, where n is the number of fields