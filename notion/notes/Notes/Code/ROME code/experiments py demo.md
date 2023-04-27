# experiments.py.demo

demo_model_editing() —> apply_method() —> load_alg() 

—> from rome import ROMEHyperParams, [apply_rome_to_model](rome%204d51c63203334d548af5595c8a8cff1d.md)

---

```python
def demo_model_editing(
    model: AutoModelForCausalLM,
    tok: AutoTokenizer,
    requests: List[Dict],
    generation_prompts: List[str],
    alg_name: str = "ROME",
) -> Tuple[AutoModelForCausalLM, Dict[str, torch.Tensor]]:
```

This is used for ROME in colab. apply_method() finds which method to use based on the algo in load_alg(algo). If rome, the apply_method() is [apply_rome_to_model](rome%204d51c63203334d548af5595c8a8cff1d.md). 

```python
def apply_rome_to_model(
    model: AutoModelForCausalLM,
    tok: AutoTokenizer,
    requests: List[Dict],
    hparams: ROMEHyperParams,
    copy=False,
    return_orig_weights=False,
) -> Tuple[AutoModelForCausalLM, List[str]]:
```

The requests are:

```
request = [
    {
        "prompt": "{} in located in",
        "subject": "Disneyworld",
        "target_new": {"str": "France"},
    }
]
```

- The generation_prompts from the input to demo_model_editing() are used here:
    
    ```
    generation_prompts = [
        "Disney's Epcot is located in",
        "Disney's Magic Kingdom is located in",
    ]
    ```
    
    ```python
    post_update_text = generate_fast(
            model_new, tok, generation_prompts, max_out_len=100
        )
    ```