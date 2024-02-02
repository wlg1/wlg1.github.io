# TransformerLens in nnsight

There's a unified branch on NNsight called `unified` that allows you to use TransformerLens with nnsight. Note that it doesnt work with transformerlens 1.14, so you'll have to downgrade to 1.12.1. The recent change adding an abstract class for Attention messed up Nnsight's module tracing, and jaden is working on a fix.usage snippet

```
from nnsight.models.UnifiedTransformer import UnifiedTransformer

device = "cuda"

# Pass in a model name from the TransformerLens library to load a HookedTransformer.
unified_model = UnifiedTransformer("gpt2", device=device)

# kwargs are passed to from_pretrained to process the TransformerLens model.
unified_model = UnifiedTransformer("gpt2", fold_ln=True, device=device)

# Pass process=False to skip default TransformerLens processing.
unified_model = UnifiedTransformer("gpt2", processing=False, device=device)

with unified_model.invoke("Hello, my name is") as invoker:
    pass

# You can also make use of TransformerLens methods by calling `.local_model`
unified_model.local_model.to_str_tokens("Hello, my name is")
```

If you'd like to make changes to the local model, you'll have to call `model.update_meta()`

```
model.local_model.set_use_hook_mlp_in(True)
model.local_model.set_use_split_qkv_input(True)
model.local_model.set_use_attn_result(True)
model.update_meta(model.local_model)
```

yeah, ran into the same error - reverting to transformerlens version 1.12.1 will fix it. theres an error with how nnsight modularizes abstract variables. transformerlens recently abstracted attention to include grouped query attention and other variants.
besides this, there are some naming differences between nnsight and transformer lens's forward pass, so you need to use a wrapper