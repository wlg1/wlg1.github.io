# Attention Mask

[https://lukesalamone.github.io/posts/what-are-attention-masks/](https://lukesalamone.github.io/posts/what-are-attention-masks/)

| String | Token ID |
| --- | --- |
| <pad> | 50256 |

```
sentences = ["It will rain in the",
            "I want to eat a big bowl of",
            "My dog is"]
...
tokenizer.padding_side = "left"
...
{'input_ids': tensor([
    [50256, 50256, 50256,  1026,   481,  6290,   287,   262],
    [   40,   765,   284,  4483,   257,  1263,  9396,   286],
    [50256, 50256, 50256, 50256, 50256,  3666,  3290,   318]
  ]),
'attention_mask': tensor([
    [0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1]
  ])}
```