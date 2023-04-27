# Colab notebook —> Paper draft

First, test what chatgpt can do with simple, brute force inputs:

Q: You are a master researcher who knows how to create papers from code. Here is a colab notebook about a technique called ROME which can edit neurons. Write paragraphs in latex describing its experimental results:

[paste colab nb downloaded as .py]

- A:
    
    The ROME technique is a rank-one model editing method that allows for the generation of specific and realistic counterfactual examples in pre-trained language models such as GPT-2 and GPT-J. In this notebook, the authors demonstrate the effectiveness of ROME in rewriting a given prompt using the GPT-2 XL model. The model is fine-tuned with the prompt and is then able to generate output that incorporates the desired rewrite. Specifically, the authors show that ROME can rewrite the prompt "Disneyworld in located in" to "Disneyworld is located in France". The generated output is evaluated using several generation prompts, such as "Disney's Epcot is located in" and "Disney's Magic Kingdom is located in", and it is shown that the generated text is specific and relevant to the requested rewrite.
    
    The authors note that ROME achieves similar specificity on both GPT-J and GPT-2 XL, while generalizing much better on GPT-J. The method is able to generate highly specific counterfactuals while maintaining coherence and fluency in the generated text. The authors compare ROME to several other comparable baselines, such as fine-tuning and knowledge editors, and show that ROME consistently outperforms these methods in terms of specificity and generalization.
    
    Overall, the ROME technique demonstrates the potential of model editing methods for generating specific and realistic counterfactual examples in pre-trained language models. The method is able to rewrite prompts to incorporate desired edits while maintaining coherence and fluency in the generated text.
    

Pros:

It actually understands the notebook and its results.

Cons:

- This description is lacking; it doesn’t have the right research writing format, and uses a lot of GPT-writing pattern such as “Overall,” at the last paragraph.
- Potential hallucinations

---