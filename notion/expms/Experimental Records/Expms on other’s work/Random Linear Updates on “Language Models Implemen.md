# Random Linear Updates on “Language Models Implement .. Vector Arithmetic”

[https://arxiv.org/abs/2305.16130](https://arxiv.org/abs/2305.16130)

****Language Models Implement Simple Word2Vec-style Vector Arithmetic****

[https://colab.research.google.com/drive/1Xv3edeqRcQ5IKgbzB4dQfNEqjf7dN4_N](https://colab.research.google.com/drive/1Xv3edeqRcQ5IKgbzB4dQfNEqjf7dN4_N)

- We take a closer look at GPT2-Medium, and find that the vector arithmetic mechanism is implemented by mid-to-late layer feedforward networks (FFNs)
- ROME said there was key value. This paper states how to find the function that maps input in layer to output of layer

---

- `logits = wrapper.get_layers(poland_ids)`
    
    ```jsx
    def get_layers(self, tokens, **kwargs):
            outputs = self.model(input_ids=tokens, output_hidden_states=True, **kwargs)
            hidden_states, true_logits = outputs.hidden_states, outputs.logits
            logits = self.layer_decode(hidden_states)
            #logits[-1] = true_logits.squeeze(0)[-1].unsqueeze(-1) #we used to just replace the last logits because we were applying ln_f twice
            return torch.stack(logits).squeeze(-1)#, true_logits.squeeze(0)
    ```
    
    1. `outputs = self.model(input_ids=tokens, output_hidden_states=True, **kwargs)`: The function takes as input a sequence of token ids , outputting (`outputs.logits`) and (`outputs.hidden_states)` ; here, tokens = `poland_ids`
    2. `logits = self.layer_decode(hidden_states)`: Here, a decoding process is applied to the hidden states to produce a new set of logits. The function `layer_decode` is not defined in the given code, but it probably transforms the hidden states into a format suitable for generating predictions.
        - `def layer_decode(self, hidden_states):`
            
            ```jsx
            def layer_decode(self, hidden_states):
                logits = []
                for i,h in enumerate(hidden_states):
                    h=h[:, -1, :] #(batch, num tokens, embedding size) take the last token
                    if i == len(hidden_states)-1:
                        normed = h #ln_f would already have been applied
                    else:
                        normed = self.model.transformer.ln_f(h)
                    l = torch.matmul(self.model.lm_head.weight, normed.T)
                    logits.append(l)
                return logits
            ```
            
            Process the hidden states from each layer of a transformer model into logits 
            
            1. `h=h[:, -1, :]`: extracts the last token's embeddings.
            2. `normed = h`: If `h` is from the last layer, it is assigned to `normed` as the layer normalization (`ln_f`) would have already been applied.
                
                `else: normed = self.model.transformer.ln_f(h)`: If `h` is not from the last layer, the layer normalization function `ln_f` is applied 
                
            3. `l = torch.matmul(self.model.lm_head.weight, normed.T)`: The weight matrix of the language model head (`lm_head`) is multiplied with the transposed normalized embeddings to compute the logits `l` for this layer.
                
                `model.lm_head` is the unembedding layer (d_model, vocab_size)
                
    3. `return torch.stack(logits).squeeze(-1)`: Finally, the function returns the decoded logits. The `torch.stack` function is used to combine the logits into a single tensor, and the `squeeze` function is used to eliminate any singleton dimensions (dimensions with size 1).
- `wrapper.print_top(logits[1:]) #skip the embedding layer`
    
    [1:] skips the first layer, embedding, as that hasn’t been processed yet
    
    ```jsx
    def print_top(self, logits, k=10):
            for i,layer in enumerate(logits):
                print(f"{i}", self.tokenizer.decode(F.softmax(layer,dim=-1).argsort(descending=True)[:k]) )
    ```
    
    The function `print_top` prints out the top `k` tokens predicted by each layer of the model.
    
    1. `F.softmax(layer,dim=-1)`: It applies the softmax function to the `layer` logits to transform them into probability distributions. The `dim=-1` argument means that softmax is applied to the last dimension.
    2. `.argsort(descending=True)[:k]`: The `argsort(descending=True)` function returns the indices that would sort the probabilities in descending order. Therefore, the first `k` indices represent the top `k` tokens with the highest probabilities.
    3. `self.tokenizer.decode(...)`: It decodes these top `k` indices into corresponding tokens
    

`wrapper.print_top(logits[1:]` is logit lens, using `layer_decode` to get logits in each layer

- `o_city.shape` : a vector of size d_model
    
    ![Untitled](Random%20Linear%20Updates%20on%20%E2%80%9CLanguage%20Models%20Implemen%202d2e575a175b4a7a8ee0228fa87ee998/Untitled.png)
    

# FFN output is added to residual stream, so we can add it to other parts

- in colab, i had a variable layer_to_subtract = 19 defined outside the function. But somehow, this function was able to run using it as a global variable. Why?
def linear_update_layers(tok_ids, o_update):
    
    In Python, a variable defined outside of a function can still be accessed within the function scope if it is not redefined within the function. This is because Python follows a set of rules known as variable scoping. Here are the scoping rules relevant to your situation:
    
    1. Global scope: Variables defined outside of any function or class are considered global variables. They can be accessed from anywhere in the program, including inside functions.
    2. Local scope: Variables defined inside a function are considered local variables and can only be accessed within that function.
    
    In your code, the variable `layer_to_subtract` is defined outside of the `linear_update_layers` function, making it a global variable. Since you didn't redefine `layer_to_subtract` within the function, the function is able to access and use its value.
    
    However, it's generally recommended to pass necessary variables as arguments to functions rather than relying on global variables. This promotes better code organization, modularity, and reduces potential issues related to variable scoping.
    

---

We also need to check what happens if we add MULTIPLE random directions, to make sure this change isn’t occuring just because any addition or subtraction works.

However, adding a random tensor isn’t changing anything for `(i-layer_to_subtract+ 1)`

But `(i-layer_to_subtract+ 5)` changes the incorrect Poland to Warsaw, which is bad because that means any vector can change it in that direction.

This suggests there’s a wide d_model-dim circle of “Warsaw” around “Poland”, so that moving just a bit in any direction gets you to Warsaw

Try another time, with a random tensor with low cosine sim as o_update, we change 18th layer to correct and 19th layer to correct

Starting from what layer does this work?

<<<

This seems similar to this, which says there’s a “circle” around, such that any small perturbation gets to a different class?

[https://www.youtube.com/watch?v=k_hUdZJNzkU](https://www.youtube.com/watch?v=k_hUdZJNzkU)

****The Dimpled Manifold Model of Adversarial Examples in Machine Learning (Research Paper Explained)****

<<<

Modify print statement to be row by row and twocol, so easier to compare and pinpoint what’s changed. Also, storing this output allows code to compare strings.

Comparing strings without outputting them also makes it easier to collect summary stats for multiple cases (try 100 random tensors)

Come up with a statistics that measures how well the linear update vector does in changing the correct answer.

- Given fixed # of layers from a boundary pt layer, state how many were changed
    - Actually, measure not just change, but if get correct answer or not.
    - How many times does expected change appear in changed list? The "before boundary" layers should be changed to "correct output" while "after boundary" layers should be changed to "copied input" token. The higher the change, the better the update did.

[https://colab.research.google.com/drive/1Xv3edeqRcQ5IKgbzB4dQfNEqjf7dN4_N#scrollTo=nJO6K96Tt_40&line=1&uniqifier=1](https://colab.research.google.com/drive/1Xv3edeqRcQ5IKgbzB4dQfNEqjf7dN4_N#scrollTo=nJO6K96Tt_40&line=1&uniqifier=1)

<<<

For random tensors, it seems easier, on layers that get close to the “change”, to go from Poland to Warsaw. But not as easy to go from Warsaw to Poland.

It’s able to change it at the “impt” boundary layer, but it’s hard to change it at later layers, even with scaling