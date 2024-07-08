# Project Planning

[Done](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Done%201c002201437341e48b55b8276859a632.md)

---

### Working on

Geometry of Activations

- ✅ browse feature plotting code
    - platonic repr
        
        [https://phillipi.github.io/prh/](https://phillipi.github.io/prh/)
        
        [https://github.com/minyoungg/platonic-rep](https://github.com/minyoungg/platonic-rep)
        
    - LLM categorical
        - linear repr repo
    - toy models superpos ARENA
        - [https://colab.research.google.com/drive/1hoD36nsHp6K0E-YeFgPzxazlstb7HPyh#scrollTo=DRQ9j4ftyHXf](https://colab.research.google.com/drive/1hoD36nsHp6K0E-YeFgPzxazlstb7HPyh#scrollTo=DRQ9j4ftyHXf)
        - [https://github.com/callummcdougall/ARENA_3.0/blob/main/chapter1_transformer_interp/exercises/part4_superposition_and_saes/utils.py](https://github.com/callummcdougall/ARENA_3.0/blob/main/chapter1_transformer_interp/exercises/part4_superposition_and_saes/utils.py)
    - neuronpedia umap (ask joseph)
- ✅ study categ geom paper thms
    
    [https://chatgpt.com/c/daf9bf12-e7dd-472b-a765-00bb6857ce37](https://chatgpt.com/c/daf9bf12-e7dd-472b-a765-00bb6857ce37)
    
    thm 8
    
    There is no perpendicular direction (in 1D space) to adjust one point without affecting the others. In higher dimensions, if vectors are not collinear, you have the freedom to move perpendicularly to affect one variable without altering the relative positions of others. 
    
    - what's the probability of w2? is that a different point on the line?
        
        Let's break it down intuitively using the concept of collinear points and probabilities.
        
        When we talk about the vectors \(\bar{\ell}*{w_0}, \bar{\ell}*{w_1}, \bar{\ell}_{w_2}\) being on a line, we are essentially saying that the positions of these points can be described using a single dimension. In this case:
        
        1. **Probabilities along a Line**: If these vectors are collinear, any change in the probability of one attribute (e.g., \(w_2\)) will necessarily influence the relative probabilities of the other attributes (\(w_0\) and \(w_1\)) because all movements are constrained to the line they form.
        2. **Probability of \(w_2\)**: The probability of \(w_2\) can be seen as a point along the line formed by \(\bar{\ell}*{w_0}, \bar{\ell}*{w_1}, \bar{\ell}_{w_2}\). To change the probability of \(w_2\), you have to move along this line. This movement will also affect the relative probabilities of \(w_0\) and \(w_1\).
        3. **Impact of Collinearity**: Since there is no direction in the line that allows you to move independently to change the probability of \(w_2\) without also affecting \(w_0\) and \(w_1\), you can't adjust one without influencing the others.
        
        To visualize this, think of the line as a tightrope. If you are walking along the tightrope (the line), every step forward or backward changes your position relative to all points on the tightrope. There's no way to step to the side (no perpendicular movement), so every move affects your relative position to all other points on the line.
        
        In summary, the probability of \(w_2\) is represented by a point on this line. To change this probability (i.e., move this point), you must move along the line, inherently affecting the relative probabilities of \(w_0\) and \(w_1\) as well.
        
- ✅ review UMAP
- ✅ find how actvs and weights plotted in
    
    [**Towards Monosemanticity**](https://www.notion.so/Towards-Monosemanticity-66d08a43363640ff9444550db9ca4151?pvs=21) 
    
    [https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html)
    
- ✅ plan feature geom sim measurement proj
    
    [Feature Geometry- Lit Review](Feature%20Geometry-%20Lit%20Review%20384f2f70a32245a7a9aa5b1481cd85ab.md) 
    
    [Geometry project ideas](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8.md) 
    
- ✅ **EXPM**: plot pretrained sae features
    - plot feature weights 2D
        - ✅ [feature_weights_pca](https://colab.research.google.com/drive/1stczggQZRSRW7OU2mwoJ2XxDxhdfyqH5#scrollTo=MNk7IylTv610).ipynb
            - ✅ use updated `basic_loading_and_analysing`.ipynb [https://colab.research.google.com/github/jbloomAus/SAELens/blob/main/tutorials/basic_loading_and_analysing.ipynb#scrollTo=XoMx3VZpv611](https://colab.research.google.com/github/jbloomAus/SAELens/blob/main/tutorials/basic_loading_and_analysing.ipynb#scrollTo=XoMx3VZpv611)
            - ✅ [ask chatgpt to plot weights in pca and umap](https://chatgpt.com/c/68ebe2fd-6d96-4ba8-8bc1-574775aa47b9)
                - ✅ pca works but usign A100 is faster
                - ✅ debug umap
                    
                    ERROR: `AttributeError: module 'numpy.linalg._umath_linalg' has no attribute '_ilp64'`
                    
                    - [https://umap-learn.readthedocs.io/en/latest/](https://umap-learn.readthedocs.io/en/latest/)
                    - [https://umap-learn.readthedocs.io/en/latest/faq.html#is-there-gpu-or-multicore-cpu-support](https://umap-learn.readthedocs.io/en/latest/faq.html#is-there-gpu-or-multicore-cpu-support)
                    - transformerlens or saelens incompat w/ latest numpy? or gpu/cpu incompat
        - ✅ [feature_weights_umap](https://colab.research.google.com/drive/1Nxw9hntiIAwu8iYpQWQyarRY9MuS4JR8#scrollTo=s7GJCvWj2yBE).ipynb: try saving pickled sae feature weights in nb that installs saelens, then plot in umap in separte nb
            - cpu works
        - analyze results
            - [for the feature weight encoder matrix of a sparse autoencoder, torch.Size([768, 24576]), trained on activations of layer 8 of gpt-2 small, what does this plot mean? why don't I see clusters?](https://chatgpt.com/c/5a819a8f-6731-457c-88e5-74c09d9d70dd)
            - make sure you’re plotting by the cols? for decoder?
                
                Yes, it does matter whether you plot by columns or rows of the weight matrix because it changes the meaning of the points in the UMAP plot.
                
                ### Plotting Rows vs. Columns
                
                1. **Plotting Rows of the Weight Matrix:**
                    - Each row represents a different feature (in your case, 768 features).
                    - The UMAP plot will show the relationships between these features in a lower-dimensional space.
                    - This is useful if you want to understand how the features are related or clustered based on the autoencoder's weight matrix.
                2. **Plotting Columns of the Weight Matrix:**
                    - Each column represents a different input dimension (in your case, 24576 dimensions).
                    - The UMAP plot will show the relationships between the input dimensions in a lower-dimensional space.
                    - This is useful if you want to understand how the input dimensions are represented or clustered based on the autoencoder's weight matrix.
                
                ### Example: Plotting Rows
                
                If you want to visualize the relationships between the features, you should plot the rows of the weight matrix.
                
                ```python
                import umap
                import matplotlib.pyplot as plt
                
                # Assuming weight_matrix is your original matrix of size [768, 24576]
                
                # Initialize UMAP
                reducer = umap.UMAP(n_neighbors=15, min_dist=0.1, metric='euclidean')
                
                # Fit and transform the data by rows
                embedding = reducer.fit_transform(weight_matrix)
                
                # Plot the UMAP result
                plt.figure(figsize=(10, 8))
                plt.scatter(embedding[:, 0], embedding[:, 1], s=5, cmap='Spectral')
                plt.title('UMAP of Weight Matrix by Rows (Features)')
                plt.xlabel('UMAP Component 1')
                plt.ylabel('UMAP Component 2')
                plt.show()
                
                ```
                
                ### Example: Plotting Columns
                
                If you want to visualize the relationships between the input dimensions, you should transpose the weight matrix and plot the columns.
                
                ```python
                # Transpose the weight matrix to get dimensions [24576, 768]
                transposed_weight_matrix = weight_matrix.T
                
                # Initialize UMAP
                reducer = umap.UMAP(n_neighbors=15, min_dist=0.1, metric='euclidean')
                
                # Fit and transform the data by columns
                embedding = reducer.fit_transform(transposed_weight_matrix)
                
                # Plot the UMAP result
                plt.figure(figsize=(10, 8))
                plt.scatter(embedding[:, 0], embedding[:, 1], s=5, cmap='Spectral')
                plt.title('UMAP of Weight Matrix by Columns (Input Dimensions)')
                plt.xlabel('UMAP Component 1')
                plt.ylabel('UMAP Component 2')
                plt.show()
                
                ```
                
                ### Choosing Rows or Columns
                
                - **Choose Rows** if you are interested in the feature relationships.
                - **Choose Columns** if you are interested in the input dimension relationships.
                
                Based on your previous context, if you want to see how the features encoded by the sparse autoencoder cluster, you should plot the rows of the weight matrix. If your interest lies in understanding how the original input dimensions (activations of layer 8 of GPT-2 small) cluster, then you should plot the columns.
                
            - how to compare two umap set of points to see if similar
                
                
            - compare to neuronpedia
                - ask slack / jb
                    
                    I was also wondering if I can ask this question on the [#neuronpedia](https://opensourcemechanistic.slack.com/archives/C06R43HV2CR) channel: I'm looking to understand the umap plots on neuronpedia better so I've been taking the feature weight matrix from saelens (sae.W_enc) and just plotting them in umap to see if I get similar plots/clusters. I was wondering if there's a paper or blog post about what Umap parameters (num_neigh, etc) were used?
                    
                    Were they similar to the parameters in Towards Monosemanticity (attached paragraph)? Also I suppose to use decoder rather than encoder weights
                    
    - plot feature actvs 2D
        - ✅ plot feature actvs in pca
            
            same nb as weights
            
        - plot feature actvs in umap
            - ✅ either umap wasn’t compat with GPU, OR umap lib wasn’t compatible with saelens lib (diff vers of numpy, etc).
                - loading umap w/ saelens doesn’t work.
                    - so we needed to save feature_acts from a separate nb that loaded saelens
                - so test if umap compat with gpu. yes; it works with gpu
                    - So when saving feature_acts from pca, can save as gpu. Note a cpu run cannot load a tensor that was saved from a gpu; must use `.cpu` before saving it
            - there are clusters, but what are they?
                
                ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled.png)
                
    - interpret feature actvs
        
        
    - scale up using Torr node
- ✅ msg luke on universal features converging across models
    
    comparing saes across models. I think your project is about finding better sae features for a model using a method you call alignment regularization; it's not directly related to what I'm thinking of, but I think you have some useful insights into how saes can better learn true features. Given that you have experience comparing saes I think I may have several questions to ask later if you have time in a few weeks. I'm running prelim geom experiments now so it'd be easier to explain once I finish them
    
    And by comparing sae features across models I mean a continuation of this: [https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality)
    
    To phrase it better, I was thinking about how your method would approximate the true features better in one LLM. For two LLMs that are initialized differently, the saes trained on each of them for a layer would likely not find many analogous features. But if you train better saes, say with your method using the aggregates of multiple saes, I was wondering how much they would "converge' to find universally similar features, esp when features splitting occurs as saes get bigger. Similar to the platonic rep hypothesis. Do you think they would converge?
    
- ✅ chatgpt on ‘hier geom’ causal inner product reasons
    
    [https://chatgpt.com/c/fbfde9a6-76fd-4c88-a2bd-267312a4d3df](https://chatgpt.com/c/fbfde9a6-76fd-4c88-a2bd-267312a4d3df)
    
    - Why do we need to use the causal inner product? Why couldn't the authors have just looked for simplex orthogonality relations directly in the embedding space (last token, last layer) or unembedding space separately?
        1. **Unification of Embedding and Unembedding Spaces**:
        The causal inner product allows for the unification of the context embedding space (Λ) and the token unembedding space (Γ) into a single representation space. This unification is essential because it ensures that concepts represented in these distinct spaces can be compared and analyzed under a common framework. The transformation using an invertible matrix \( A \) and a constant vector \( \gamma_0 \) aligns these spaces such that the Euclidean inner product in the transformed space respects the semantics of language【6:2†source】.
        2. **Simplicity and Structure**:
        The causal inner product allows for the representation of categorical and hierarchical concepts as simple geometric structures, such as simplices. This geometric representation is more interpretable and aligns with the hierarchical nature of semantic concepts. By ensuring orthogonality and maintaining a unified representation space, the causal inner product supports the formation of these geometric structures, facilitating easier manipulation and understanding of the concepts【6:12†source】【6:14†source】.
        3. **Empirical Validation**:
        The theoretical results are empirically validated using a large language model (Gemma-2B). The transformation to a canonical representation space via the causal inner product allows for the alignment of the embedding and unembedding representations, enabling the observation and measurement of the predicted geometric structures in practice. This empirical validation strengthens the theoretical foundation laid out by the authors【6:12†source】.
        
        Directly looking for simplex orthogonality relations in either the embedding space or the unembedding space separately would not ensure the alignment of these spaces or respect the hierarchical and causal relationships between concepts. The causal inner product provides a rigorous mathematical framework that ensures these properties are maintained, enabling a more accurate and interpretable representation of semantic structures in language models.
        
    - Was LDA used to get a vector in the causal inner product's space? If we just look at individual activation spaces of a layer, do we need LDA or can we just look at the activation vector directly?
        1. **Separate Classes**: The primary role of LDA is to find a projection that maximizes the separation between different classes (e.g., words belonging to different concepts) while minimizing the variance within each class. This helps in creating a clear distinction between concepts in the representation space.
        2. **Minimize Variance**: By minimizing the within-class variance, LDA ensures that the projection of the unembedding vectors for tokens associated with a specific concept (e.g., "mammal") is consistent, which aligns with the requirement that concepts should have well-defined vector representations with minimal variance around a central value.
        3. **Align with Theoretical Results**: The LDA-based estimation of vector representations aligns with the theoretical framework provided by the causal inner product, ensuring that the geometric properties such as orthogonality and simplex structures are preserved and observable in the empirical results.
        
        ### Looking at Individual Activation Spaces
        
        If we were to look at the activation vectors directly within an individual layer without transforming them via the causal inner product, there are some key considerations:
        
        1. **Representation Alignment**: Without the transformation provided by the causal inner product, the embeddings and unembeddings might not be aligned in a way that respects the semantic relationships between concepts. This misalignment can obscure the geometric structures (such as orthogonality and simplices) that are crucial for understanding the hierarchical relationships.
        2. **Need for LDA**: In the individual activation spaces, LDA can still be beneficial because it helps in finding directions that separate different classes of concepts. However, if the goal is to directly observe activation vectors, LDA might not be strictly necessary if the vectors already exhibit clear separations. Yet, typically, raw activation vectors might not be as well-separated without some form of dimensionality reduction or projection technique like LDA.
        3. **Empirical Consistency**: The empirical validation of theoretical results often requires transformations like LDA to ensure consistency with the theoretical framework. Direct observation of raw activation vectors might miss subtle relationships that are more apparent after applying LDA or similar techniques.
        
        ### 
        
    - actually LDA is used to get a vector for an attribute, which is a collection of tokens, using those tokens?
        
        Yes, you're correct. LDA (Linear Discriminant Analysis) is indeed used to get a vector representation for an attribute, which is essentially a collection of tokens. Here's a detailed explanation of how LDA is utilized in this context:
        
        ### Purpose of LDA in the Study
        
        LDA is employed to estimate the vector representations of attributes by utilizing the tokens associated with those attributes. Here's how this works:
        
        1. **Attribute and Token Relationship**: Each attribute (e.g., "mammal") is associated with a set of tokens (e.g., "dog," "cat," "elephant"). The goal is to find a vector that represents this attribute based on the embeddings of these tokens.
        2. **Class Separation**: LDA helps in finding a projection that maximizes the separation between the tokens associated with the attribute and those that are not. This ensures that the vector representation of the attribute captures the distinguishing features of the tokens that belong to it.
        3. **Minimizing Within-Class Variance**: LDA also minimizes the variance within the tokens of the same attribute. This means that the tokens associated with the attribute should have similar projections onto the resulting vector, making the representation consistent.
        
        ### Process of Using LDA
        
        Here's a step-by-step process of how LDA is used in this study:
        
        1. **Collect Tokens**: Gather the tokens that belong to the attribute (e.g., all tokens that can be considered "mammals").
        2. **Compute Unembedding Vectors**: For each token, compute its unembedding vector in the representation space.
        3. **Estimate the Vector Representation**: Use LDA to find the direction that best separates the tokens associated with the attribute from those that are not. This involves:
            - Calculating the mean vector for the tokens of the attribute.
            - Calculating the covariance matrix of these tokens.
            - Finding the direction that maximizes the between-class variance and minimizes the within-class variance.
        
        ### Equation for LDA-based Vector Estimation
        
        The LDA-based estimation of the vector representation for an attribute \( w \) is given by:
        \[ \ell_w = \frac{\text{Cov}(g_w)^{-1} \mathbb{E}(g_w)}{\|\text{Cov}(g_w)^{-1} \mathbb{E}(g_w)\|_2} \]
        where \( g_w \) represents the unembedding vectors of the tokens associated with the attribute \( w \), and \(\text{Cov}(g_w)\) is the covariance matrix of these vectors.
        
        ### Empirical Validation
        
        Using LDA in this manner ensures that the resulting vector representation of the attribute aligns with the theoretical expectations, such as the orthogonality of hierarchically related concepts and the simplex structure of categorical concepts. This process helps in empirically validating the theoretical results by showing that the estimated vectors exhibit the expected geometric properties.
        
        ### Conclusion
        
        LDA is indeed used to get a vector for an attribute by utilizing the tokens associated with that attribute. This approach ensures that the resulting vector representation accurately captures the distinguishing features of the attribute and aligns with the theoretical framework provided by the causal inner product.
        
    - i dont see here how multiple tokens aer used? it says g_w is just a word sampled
        
        The confusion arises from the notation and the explanation in the text. Let's clarify how multiple tokens are used to estimate the vector representation for an attribute using LDA:
        
        ### Explanation of the Equation
        
        1. **Tokens Associated with Attribute \( w \)**:
            - \( Y(w) \) represents the set of tokens associated with the attribute \( w \). For example, if \( w \) is "mammal," \( Y(w) \) might include tokens like "dog," "cat," "elephant," etc.
        2. **Unembedding Vectors**:
            - \( g_w \) represents the unembedding vector of a word sampled uniformly from \( Y(w) \). This means that for the calculation, each word in \( Y(w) \) has an unembedding vector \( g \), and \( g_w \) is the set of these vectors for all tokens in \( Y(w) \).
        3. **Covariance Matrix**:
            - The covariance matrix \( \text{Cov}(g_w) \) is computed using the unembedding vectors of all tokens in \( Y(w) \). This involves taking all the tokens associated with \( w \) and calculating the covariance of their unembedding vectors.
        4. **LDA Estimation**:
            - The vector \( \ell_w \) for the attribute \( w \) is estimated using these unembedding vectors. Specifically, the estimation involves calculating the mean vector \( \mathbb{E}(g_w) \) and the covariance matrix \( \text{Cov}(g_w) \) for the set of tokens.
        
        ### Detailed Steps
        
        1. **Collect Tokens**:
            - Gather all tokens that are associated with the attribute \( w \). This forms the set \( Y(w) \).
        2. **Compute Unembedding Vectors**:
            - For each token in \( Y(w) \), compute its unembedding vector. Let's denote the set of these vectors as \( \{ g_{w1}, g_{w2}, ..., g_{wn} \} \).
        3. **Calculate Covariance Matrix**:
            - Calculate the covariance matrix \( \text{Cov}(g_w) \) using the unembedding vectors of all tokens in \( Y(w) \). This matrix captures the variance and correlations of the vectors within the set.
        4. **Estimate Vector Representation**:
            - Use LDA to find a projection that separates the tokens associated with \( w \) from those not associated with it. The LDA process maximizes the separation between classes (tokens associated with \( w \) vs. those that are not) while minimizing the within-class variance.
        5. **Compute the Vector**:
            - The vector \( \ell_w \) is computed using the pseudo-inverse of the covariance matrix and the mean vector of the unembedding vectors. The formula provided in the text is:
            \[
            \ell_w = \left( \tilde{g}_w^T \mathbb{E}(g_w) \right) \tilde{g}_w, \quad \text{with} \quad \tilde{g}_w = \frac{\text{Cov}(g_w)^\dagger \mathbb{E}(g_w)}{\| \text{Cov}(g_w)^\dagger \mathbb{E}(g_w) \|_2}
            \]
            - Here, \( \mathbb{E}(g_w) \) is the mean of the unembedding vectors of tokens in \( Y(w) \), and \( \text{Cov}(g_w)^\dagger \) is the pseudo-inverse of the covariance matrix.
        
        ### Summary
        
        While the text may seem to suggest using a single token, it actually involves using the set of tokens associated with the attribute to compute the mean and covariance matrix. These are then used in the LDA process to estimate the attribute's vector representation. Thus, multiple tokens are indeed used to derive the vector \( \ell_w \) for the attribute \( w \).
        
    - why were these attribute vectors such as “L_bird” used, rather than individual tokens such as “bird”?
        
        The attribute vectors (e.g., \( \ell_{\text{bird}} \)) are used rather than individual token vectors (e.g., "bird") for several key reasons:
        
        ### 1. Capturing Generality and Abstraction
        
        - **Attribute vectors** represent the general concept or category that encompasses all tokens associated with that attribute. For example, the attribute vector \( \ell_{\text{bird}} \) captures the essence of the concept "bird" which includes all specific instances of birds (like "sparrow," "eagle," "parrot").
        - **Individual token vectors** represent specific words, which may only capture particular instances or narrower aspects of the attribute. The vector for "bird" might only reflect the specific usage of the word "bird" in the training data, rather than the entire category.
        
        ### 2. Reducing Variability and Noise
        
        - **Attribute vectors** are calculated by aggregating information from multiple tokens, reducing the variability and noise inherent in individual word usage. This aggregation results in a more robust and stable representation of the concept.
        - **Individual token vectors** can vary significantly depending on context and usage frequency, leading to less reliable representations if used in isolation.
        
        ### 3. Semantic Coherence
        
        - **Attribute vectors** ensure that the semantic properties of the entire category are captured. For instance, the vector \( \ell_{\text{bird}} \) is derived from multiple bird-related tokens, ensuring that the representation is semantically coherent and representative of the entire class.
        - **Individual token vectors** might not fully capture the hierarchical or categorical relationships within the data, missing out on the broader semantic context.
        
        ### 4. Facilitating Geometric Interpretations
        
        - **Attribute vectors** allow for the application of geometric interpretations such as orthogonality and simplex structures. These interpretations are crucial for understanding relationships between different concepts and categories in the representation space.
        - **Individual token vectors** do not provide a straightforward way to apply these geometric interpretations, as they are tied to specific instances rather than abstract categories.
        
        ### 5. Enabling Hierarchical and Categorical Analysis
        
        - **Attribute vectors** support the analysis of hierarchical and categorical relationships, which is essential for understanding the structure of semantic representations in language models. For example, \( \ell_{\text{mammal}} \) and \( \ell_{\text{animal}} \) can be used to study the hierarchical relationship between mammals and animals.
        - **Individual token vectors** do not easily facilitate this kind of analysis, as they do not inherently represent the broader categories or hierarchical levels.
        
        ### Practical Implementation
        
        As detailed in the provided document, the authors used LDA to derive these attribute vectors from the unembedding vectors of multiple tokens associated with each attribute. This method ensures that the resulting vectors are representative of the entire category rather than just individual instances.
        
        ### Conclusion
        
        Using attribute vectors such as \( \ell_{\text{bird}} \) instead of individual tokens like "bird" allows for more general, stable, and semantically coherent representations. These vectors facilitate the analysis of hierarchical and categorical structures in the representation space of language models, which is essential for understanding and interpreting the underlying semantic relationships.
        
    
    It seems like the statement “"the simplex of fish,mammal, bird is orthogonal to the vector representation of animal" is interpreted as span{¯ℓmammal,¯ℓbird,¯ℓfish} is orthogonal to L_animal. If so,  what does it mean that a * mammal + b*bird + c*fish is orthogonal to L_animal?
    
    - Semantically what does a * mammal + b*bird + c*fish mean? How can a specific vector be a combination of those?
        
        **Example**: Interpolating between "mammal" and "bird" might create a vector that captures semantic similarities or shared characteristics, such as being warm-blooded.
        
    - do the vectors in span{¯ℓmammal,¯ℓbird,¯ℓfish} represent specific animals?
        
        The vectors in \(\text{span}\{\ell_{\text{mammal}}, \ell_{\text{bird}}, \ell_{\text{fish}}\}\) do not necessarily represent specific animals directly. Instead, they represent combinations of the attributes associated with mammals, birds, and fish. Here’s a more detailed explanation:
        
        ### Understanding the Span
        
        1. **Span of Vectors**:
            - The span of \(\{\ell_{\text{mammal}}, \ell_{\text{bird}}, \ell_{\text{fish}}\}\) consists of all possible linear combinations of these vectors. Mathematically, this means any vector \( v \) in this span can be expressed as:
            \[
            v = a \cdot \ell_{\text{mammal}} + b \cdot \ell_{\text{bird}} + c \cdot \ell_{\text{fish}}
            \]
            - Here, \(a\), \(b\), and \(c\) are scalar coefficients.
        
        ### Semantic Interpretation
        
        1. **Attribute Combinations**:
            - The vectors within this span represent different mixtures or combinations of the semantic attributes associated with mammals, birds, and fish. They do not correspond to specific animals but rather to abstract concepts that blend these attributes.
        2. **Conceptual Space**:
            - For example, a vector in this span might represent a general concept that has some mammalian traits, some avian traits, and some piscine traits. This is more about capturing the shared and overlapping characteristics rather than pinpointing specific animals.
        3. **Abstract Entities**:
            - Such combinations could be used to model abstract or hypothetical entities. For instance, in a hypothetical or fantasy context, a vector in this span could represent a creature with a mix of traits from mammals, birds, and fish.
        
        ### Specific Animals and Attribute Vectors
        
        1. **Representing Specific Animals**:
            - Specific animals like "dog," "sparrow," or "salmon" would typically be represented by their own unique vectors, derived from their particular contexts and usage in the training data.
            - These specific animal vectors would be located in the broader semantic space, which might be influenced by the attribute vectors \(\ell_{\text{mammal}}, \ell_{\text{bird}}, \ell_{\text{fish}}\), but not confined to their span.
        2. **Hierarchical and Categorical Representation**:
            - The span of these attribute vectors provides a subspace that helps in understanding and organizing the broader semantic space. It’s useful for analyzing relationships and hierarchies but doesn’t directly map to specific instances.
        
        ### Practical Example
        
        - **Combining Attributes**: If you have \(\ell_{\text{mammal}}\), \(\ell_{\text{bird}}\), and \(\ell_{\text{fish}}\), a vector \(0.5 \cdot \ell_{\text{mammal}} + 0.3 \cdot \ell_{\text{bird}} + 0.2 \cdot \ell_{\text{fish}}\) might represent an abstract concept that combines features of these three classes. This vector is not a direct representation of a specific animal but rather an abstract blend.
        
        ### Conclusion
        
        The vectors in \(\text{span}\{\ell_{\text{mammal}}, \ell_{\text{bird}}, \ell_{\text{fish}}\}\) represent abstract combinations of the attributes associated with mammals, birds, and fish. They do not correspond directly to specific animals but provide a useful subspace for exploring the relationships and characteristics of these broader categories. Specific animals are represented by their own unique vectors within the broader semantic space of the model.
        
- ✅ How does whitening matrix "make" variables uncorrelated? Shouldn't the correlation be how the variables truly are? Or is it transforming the data into a perspective such that when look at it from that basis, the data is uncorrelated on that basis?
    
    [https://chatgpt.com/c/3091fef0-4b87-41f9-8df3-c4c4ef37db3f](https://chatgpt.com/c/3091fef0-4b87-41f9-8df3-c4c4ef37db3f)
    
    The concept of whitening a matrix is indeed to transform the data into a new basis where the variables are uncorrelated and standardized. This transformation doesn't change the true relationships between the variables but provides a different perspective or basis where the correlations between the transformed variables are zero, and their variances are equal to one. Here’s how it works and why it’s useful:
    
    ### How Whitening Works
    
    1. **Centering the Data**: The first step is to center the data by subtracting the mean of each variable, making the dataset have a mean of zero for each variable.
    2. **Covariance Matrix**: Compute the covariance matrix \( \Sigma \) of the centered data. This matrix contains the variances along the diagonal and the covariances off-diagonal, representing the relationships between the original variables.
    3. **Eigenvalue Decomposition**: Perform eigenvalue decomposition on the covariance matrix:
    \[
    \Sigma = V \Lambda V^T
    \]
    where \( V \) is a matrix of eigenvectors, and \( \Lambda \) is a diagonal matrix of eigenvalues.
    4. **Whitening Transformation**: The whitening matrix \( W \) is constructed using the eigenvectors and the inverse square root of the eigenvalues:
    \[
    W = \Lambda^{-\frac{1}{2}} V^T
    \]
    The whitened data \( X_{\text{whitened}} \) is obtained by multiplying the centered data \( X \) by the whitening matrix:
    \[
    X_{\text{whitened}} = X W
    \]
    
    ### Why Whitening Makes Variables Uncorrelated
    
    The multiplication by the whitening matrix \( W \) transforms the original data into a new space where:
    
    - **Uncorrelated Variables**: The covariance matrix of \( X_{\text{whitened}} \) becomes the identity matrix \( I \), meaning the variables are uncorrelated. This is because the whitening transformation diagonalizes the covariance matrix and rescales the eigenvalues to one.
    - **Unit Variance**: Each variable in the whitened data has a variance of one.
    
    ### Interpretation and Utility
    
    - **Perspective Transformation**: Whitening provides a new basis in which the data is analyzed. It doesn't alter the inherent relationships in the data but represents it in a way that is often more useful for certain algorithms and analyses (e.g., principal component analysis, independent component analysis).
    - **Standardization**: Whitening standardizes the data, which can be particularly beneficial for machine learning algorithms that are sensitive to the scale and correlation of the data (e.g., gradient-based optimization algorithms).
    
    ### Summary
    
    Whitening transforms the data such that, in the new basis, the variables are uncorrelated and have unit variance. This transformation is a mathematical tool to facilitate certain analyses and algorithms, not a reflection of the "true" state of the variables in their original form. The true correlations remain in the original data, but in the transformed space, the data is easier to work with for various applications.
    
- ✅ email kiho on project idea
    
    Hi, I was wondering if you have some advice on adjusting this project plan:
    
    I was thinking about how to detect simplex structures in intermediate layers. A starting point would be to just look at the embedded activation vectors of individual tokens, and to use LDA to calculate vectors for the attribution sets they belong to. Then we can calculate the orthogonality relations of these attribute vectors. I have a few questions about how to extend the “Hierarchical concepts” paper to intermediate layers:
    
    1) The paper looks for the structure in a canonical representation space with the causal inner product, not just in the embedding space. Would we have to “unify” an intermediate layer embedding with the unembedding space, if this is possible right now? Or would it make sense to look for orthogonality relations of attribute vectors constructed directly by LDA from activation vectors of individual tokens?
    
    2) In Figure 5, my understanding is the adjacency matrix doesn’t depend on the vectors, but is already there from Wordnet, and we want to check if it appears in the cosine sim matrix (fig 5b) but not for child-parent (fig 5c). Can we do this for intemediate space experiments? Also, would fig 5c show there’s a “nested” hierarchy where (animal - mammal) may be manipulated separately from (mammal-elephant)?
    
    3) Experimentally, should we show this for polytopes of say span{4 members or more} and not just span{3 members}?
    
    (The question below is less important for planning, so not needed to answer now):
    
    A) Why were these attribute vectors such as “L_bird” used, rather than individual tokens such as “bird”? I’m guessing we’re not trying to study individual tokens, but a general “subspace” of an attribute; a set of tokens in an attribute set form a “cluster” and we want to obtain the vector that represents that cluster over other clusters (so LDA maximizes between-class variance). Then L_bird estimates this “subspace” better. But what’s a good response if someone questions why we don’t just use “bird”?
    
    B) It seems like the statement "the simplex of fish,mammal, bird is orthogonal to the vector representation of animal" is interpreted as span{¯ℓmammal,¯ℓbird,¯ℓfish} is orthogonal to L_animal. If (a * mammal - b*bird + c*fish) is a member of the span, what does that mean semantically (I think we pass in an input that contains “traits” of all three?) and does it mean that semantically speaking, those specific traits are orthogonal to L_animal?
    
- ✅ writeup geom plan (org notes just on it) and slides
    
    [https://docs.google.com/presentation/d/1AHuy77JmlQ0xzLxSiwVxaNS-5U3BLWn-z9HMoM2R-Rs/edit#slide=id.g2e9f646b02d_0_13](https://docs.google.com/presentation/d/1AHuy77JmlQ0xzLxSiwVxaNS-5U3BLWn-z9HMoM2R-Rs/edit#slide=id.g2e9f646b02d_0_13)
    
    - Universality by Geometry, v2
        
        [https://docs.google.com/presentation/d/1QQ9cnGzRH7MCkRF1RlQ_28M9gJ1j9ra3umWy96v5slc/edit#slide=id.g2ea1a29255c_0_71](https://docs.google.com/presentation/d/1QQ9cnGzRH7MCkRF1RlQ_28M9gJ1j9ra3umWy96v5slc/edit#slide=id.g2ea1a29255c_0_71)
        
    - how ph paper finds the “right” layer across 2 models to compare?
    - understand mutual nearest neighbors. kernel alignment metric computes a score based on datapoints passed thru metrics.
    - model stitching
- ✅ **EXPM**: plot feature acts, and compare before vs after steering/ablating/patching
    - in another layer, track how a specific set of features (eg. love or cat) changes after steering
        - [save_actvs_afterSteer](https://colab.research.google.com/drive/1Kvb-MJUdSyolrmXTON2432l8UIAHQmwq#scrollTo=SRZ1lgrSBVBE).ipynb
        - [feature_actvs_afterSteer_umap](https://colab.research.google.com/drive/1brV9lxVX9uR_GHtWprUqSFEWqgriB0ZX#scrollTo=4vuh4LF02nKs).ipynb
            - get CCA scores, but it’s slow
                
                Canonical Correlation Analysis (CCA) can indeed be computationally intensive, especially for large datasets or high-dimensional feature spaces. If you’re finding CCA to be very slow, there are several approaches and alternative methods you can consider to make the comparison more efficient and effective.
                
                Here’s a comprehensive guide to faster and more efficient ways to compare UMAP embeddings, including methods to speed up CCA and other alternatives:
                
                ### 1. **Optimizing CCA Performance**
                
                If you still want to use CCA, here are some strategies to optimize its performance:
                
                ### **a. Reduce Dimensionality Before CCA**
                
                Reducing the dimensionality of your feature space before applying CCA can significantly speed up the computation. You can use PCA (Principal Component Analysis) or any other dimensionality reduction technique for this purpose.
                
                ```python
                from sklearn.decomposition import PCA
                from sklearn.cross_decomposition import CCA
                
                # Reduce dimensionality with PCA before CCA
                pca1 = PCA(n_components=50)  # Adjust the number of components as needed
                pca2 = PCA(n_components=50)
                data1_reduced = pca1.fit_transform(embedding1)
                data2_reduced = pca2.fit_transform(embedding2)
                
                # Apply CCA
                cca = CCA(n_components=10)
                cca.fit(data1_reduced, data2_reduced)
                
                # Transform the data
                data1_c, data2_c = cca.transform(data1_reduced, data2_reduced)
                
                ```
                
                ### **b. Use Approximate CCA Algorithms**
                
                Consider using libraries or implementations optimized for large datasets. For instance, you can use the `sklearn` implementation of CCA, but there are also other libraries and frameworks designed for efficiency in large-scale computations.
                
                ### 2. **Alternative Methods for Comparing UMAP Embeddings**
                
                Here are several alternative methods for comparing UMAP embeddings that are generally faster and may provide useful insights:
                
                ### *a. **Procrustes Analysis**
                
                Procrustes analysis is a method for comparing the shapes of two datasets and can be done quickly with the `scipy` library.
                
                ```python
                from scipy.spatial import procrustes
                
                # Perform Procrustes analysis
                mtx1, mtx2, disparity = procrustes(embedding1, embedding2)
                
                print(f"Procrustes Disparity: {disparity}")
                
                ```
                
                ### *b. **k-Nearest Neighbors (k-NN) Consistency**
                
                Comparing the k-NN consistency measures how well the neighborhood structure is preserved across the two datasets.
                
                ```python
                from sklearn.neighbors import NearestNeighbors
                
                def knn_consistency(embedding1, embedding2, n_neighbors=5):
                    nbrs1 = NearestNeighbors(n_neighbors=n_neighbors).fit(embedding1)
                    nbrs2 = NearestNeighbors(n_neighbors=n_neighbors).fit(embedding2)
                    indices1 = nbrs1.kneighbors(return_distance=False)
                    indices2 = nbrs2.kneighbors(return_distance=False)
                    consistency = np.mean([len(np.intersect1d(indices1[i], indices2[i])) / n_neighbors for i in range(len(embedding1))])
                    return consistency
                
                knn_consistency_score = knn_consistency(embedding1, embedding2)
                print(f"k-NN Consistency: {knn_consistency_score}")
                
                ```
                
                ### *c. **Distance Correlation**
                
                Distance correlation measures both linear and non-linear relationships and is generally computationally efficient.
                
                ```python
                from scipy.spatial.distance import pdist, squareform
                from scipy.stats import pearsonr
                
                def distance_correlation(X, Y):
                    X_dist = squareform(pdist(X, 'euclidean'))
                    Y_dist = squareform(pdist(Y, 'euclidean'))
                    corr, _ = pearsonr(X_dist.ravel(), Y_dist.ravel())
                    return corr
                
                dist_corr = distance_correlation(embedding1, embedding2)
                print(f"Distance Correlation: {dist_corr}")
                
                ```
                
                ### *d. **Mutual Nearest Neighbors (MNN) Analysis**
                
                Mutual nearest neighbors can also be used to compare embeddings, though it may be less common.
                
                ```python
                from sklearn.neighbors import NearestNeighbors
                
                def mutual_nearest_neighbors(embedding1, embedding2, n_neighbors=5):
                    nbrs1 = NearestNeighbors(n_neighbors=n_neighbors).fit(embedding1)
                    nbrs2 = NearestNeighbors(n_neighbors=n_neighbors).fit(embedding2)
                    indices1 = nbrs1.kneighbors(return_distance=False)
                    indices2 = nbrs2.kneighbors(return_distance=False)
                    mnn_count = 0
                    for i in range(len(embedding1)):
                        mnn_count += len(set(indices1[i]).intersection(indices2[i]))
                    mnn_ratio = mnn_count / len(embedding1)
                    return mnn_ratio
                
                mnn_score = mutual_nearest_neighbors(embedding1, embedding2)
                print(f"Mutual Nearest Neighbors Ratio: {mnn_score}")
                
                ```
                
                ### 3. **Visualization for Initial Comparison**
                
                Sometimes, visual inspection of the UMAP embeddings can provide useful insights, and it is a quick first step:
                
                ```python
                import matplotlib.pyplot as plt
                
                # Plot the UMAP results
                fig, axes = plt.subplots(1, 2, figsize=(12, 6))
                axes[0].scatter(embedding1[:, 0], embedding1[:, 1], c='blue', label='Dataset 1')
                axes[0].set_title('UMAP Projection of Dataset 1')
                axes[0].legend()
                
                axes[1].scatter(embedding2[:, 0], embedding2[:, 1], c='green', label='Dataset 2')
                axes[1].set_title('UMAP Projection of Dataset 2')
                axes[1].legend()
                
                plt.show()
                
                ```
                
                ### 4. **Using UMAP’s `transform` for Different Seeds**
                
                To ensure consistent results across different seeds, you can set a fixed seed value for reproducibility in UMAP, but it's important to note that it does not eliminate the inherent randomness completely.
                
                ```python
                import umap
                
                # UMAP with a fixed seed for reproducibility
                reducer = umap.UMAP(random_state=42)
                embedding1 = reducer.fit_transform(data1)
                embedding2 = reducer.fit_transform(data2)
                
                ```
                
                ### 5. **Comparing UMAP Embeddings with Other Dimensionality Reduction Techniques**
                
                You might also want to compare UMAP embeddings using other dimensionality reduction techniques like t-SNE or PCA.
                
                ```python
                from sklearn.manifold import TSNE
                from sklearn.decomposition import PCA
                
                # t-SNE
                tsne = TSNE(n_components=2, random_state=42)
                embedding1_tsne = tsne.fit_transform(data1)
                embedding2_tsne = tsne.fit_transform(data2)
                
                # PCA
                pca = PCA(n_components=2)
                embedding1_pca = pca.fit_transform(data1)
                embedding2_pca = pca.fit_transform(data2)
                
                ```
                
                ### Summary Table of Methods and Performance
                
                | Method | Pros | Cons | Speed |
                | --- | --- | --- | --- |
                | CCA | Detailed canonical correlation analysis | Computationally intensive for large datasets | Slow |
                | PCA + CCA | Reduces dimensionality before CCA | Requires setting PCA components properly | Moderate |
                | Procrustes Analysis | Fast, effective for shape comparison | Measures only shape similarity | Fast |
                | k-NN Consistency | Simple, measures neighborhood structure | May not capture all relationships | Fast |
                | Distance Correlation | Captures both linear and non-linear relationships | Measures overall similarity | Fast |
                | Mutual Nearest Neighbors | Measures neighborhood consistency | Less common, may be less intuitive | Fast |
                | Visualization | Provides intuitive visual insights | Not a quantitative measure | Fast |
                | Other Dimensionality Reduction (t-SNE, PCA) | Useful for comparison, can be faster | t-SNE can be slow for large datasets | Moderate |
                
                ### Conclusion
                
                While CCA can be slow, there are several alternative methods for comparing UMAP embeddings that are computationally more efficient. By reducing dimensionality, using alternative comparison methods, or employing effective visualization techniques, you can achieve meaningful comparisons without extensive computation times.
                
                You can choose the approach based on the size of your dataset, the specific aspects you are interested in comparing, and the computational resources available to you.
                
                ### Example Code with Optimizations and Alternatives
                
                Here’s a comprehensive example incorporating PCA for dimensionality reduction, along with Procrustes Analysis, Distance Correlation, and k-NN Consistency:
                
                ```python
                import numpy as np
                import umap
                import cupy as cp
                from sklearn.decomposition import PCA
                from sklearn.neighbors import NearestNeighbors
                from scipy.spatial import procrustes
                from scipy.spatial.distance import pdist, squareform
                from scipy.stats import pearsonr
                from sklearn.datasets import make_blobs
                from time import time
                import matplotlib.pyplot as plt
                
                # Generate or load data
                data1 = np.random.rand(10000, 50)  # Synthetic data
                data2 = np.random.rand(10000, 50)  # Another synthetic dataset
                
                # Apply UMAP with a fixed random state
                reducer = umap.UMAP(random_state=42)
                embedding1 = reducer.fit_transform(data1)
                embedding2 = reducer.fit_transform(data2)
                
                # Reduce dimensionality with PCA before CCA
                pca1 = PCA(n_components=50)
                pca2 = PCA(n_components=50)
                data1_reduced = pca1.fit_transform(embedding1)
                data2_reduced = pca2.fit_transform(embedding2)
                
                # Apply CCA
                cca = CCA(n_components=
                ```
                
            - can i use cca on umap?
                
                Yes, you can use Canonical Correlation Analysis (CCA) on UMAP embeddings to compare the embeddings of two different datasets. The idea is to first reduce the dimensionality of both datasets using UMAP, and then use CCA to find the linear combinations of the UMAP embeddings that are maximally correlated.
                
                ### Step-by-Step Guide
                
                Here is a step-by-step guide to apply CCA on UMAP embeddings:
                
                1. **Install the Required Libraries**:
                Ensure you have `umap-learn`, `numpy`, `scikit-learn`, and `matplotlib` installed.
                    
                    ```python
                    !pip install umap-learn numpy scikit-learn matplotlib
                    
                    ```
                    
                2. **Import Libraries**:
                Import the necessary libraries for UMAP, CCA, and data manipulation.
                    
                    ```python
                    import numpy as np
                    import umap
                    from sklearn.cross_decomposition import CCA
                    import matplotlib.pyplot as plt
                    
                    ```
                    
                3. **Generate or Load Data**:
                For demonstration purposes, let's create some synthetic data.
                    
                    ```python
                    # Generate synthetic data for demonstration
                    data1 = np.random.rand(100, 50)  # 100 samples with 50 features
                    data2 = np.random.rand(100, 50)  # Another dataset with the same dimensions
                    
                    ```
                    
                4. **Apply UMAP**:
                Use UMAP to reduce the dimensionality of both datasets.
                    
                    ```python
                    # Apply UMAP to both datasets
                    reducer = umap.UMAP(n_components=10, random_state=42)
                    embedding1 = reducer.fit_transform(data1)
                    embedding2 = reducer.fit_transform(data2)
                    
                    ```
                    
                5. **Apply CCA**:
                Use CCA to find the linear combinations of the UMAP embeddings that are maximally correlated.
                    
                    ```python
                    # Apply CCA on UMAP embeddings
                    cca = CCA(n_components=2)  # Number of components to extract
                    cca.fit(embedding1, embedding2)
                    
                    # Transform the data using CCA
                    cca_embedding1, cca_embedding2 = cca.transform(embedding1, embedding2)
                    
                    # Optional: To see the correlation coefficients
                    corrs = [np.corrcoef(cca_embedding1[:, i], cca_embedding2[:, i])[0, 1] for i in range(cca_embedding1.shape[1])]
                    print("Canonical Correlation Coefficients:", corrs)
                    
                    ```
                    
                6. **Visualize the Results**:
                Plot the first two canonical variables to visually inspect the correlation.
                    
                    ```python
                    # Plot the first two canonical variables
                    plt.figure(figsize=(12, 6))
                    
                    plt.subplot(1, 2, 1)
                    plt.scatter(cca_embedding1[:, 0], cca_embedding1[:, 1], c='blue', label='UMAP Dataset 1')
                    plt.title('Canonical Variables of UMAP Dataset 1')
                    plt.xlabel('Canonical Variable 1')
                    plt.ylabel('Canonical Variable 2')
                    plt.legend()
                    
                    plt.subplot(1, 2, 2)
                    plt.scatter(cca_embedding2[:, 0], cca_embedding2[:, 1], c='green', label='UMAP Dataset 2')
                    plt.title('Canonical Variables of UMAP Dataset 2')
                    plt.xlabel('Canonical Variable 1')
                    plt.ylabel('Canonical Variable 2')
                    plt.legend()
                    
                    plt.show()
                    
                    ```
                    
                
                ### Complete Example Code
                
                Here's the complete code for applying CCA on UMAP embeddings and visualizing the results:
                
                ```python
                # Install the required libraries
                !pip install umap-learn numpy scikit-learn matplotlib
                
                # Import libraries
                import numpy as np
                import umap
                from sklearn.cross_decomposition import CCA
                import matplotlib.pyplot as plt
                
                # Generate synthetic data for demonstration
                data1 = np.random.rand(100, 50)  # 100 samples with 50 features
                data2 = np.random.rand(100, 50)  # Another dataset with the same dimensions
                
                # Apply UMAP to both datasets
                reducer = umap.UMAP(n_components=10, random_state=42)
                embedding1 = reducer.fit_transform(data1)
                embedding2 = reducer.fit_transform(data2)
                
                # Apply CCA on UMAP embeddings
                cca = CCA(n_components=2)  # Number of components to extract
                cca.fit(embedding1, embedding2)
                
                # Transform the data using CCA
                cca_embedding1, cca_embedding2 = cca.transform(embedding1, embedding2)
                
                # Optional: To see the correlation coefficients
                corrs = [np.corrcoef(cca_embedding1[:, i], cca_embedding2[:, i])[0, 1] for i in range(cca_embedding1.shape[1])]
                print("Canonical Correlation Coefficients:", corrs)
                
                # Plot the first two canonical variables
                plt.figure(figsize=(12, 6))
                
                plt.subplot(1, 2, 1)
                plt.scatter(cca_embedding1[:, 0], cca_embedding1[:, 1], c='blue', label='UMAP Dataset 1')
                plt.title('Canonical Variables of UMAP Dataset 1')
                plt.xlabel('Canonical Variable 1')
                plt.ylabel('Canonical Variable 2')
                plt.legend()
                
                plt.subplot(1, 2, 2)
                plt.scatter(cca_embedding2[:, 0], cca_embedding2[:, 1], c='green', label='UMAP Dataset 2')
                plt.title('Canonical Variables of UMAP Dataset 2')
                plt.xlabel('Canonical Variable 1')
                plt.ylabel('Canonical Variable 2')
                plt.legend()
                
                plt.show()
                
                ```
                
                ### Explanation
                
                1. **UMAP**: Reduces the dimensionality of the datasets to a more manageable number of components (10 in this case).
                2. **CCA**: Finds the linear combinations of the UMAP embeddings that are maximally correlated.
                3. **Visualization**: Plots the first two canonical variables for both datasets to inspect the correlation visually.
                
                By following this approach, you can effectively use CCA on UMAP embeddings to compare the relationships between two datasets.
                
            - how to itnerpret this: Canonical Correlations: -0.23755626716455025
                
                Interpreting the results from Canonical Correlation Analysis (CCA) involves understanding both the canonical correlations and the correlation coefficients:
                
                ### Canonical Correlations
                
                The canonical correlations indicate the overall relationship between the sets of canonical variables. These values represent the strength of the linear relationships between the two sets of UMAP embeddings.
                
                - **Canonical Correlations**: These are the correlations between the first pair of canonical variables, the second pair, and so on. In your case, the canonical correlation values were found to be:
                    - 0.23755626716455025
                
                The negative value here might indicate an inverse relationship for the first canonical variable pair. Canonical correlations close to 1 or -1 indicate strong linear relationships, while those close to 0 indicate weak relationships.
                
                ### Correlation Coefficients
                
                The correlation coefficients between the transformed UMAP embeddings (canonical variables) represent how well the corresponding pairs of canonical variables correlate with each other.
                
                - **Correlation Coefficients**: These values show the correlation between the pairs of canonical variables. In your case, the coefficients are:
                    - [0.49006658992455354, 0.26686220794459087]
                
                Here's what these coefficients mean:
                
                1. **First Canonical Variable Pair**:
                    - Correlation Coefficient: 0.49006658992455354
                    - This indicates a moderate positive linear relationship between the first pair of canonical variables derived from the UMAP embeddings of the two datasets.
                2. **Second Canonical Variable Pair**:
                    - Correlation Coefficient: 0.26686220794459087
                    - This indicates a weaker positive linear relationship between the second pair of canonical variables.
                
                ### Interpretation Summary
                
                - The first canonical correlation is negative, suggesting an inverse relationship for the first pair of canonical variables.
                - The correlation coefficient for the first canonical variable pair is around 0.49, indicating a moderate positive relationship. This suggests that the first pair of canonical variables derived from the UMAP embeddings have a moderate positive linear association.
                - The correlation coefficient for the second canonical variable pair is around 0.27, indicating a weak positive relationship.
                
                These results suggest that while there is some degree of linear association between the canonical variables derived from the UMAP embeddings of your datasets, the relationships are not very strong. This implies that the structures captured by the UMAP embeddings of the two datasets have moderate to weak linear relationships when examined through the lens of CCA.
                
                ### Improving Interpretability
                
                To further interpret and validate these results, you might consider:
                
                1. **Visual Inspection**:
                    - Plot the pairs of canonical variables to visually inspect their relationships. This can help you understand the nature of the relationships better.
                    
                    ```python
                    plt.figure(figsize=(12, 6))
                    
                    plt.subplot(1, 2, 1)
                    plt.scatter(cca_embedding1[:, 0], cca_embedding2[:, 0], c='blue', label='First Canonical Variable Pair')
                    plt.title('First Canonical Variable Pair')
                    plt.xlabel('First Canonical Variable (Dataset 1)')
                    plt.ylabel('First Canonical Variable (Dataset 2)')
                    plt.legend()
                    
                    plt.subplot(1, 2, 2)
                    plt.scatter(cca_embedding1[:, 1], cca_embedding2[:, 1], c='green', label='Second Canonical Variable Pair')
                    plt.title('Second Canonical Variable Pair')
                    plt.xlabel('Second Canonical Variable (Dataset 1)')
                    plt.ylabel('Second Canonical Variable (Dataset 2)')
                    plt.legend()
                    
                    plt.show()
                    
                    ```
                    
                2. **Dimensionality Reduction Before CCA**:
                    - If the datasets are very high-dimensional, consider using PCA to reduce the dimensionality before applying UMAP and CCA. This can sometimes enhance the interpretability of the canonical variables.
                3. **Investigating Other Relationships**:
                    - If the linear relationships are weak, you might consider investigating non-linear relationships using other methods such as kernel CCA or distance correlation.
                
                By examining these additional aspects, you can gain deeper insights into the relationships between your datasets as captured by UMAP and analyzed by CCA.
                
- ✅ is there an issue with comparing umap due to randomness? how to better quantitatively compare them?
    
    [https://chatgpt.com/c/ca134e95-ac2c-4290-b9c7-107dbeba93fe](https://chatgpt.com/c/ca134e95-ac2c-4290-b9c7-107dbeba93fe)
    
    - umap is NOT random on projection (cosine sim) but becomes random after uniform nearest neighbor
- ✅ [UMAP](UMAP%206019e8cd74ca4abebc143f9f13760055.md)

Compare SAEs of Different Toy Models

- ✅ ask #sparse-autoencoders OpenMI slack for prev work (chatgpt doesnt find anything)
    
    Hi, I'm looking to run experiments similar to this section:
    
    [https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality)
    
    which involves comparing "different dictionary learning runs trained on different activations from a different transformer with different random seeds but otherwise identical hyperparameters." I was wondering if anyone has also done anything similar to this before (say a blog post / repo) and if they found any additional insights not mentioned by the Towards Monosemanticity paper? Would add to my lit review too
    
    I may not have the resources to train on 100 billion tokens from the pile like Anthropic did, so looking to scale it down or do something similar with toy models, hoping the saes on these toy models would still find "true enough" features that could be compared
    
- ⚠️ **EXPM**: train saes on toy model
    
    Models to Reproduce
    
    [https://colab.research.google.com/drive/1elITv-IptxH-J8aeDDvjXLNsu7p5JbxL#scrollTo=Gh3FW5X2BrsM](https://colab.research.google.com/drive/1elITv-IptxH-J8aeDDvjXLNsu7p5JbxL#scrollTo=Gh3FW5X2BrsM)
    
    - [https://www.lesswrong.com/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition](https://www.lesswrong.com/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition)
    - [https://www.lesswrong.com/posts/a5wwqza2cY3W7L9cj/sparse-autoencoders-find-composed-features-in-small-toy](https://www.lesswrong.com/posts/a5wwqza2cY3W7L9cj/sparse-autoencoders-find-composed-features-in-small-toy)
    - [https://transformer-circuits.pub/2023/monosemantic-features#problem-setup](https://transformer-circuits.pub/2023/monosemantic-features#problem-setup)
        - NOTE: these are not toy models, just 1L models, because trained on 100 billion tokens, so may not be reproducible. Try toy models.
        - ✅ Model Dataset and Sizes
            
            ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%201.png)
            
        - ✅ training feasibility how-to
            - [https://chatgpt.com/c/13d7b189-1900-439f-ba71-a2a478416f7e](https://chatgpt.com/c/13d7b189-1900-439f-ba71-a2a478416f7e)
            - [https://transformer-circuits.pub/2023/monosemantic-features#setup-transformer](https://transformer-circuits.pub/2023/monosemantic-features#setup-transformer)
            - [https://transformer-circuits.pub/2023/monosemantic-features#appendix-transformer](https://transformer-circuits.pub/2023/monosemantic-features#appendix-transformer)
        - ✅ tokenizer
            
            BPE tokenizer: **Byte-Pair Encoding tokenization**
            
            [https://arxiv.org/pdf/2101.00027](https://arxiv.org/pdf/2101.00027)
            
            We analyze the distribution of document lengths, as well as the number of bytes-per-token using the GPT-2 tokenizer
            
        - ISSUE: on `train_loader`, FileNotFoundError: [https://the-eye.eu/public/AI/pile/train/00.jsonl.zst](https://the-eye.eu/public/AI/pile/train/00.jsonl.zst)
    - No_Position_Experiment.ipynb: [https://colab.research.google.com/github/TransformerLensOrg/TransformerLens/blob/main/demos/No_Position_Experiment.ipynb#scrollTo=seo_rX_d1uO6](https://colab.research.google.com/github/TransformerLensOrg/TransformerLens/blob/main/demos/No_Position_Experiment.ipynb#scrollTo=seo_rX_d1uO6)
    - ARENA 1.4: Training Toy Model with Superposition
        
        [https://colab.research.google.com/drive/1mHKZpkhYAr0WWAQo2Y6pXL08yNfJHOVx?usp=sharing#scrollTo=MtjKlA3D5DS0](https://colab.research.google.com/drive/1mHKZpkhYAr0WWAQo2Y6pXL08yNfJHOVx?usp=sharing#scrollTo=MtjKlA3D5DS0)
        
    - nanda tutorail: [https://colab.research.google.com/drive/1u8larhpxy8w4mMsJiSBddNOzFGj7_RTn?usp=sharing](https://colab.research.google.com/drive/1u8larhpxy8w4mMsJiSBddNOzFGj7_RTn?usp=sharing)
- ✅ [Ashkan meeting notes](Ashkan%20meeting%20notes%20cf47680d80a04812ac616fd4597e9e09.md)
- ✅ summary to fazl
    
    Hi, as a quick summary of last week, I was running experiments and researching for a new project topic I can discuss with you next meeting. After some discussions with the other interns and lab members such as Ashkan, I decided this new project was more novel and impactful. The topic is about improving the understanding of SAE feature universality via geometric metrics such as canonical correlation analysis. Essentially, it is an extension of this Anthropic work: [https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality)
    
    My approach, which has not been tried yet on SAE feature space, uses geometric measurement techniques similar to (Kornblith et al, 2019),  “Similarity of Neural Network Representations Revisited” (of which Geoffrey Hinton is a coauthor). My project’s aim is also similar to that paper.
    
    I talked with other interns who offered good advice for the next experimental steps. I also presented the project to Ashkan, who gave a lot of other good advice in our meeting and found the proposed approach to be viable and interesting. 
    
- ✅ [Sim of NN revisted](Repr%20sim%20papers%20f1e073e6e4124d3ba7b6929d92cee13d/Sim%20of%20NN%20revisted%2074743e14a51b4f7593e67ad7b2e92162.md)
- ✅ [**Sholto Douglas & Trenton Bricken - How to Build & Understand GPT-7's Mind**](https://www.youtube.com/watch?v=UTuuTTnjxMQ&ab_channel=DwarkeshPatel)
    - deception circuit
    - universality
    - doing research part-time into residency
- ✅ **EXPM**: CCA on pretrained SAEs (across models)
    
    [CM_pretrained_SAE_save_actvs](https://colab.research.google.com/drive/1hzWwIq0iULPvZt-GFnY8TPNvqZiDgsen#scrollTo=V5O39_ub_e0_)
    
    - ✅ load two SAEs : gpt2, gemma-2b
        - latest loading nb: https://github.com/jbloomAus/SAELens
        - [https://jbloomaus.github.io/SAELens/sae_table/](https://jbloomaus.github.io/SAELens/sae_table/)
            - [https://chatgpt.com/c/56aeb74d-8e2d-4673-a087-bdef0e1e37f6](https://chatgpt.com/c/56aeb74d-8e2d-4673-a087-bdef0e1e37f6)
            - [https://www.lesswrong.com/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream](https://www.lesswrong.com/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream)
    - ✅ get LLM then SAE actvs and save to drive
    
    [CM_pretrained_SAE_UMAP_CCA.ipynb](https://colab.research.google.com/drive/1lDWBYXwKSxOiwJzILvedjMCxNCkT0xsG#scrollTo=kUYRF57KNxrL)
    
    - ✅ for every pair of their middle layers, run UMAP then CCA
        - make sure you use UMAP correctly
        - [https://chatgpt.com/c/ca93999b-8aab-40e7-b5cf-fbacbb639bc6](https://chatgpt.com/c/ca93999b-8aab-40e7-b5cf-fbacbb639bc6)
- Find features with high actv corr in pretrained SAEs (across models)
    
    [actv_corr_mat.ipynb](https://colab.research.google.com/drive/1iM4Ta6NLR9Ka4sG6q9YUzpla-Rezm0bx#scrollTo=qdOPsIx9vHIH)
    
    - ✅ "For each feature in run A/1, we find the closest feature by activation similarity in run B/1," what's an efficient algorithm to do this?
        
        [https://chatgpt.com/c/38c634db-f342-480d-bbf7-3371938dca51](https://chatgpt.com/c/38c634db-f342-480d-bbf7-3371938dca51)
        
    - BRUTE FORCE: for each input sample, get actvs for all features. a batch sample of N has N x F activations. So there are F vectors of size N. In the second SAE, ther are F_2 vectors of size N. We can take the cosine sim of every F vector with every F_2 vector to get a cosine sim, and find the highest
        - ✅ load saved actvs
        - cosine sim mat: [https://chatgpt.com/c/100362a0-be1e-4bc1-97ca-a97fed673706](https://chatgpt.com/c/100362a0-be1e-4bc1-97ca-a97fed673706)
            
            [https://claude.ai/chat/ca272816-0223-49f4-9660-bbf6cb726061](https://claude.ai/chat/ca272816-0223-49f4-9660-bbf6cb726061)
            
            - NOTE: this is not 1-1 mapping, but each feature has a ranking
        - ✅ given cosine_sim_matrix , for each feature in A, find the top 3 features in B, and vice versa. make this into a function.
        - function that finds the top 5 pairs with the highest sim
            - compare these on neuronpedia
                - jump to feature: [https://www.neuronpedia.org/gpt2-small](https://www.neuronpedia.org/gpt2-small)
                - ISSUE: can’t jump to feature for L12 of gemma-2b, only L6
                - Save gemma L6 feat actvs
    - Reproduce Anthropic’s A vs B actvs plot
        - ✅ take a slice of last dim of (batch*seq, features) for each A and B
        - ✅ is this nonzero actvs? most tokens should be 0 for one feature
            
            no; plot says most actvs are around 0, if you look at the long line of pts at each axis’s 0 that represents how those pts are 0 at A but zero or nonzero at B, etc.
            
        - what data pts do they use? every (btach, seq) of a sample?
            - two features would be similar in this sense if they take similar values over a diverse set of data.
                - they cite SVCCA. So they must’ve tried it. once you try your obvious cca approaches, ask them what issues there were with it, and if any issues with yours.
        - ✅ how come get nans in corrcoeff
            
            If you're getting NaN values in the correlation coefficient calculation, it's usually due to one of these reasons:
            
            1. Constant values: If all values in one or both of the tensors are the same (i.e., the tensor has zero variance), the correlation coefficient will be undefined (NaN).
            2. Presence of NaN or infinity values: If your tensors contain NaN or infinity values, these will propagate through the correlation calculation.
            3. All zero values: If one or both tensors contain all zeros, this can also lead to NaN in the correlation calculation.
            
            To diagnose and fix this issue, you can try the following:
            
            1. Check for constant values:
            
            ```python
            print("A constant?:", torch.all(tensor_A == tensor_A[0]))
            print("B constant?:", torch.all(tensor_B == tensor_B[0]))
            
            ```
            
            1. Check for NaN or infinity values:
            
            ```python
            print("A has NaN:", torch.isnan(tensor_A).any())
            print("B has NaN:", torch.isnan(tensor_B).any())
            print("A has inf:", torch.isinf(tensor_A).any())
            print("B has inf:", torch.isinf(tensor_B).any())
            
            ```
            
            1. Check for all zero values:
            
            ```python
            print("A all zeros?:", torch.all(tensor_A == 0))
            print("B all zeros?:", torch.all(tensor_B == 0))
            
            ```
            
            1. If you're still getting NaNs, you can try to calculate the correlation manually:
            
            ```python
            def manual_correlation(x, y):
                x_mean = x.mean()
                y_mean = y.mean()
                x_std = x.std()
                y_std = y.std()
            
                if x_std == 0 or y_std == 0:
                    return 0  # or you might want to return NaN here
            
                return ((x - x_mean) * (y - y_mean)).mean() / (x_std * y_std)
            
            corr = manual_correlation(tensor_A, tensor_B)
            print("Manual correlation:", corr)
            
            ```
            
            1. If you're dealing with very small numbers, numerical precision issues could arise. In this case, you might want to scale your data:
            
            ```python
            tensor_A_scaled = (tensor_A - tensor_A.mean()) / tensor_A.std()
            tensor_B_scaled = (tensor_B - tensor_B.mean()) / tensor_B.std()
            correlation = np.corrcoef(tensor_A_scaled.numpy(), tensor_B_scaled.numpy())[0, 1]
            
            ```
            
            After applying these checks and potential fixes, you should be able to identify the cause of the NaN values and address it appropriately. If you're still having issues, you might want to examine a small subset of your data to see if there are any unexpected patterns or values.
            
        - if A is first feature vector and so is B (For two models), is this is the same as their corrcoef: cosine_sim_matrix[0][0]
            
            You're on the right track, but there's an important distinction to make between correlation coefficients and cosine similarity. While they're related, they're not exactly the same. Let's break this down:
            
            1. Correlation coefficient (Pearson's r):
                - Measures the linear relationship between two variables
                - Ranges from -1 to 1
                - Is invariant to scaling and shifting of the variables
            2. Cosine similarity:
                - Measures the cosine of the angle between two vectors in a multi-dimensional space
                - Ranges from -1 to 1 for real numbers (1 for identical orientation, 0 for orthogonal, -1 for opposite orientation)
                - Is invariant to scaling but not to shifting (direction)
            
            In many cases, especially when dealing with centered data (mean = 0), the cosine similarity and the Pearson correlation coefficient will be very close or even identical. However, they can differ significantly if the data is not centered.
            
            Given your context:
            
            - If `A` is the first feature vector from one model and `B` is the first feature vector from another model
            - And `cosine_sim_matrix[0][0]` represents the cosine similarity between these two vectors
            
            Then `cosine_sim_matrix[0][0]` would indeed give you the cosine similarity between the first feature vectors of the two models. This is often a good measure of how similar the features are across models.
            
            To compare this with the correlation coefficient:
            
            ```python
            import numpy as np
            from scipy.spatial.distance import cosine
            
            # Assuming A and B are your feature vectors (as numpy arrays or torch tensors)
            A = ...  # Your first feature vector from model A
            B = ...  # Your first feature vector from model B
            
            # Convert to numpy if they're torch tensors
            if torch.is_tensor(A):
                A = A.numpy()
            if torch.is_tensor(B):
                B = B.numpy()
            
            # Cosine similarity
            cosine_sim = 1 - cosine(A, B)  # cosine() returns distance, so we subtract from 1
            
            # Correlation coefficient
            correlation = np.corrcoef(A, B)[0, 1]
            
            print(f"Cosine similarity: {cosine_sim}")
            print(f"Correlation coefficient: {correlation}")
            
            ```
            
            If your data is centered (mean subtracted), these values should be very close. If not, they might differ. The choice between cosine similarity and correlation coefficient depends on your specific needs:
            
            - Use cosine similarity if you're interested in the angle between the vectors regardless of their magnitudes or if you want to ignore constant offsets.
            - Use correlation coefficient if you're specifically interested in linear relationships and want to account for both the angle and the spread of the data.
            
            In the context of comparing feature activations across models, cosine similarity is often preferred because it focuses on the direction of the feature vectors rather than their exact magnitudes.
            
        - is "not invariant shifting" meaning will have diff values if translate vectors say diff origin, but not direction?
            
            You've got it exactly right. Let me break this down to clarify:
            
            1. "Not invariant to shifting" means that if you translate the vectors (i.e., add a constant to all elements), the cosine similarity can change.
            2. This is in contrast to the direction of the vectors, which remains unchanged by translation.
            
            Here's a simple example to illustrate:
            
            Let's say we have two vectors:
            A = [1, 2, 3]
            B = [2, 3, 4]
            
            The cosine similarity between A and B will be some value, let's call it X.
            
            Now, if we shift both vectors by adding 10 to each element:
            A' = [11, 12, 13]
            B' = [12, 13, 14]
            
            The cosine similarity between A' and B' will be different from X.
            
            However, the direction of the vectors in space remains the same. If you were to plot these vectors, A and A' would point in the same direction, as would B and B'.
            
            This property is why cosine similarity is often used in text analysis and recommendation systems where the magnitude of the vectors might not be as important as their direction.
            
            In contrast, correlation coefficient is invariant to both scaling and shifting. If you add a constant to all elements of both vectors, the correlation coefficient will remain the same.
            
            This difference can be important depending on your specific application and what aspect of the data you're most interested in comparing.
            
        - give equation for corr coeff
            
            Certainly! The equation for the correlation coefficient, specifically Pearson's correlation coefficient, is as follows:
            
            r = Σ((x_i - x̄)(y_i - ȳ)) / (√Σ(x_i - x̄)² * √Σ(y_i - ȳ)²)
            
            Where:
            
            - r is the Pearson correlation coefficient
            - x_i and y_i are individual sample pairs
            - x̄ is the mean of all x values
            - ȳ is the mean of all y values
            - Σ represents the sum over all samples
            
            This can also be written as:
            
            r = cov(X,Y) / (σ_X * σ_Y)
            
            Where:
            
            - cov(X,Y) is the covariance of X and Y
            - σ_X is the standard deviation of X
            - σ_Y is the standard deviation of Y
            
            In computational terms, you might see it implemented like this:
            
            r = Σ((x_i - x̄)(y_i - ȳ)) / (n * σ_X * σ_Y)
            
            Where n is the number of samples.
            
            This formula calculates the normalized measure of the covariance between two variables X and Y, giving a value between -1 and 1, where:
            
            - 1 indicates a perfect positive linear correlation
            - 0 indicates no linear correlation
            - 1 indicates a perfect negative linear correlation
            
            The correlation coefficient measures both the strength and direction of the linear relationship between two variables.
            
    - reproduce their plot of finding highest mapping for each feature
        
        ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%202.png)
        
    - ✅ ask #neuronpedia for pretrained SAEs
        
        I saw in sae_table that there’s SAEs for the GPT2 small, Gemma-2B, and Mistrial-7B models. I also see several pretrained SAEs on other models (Llama-3, PMs, etc). I was wondering if there’s a list of links to uploaded pretrained SAEs in general (eg. GeLU-1L, tinystories, GPT2-medium)? 
        
        I’m guessing people may have filled out the form to upload them to Neuronpedia too and they’re currently being processed. Also, as seen in sae_table, we can load gemma-2b-res-jb layer 12 post, but not search/steer it on Neuronpedia. I was wondering why? Also, were there only SAEs for L0, L6 and L12 due to cost?
        

---

### Future work

- compare actvs using narrow dataset (eg. only Arabic)

ISSUE: different tokenizers

[https://chatgpt.com/c/7e74ddc0-0694-46da-9b4a-447ee68093c2](https://chatgpt.com/c/7e74ddc0-0694-46da-9b4a-447ee68093c2)

- ask neuronpedia on advice for sae training

https://github.com/jbloomAus/SAELens/issues/191

[https://www.lesswrong.com/posts/5XmxmszdjzBQzqpmz/interpreting-preference-models-w-sparse-autoencoders](https://www.lesswrong.com/posts/5XmxmszdjzBQzqpmz/interpreting-preference-models-w-sparse-autoencoders)

can feasibly train saes on: tinystories (up to 4L), gpt2

[https://www.lesswrong.com/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream](https://www.lesswrong.com/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream)

- what's the estimated cost for training effective saes for all layers of gpt-2 medium?
    
    [https://chatgpt.com/c/78867e7f-511e-4a8d-b5fd-c05473c92f99](https://chatgpt.com/c/78867e7f-511e-4a8d-b5fd-c05473c92f99)
    

- matrix plot of cca for layer-layer similarity

- proposal: (timestamped, ask fazl first before send to others)
    - in-scope list of (justified) ideas and concrete plan to enact them
    - out-of-scope future work

1. train saes on toy model
    - ask amir for advice
        
        hi, as part of my project, I'm looking to extend the results of
        [https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality)
        
        in which they compare sae feature activations (of a dataset) for two 1-layer LLMs trained on The Pile with 100 billion tokens. Given that's infeasible for me, I'm looking to train 2 toy model LLMs and compare their saes with CCA, etc. The pretrained SAElens models are too different to compare (eg. gpt2, gemma, mistrial use diff tokenizers). I was wondering if you have any advice for picking the params for the toy models and their saes, and est time + costs? thanks!
        
    1. look for feature splitting
2. sim code for between saes
    1. ISSUE: your umap isn’t right by plotting the batch*seq; correct this
    2. CCA or CKA
3. in another layer, track how a specific set of features (eg. love or cat) changes after steering

- ISSUE: what if two LLMs use different tokenizer? then how do you compare if they have the same tokens? for now, try to compare LLMs with same tokenizer.
- funcsim: are two features across models also connected to analogous features in later layers?
- can you compare ground truth features as the intermediary? no- the "ground truth features" are model specific right, so it wouldn't make sense to see if two diff LLMs are learning the same ground truth feature

- people to contact:
    
    (towards / scaling anthropic papers)
    
    ask fazl beforehand to ensure timestamp (no work leaks) [he knows who can be trusted as if they have incentive to not steal his work]
    
    8/20, code base distr sys: [https://boards.greenhouse.io/anthropic/jobs/4020305008](https://boards.greenhouse.io/anthropic/jobs/4020305008)
    
    - josh batson
        
        [https://www.youtube.com/watch?v=sQar5NNGbw4&ab_channel=Anthropic](https://www.youtube.com/watch?v=sQar5NNGbw4&ab_channel=Anthropic)
        
    - [https://www.trentonbricken.com/about/](https://www.trentonbricken.com/about/)
        - [https://www.youtube.com/watch?v=UTuuTTnjxMQ&ab_channel=DwarkeshPatel](https://www.youtube.com/watch?v=UTuuTTnjxMQ&ab_channel=DwarkeshPatel)
    - callum

- 8/8: contact anthropic
    - started in july
    - they cite SVCCA. So they must’ve tried it. once you try your obvious cca approaches, ask them what issues there were with it, and if any issues with yours.
        - compare approaches; give pros/cons each
    - show them the mapping of higher order structures and working with kiho
        - eg) do they both arrange months circular? what other circulars found by algo?
            - can we map the circular structures?
    - toy model feature splitting: give cost estimates of llm and sae training
    - complexity of mapping algorithms

- train a model to map between features from two saes

Run code of “The Geometry of Categorical” on new data related to behavior

- email kiho on interpreting paper and checking if method to measure simplex based on orth relations is right
    - ask about comparing relations across models
    - ask if using TDA to identify simplex works
        - in a space of data point, how do I find which data points belong to an n-simplex, etc, using algorithms?
- brainstorm how to extend hierarchical concepts
    - steer by animal simplex
        - get convex hull that represents “animal” and add it?
            - how do you even add this?
            - estimate vector and convex hull using trained projection (LDA, linear map)- which to recommend?
- put face features thru existing code (geom, circ) on multiple models and look for hierachy (dog face and human face orthon) and other patterns
- find where hierarchy is detected in code nbs
    
    3_Noun_Heatmap.ipynb
    
    animal has cosine 1 with all others concepts bc they are all related to animal. but why 1, the max?
    

[**Anthropic Beta Steering API**](https://docs.google.com/forms/d/e/1FAIpQLSc9HRcRFOdid4NJ4-Lyo3HdUybbevMqERWscJIbqilLQRuSQA/viewform)

---

Steering circuits

- [The fact that both features contribute to the final output indicates that the model has partially predicted a sentiment from John's statement (the second feature) but will do more downstream processing on the content of his statement (as represented by the first feature) as well.](https://www.notion.so/Scaling-Monosemanticity-Extracting-Interpretable-Features-from-Claude-3-Sonnet-3219b222ee8943ac9ba1a07963f975b0?pvs=21)
    - Can we better formalize these causal relations between features?
- 80Gb instead of 40Gb for A100- vast ai may specify this
- automatically find steering vectors using dataset samples
- [https://www.lesswrong.com/posts/qykrYY6rXXM7EEs8Q/understanding-sae-features-with-the-logit-lens#Characterizing_Features_via_the_Logit_Weight_Distribution](https://www.lesswrong.com/posts/qykrYY6rXXM7EEs8Q/understanding-sae-features-with-the-logit-lens#Characterizing_Features_via_the_Logit_Weight_Distribution)
- [https://discordapp.com/channels/1080558777608183829/1229803194331304047](https://discordapp.com/channels/1080558777608183829/1229803194331304047)
- UNDERSTANDING AND CONTROLLING A MAZESOLVING POLICY NETWORK
    
    [https://arxiv.org/pdf/2310.08043](https://arxiv.org/pdf/2310.08043)
    
    decompose cheese vector
    
- saelens: train sae on gpt2-xl L20 and put steering vector through it, then interpret top features
- [**Scaling Laws for Dictionary Learning**](https://transformer-circuits.pub/2024/april-update/index.html#scaling-laws)
    - [https://transformer-circuits.pub/2024/april-update/index.html](https://transformer-circuits.pub/2024/april-update/index.html)
    - [https://transformer-circuits.pub/2024/april-update/index.html#ablation-exps](https://transformer-circuits.pub/2024/april-update/index.html#ablation-exps)
        - scaling features and observe behavior change
- [**Sparse Interpretable Features in Vision Transformers**](https://www.lesswrong.com/posts/bCtbuWraqYTDtuARg/towards-multimodal-interpretability-learning-sparse-2)
- Copy of HookedSAETransformerDemo.ipynb
    
    [https://colab.research.google.com/drive/1GlrX5K1LlZWrMWhr2EGCttqBIJ1jPrEn](https://colab.research.google.com/drive/1GlrX5K1LlZWrMWhr2EGCttqBIJ1jPrEn)
    
    why priveleged basis: [https://dynalist.io/d/n2ZWtnoYHrU1s4vnFSAQ519J](https://dynalist.io/d/n2ZWtnoYHrU1s4vnFSAQ519J)
    
- Llama2_TL_SAE_training_v1
- where are multiple feature vectors if steering vectors are an avg??

instead of deleting file, transfer new code into shared nb by deleting all old cells and pasting new ones from ‘select all’

---

- Method to reduce dead neurons using loss constraints which force learned wright's to have activations be within useful feature range
- Steering is by prompts, not model. CMAP is by model. Compare them.
- [https://apartresearch.com/project/from-sparse-to-dense-refining-the-machiavelli-benchmark-for-real-world-ai-safety](https://apartresearch.com/project/from-sparse-to-dense-refining-the-machiavelli-benchmark-for-real-world-ai-safety)
- Study: https://github.com/nrimsky/CAA
    - is it 3rd last b/c adds end of seq token somehow in some operation? Find this operation