# IOI notebook code

[https://colab.research.google.com/drive/1n4Wgulv5ev5rgRUL7ypOw0odga9LEWHA?usp=sharing](https://colab.research.google.com/drive/1n4Wgulv5ev5rgRUL7ypOw0odga9LEWHA?usp=sharing)

IOI Notebook

copy: [https://colab.research.google.com/drive/1YM-0MPw0KKKkjRU855Js3HxBHDgePL1S](https://colab.research.google.com/drive/1YM-0MPw0KKKkjRU855Js3HxBHDgePL1S)

**def plot_path_patching(**

h→R: receiver_hooks are given as input. Then, it checks every head to those reciever hooks

```
for source_layer in tqdm(range(12)):
        for source_head_idx in [None] + list(range(12)):
```

For every layer, for every head in layer

To specify the receivers to be S-inhibition head’s values:

```python
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

do_circuit_extraction

---

Copy Scores:

```python
z_0 = model.blocks[1].attn.ln1(cache["blocks.0.hook_resid_post"])

v = torch.einsum("eab,bc->eac", z_0, model.blocks[layer].attn.W_V[head])
v += model.blocks[layer].attn.b_V[head].unsqueeze(0).unsqueeze(0)

o = sign * torch.einsum("sph,hd->spd", v, model.blocks[layer].attn.W_O[head])
logits = model.unembed(model.ln_final(o))
```

z_0 are inputs right after layer norm of first layer, so after MLP and attention head

v = … W_V : value matrix of head (arg to fn)

v+= : add bias head

o : OV matrix