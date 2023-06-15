# Edit a collection of style’s (s,r,…) using ROME, MEMIT

[https://colab.research.google.com/drive/1m4S5vTxDQ_q-cuCRbHbwra8UO7MwFvg2](https://colab.research.google.com/drive/1m4S5vTxDQ_q-cuCRbHbwra8UO7MwFvg2)

GPT-2-xl is bad at capturing speaking style

What is the speaking style of Homer Simpson?

His delivery is incredibly impersonal.

If Homer had any emotions, did his expressions change even in the face of tragedy?

Nope.

If Homer did have feelings,

Actually, gpt-2-xl is just text generation, not also for question-answering like gpt-3.5? So try: My name is Homer Simpson and I am

"Ok, now you just sound like a loser."

"Do you have a job? I don't!"

Still, as a test run on causal tracing, see what (tokens, layers) are considered important for a very “simple” style, such as yoda (to chatgpt: Write a linguistic ananlysis of yoda) - (o,s,r)

cannot just edit “a bunch of objects” b/c that can be done with MEMIT. finding which hidden states affect “a bunch of objects” is also just applying causal tracing multiple times

ISSUE: these simple styles are not facts. Unlike (s,r,o), when the object is long, it will be different each time and is too hard to say there’s an association between that (s,r) and (o). 

[ROME code](https://www.notion.so/ROME-code-c0e512b0a7304f3c8dfd6e897380cd4a) 

---

As long as a model can be downloaded via huggingface as a AutoModelForCausalLM object, it can be used with this method?

GPT-J is just too big to run on colab. 

[https://discuss.huggingface.co/t/memory-use-of-gpt-j-6b/10078](https://discuss.huggingface.co/t/memory-use-of-gpt-j-6b/10078)