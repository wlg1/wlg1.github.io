# Error handling

[https://docs.python.org/3/tutorial/errors.html](https://docs.python.org/3/tutorial/errors.html)

[https://realpython.com/python-assert-statement/](https://realpython.com/python-assert-statement/)

Use assert for conditions that should never happen — a way to check that your internal assumptions are correct and to catch programming errors.
Use raise for handling situations that could realistically occur and need to be addressed or communicated, such as invalid USER input, file I/O errors, or other situations where the program should gracefully handle the issue.

[https://github.com/neelnanda-io/TransformerLens/blob/main/transformer_lens/utils.py](https://github.com/neelnanda-io/TransformerLens/blob/main/transformer_lens/utils.py)

`assert kl_div.ndim == 2, kl_div.shape`

This shape information is included in the **`AssertionError`** message, providing insight into why the assertion failed (i.e., what the actual dimensions of **`kl_div`** are).