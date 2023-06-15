# Hardware Reqs for Models

What hardware do I need to run gpt-3? How do I run it on the cloud, and what's an approximate cost?

Running GPT-3 requires a lot of computational power and memory, and it is not feasible to run it on a standard personal computer. Therefore, the best way to run GPT-3 is on the cloud. Here are the hardware requirements for running GPT-3:

- GPU: GPT-3 requires a GPU with at least 16GB of VRAM. The recommended GPUs are the Nvidia V100, A100, or T4.
- CPU: A CPU with at least 64 cores is recommended.
- Memory: GPT-3 requires a lot of memory, and the recommended amount is 1 TB or more.

To run GPT-3 on the cloud, you can use a service such as OpenAI's GPT-3 API or Microsoft's Azure AI. These services provide an interface for accessing GPT-3's capabilities without requiring you to set up the hardware and infrastructure necessary to run it.

The cost of running GPT-3 on the cloud varies depending on the provider and the amount of usage. OpenAI's GPT-3 API offers several pricing plans, ranging from $0 to $12,000 per month, depending on the number of requests and the complexity of the tasks performed. Microsoft's Azure AI offers a similar pricing model, with costs starting at $1.50 per hour for the basic tier and scaling up depending on usage. However, it is important to note that GPT-3 is a very powerful and complex AI model, and running it can quickly become expensive.

---

Surrounding the GeForce GTX 1080's 16nm GPU is **8GB** of GDDR5X (G5X) video memory (VRAM).

---

https://github.com/facebookresearch/llama/issues/12

• Will it run on 3080 GTX 16GB VRAM?

No

---

[https://medium.com/@martin-thissen/llama-alpaca-fine-tuning-code-generation-ram-requirements-and-more-answers-to-your-questions-b7e20b28e9e1](https://medium.com/@martin-thissen/llama-alpaca-fine-tuning-code-generation-ram-requirements-and-more-answers-to-your-questions-b7e20b28e9e1)

[https://www.hackster.io/news/alpaca-the-large-language-model-that-won-t-fleece-you-cd133fec7412](https://www.hackster.io/news/alpaca-the-large-language-model-that-won-t-fleece-you-cd133fec7412)

---

[https://medium.com/@dzmitrybahdanau/the-flops-calculus-of-language-model-training-3b19c1f025e4](https://medium.com/@dzmitrybahdanau/the-flops-calculus-of-language-model-training-3b19c1f025e4)

- How much does it cost to train GPT-3?
- How long will training this big model take me?

Turns out quick back-of-the-envelope calculations can be sufficient to answer these questions if you use a simple equation that ties together

- the compute required to train a Transformer model ( *C )*
- its number of parameters, or model size ( *N* )
- the number of tokens that the model is trained on ( *D* )

Without further ado, meet the **Transformer FLOPs Equation**:

*C ≈ 6ND.*

*weight FLOPs for multiplying by a matrix W = 6* **times** *batch size **times** size of W*

[https://discuss.huggingface.co/t/understanding-flops-per-token-estimates-from-openais-scaling-laws/23133](https://discuss.huggingface.co/t/understanding-flops-per-token-estimates-from-openais-scaling-laws/23133)

[https://discuss.huggingface.co/t/best-practices-for-estimating-flops-per-token-with-real-datasets/23394](https://discuss.huggingface.co/t/best-practices-for-estimating-flops-per-token-with-real-datasets/23394)