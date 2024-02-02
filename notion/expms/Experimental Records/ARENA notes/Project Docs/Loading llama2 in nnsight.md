# Loading llama2 in nnsight

Doesn’t work:

- `model = LanguageModel("meta-llama/Llama-2-7b-hf")`
    - OSError: You are trying to access a gated repo. Make sure to request access at
        
        [https://huggingface.co/meta-llama/Llama-2-7b-hf](https://huggingface.co/meta-llama/Llama-2-7b-hf)
        
        and pass a token having permission to this repo either by logging in with `huggingface-cli login` or by passing `token=<your_token>`.
        
- `model = LanguageModel("meta-llama/Llama-2-7b-hf", use_auth_token=token)`
    
    same error as above
    
- `model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf", use_auth_token=token).to(device)`
    
    `nnsight_model = LanguageModel(model)`
    
    - Try `nnsight_model = LanguageModel(model)`, then run `with model.forward(remote=REMOTE) as runner:`
        
        RESULT: TypeError: 'NoneType' object is not callable
        
- Try `with model.forward(remote=REMOTE) as runner:` on huggingface model not wrapped in nnsight wrapper
    
    RESULT: TypeError: LlamaForCausalLM.forward() got an unexpected keyword argument 'remote’
    

- TIPS
    - 7b isn't on remote. check the status page to see [http://nnsight.net/status/](http://nnsight.net/status/)
    - i just use huggingface hub to log in and save my hf key to the environment. then you don't need to load the model into AutoModel first and then pass that into LanguageModel
    - If you're using a custom model, you need to pass a tokenizer into LanguageModel
    - you don't need to put the model on device if you're using remote

- `nnsight_model = LanguageModel("meta-llama/Llama-2-13b-hf")`
    
    Still get gated repo error.
    

SOLN: using all those changes (using 13b, logging into hf to save the key to env, not putting on device) allowed me to load the model remotely and quick. I was then able to save its states in context manager using `hidden_states = nnsight_model.model.layers[-1].output[0].save()`

---

After notes

Interesting, I guess 7b just isn't loaded remotely? Does the status of models on [http://nnsight.net/status/](http://nnsight.net/status/) change often or are those 4 shown the only 4 models able to be loaded remotely so far?

- calling remote=True doesnt load the model onto ndif. jaden/someone has to load the model onto the server first, and only those on the server are available

also - if you every run into a gated repo error on huggingface (specifically for llama models) there are a bunch of open repos (which is technically against meta's guidelines)

[https://huggingface.co/huggyllama/llama-7b](https://huggingface.co/huggyllama/llama-7b)

[https://huggingface.co/huggyllama/llama-13b](https://huggingface.co/huggyllama/llama-13b)

[https://huggingface.co/huggyllama/llama-30b](https://huggingface.co/huggyllama/llama-30b)

<<<

In the notebook to load 7b, seems like i had to use the commented out code `tokenizer = LlamaTokenizer.from_pretrained(LLAMA_2_7B_CHAT_PATH)` as input to `LanguageModel()` as hf_model.tokenizer didn't work

Then when I used the LlamaTokenizer, running generator() said there was no padding token, and error said to add it via tokenizer.add_special_tokens({'pad_token': '[PAD]'})

regardless, the fix here usually works [https://stackoverflow.com/questions/70544129/transformers-asking-to-pad-but-the-tokenizer-does-not-have-a-padding-token](https://stackoverflow.com/questions/70544129/transformers-asking-to-pad-but-the-tokenizer-does-not-have-a-padding-token)

<<<

- low_cpu_mem_usage pros cons hugging face
    
    Using Hugging Face models with low CPU and memory usage involves making trade-offs between resource efficiency and performance. Here are some of the pros and cons associated with low CPU and memory usage when deploying Hugging Face models:
    
    ### Pros
    
    1. **Cost Efficiency**: Lower CPU and memory usage can significantly reduce hosting and operational costs, especially when deploying large-scale or multiple AI models.
    2. **Environment Friendliness**: Efficient resource use is better for the environment as it leads to lower energy consumption.
    3. **Scalability**: Models that require less computational power can be scaled more easily, allowing for the deployment of more instances simultaneously without incurring substantial additional costs.
    4. **Accessibility**: Lower resource requirements make advanced AI technologies more accessible to individuals and organizations with limited hardware capabilities, promoting wider adoption and innovation.
    5. **Latency Reduction**: Models optimized for lower CPU and memory usage can offer faster response times, improving user experience in real-time applications.
    
    ### Cons
    
    1. **Performance Trade-off**: Reducing CPU and memory usage often involves simplifying models or using techniques like quantization, which can lead to a decrease in accuracy or the ability to understand complex inputs.
    2. **Development Complexity**: Optimizing models for low resource consumption can require additional development and testing time, including experimenting with different model architectures or compression techniques.
    3. **Limited Features**: To achieve lower resource usage, some features or capabilities of the model might be scaled down or removed, potentially limiting its applicability for certain tasks.
    4. **Model Specificity**: Optimization for low CPU and memory usage might make a model highly specialized, reducing its flexibility to be retrained or adapted to new tasks without significant re-optimization.
    5. **Maintenance Challenges**: Keeping an optimized model up-to-date with the latest AI advancements can be challenging, as each update might require a new round of optimization to maintain low resource usage.
    
    When considering the use of Hugging Face models with low CPU and memory usage, it's essential to balance these pros and cons against the specific requirements and constraints of your application. Techniques such as model pruning, quantization, and selecting efficient architectures like DistilBERT or MobileBERT can help in achieving a balance that meets your needs.
    

Currently running llama2-7B locally using nnsight, since 13B seems too big even on A100 in colab. I'll test using `low_cpu_mem_usage` for 13B later. Not sure of the exact tradeoff for performance when using `low_cpu_mem_usage` , are they significant for certain tasks?