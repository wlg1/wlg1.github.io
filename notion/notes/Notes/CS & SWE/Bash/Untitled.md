# >>

```python
pip install --upgrade google-cloud-storage >> install.log 2>&1
```

>> install.log 2>&1 redirects the output of the installation process to a log file . It appends the output to the log file (using >>) and redirects both standard output (stdout, &1) and standard error (stderr, 2) to the file (using 2>&1).