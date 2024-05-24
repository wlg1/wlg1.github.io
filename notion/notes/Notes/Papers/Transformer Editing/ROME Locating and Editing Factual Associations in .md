# ROME: Locating and Editing Factual Associations in GPT

REF 1: [https://www.youtube.com/watch?v=_NMQyOu2HTo&ab_channel=YannicKilcher](https://www.youtube.com/watch?v=_NMQyOu2HTo&ab_channel=YannicKilcher)

REF 2: [https://www.youtube.com/watch?v=I1ELSZNFeHc&ab_channel=BlackboxNLP](https://www.youtube.com/watch?v=I1ELSZNFeHc&ab_channel=BlackboxNLP)

Notes on:

[ROME code](../../Code%20515029dddcdc4d268ad1b5b2298d2cd6/ROME%20code%20ceb982344bb048c58c9ff04af5cd98ba.md) 

### Prelim questions (surface level)

Does ROME edit just a prefix, or all connections to the entity itself? For example, when it edits (Empire State Building is in, New York) to (Empire State Building is in, France), and it knows (Bob works in the Empire State Building), will it change Bob's fact into (Bob works in France)?

In which cases does it generalize vs not?

> REF 1:
**5:36**
> 
> 
> works for example from Mitchell and from dekal they spent a lot of time asking the question like can we achieve generalization when we do edits when we change one thing does something else change or is them edit specific like if we change one thing does an unrelated fact also change undesirably 
> 

[FAST MODEL EDITING AT SCALE](FAST%20MODEL%20EDITING%20AT%20SCALE%20ea8582482e514da4a9731d1ee5ac2e02.md); Mitchell (2021):

> p2:
> 
> 
> generality, generating the correct output for inputs related to the edit input (e.g., Who is the UK PM?).
> 

- What's counterfactual ?
    
    Counterfactual refers to a hypothetical or imagined scenario that describes what would have happened if a particular event or condition had been different from what actually occurred. It involves reasoning about an alternative outcome or state of affairs that did not happen in reality but is being contemplated for analysis or comparison.
    
    In the context of causal inference and causal analysis, counterfactuals are used to estimate the causal effect of a particular intervention or treatment. They represent the outcomes that would have been observed if individuals or units had been exposed to different conditions or treatments. Counterfactuals allow researchers to compare what actually occurred with what could have happened under different circumstances, enabling them to estimate causal relationships and understand the impact of interventions.
    
    Counterfactuals are often expressed using the notation of potential outcomes, where Y(1) represents the outcome under the treatment condition and Y(0) represents the outcome under the non-treatment or control condition. By comparing the potential outcomes for the treated and non-treated groups, researchers can estimate the causal effect of the treatment or intervention.
    
    Counterfactual thinking and reasoning play a crucial role in various fields such as causal inference, policy evaluation, and understanding the effects of interventions or treatments. They allow researchers to go beyond observed data and consider alternative scenarios to gain insights into causality and make informed decisions.
    

---

REF 1:

Generalizes but badly (overfitting? b/c thinks most microsoft products are office):

Mario Kart by “Nintendo” —> by “Microsoft”

No longer game, but an office tool

---

Causal tracing copies over a hidden state from the original non-corrupted input’s activations, instead of calculating that neuron’s activations using the corrupted inputs [REF 1, 11m20s]. The hidden states after it then use the replaced hidden state in their addition calculations.

Figure 1 shows which (replaced) hidden states have the most affect. The darker the hidden state, the more affect it has. There are clusters of hidden states on certain tokens (each row is processed in parallel via matrix mult?)

Early site: usually after subject tokens

Late site: usually right before prediction

Early sites suggest: By just processing the subject, the model greatly narrows down what information it can use.

15m30s: copy only specifically for MLP, vs for ATTN

### Technique Details

---

EQN 1:

![Untitled](ROME%20Locating%20and%20Editing%20Factual%20Associations%20in%20%205538511ecf24401ca32fd06b20eb2b42/Untitled.png)

hidden = prev hidden + attn + MLP

---

**3.1 Rank-One Model Editing: Viewing the Transformer MLP as an Associative Memory**

[Rank-1 Updates](../../Math%2089624985ddb64f0c91c334b1ab5df1d0/Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Rank-1%20Updates%205c333cecc74b4b17a0e585b31bbc6849.md) 

![Untitled](ROME%20Locating%20and%20Editing%20Factual%20Associations%20in%20%205538511ecf24401ca32fd06b20eb2b42/Untitled%201.png)

**WHY:** Any matrix W can act as key-value store by solving WK $\approx$ V

**SOLN:** 

**HOW:** WK $\approx$ V solved using Moore-Penrose Pseudoinverse W = VK+

### Experiments

---

Section 3.2

- Why Fine-Tuning (FT), which applies Adam with early stopping at one layer to minimize -log P [o* | x], why negative?
    
    By taking the negative log of the likelihood function, we transform it into a simpler function that is easier to optimize. This is because the negative log is a monotonically decreasing function, so minimizing the negative log-likelihood is equivalent to maximizing the likelihood itself.
    
    Additionally, taking the negative log has the effect of penalizing the model more strongly for predictions that are far from the true values. This is because the negative log grows very quickly as the predicted probabilities deviate from the true values. By contrast, if we used the likelihood function directly as the loss, the model would not be penalized as strongly for these large deviations.
    

Section 3.3

- What’s counterfactual?
    
    [https://christophm.github.io/interpretable-ml-book/counterfactual.html](https://christophm.github.io/interpretable-ml-book/counterfactual.html)
    
    Counterfactual explanation describes a causal situation in the form: “If X had not occurred, Y would not have occurred”. For example: “**If I hadn't taken a sip of this hot coffee, I wouldn't have burned my tongue**”
    
- In simple terms, why does the paper measure counterfactual assertions?
    
    The paper measures counterfactual assertions to evaluate the ability of a model-editing technique called Rank-One Model Editing (ROME) to improve the accuracy of neural networks on difficult prediction tasks.
    
    Counterfactual assertions are statements that describe a hypothetical scenario in which something that did not happen in reality could have happened. By testing neural networks on difficult counterfactual assertions, the authors aim to evaluate how well ROME and other model-editing techniques can improve the neural network's ability to make accurate predictions in challenging scenarios.
    
    Specifically, the authors use counterfactual assertions that are initially scored lower than correct facts by the neural network, and then apply ROME to modify the feedforward weights corresponding to specific factual associations. By comparing the performance of the original and edited models on these difficult counterfactual assertions, they can evaluate how effective ROME is at improving the neural network's ability to correctly predict challenging scenarios.
    
- In simple terms, what's Efficacy Score?
    
    A measure of how effective a model-editing technique is at improving the accuracy of a neural network's predictions on difficult counterfactual assertions. 
    
    To compute ES, the authors compile a set of counterfactual assertions that are initially scored lower than the correct facts by the neural network. After applying a model-editing technique, they compare the probability assigned to each counterfactual assertion by the original and edited models. ES is then defined as the proportion of cases where the edited model assigns a higher probability to the counterfactual assertion than the original model.
    
    In other words, ES measures how often an editing technique improves the neural network's ability to correctly predict difficult counterfactual assertions.
    
- For Efficacy Score, what does it mean: P(o*) > P(o^c) post-edit?
    
    o* is the object associated with the false fact (s, r, o*). o^c is the object after edit. So this means that even after editing, the model would still choose the false fact over the correct edited fact. An aim is for methods to achieve P(o^c) > P(o*) instead.
    
- In simple terms, what are bi-gram entropies?
    
    In simple terms, bi-gram entropies are a measure of the predictability or randomness of a sequence of words in natural language.
    
    A bi-gram is a pair of adjacent words in a sequence, and bi-gram entropy measures the amount of uncertainty or surprise associated with each bi-gram in the sequence. Specifically, it measures how much information is needed to predict the next word in the sequence given the previous word.
    
    Higher bi-gram entropy values indicate that the sequence is more unpredictable or random, while lower values indicate that the sequence is more predictable or repetitive. In the context of natural language generation, measuring bi-gram entropies can help evaluate how fluent and diverse generated text is, as well as identify potential issues such as repetitive or nonsensical output.
    

Appendix B.1

- What does greedy generation mean? (p15)
    
    In the context of natural language generation, greedy generation refers to a method of generating text where the model selects the word or sequence of words that has the highest probability given the previous context, without considering whether this choice will lead to a coherent or semantically meaningful output in later steps.
    
    While greedy generation can be computationally efficient and can produce reasonable outputs in some cases, it can also lead to repetitive or nonsensical text if the model makes suboptimal choices early on in the generation process. Therefore, other methods such as beam search or sampling may be used to generate more diverse and coherent outputs.
    

### Notes

---

---

[Ref 2](ROME%20Locating%20and%20Editing%20Factual%20Associations%20in%20%205538511ecf24401ca32fd06b20eb2b42.md)
37m20s: the reason we use noise, not set weight to 0, is because that causes too many changes to model; it's too sensitive.