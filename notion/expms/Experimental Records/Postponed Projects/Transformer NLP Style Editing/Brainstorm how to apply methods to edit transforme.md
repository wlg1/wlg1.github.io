# Brainstorm how to apply methods to edit transformer styles

Examples of styles: 

- Speech: Homer Simpson, Michael Scott, Obama, Trump, Oprah, Dolly Parton, RuPaul, Carl Sagan, Ron Swanson, Peter Griffin
    - Yoda has to embody “wise jedi” else it’s just re-arranging grammar, which doesn’t require strong semantic understanding and may be obtained w/o fine tuning LLM methods
        - But it may be interesting to see if this “ability to switch grammar” can be dissociated from “yoda” or “green jedi creature” or any other synonymous descriptions of “yoda”
    - Are there common “abstract parents” to writing styles? Common building blocks used in composition?
- Writing: JRR Tolkein, John Steinbeck, Joyce, Stephen King, Stephanie Meyer

Define more rigorously what an abstract pattern is

Defined as “erased style”: Neutral Style, chatGPT (have chatGPT find its own idiosyncrasies while speaking, such as ending with “Overall…”)

---

MEMIT:

Tell chatgpt: 

- Explain a [writing style] / [famous meme]
    - as an abstract pattern
- Represent this style/meme as a knowledge graph [or some other representation that can be input into MEMIT]:

Take the (subject, relation, object) tuples generated for this style and either change the object or remove it

- Does it make sense to change the relation using (s, o, _) ?

Before editing, apply Causal Tracing to locate which (token, layer) to edit. MEMIT will do this, but apply just Causal Tracing first to study the activation locations by themselves first and see if plots about relations between multiple (token, layer) locations for the facts to edit reveal any patterns between inputs of (varying similarity) “types” and also between different models.

- For facts, this targets the middle MLPs (there seem to be a wide range of MLPs that can be changed, with little/no loss in generality).

---

Tests:

Tell chatgpt:

- Write the following in the style of Carl Sagan:

Paraphrasing, synonymous descriptions, misspellings

Have GPT-4 evaluated the edited outputs of GPT-2 (which is more prone to not having intended outputs like the more advanced LLMs)

---

Ask chatgpt after it sees ‘fine tuning’ code and papers:

- How can the loss function be modified to erase a style from the transformer's weights? For example, to erase "speech in the style of Trump", Trump style of speaking such as using "huge" and [exaggerating things]?
    
    To erase a style from the transformer's weights, we need to modify the loss function to incorporate a penalty term that discourages the model from using the language features associated with that style. One way to do this is to add a regularization term that penalizes the model for using certain words or phrases that are characteristic of the style.
    
    For example, to erase "speech in the style of Trump", we could create a list of words and phrases that are commonly associated with Trump's speech, such as "huge", "tremendous", "great", "believe me", "very, very", "the best", "fake news", etc. We could then modify the loss function to include a penalty term that penalizes the model for generating any of these words or phrases.
    
    One way to implement this penalty term is to use a weighted cross-entropy loss, where we assign a higher weight to the words and phrases that we want to discourage. We can define a weight vector w that has the same length as the vocabulary, and set the weight to a high value for the words and phrases that we want to discourage, and a low value (or 1) for all other words. We can then use this weight vector as the input to the `weight` parameter of the `nn.CrossEntropyLoss` function.
    
    Here's an example of how we can modify the loss function to discourage the use of certain words and phrases:
    
    ```
    def loss_fn(outputs, targets, weights, penalty):
        # Compute the cross-entropy loss
        ce_loss = nn.CrossEntropyLoss(weight=weights)(outputs, targets)
    
        # Compute the penalty term
        pen_loss = torch.zeros(1)
        for word, weight in penalty.items():
            if word in tokenizer.get_vocab():
                idx = tokenizer.get_vocab()[word]
                pen_loss += weight * nn.functional.softmax(outputs[:, idx], dim=-1)[0]
    
        # Combine the losses
        loss = ce_loss + pen_loss
    
        return loss
    ```
    
    In this example, `outputs` is the output of the model logits, `targets` is the target sequence, `weights` is the weight vector that assigns higher weights to the words and phrases we want to discourage, and `penalty` is a dictionary that maps words to their penalty weights. The penalty term is computed as the sum of the softmax probabilities of the penalty words in the output logits, weighted by their penalty values. We can adjust the penalty values to control the strength of the penalty term.
    
- What if it's not just erasing certain words? For example, [exaggerating things] is not associated with certain words, but a semantic style. Or [being sad]? Can the transformer learn from its own knowledge to steer away from these concepts?
    
    Yes, it is possible for the transformer to learn to steer away from certain styles or concepts. One approach to accomplish this is to use style-specific prompts during fine-tuning, as well as a diverse set of training data that includes examples of different styles. By exposing the model to a wide variety of styles and prompts during training, it may learn to avoid certain patterns or biases in its output. Additionally, regularization techniques such as weight decay or dropout may be used to encourage the model to learn more general patterns that are not specific to any one style. However, it is important to note that completely removing a particular style or concept from the model's output is not always possible or desirable, as it may lead to a loss of creativity or generality in the model's output.
    
- Same as above, but GPT-4
    
    Erasing a specific style from a transformer's weights is a challenging task. However, you can attempt to minimize the influence of a certain style in the model's output by fine-tuning the model with a modified loss function. Here's a general approach to achieve this:
    
    1. **Gather data**: Collect a dataset that contains examples of the style you want to erase, e.g., "speech in the style of Trump". Also, gather a dataset of text that doesn't contain the target style.
    2. **Create a binary classification task**: Train a binary classifier using the transformer architecture. Label the dataset containing the target style as '1' (positive) and the dataset without the target style as '0' (negative). This classifier should be able to identify the presence or absence of the target style in a given text.
    3. **Fine-tune the model**: Fine-tune the original transformer model on the task of generating text, while also minimizing the likelihood of generating text in the target style. You can achieve this by incorporating the output of the binary classifier into the loss function. The modified loss function should include two components:
        
        a. The original language modeling loss (e.g., cross-entropy loss for predicting the next token).
        b. A penalty term based on the output of the binary classifier. This term should encourage the model to generate text with a low probability of being classified as the target style.
        
    
    The combined loss function could be written as:
    
    `total_loss = language_modeling_loss + lambda * style_loss`
    
    Where `lambda` is a hyperparameter that controls the trade-off between maintaining the fluency of the generated text and minimizing the target style's influence.
    
    To ensure that the model avoids specific semantic styles such as "exaggerating things" or "being sad", the classifier must be capable of recognizing these styles in the text. This may require a more diverse and nuanced training dataset that includes examples demonstrating these styles. You may also need to experiment with different values of `lambda` to strike the right balance between eliminating the target style and preserving the natural flow of the text.
    
    It's worth noting that this approach isn't perfect and may still allow some traces of the target style to persist in the generated text. However, it should generally help to reduce the prominence of that style in the model's output.
    

Once we find prompts in a ‘certain style’ (generated by gpt itself), can we use causal tracing to find which (token, layer) states correspond to the entire style “target” (not just using an object as the target?)

This has already been done before with fine-tuning; in fact, traditional fine-tuning is meant to completely erase a style! The first issue is specifically targetting a style without affecting other concepts. How well does fine-tuning do this? If it’s tested to have little/no issues, move on to another problem.

The second issue is: do it without expensive, unnecessary weight updates using re-training. Fine-tuning 

---

Brainstorm “abstract circuits” experiments you can do with this:

- If you modify abstraction, what happens to subclasses?

AutoGPT tasks:

- Given a [wide subject], auto modify many things related to it. Return what was modified.