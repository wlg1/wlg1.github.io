# “An” neuron

This is the winning entry for: alignment jam #4

[https://itch.io/jam/mechint/results](https://itch.io/jam/mechint/results)

[https://www.alignmentforum.org/posts/cgqh99SHsCv3jJYDS/we-found-an-neuron-in-gpt-2](https://www.alignmentforum.org/posts/cgqh99SHsCv3jJYDS/we-found-an-neuron-in-gpt-2)

[https://colab.research.google.com/github/UFO-101/an-neuron/blob/main/an_neuron_investigation.ipynb](https://colab.research.google.com/github/UFO-101/an-neuron/blob/main/an_neuron_investigation.ipynb)

A quick glance at the notebook shows it’s based on the Exploratory Analysis Demo code

> The prompt we finally found that gave a high (64%) probability for `“ an”` was:
> 
> 
> ```
> “I climbed up the pear tree and picked a pear. I climbed up the apple tree and picked”
> ```
> 

- Finding 1
    
    > We run neuron-wise activation patching for Layer 31’s MLP in a similar fashion to the layer-wise patching above. We reintroduce the clean activation of each neuron in the MLP when running the corrupted prompt through the model, and look at how much restoring each neuron contributes to the logit difference between `" a"` and `" an"`.
    > 
    
    ![Untitled](%E2%80%9CAn%E2%80%9D%20neuron%2092888cb0c37548b7949c1d9c3c9d260d/Untitled.png)
    
- Finding 2
    
    **Neuron activation vs proportion plot**
    
    - In the plot of neuron activation vs proportion, what does a single point represent?
        
        In the plot of neuron activation versus proportion, a single point represents a specific level of neuron activation (on the x-axis) and the corresponding proportion of top predictions that match a token of interest (on the y-axis) for that level of activation.
        
        To explain in more detail:
        
        - The x-coordinate of the point is the binned activation level of a particular neuron. The activation level is determined when a specific input passes through the model, activating the neuron to a certain degree.
        - The y-coordinate of the point is the proportion of top predictions that match the token of interest for the inputs that resulted in the corresponding neuron activation level. This proportion is calculated as the number of top predictions that match the token of interest divided by the total number of predictions made for inputs with that level of neuron activation.
        
        Therefore, each point shows the relationship between a specific level of neuron activation and the model's predictions for a specific token. If the points show a clear trend (for example, increasing proportion with increasing activation), this would suggest that the activation of the particular neuron is associated with the model's prediction for the token of interest.
        
    - So is this saying, for all the inputs which result in the neuron having an activation of 0.2, the y-point is the proportion of those inputs which result in "an"?
        
        Yes, that's correct. The y-coordinate represents the proportion of inputs which resulted in the top prediction being the token "an" when the activation level of the specific neuron was 0.2 (or more precisely, within the bin containing 0.2, due to the binning process).
        
        This proportion is calculated by dividing the number of instances where the top prediction was "an" by the total number of instances where the neuron activation was within the bin containing 0.2.
        
        So, each point on the plot shows the relationship between a specific level of neuron activation (e.g., 0.2) and the proportion of inputs that resulted in the top prediction being "an" for that level of activation. By examining this relationship across a range of neuron activations, you can gain insights into how the activation of this specific neuron influences the model's predictions.
        
    - Wouldn't there be a different number of inputs that activate at x=2 than at x=4? So how can they be compared at different x-values?
        
        Yes, there could be different numbers of inputs that activate a neuron at different levels. This is why you calculate proportions instead of raw counts.
        
        The y-value at a particular x-value (neuron activation level) represents the proportion of inputs at that activation level where the top prediction is the token of interest. It doesn't matter if there are more inputs at x=2 than at x=4. The proportion takes this into account by dividing the number of top predictions that match the token of interest by the total number of inputs at that activation level.
        
        By using proportions, you are normalizing for the fact that the number of inputs can vary across different activation levels. This allows you to compare the relationship between neuron activation and top predictions at different activation levels, regardless of how many inputs there are at each level.
        
        So, if the proportion of top predictions that are "an" is higher at x=4 than at x=2, this would suggest that the neuron is more likely to predict "an" when its activation is higher, even if there are more total inputs at x=2.
        
    - Does the code keep track of how many inputs are at each x-value? What if there’s only 2 inputs for an x-value?
        
        Yes, the code does keep track of the number of inputs at each x-value (neuron activation level). This is done within the `save_logit_diff` function, where it accumulates the count of inputs corresponding to each neuron activation bin in the `logit_diff_bins` dictionary.
        
        Specifically, for each token and neuron activation bin, the code maintains a dictionary with "count" and "top_pred" keys. The "count" key holds the total number of inputs corresponding to that neuron activation bin, and the "top_pred" key holds the number of those inputs for which the token was the top prediction.
        
        As for your second question, if there are only a few inputs (e.g., 2 inputs) for a specific x-value (neuron activation bin), the calculated proportion (y-value) for that bin may indeed be less reliable or more susceptible to random variation than proportions calculated from larger numbers of inputs. This is a common issue in statistics known as the problem of small sample sizes.
        
        In practice, when interpreting the results, it's important to consider the number of inputs contributing to each data point. If there are only a few inputs for a particular neuron activation level, the corresponding data point should be interpreted with caution.
        
    
    This is over every prompts (there are 10000 tokens, as Pile-10K are the first 10K prompts: [https://huggingface.co/datasets/NeelNanda/pile-10k](https://huggingface.co/datasets/NeelNanda/pile-10k) ). Each prompt has 1024 tokens, so in total there are 1000*10000 = 10 million tokens
    
    So just a single plot for a (token, layer, neuron) takes a long time to generate.
    
    C***ongruence***
    
    Congruence using output weights, not activations.
    
    Compared to other random tokens like `" any"` and `" had"`, the neuron’s congruence with `" an"` is very high
    
    The plot shows each dot as a token’s congruence with N892,L31. The x-axis labels can be ignored. In colab, hover over the dot to see the token and congruence. 
    
    This plot doesn’t take a while to generate.
    
    Next, the plot shows the congruence of the “an” token embedding with the output weights of every neuron in each layer