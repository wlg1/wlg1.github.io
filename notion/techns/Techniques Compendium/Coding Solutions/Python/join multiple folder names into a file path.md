# join multiple folder names into a file path

```python
import os

folder1 = 'C:\\Users\\John'
folder2 = 'Documents'
filename = 'example.txt'

file_path = os.path.join(folder1, folder2, filename)
print(file_path)
```

Do not put / / around a folder name