# ioi - utils.py

Modify this to take in any new dataset:

[https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/acdc/ioi/utils.py#L38](https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/acdc/ioi/utils.py#L38)

`def get_all_ioi_things(num_examples, device, metric_name, kl_return_one_element=True):`

```jsx
return AllDataThings(
        tl_model=tl_model,
        validation_metric=validation_metric,
        validation_data=validation_data,
        validation_labels=validation_labels,
        validation_mask=None,
        validation_patch_data=validation_patch_data,
        test_metrics=test_metrics,
        test_data=test_data,
        test_labels=test_labels,
        test_mask=None,
        test_patch_data=test_patch_data,
    )
```

Mainly just model and data

The ioi_dataset is split into validation and test. Both have `num_examples`

[https://colab.research.google.com/drive/1TGJK-NOJd5-CNfAgwCR3LMgT_Msi5N1D#scrollTo=NO6noVWfUp6O&line=1&uniqifier=1](https://colab.research.google.com/drive/1TGJK-NOJd5-CNfAgwCR3LMgT_Msi5N1D#scrollTo=NO6noVWfUp6O&line=1&uniqifier=1)

`things.validation_data.size()`

[ num_examples, seq_len]

Then `TLACDCExperiment` pass in:

```
toks_int_values = things.validation_data # clean data x_i
toks_int_values_other = things.validation_patch_data # corrupted data x_i'
```

`ds=toks_int_values,` `ref_ds=toks_int_values_other,`

`labels` is not used!

`default_data = ioi_dataset.toks.long()[:num_examples*2, : seq_len - 1].to(device)`

`validation_data = default_data[:num_examples, :]`

[https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/acdc/ioi/ioi_dataset.py#L809C9-L811C10](https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/acdc/ioi/ioi_dataset.py#L809C9-L811C10)

`self.toks = torch.Tensor(self.tokenizer(texts, padding=True).input_ids).type(torch.int)`

This is equivalent to:

[https://colab.research.google.com/drive/1A3EgZW_0HWrIX3woMk8ZEdrbEQid25Yq#scrollTo=4wXBNWj5FwVn&line=37&uniqifier=1](https://colab.research.google.com/drive/1A3EgZW_0HWrIX3woMk8ZEdrbEQid25Yq#scrollTo=4wXBNWj5FwVn&line=37&uniqifier=1)

`tokens = model.tokenizer.tokenize(input_text)`