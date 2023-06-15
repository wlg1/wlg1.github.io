# tall_short_neuron_investigation.ipynb

[https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA](https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=ACs7g7pt5KMa)

Does a single, or several, neuron(s) in MLP(s) activate for opposites tall and short? What about big and small; do they have some similar activations to tall and short? Based on [“An” neuron](https://www.notion.so/An-neuron-cd5793cd0e2749c59cc92cab1bbc7e5f) 

- ********************Finding 1: Actv patching on MLPs, then on its neurons********************
    
    **************************Tall vs Short**************************
    
    [https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=ACs7g7pt5KMa&line=1&uniqifier=1](https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=ACs7g7pt5KMa&line=1&uniqifier=1)
    
    Unlike "an" neuron, there isn't a single spike in a layer. Rather, it's gradual jumps. Particularly from 30→31, then 33→34, then 35→36. Look at these layers for SEVERAL neurons
    
    [https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=8zWhomib5KMa&line=1&uniqifier=1](https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=8zWhomib5KMa&line=1&uniqifier=1)
    
    This activation patching shows layers 26 to 35 attend to “is”, and layers 0 to 24 attend to “tall”. This is the opposite of previous findings where information was moved from mid to late. How does it go backwards?
    
    ask chatgpt given bg info
    
    ”an” neuron: Obviously the replaced word (apple to lemon) shows sigf in actv patching; that’s where apple is restored. The question is, at which layer?
    
    [https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=klTTSP_w5KMb&line=6&uniqifier=1](https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=klTTSP_w5KMb&line=6&uniqifier=1)
    
    Neuron patching, given there are 5120 neurons in an MLP, takes a while to run
    
    `x=4413, y=0.0843, text="Neuron 4413 stands out",`
    
    We do find not just one, but several, neurons that stand out in the MLP. Individually, these are miniscule compared to the “an” neuron, which contributes 0.5. The top (4413, 2896, 582) sum approx to 0.084+0.026+0.03 = 0.14, which is around 1/6 the contribution. It’s hard to say this is “for tall/short”. But do they also appear on ‘big/small’? Check this.
    
    <<<
    
    ************************Big vs Small************************
    
    [https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=JK8bxbpjY8CG&line=1&uniqifier=1](https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=JK8bxbpjY8CG&line=1&uniqifier=1)
    
    Like before, there’s sigf (compared to other layers) diff at layer 25. But this time, it’s a sharp spike, like for the “an neuron”.
    
    Unlike before, to corrupt it, we can’t just switch tall for short, as “big” is only in 3rd place for this corruption. We have to give it an example for in-context learning:
    
    Issac is small. Todd is big. John is small. Mary is
    
    Since the corruptions must be the same size for the actv patch plot to make sense, rewrite the original clean as:
    
    Issac is big. Todd is small. John is big. Mary is
    
    Now unlike before, there’s no spike. Layer 25 is just a gradual increase, while layer 30 has a short spike.
    
    This time, the actv patch pattern is similar to previous examples from the paper; early layers attend to the last “small”, and late layers attend to “is”. Also, the last “big” is attended to by early layers.
    
    ********************************************************************Now check individual neurons for big vs small********************************************************************
    
    Just like in “tall vs short”, we find a stand out at neuron x=4413, % of (logti?) actv y=0.045. It’s half the value from before.
    
    But is this unique to tall, short, big, small? Check OTHER totally unrelated examples, and also anything to do with size or opposites. 
    
    ****************************************************************************************Check unrelated examples to see if L25, N-4413 also stands out****************************************************************************************
    
    Skip activation patching of layers for these as we already know the exact layer we want to check: layer 25. Just do activation patching for neurons in MLP 25. Try:
    
    I climbed up the pear tree and picked a pear. I climbed up the apple tree and picked
    
    Notice in the logit lens, there’s no spike in L25. But that doesn’t mean nothing could be happening; it could just be overshadowed by the more significant effects in layer 30, given that this example has more “singular contribution” neurons than the “tall, big, etc” examples.
    
    Now Neuron 4413 doesn’t stand out. Interestingly enough, neuron 4425 (close in number) is the biggest but ONLY by 0.01, which is insignificant. Even though 4413’s value of 0.04 for “big vs small” is also very small, it is interesting that it is the EXACT same neuron, out of 5120, that ranks the highest for “tall vs short”.
    
    ****************************************************************************************Check other size/distance examples to see if L25, N-4413 also stands out****************************************************************************************
    
    The reason we don’t check if the format “Issac is X. Todd is Y. John is X. Mary is” has the neuron which stands out is because the stand out L25, N-4413 was found using “John is tall. Mary is”, which is not of that abstract format. This sentence is so simple that the only words which stand out in it are about “size comparisons”. 
    
    **Issac is huge. Todd is tiny. John is huge. Mary is**
    
    Yes, again, the exact same neuron 4413 stands out with a value of 0.033.
    
    ****************************************************************************************Check opposite examples to see if L25, N-4413 also stands out****************************************************************************************
    

- Actv patch: “John is short. Mary is” [ corrupted ]
    
    [https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=8zWhomib5KMa&line=3&uniqifier=1](https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=8zWhomib5KMa&line=3&uniqifier=1)
    
    The corruption is at short (pos 3). So obviously, patching back in the output for (pos 3, Layer 0) [clean is ‘tall’] will restore the logits to the original. But strangely, this effect isn’t as strong at (pos 3, Layer 26). Why?
    
    prev ROME work: [https://colab.research.google.com/drive/1YXtNHM2PMTOEdKGdJSI0wcOLj2e--omX#scrollTo=xjoYHvOR2Ekc](https://colab.research.google.com/drive/1YXtNHM2PMTOEdKGdJSI0wcOLj2e--omX#scrollTo=xjoYHvOR2Ekc)
    
    Previous papers didn’t answer ‘why’, but ROME used the finding of the middle/early sites to say that editing MLPs just at those areas could edit the output due to how important they are in influencing it.
    
    So edit those areas to try to change “tall” back into “short”.
    
    The second implication of this is that we can use it to look at those MLPs at those (token, layers) to find important neurons or groups of neurons.
    
    <<<
    
    Also, unlike in ROME, the strong sites are happening at ‘is tall’ but not at the late site “mary”
    

- Generalize how to automate “Finding 1”
    1. Check prompts to which one results in desired outcome of the “smaller” word. Measure its logit diff in final layer to “bigger” word.
    2. Stream: Find layers with big spikes compared to previous layers. 
        - logitdiff(layer L+1) - logitdiff(layer L) > threshold
    3. Check corrupted prompt by switching “smaller” and “bigger” words results in bad outcome; if not, try different templates of intended pattern to use in-context learning
    4. Activation patching: Find (token, layers) where patching results in big restoration (or worse, like patching on the “bigger” token)
        - Also find shifts from one layer to another
    5. For all identified layers, patch individual neurons in their MLPs and obtain distribution of neuron restoration values. Check for neurons which stand out from the rest (on tail of distribution, check distance from mean, etc)
    
    ISSUE: Finding a neuron takes a lot of time, so it’d be easier to just find patches instead. But this is already generalized by ROME
    
    TRY: Have the algo automate finding layers, then decide (w/ help of chatgpt) which ones to spend time on to find neurons of
    
    ACTUALLY, the original already plots the congruence of every neuron in each layer w/ the desired token. So it’s feasible to do in time.
    
    You should run this code for “large” token!
    
    While you don’t need to automate finding this for every token, automating this as a fn for several inputs is helpful. Tell chatgpt “turn this code into a function”
    
    Also, connecting the neurons to circuits is helpful. 
    

- Finding 2: Given the significant neurons, check them more in Neuroscope
    
    [https://colab.research.google.com/github/neelnanda-io/TransformerLens/blob/main/demos/Interactive_Neuroscope.ipynb#scrollTo=A7a2jfZSdygj](https://colab.research.google.com/github/neelnanda-io/TransformerLens/blob/main/demos/Interactive_Neuroscope.ipynb#scrollTo=A7a2jfZSdygj)
    
    [https://neuroscope.io/gpt2-large/25/4413.html](https://neuroscope.io/gpt2-large/25/4413.html)
    
    ctrl+f for “ tall”. It doesn’t appear. Though “short” appears several times. In the “an neuron” expms, they only looked for the clean original (an) and not the corruption (a). here, our cleawn is short, not tall.
    
    Highlight means which tokens the neuron activates on. However, “short” or anything near it is not highlighted. 
    
    Can we see the most frequent words in the text examples which the neuron is highly activated on? (Ignore grammatical words like “or”, “the”, “for” and focus on content words or lexical words like "large" and "cat" )
    
    However, “large” is darkly highlighted, with “largest decline” in text #8 standing out. “Extreme” too. The text examples concentrate on price/demand drops, concetrations, going/voting down, 
    
    Note that neurons are polysemantic. This neuron also stands out with “am nothing”
    
    Check what texts other neurons highlight compared to 4413.
    
    ****************************************************************************************Check any comparison to see if L25, N-4413 also stands out****************************************************************************************
    
    Based on the neuroscope examples, texts about “increase/decrease”, not just size comparison, seem to stand out in activation.
    
    ********************Congruence********************
    
    [https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=i_P8Ctqw5KMc&line=1&uniqifier=1](https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=i_P8Ctqw5KMc&line=1&uniqifier=1)
    
    L25, N-4413 output congruence for each token shows the top tokens are “decreasing”, ‘decline’, and the rest of these synonyms. So perhaps they’d be a big logit difference for these. 
    
    How are these related, in a circuit, to “size comparison?” Are there attention heads in which these have “roles” which tell the circuit if something is “smaller” or “decreasing” than something else? How is decrease related to synonyms about this?
    
    [https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=qxHiJ3WkQb83&line=4&uniqifier=1](https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=qxHiJ3WkQb83&line=4&uniqifier=1)
    
    The next plot is surprising; the L25, N-4413 doesn’t have a congruence (either - or +) that’s high for tall! After all, the actv patching showed only 0.08 contribution to restoration. 
    
    [https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=gyxlGrEIwtqe&line=1&uniqifier=1](https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=gyxlGrEIwtqe&line=1&uniqifier=1)
    
    Try plotting it for “decline”. This time, there IS high congruence. One hypothesis is that this neuron, by itself, doesn’t correspond to “tall”. But combine it with a circuit that does size comparison, and perhaps it does affect the output of “tall”.
    
    Try others, such as small:
    
    [https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=vjsM4M2yxXvo&line=1&uniqifier=1](https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=vjsM4M2yxXvo&line=1&uniqifier=1)
    
    There is no high congruence bewteen small and this neuron.
    
    [https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=rWWf8L4ezCH3&line=6&uniqifier=1](https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=rWWf8L4ezCH3&line=6&uniqifier=1)
    
    The neuron N-1632, L32 seems to have high congruence for small. yet this logit diff plot shows it activates very little for “small”.
    

- make fns from prev nb, put into new nb
    
    [https://colab.research.google.com/drive/1Gvt1esiymU9UPfDKB1Nc7gMMUhJadLa1](https://colab.research.google.com/drive/1Gvt1esiymU9UPfDKB1Nc7gMMUhJadLa1)
    

The attention heads circuit takes information from MLPs. So find specific MLPs they interact with. We need to understand the dimensions of the MLP and embedded tokens to see how they are multiplied with the attention in the circuit.

- Congruence code
    
    All the neurons (36*5120 = 184320)
    
    `mlp_output_weights = torch.cat([block.mlp.W_out for block in model.blocks], dim=0)`
    
    `# (n_layer * d_mlp, d_model)` = `torch.Size([184320, 1280])`
    
    `d_model` = `1280` , which is 
    
    - Details
        
        This line of code concatenates the output weight matrices (`W_out`) of all the blocks (transformer layers) in the model. The concatenation is performed along dimension 0.
        
        Each block in a transformer-based model like GPT-2 contains a multi-layer perceptron (MLP) that uses a weight matrix `W_out` as part of its operations. These weight matrices play a crucial role in how the block processes and transforms its input data.
        
        The line of code is creating a new tensor, `mlp_output_weights`, that stacks the `W_out` tensors of all the blocks. This tensor will have a shape of `(N*D, E)`, where `N` is the number of layers (blocks) in the model, `D` is the number of neurons in each layer's MLP, and `E` is the dimension of the model's hidden states.
        
    
    Are the total nodes the MIDDLE layers of the 3 layer MLP (input, hidden, output) or the LAST? They should be the middle, based on the diagram with green weights in the “an neuron” writeup.
    
    - Diagram
        
        ![Untitled](tall_short_neuron_investigation%20ipynb%20b6fb8fd5adfc47f4b7b737249042ae53/Untitled.png)
        
    
    Matrix is nd * d1 = WX
    
    W: Rows of output weights = n = output neurons → $[w_{1j} … w_{nj}]$
    
    W: Cols of output weights = 1280 → $[w_{i1} … w_{id}]$ 
    
    X: rows of embedded tokens = 1280 → [x1 … xd]
    
    ![Untitled](tall_short_neuron_investigation%20ipynb%20b6fb8fd5adfc47f4b7b737249042ae53/Untitled%201.png)
    
    ![Untitled](tall_short_neuron_investigation%20ipynb%20b6fb8fd5adfc47f4b7b737249042ae53/Untitled%202.png)
    
    The above diagram shows the number of input nodes = rows of X = d = cols of W
    
    The number of output nodes = rows of W = n 
    
    We assumed that n := (# of middle nodes of MLP), based on the diagram.
    
    The “an neuron” diagram’s green weights line up with the single color weights for all going into one output in the above diagram IF WE FLIP ONE OF THE DIAGRAMS. Now everything lines up:
    
    ![Untitled](tall_short_neuron_investigation%20ipynb%20b6fb8fd5adfc47f4b7b737249042ae53/Untitled%203.png)
    
    ![Untitled](tall_short_neuron_investigation%20ipynb%20b6fb8fd5adfc47f4b7b737249042ae53/Untitled%204.png)
    
    So this is like the reverse matrix multiplication WX in the MLP. it’s the tranpose of W; in the MLP, W is actually d x n, not n x d. This is because the input is the middle, which is n, the cols. But here, the rows are the middle.
    
    The reason we do this is because we want the output to have a value of every n. This means the rows of W, the output, must be n. 
    
    On a side note, the green weights represents a single neuron’s contribution to all the tokens (in parallel). So there are “d” green weights for a single neuron.
    
    The neuron’s “actions on” something is represented by its outgoing weights. This is because the ingoing weights define the activation value of the neuron, but the outgoing weights represents how that activation value is used in future computations.
    
    When we take the dot product of a token embedding (calculated at the start) with a neuron’s output weights, we get “how similar they are” in a direction. The more similar (same direction; parallel) they are, the more of an effect they have upon dot product (whether it’s + or -). The less similar, the more orthogonal they are, and thus their dot product would be smaller.
    
    Thus, we can say that similar vectors point in the same direction. The output weights, to “mimic” an embedded token vector, would have a lot of effect on that vector’s propagation through the model if it’s more similar to it (points in the same direction). 
    
    In other words, the outgoing weights of a neuron matches a feature if it’s in a similar direction as the feature vector.
    
    Therefore, we can say what a neuron’s weights “converges” towards when that neuron wants to model a feature (say, a token). 
    
    Verify this by checking the VALUE of the outgoing weight and VALUE of embedding; these are too big to check other than by dot product, but if we project them by PCA, we can see their direction according to the measurement of PC1 and PC2. In those directions, there’s a good chance they’ll still be similar.
    
    Another implication of this is that embeddings are usually done without any regards to semantics. So “large” and “huge” wouldn’t be in a similar direction in the embedding space. But putting them through the model transforms them, at some point, to point in a close enough direction (this may be the region of “large/huge/big/tall, etc.”)
    
    Check the dot products of “large” and “small” after being put through the model.
    
    Actually this doesn’t make sense, b/c the Congruence uses the original “large”. Actually, the embedding is LEARNED! It’s not like positional, which is fixed. So it’s not “put through the model”, it’s the embeddings are learned based on backprop, which takes into account the rest of the model.
    
    The model learns to create both the feature and feature detector (neuron) at the same time.
    
    Now if MLPs correspond to directions, attention perhaps also corresponds to feature directions. It’s saying this token has ‘high attention” to another but by “query key weights”- this is a dot product, measuring similarity between query vector and key vector, which are obtained by embedding (or whatever input) * attention weight.
    
    Note that these vectors can be represented using different basis. So they don’t need to be in the same direction in the same vector space?
    
    ---
    
    `model.embed.W_E` are the embedded tokens. `torch.Size([50257, 1280])`
    
    d = total # tokens = `50257`
    
    `model.embed.W_E[tokens_of_interest[i]]` is just a 1-D embedded vector of size `1280`
    
    `torch.einsum("d, nd -> n", model.embed.W_E[tokens_of_interest[i]], mlp_output_weights)`
    
    Gets NAMES (L,N) of every neuron:
    
    `neuron_names = [f"Layer {i//model.cfg.d_mlp}" + (f" Neuron {i%model.cfg.d_mlp}" if i%model.cfg.d_mlp != 0 else "") for i in range(mlp_output_weights.shape[0])]`
    
    This has 5120*36 neurons. Despite this, the dot product of each one with a token is very fast. This is because it’s just one dot product
    

Brainstorm a workflow from broad to specific to find MULTIPLE neurons for each token and see how they add up with each other and with the attention heads circuit:

1. Congruence of all neurons in all layers with each token of the input.
    1. Find neurons at tails of this distribution. Automate this; no need to plot.
2. Take those neurons at tails and get their congruence with all tokens
    1. This is to find similar (synonymous) tokens they’re associated with, which would mean a common association “cluster network” of tokens “sharing” the same clusters based on using neurons as directions in latent space. 
3. 

### To do

Look for circuit for these size comparison inputs

- Incorporate reflexion chatGPT into workflow
    1. Have chatGPT reflect, when keep trying prompts, which one results in desired outcome of the “smaller” word. 
        1. If it works, store this info in vector DB so it can use this template as a prompt. From vector DB
    

The Pile: check instances of size comparison (predict ‘tall’ , ‘large’, etc- generate synonyms using chatgpt)

Does ablating the neuron do anything?

Note that this contribution is small. Instead of manual inspection, use actv patching to obtain the values across all layers (that pass a certain threshold), and get the top ranking neurons. See if there’s a way they combine in a circuit to interact and contribute to the final logit value for the top, correct prediction.

- the neuron’s output weights have a high dot product with the embedding for the token `“ an”`?
- finding 3
- Sparse coding says groups of neurons, so neurons with low amounts are impt if together they contribute. Look for ones in ranking that stand out, even if low actv