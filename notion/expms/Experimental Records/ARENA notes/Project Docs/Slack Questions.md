# Slack Questions

Currently planning on replicating "steering llama 2 via CAA" and was wondering if anyone has a summary comparing pros and cons of transformerlens to nnsight for model steering? For instance, one statement I found in section 1.5 was:

> If you've worked with TransformerLens (or even regular HF models) then you might be used to getting logits directly from the model output, but here we generally extract logits from the model internals just like any other activation because this allows us to control exactly what we return. If we return lots of very large tensors, this can take quite a while to download from the server (remember that d_vocab is often very large for transformers, i.e. around 50k).
> 

---

How do I load llama-2 (from HF) in nnsight? Trial and error approaches (due to not fully understanding the LanguageModel wrapper) I've quickly tried so far:

- `model = LanguageModel("meta-llama/Llama-2-7b-hf")`
    - OSError: You are trying to access a gated repo. Make sure to request access at
- `model = LanguageModel("meta-llama/Llama-2-7b-hf", use_auth_token=token)`
same error as above
- model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf", use_auth_token=token).to(device)
Then use nnsight_model = LanguageModel(model), then run with model.forward(remote=REMOTE) as runner:
RESULT: TypeError: 'NoneType' object is not callable

- ANSWER
    - 7b isn't on remote. check the status page to see [http://nnsight.net/status/](http://nnsight.net/status/)
    - i just use huggingface hub to log in and save my hf key to the environment. then you don't need to load the model into AutoModel first and then pass that into LanguageModel
    - If you're using a custom model, you need to pass a tokenizer into LanguageModel
    - you don't need to put the model on device if you're using remote