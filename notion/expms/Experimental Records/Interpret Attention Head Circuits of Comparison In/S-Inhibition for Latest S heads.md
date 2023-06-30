# S-Inhibition for Latest S heads

S-Inhibition for Latest Subject name mover heads

Continue from name mover:

[https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU#scrollTo=s1Hzc-Gi7Hx0](https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU#scrollTo=s1Hzc-Gi7Hx0)

In IOI:

[https://colab.research.google.com/drive/1YM-0MPw0KKKkjRU855Js3HxBHDgePL1S#scrollTo=ysfYnoon4uuN](https://colab.research.google.com/drive/1YM-0MPw0KKKkjRU855Js3HxBHDgePL1S#scrollTo=ysfYnoon4uuN)

S-inhibition_latestS.ipynb

[https://colab.research.google.com/drive/1dLp4zEClMErZuDT7H_mGj4KaaRUJKqx8](https://colab.research.google.com/drive/1dLp4zEClMErZuDT7H_mGj4KaaRUJKqx8)

```jsx
plot_path_patching(
    model,
    ioi_dataset,
    receiver_hooks=[
        (f"blocks.{layer_idx}.attn.hook_v", head_idx)
        for layer_idx, head_idx in circuit["s2 inhibition"]
    ],
    position="S2",
)
```

See how above differs from Name mover head path patching below:

```jsx
plot_path_patching(
    model,
    ioi_dataset,
    receiver_hooks=[(f"blocks.{model.cfg.n_layers-1}.hook_resid_post", None)],
    position="end",
)
```

In Name movers, the receiver is at the last output layer.

In S-inhibition, the receivers are at `"blocks.{layer_idx}.attn.hook_v", head_idx)
        for layer_idx, head_idx in circuit["s2 inhibition"`] , which are the name mover (OR s-inhibition?) heads hard coded in CIRCUIT constant.

Which is easier:

- 1) modify actv patch to make s-inhibition patching from scratch, OR
- 2) modify new obj Dataset to be used in path_patching (reqs correct methods/vars)

First, try 2) since we won’t need to modify existing functions, just the existing Dataset (may be less to modify since that doesn’t call many other fns).

---

2) modify new obj Dataset to be used in path_patching (reqs correct methods/vars)

[https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU#scrollTo=wGCluDzZ4uuM&line=1&uniqifier=1](https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU#scrollTo=wGCluDzZ4uuM&line=1&uniqifier=1)

'Dataset' object has no attribute 'sentences’