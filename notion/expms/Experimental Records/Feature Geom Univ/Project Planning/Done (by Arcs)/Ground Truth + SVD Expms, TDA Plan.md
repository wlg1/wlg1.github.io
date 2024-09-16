# Ground Truth + SVD Expms, TDA Plan

Ground truth jaccard on high cosine features

- ✅ [synthData_jaccard_v1.ipynb](https://colab.research.google.com/drive/1BlFYR_ubdkNyC5yF_ftY5RY-Qt1K-WLI): ground truth features: highest cosine sim shuffle matrix then apply jaccard
    - re-run get cluster actvs bc didnt save right GTF
    - ISSUE: `grTrue_feats[highest_correlations_indices]` ; RuntimeError: CUDA error: device-side assert triggered
        - error msg
            
            RuntimeError: CUDA error: device-side assert triggered
            CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
            For debugging consider passing CUDA_LAUNCH_BLOCKING=1.
            Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.
            
        
        after get this error, must restart nb, so make sure save all data before runnign this
        
        SOLN: `grTrue_feats.cpu()[:, highest_correlations_indices]` because we’re correlating the cols (features) in synth feats (encoder), not decoder (which uses features as rows), so it’s diffferent from using it in jaccard_subset_ts_1L_2L.ipynb
        
    - Also, we should use `jaccard_similarity(grTrue_feats.cpu(), enc_weights_a.t()[:, highest_correlations_indices])` because the `highest_correlations_indices`
    - `highest_correlations_values, highest_correlations_indices = cos_sims.max(dim=0)`
    does highest_correlations_indices have the row indices as the indices and col indices as values or other way around?
        
        In the context of the code snippet you provided, `highest_correlations_indices` will have the **column indices as the indices** and the **row indices as the values**.
        
        Here's what happens step-by-step:
        
        1. `cos_sims.max(dim=0)`:
            - This calculates the maximum value along dimension 0 (i.e., along the rows for each column).
            - The `max(dim=0)` function returns two tensors:
                - `highest_correlations_values`: Contains the maximum value for each column.
                - `highest_correlations_indices`: Contains the index (row index) of the maximum value for each column.
        2. `highest_correlations_indices`:
            - This tensor will have the same number of elements as there are columns in `cos_sims`.
            - Each element in `highest_correlations_indices` represents the row index where the maximum value was found for that particular column.
        
        So, in summary:
        
        - The **indices** of `highest_correlations_indices` correspond to the **column indices**.
        - The **values** of `highest_correlations_indices` correspond to the **row indices** where the maximum value was found for each column.
    - So using cos_sims = torch.matmul(learned_norm.t(), ground_truth_norm), should I do learned_norm.t()[:, highest_correlations_indices] to match the cols?
        
        If you want to match the columns of `learned_norm.t()` with the indices obtained in `highest_correlations_indices` to align with the ground truth based on the highest cosine similarity, the operation you mentioned is almost correct but needs a slight adjustment.
        
        Given that `highest_correlations_indices` contains the row indices from the original `learned_norm.t()`, you want to select the corresponding columns from `learned_norm.t()` based on these indices.
        
        However, `highest_correlations_indices` is expected to be a 1D tensor where each element represents a row index for a specific column, so you would use the following approach:
        
        ```python
        aligned_learned = learned_norm.t()[:, highest_correlations_indices]
        
        ```
        
        This will give you the columns of `learned_norm.t()` that correspond to the indices in `highest_correlations_indices`.
        
        ### Detailed Explanation:
        
        - `learned_norm.t()` gives you the transpose of `learned_norm`, so the shape changes from `(num_samples, num_features)` to `(num_features, num_samples)`.
        - `highest_correlations_indices` is a 1D tensor with a length equal to the number of columns in `cos_sims` (which corresponds to the number of columns in `ground_truth_norm` and the rows in `learned_norm.t()`).
        - `learned_norm.t()[:, highest_correlations_indices]` selects columns from `learned_norm.t()` corresponding to the row indices stored in `highest_correlations_indices`.
        
        After this operation, `aligned_learned` will have columns reordered to match the highest cosine similarity with the ground truth.
        
    - normalizing each matrix before taking cosine sim mat doesn’t make a difference
- ✅ generate B using shared GTF, and rearrange col (G) ordering so diff freqs
    - ✅ same time on A100 vs T4 bc few matmuls, most time is sampling
    - ✅ pick 50% shared features and record the shared indices
    - ✅ rearrange col (G) ordering so diff freqs (actually no need; the selected inds already shuffles the features)
    - ✅ measure jaccard sim on that 50% shared
        - find which features in SAE B weights have highest cosine sim with
            - [give a 256x512 matrix X and another matrix Y that's 256x256, how to find the cols of X that have highest cosine sim to the cols in Y?](https://chatgpt.com/c/d202916e-ce2c-4304-b5f3-2875d54958f0)
    - ✅ jaccard on non-repeats
        - RESULT: also high
    - ✅ the MMCS is also higher for A & B on the shared than for total. Why?
        - Why is MMCS between models higher than between models and GTF?
        - Why is MMCS the same for unshared and B, but jaccard is low for unshared and B?
        - **SOLN: you used** `calculate_MMCS(shared.cpu(), Afeats_sharedGTF, device)`. Before, you used `calculate_MMCS(enc_weights_a.t(), grTrue_feats, device)`, and luke’s code switches only if not equal. But now, we use (256, 256), so it’s always equal and won’t switch (?)
            - NOTE: get diff results for `calculate_MMCS(Afeats_sharedGTF, shared.cpu(), device)` vs `calculate_MMCS(shared.cpu(), Afeats_sharedGTF, device)`
                - MMCS is not symmetric, unlike Jaccard
            - Finally, `calculate_MMCS(Afeats_sharedGTF, unshared.cpu(), device)` is low while doing it with shared is high.
            - The REASON why we shouldn’t use `.t()` is because we already did `Bfeats_sharedGTF = enc_weights_b.t()[:, max_sim_indices_b]`, so using `.t()` would be undoing it!
    - weird thing is, jaccard is same value  after shuffling. doesn’t matter if corr or not. but this shuffling destroys it in tinystories. why?
        - in tinystories, you didn’t re-arrange; you took different subsets. k-NN seems to always give the same output regardless of col order.
            - SOLN: that is because we are COMPARING ROWS. When we shuffled, we changed cols and kept the rows, so of course everythihng is the same
    - when we compare the rows of GTF vs SAE encoder, that’s the model dims. So we’re comparing by the same neuron. That’s valid.
        - We can also compare via correlated features. Note that before, we DIDN’T re-arrange the correlations of the shared feats vs model A, so that’s why corr is still low.
        - This is correct because we didn’t use `.t()` yet: `jaccard_similarity(grTrue_feats.cpu(), enc_weights_a.t()[:, highest_correlations_indices])` . `grTrue_feats` is hxG, and `enc_weights_a.t()` is hxG
            - But bc we use `.t()` here, `Bfeats_sharedGTF = enc_weights_b.t()[:, max_sim_indices_b]`, then `Bfeats_sharedGTF` is already hxG.
                - THIS IS CORRECT: `Afeats_sharedGTF_shuffled = Afeats_sharedGTF[:, torch.tensor(col_idxs)]`
                - we should just fix it so that we get rid of the .t() AND put max sim indices (of features) in rows when making _sharedGTF: `Bfeats_sharedGTF = enc_weights_b[max_sim_indices_b, :]` This makes it less confusing when calling Jaccard, as we usually think of the encoder as Gxh (since it takes in as input and outputs features).
                    - note that MMCS should always use features in cols, since it’s taking cosine sim for every col pair. If we use h in col, that’s taking cosine sim for every neuron pair. Meaningless when it comes to SAE feature similarity!
        - before each comparison, note if `.t()` turns each arg into hxG or Gxh!!!
        - Then how can `jaccard_similarity(Afeats_sharedGTF, Bfeats_sharedGTF)` make sense, because those use h from different “models”?
- ✅ `highest_correlations_values, highest_correlations_indices = cos_sims.max(dim=0)`
what does this do? are the index values in highest_correlations_indices the indices for the first or second arg of this: cos_sims = torch.matmul(learned_norm.t(), ground_truth_norm)
    
    This line finds the maximum values along a specific dimension (`dim=0`) in the `cos_sims` matrix.
    
    - `dim=0`: This specifies that the operation should be performed along the first dimension (rows) of the matrix. Since `cos_sims` has a shape of `(n, p)`, this operation will be performed across each column of the matrix, i.e., for each of the `p` columns.
    - `cos_sims.max(dim=0)` returns two tensors:
        - `highest_correlations_values`: A tensor containing the maximum value from each column.
        - `highest_correlations_indices`: A tensor containing the index (row) at which the maximum value occurs for each column.
    
    ### Which indices are in `highest_correlations_indices`?
    
    The indices in `highest_correlations_indices` correspond to the rows of the `cos_sims` matrix. Therefore, they indicate the indices from the **first argument** (`learned_norm.t()`, which is the transpose of `learned_norm`) of the `torch.matmul` operation.
    
    ### Summary:
    
    - The `highest_correlations_indices` tensor contains the indices of the rows in `cos_sims` (and therefore the indices from the **first argument** of `torch.matmul`, which corresponds to `learned_norm.t()` or `learned_norm`) that have the highest cosine similarity with each column of `ground_truth_norm` (the second argument).
- ✅ so would learned_features[highest_correlations_indices, :] or ground_truth_features[highest_correlations_indices, :] be the correct way to rearrange
    
    Given the context, the goal appears to be rearranging the features in either `learned_features` or `ground_truth_features` based on the indices found in `highest_correlations_indices` to align with the highest cosine similarities.
    
    Let's clarify the situation:
    
    - `cos_sims = torch.matmul(learned_norm.t(), ground_truth_norm)` produces a matrix where each element represents the cosine similarity between a feature vector from `learned_norm` and a feature vector from `ground_truth_norm`.
    - `highest_correlations_indices` contains the indices of the rows in `learned_norm` (since `learned_norm.t()` is the transpose of `learned_norm`) that have the highest similarity with each column of `ground_truth_norm`.
    
    ### Rearranging `learned_features` vs. `ground_truth_features`:
    
    - `learned_features[highest_correlations_indices, :]`:
        - This would rearrange the rows of `learned_features` to match the order of indices with the highest cosine similarity for each column in `ground_truth_features`.
    - `ground_truth_features[highest_correlations_indices, :]`:
        - This would rearrange the rows of `ground_truth_features` based on the indices from `learned_features`. However, since `highest_correlations_indices` corresponds to indices from `learned_features`, using these indices to rearrange `ground_truth_features` does not align semantically.
    
    ### Correct Approach:
    
    To align the features based on the highest cosine similarity, you should rearrange the `learned_features` using `highest_correlations_indices`. This ensures that each feature in `learned_features` is aligned with the corresponding feature in `ground_truth_features` that it is most similar to.
    
    **Therefore, the correct way to rearrange the features is:**
    
    ```python
    rearranged_learned_features = learned_features[highest_correlations_indices, :]
    
    ```
    
    This rearranged matrix `rearranged_learned_features` should now have rows ordered in a way that maximizes similarity with the corresponding rows of `ground_truth_features`.
    
- ✅ note that as a whole, finding corr of GTF and encoder A may not work. perhaps certain subsets do better. can we “rank” these subsets?
    - note that the shared_GTF ALREADY takes indices of the encoder features with highest GTF with shared. So `Afeats_sharedGTF[Afeats_sharedGTF_corrinds, :]` does nothing.
    - we can first try testing only those features with the highest correlations
        - [modify this to keep only top 100 indices with highest values, outputting both those indices and the values in highest_correlations_indices of those indices:](https://chatgpt.com/c/5ecabd2c-b50e-449b-91b4-7a3ab33ab3c4)
        - This does well!
            
            ![Untitled](Ground%20Truth%20+%20SVD%20Expms,%20TDA%20Plan%2039c103e13e3b4c248cbc77804d43216e/Untitled.png)
            
        - take unique members of this. if it’s only 20, DON’T use k=10 else get something high. try k=3.
        - but note that the “highest corr features” not necc are from same cluster!
    - the top 200 matches to the 512 SAE features: only 25 of those SAE features are unique.
        - check that kNN isn’t getting the same features each time
        - but random shuffling of indices doesn’t depend on that.
        - anyways, doesn’t this mean that the SAE features are polysemantic as these top 25 match to multiple GTFs?
    - all this is really saying is that the clusters are learned along with the features
    - Plot and color those features on a umap
- ✅ [for jaccard similarity using knn as a similarity metric, do the paired instances have to be 1-1?](https://chatgpt.com/c/d16b63b0-cc0f-4f1e-8929-2a6f0955d5cc)
    
    When using Jaccard similarity as a metric within the k-Nearest Neighbors (k-NN) algorithm, the paired instances do not necessarily have to be 1-1 in a strict sense, but typically, you do compare each instance in the dataset against every other instance in a pairwise manner.
    
    ### Here's how it works:
    
    1. **Jaccard Similarity**: This metric is typically used for comparing the similarity of sets. Given two sets \( A \) and \( B \), the Jaccard similarity is calculated as:
    \[
    \text{Jaccard Similarity}(A, B) = \frac{|A \cap B|}{|A \cup B|}
    \]
    where \( |A \cap B| \) is the size of the intersection of the sets, and \( |A \cup B| \) is the size of the union of the sets.
    2. **k-NN and Jaccard Similarity**:
        - In the context of k-NN, when you want to calculate the Jaccard similarity between instances, each instance is typically treated as a set of features (or binary attributes).
        - For instance, if you have binary vectors representing whether certain features are present or not, you compute the Jaccard similarity between these vectors.
        - You would compare each instance (or binary vector) with every other instance to determine the similarity, and then choose the k nearest neighbors based on the highest Jaccard similarity values.
    3. **1-1 Pairing**:
        - The concept of "1-1" typically refers to a one-to-one relationship between elements in two sets. However, in k-NN with Jaccard similarity, you don't pair up elements within the sets themselves. Instead, you're comparing entire sets (or instances) with each other.
        - The pairing happens when you are calculating the Jaccard similarity between each possible pair of instances in the dataset.
    
    ### Summary:
    
    - The instances themselves do not have to be in a 1-1 relationship for Jaccard similarity. The pairing refers to comparing each instance with every other instance.
    - The Jaccard similarity is used to determine how similar two sets (or binary vectors) are, and this similarity metric is then used to identify the nearest neighbors in the k-NN algorithm.
    
    Let me know if you need more detailed clarification or examples!
    
- ✅ try jaccard on unif distrb
    - the jaccard sim after aligning correlated features seems pretty good compared to random
        
        ![Untitled](Ground%20Truth%20+%20SVD%20Expms,%20TDA%20Plan%2039c103e13e3b4c248cbc77804d43216e/Untitled%201.png)
        
    - the uniqueness is also better
        
        `len(list(set(highest_correlations_indices)))` is 503 out of 512
        
    - even better if you take the top 100 feats
        
        ![Untitled](Ground%20Truth%20+%20SVD%20Expms,%20TDA%20Plan%2039c103e13e3b4c248cbc77804d43216e/Untitled%202.png)
        
        ![Untitled](Ground%20Truth%20+%20SVD%20Expms,%20TDA%20Plan%2039c103e13e3b4c248cbc77804d43216e/Untitled%203.png)
        

Writeup + Slides of Progress So far

- ✅ make fig of jaccard (idroo, slides), put in overleaf + slides
- ✅ writeup jaccard on synth actvs & tinystories in overleaf + slides
    - in meetings, say “some evidence” for X- don’t say weak or few or suggests
    - possible to compare (in a table):
        - GTF_A vs SAE_A
        - shared_GTF_A vs SAE_A
        - unshared_GTF_A vs SAE_A
        - unshared_GTF_B vs SAE_A (this is the 2nd output of GTF_shared)
        - SAE_A vs SAE_B
        - repeated matches & no repeated matches
        - jaccard on scrambled
        - jaccard using h (toymod neuron) in common vs using correlated features in common
            - only former works; later doesn’t
            - using h means cluster by neuron index based on their features. this doesn’t mean nearby features; it means neurons are nearby
    - we can’t compare synth actv SAE actvs bc there’s no tokens to put thru the SAE
    - table: random VS correlated feature matching, then MMCS & Jaccard
        - mean, SD, t-stat, df, p-val, conf intv
- ✅ slides: list of strongest / most interesting results so far
    1. Jaccard on tinystories SAE actvs (3 strong, 3 interesting)
    2. Jaccard on tinystories entire space of corr weights (3 strong, 3 interesting)
    3. Jaccard on tinystories subspaces of corr weights (2 strong, 3 interesting)
    4. Jaccard on synthetic actv SAE weights (2 strong, 2 interesting)
        1. uniform & top 100 (mostly unique) only when high cosine pairs
        2. clustered top 100 (needs to be mostly unique) only when high cosine pairs
        3. Across models: SAE features with high cosine sim to shared GTF are more similar in MMCS (obviously) and somewhat more similar in terms of Jaccard
    5. Mapper (1 strong, 3 interesting)
    6. UMAP Fsplit (1 strong, 3 interesting)
- make slides
    - (not colab screenshots, just text)
    - first outline order of expms to put in
    - take text from editor, not pdf!
    - very short text bullets (copied from overleaf)
    - make figures and tables of expms
- prepare to ask for advice in meetings
    - email to ask for tips on writing: advice for turning bullet points so far into better introduction? questions readers may have about project that they may have after reading abstract? how to rearrange/outline points to include? relation to safety?
    - other expms for stronger arguments?
    - better tests than t test?
    - better ways to test- instead of random corr?
    - feedback on figures / tables to put in paper
- ✅ msg **enjalot** on viz code for 2 umap hover

SVD on Encoder matrices

[Aug 13th Vidit meeting notes](Ground%20Truth%20+%20SVD%20Expms,%20TDA%20Plan%2039c103e13e3b4c248cbc77804d43216e/Aug%2013th%20Vidit%20meeting%20notes%20b4cbd391c12c4a54b99baa7b8f81021c.md)

- [svd_on_SAE_univ.ipynb](https://colab.research.google.com/drive/1fDhJgYSzoeQ-7ElqX4xylDSQgWKT2ESD#scrollTo=HmEJdeCjPC4e)
    - [https://chatgpt.com/c/bcf62580-c0b7-4bd5-8857-de80b9021f94](https://chatgpt.com/c/bcf62580-c0b7-4bd5-8857-de80b9021f94)
    - comm dia justify SVD: [https://chatgpt.com/c/8ab1cc0f-5881-4bbd-9957-9ec6693700fd](https://chatgpt.com/c/8ab1cc0f-5881-4bbd-9957-9ec6693700fd)
    - comm dia: [https://www.overleaf.com/project/66bb6a3625411b3a8a5667e7](https://www.overleaf.com/project/66bb6a3625411b3a8a5667e7)
    - is svd singular value similarity not rotation invariant?
        
        No, SVD (Singular Value Decomposition) is indeed **rotation invariant** in the sense that the singular values themselves do not change under rotations or more generally under orthogonal (or unitary) transformations.
        
    - does it make sense to take cosine sim of two singular value vectors
        
        Taking the cosine similarity of two singular value vectors can be done, but it may not be particularly meaningful or useful in most contexts. Here's why:
        
        ### 1. **Nature of Singular Values:**
        
        - **Magnitude Information:** Singular values represent the magnitude of the variance captured by corresponding singular vectors. They are non-negative and usually ordered from largest to smallest.
        - **Relative Importance:** Singular values typically convey the relative importance of different features (or directions) in the data. The larger the singular value, the more important the corresponding feature.
        
        ### 2. **Cosine Similarity:**
        
        - **Definition:** Cosine similarity measures the cosine of the angle between two non-zero vectors in an inner product space. It is a measure of orientation rather than magnitude, ranging from -1 (opposite direction) to 1 (same direction), with 0 indicating orthogonality.
        - **Use Cases:** Cosine similarity is often used in text analysis, recommendation systems, and other contexts where the orientation or direction of the vectors (rather than their magnitude) is important.
        
        ### 3. **Why It May Not Be Meaningful for Singular Values:**
        
        - **Non-Negative Vectors:** Since singular values are non-negative, the cosine similarity between two singular value vectors will always be between 0 and 1, which reduces the interpretability compared to when it is used on vectors with potentially negative values.
        - **Magnitude vs. Direction:** Singular values convey magnitude, not direction. Cosine similarity is designed to compare directions, so using it to compare singular values (which are about magnitude) might not yield insights that are directly useful or interpretable.
        - **Normalization Effect:** Singular values are often already ordered and represent proportions of the data's variance. Using cosine similarity might obscure these proportions, as it doesn't take the actual magnitude into account as effectively as a measure like L2 distance does.
        
        ### When It Might Make Sense:
        
        - **Normalized Singular Values:** If you normalize the singular values first (e.g., dividing each singular value by the sum of all singular values), then taking the cosine similarity might be more interpretable, as you're comparing the shape or relative distribution of the singular values across the two vectors.
        - **Specific Applications:** In certain niche applications, where the relative proportions or patterns of singular values are more important than their absolute magnitudes, cosine similarity might be a useful comparison metric. However, this is less common in standard matrix analysis.
        
        ### Alternatives:
        
        - **L2 Distance:** Typically, the L2 distance (Euclidean distance) between singular value vectors is used to compare them because it reflects the actual magnitude differences between the vectors.
        - **Percentage Difference:** Normalizing the singular values and then comparing them using percentage differences or other normalized metrics might provide more insight than cosine similarity.
        
        ### Conclusion:
        
        While it is technically possible to compute the cosine similarity between two singular value vectors, it is generally not the most meaningful or insightful metric for comparing singular values. The magnitude-focused nature of singular values makes distance-based metrics (like L2 distance or normalized percentage difference) more appropriate for comparison in most contexts. Cosine similarity is better suited for situations where direction, rather than magnitude, is the primary concern.
        
    - [https://www.baeldung.com/cs/euclidean-distance-vs-cosine-similarity](https://www.baeldung.com/cs/euclidean-distance-vs-cosine-similarity)
    - is np.linalg.norm the same as singular_values / np.sum(singular_values)
        
        No, `np.linalg.norm(singular_values)` and `singular_values / np.sum(singular_values)` are not the same, and they serve different purposes in normalization.
        
        ### 1. **`np.linalg.norm(singular_values)` (L2 Norm):**
        
        - **Definition:** `np.linalg.norm(singular_values)` computes the L2 norm (also known as the Euclidean norm) of the `singular_values` vector.
        - **Formula:** For a vector \( \mathbf{s} = [s_1, s_2, \dots, s_n] \), the L2 norm is calculated as:
        \[
        \|\mathbf{s}\|_2 = \sqrt{s_1^2 + s_2^2 + \dots + s_n^2}
        \]
        - **Purpose:** The L2 norm gives a measure of the overall magnitude of the vector. Normalizing by the L2 norm is useful when you want to scale the vector so that its overall magnitude (length) becomes 1, but retain the relative proportions of its components.
        
        ### 2. **`singular_values / np.sum(singular_values)` (Sum Normalization):**
        
        - **Definition:** `singular_values / np.sum(singular_values)` normalizes the `singular_values` vector by dividing each singular value by the sum of all singular values.
        - **Formula:** For a vector \( \mathbf{s} = [s_1, s_2, \dots, s_n] \), the sum normalization is calculated as:
        \[
        \mathbf{s}*{\text{normalized}} = \left[\frac{s_1}{\sum*{i=1}^n s_i}, \frac{s_2}{\sum_{i=1}^n s_i}, \dots, \frac{s_n}{\sum_{i=1}^n s_i}\right]
        \]
        - **Purpose:** Sum normalization scales the vector so that the sum of all its components becomes 1. This is useful when you want to interpret the components of the vector as proportions or probabilities.
        
        ### Key Differences:
        
        - **Magnitude vs. Proportion:**
            - **L2 Norm Normalization:** This keeps the vector's direction the same but scales it to unit length. It’s about preserving the shape of the vector while adjusting its overall magnitude.
            - **Sum Normalization:** This adjusts each component to represent a fraction of the total sum, which is useful for interpreting the components as relative contributions or proportions.
        
        ### Example to Illustrate the Difference:
        
        ```python
        import numpy as np
        
        # Example singular values
        singular_values = np.array([3, 4, 5])
        
        # L2 Norm of singular values
        l2_norm = np.linalg.norm(singular_values)
        
        # L2 Norm Normalization
        l2_norm_normalized = singular_values / l2_norm
        
        # Sum of singular values
        sum_singular_values = np.sum(singular_values)
        
        # Sum Normalization
        sum_normalized = singular_values / sum_singular_values
        
        print("Singular Values:", singular_values)
        print("L2 Norm:", l2_norm)
        print("L2 Norm Normalized:", l2_norm_normalized)
        print("Sum of Singular Values:", sum_singular_values)
        print("Sum Normalized:", sum_normalized)
        
        ```
        
        ### Expected Output:
        
        ```
        Singular Values: [3 4 5]
        L2 Norm: 7.0710678118654755
        L2 Norm Normalized: [0.42426407 0.56568542 0.70710678]
        Sum of Singular Values: 12
        Sum Normalized: [0.25 0.33333333 0.41666667]
        
        ```
        
        ### Interpretation:
        
        - **L2 Norm Normalized:** The vector `[0.42426407, 0.56568542, 0.70710678]` has a unit L2 norm (length of 1), but the relative proportions between the components are preserved from the original vector.
        - **Sum Normalized:** The vector `[0.25, 0.33333333, 0.41666667]` has components that sum to 1, representing the relative proportions of the original singular values.
        
        ### Conclusion:
        
        `np.linalg.norm(singular_values)` and `singular_values / np.sum(singular_values)` are different normalization techniques with different purposes. L2 norm normalization is about scaling the vector to unit length, while sum normalization is about scaling the vector so that its components sum to 1, making them interpretable as proportions.
        
    - which one makes more sense for comparing singular values
        
        When it comes to comparing singular values between two matrices, the choice of normalization technique depends on what aspect of the singular values you're interested in:
        
        ### 1. **Sum Normalization (Proportional Comparison):**
        
        - **Purpose:** Sum normalization is useful when you want to compare the relative importance of each singular value within the context of its matrix. This method makes each singular value a proportion of the total "energy" or variance captured by the matrix.
        - **Use Case:** If your goal is to understand how much of the total variance each singular value contributes in each matrix and to compare these contributions across matrices, sum normalization is the better choice. It effectively transforms the singular values into a probability distribution, which can then be compared using measures like L2 distance or Kullback-Leibler divergence.
        - **Example:** Suppose you're comparing two matrices to see how similarly they distribute variance across different dimensions (i.e., how similar their feature distributions are). Sum normalization would highlight whether one matrix concentrates more variance in a few dimensions while another distributes it more evenly.
        
        ```python
        def sum_normalize(singular_values):
            return singular_values / np.sum(singular_values)
        
        ```
        
        ### 2. **L2 Norm Normalization (Shape Comparison):**
        
        - **Purpose:** L2 norm normalization is useful when you want to compare the overall shape or distribution of the singular values between matrices while ensuring that the comparison is not biased by the overall scale (magnitude) of the singular values.
        - **Use Case:** If your focus is on comparing the "shape" or distribution pattern of the singular values (i.e., how the energy is distributed across dimensions) while abstracting away from their absolute magnitudes, L2 norm normalization is appropriate. It treats the singular values as a direction in a vector space and normalizes them to a unit vector, allowing for comparison based on the angle or shape of this distribution.
        - **Example:** If you're analyzing how similar two datasets are in terms of the patterns or structure they capture, regardless of the absolute amount of variance, L2 norm normalization would be more relevant.
        
        ```python
        def l2_normalize(singular_values):
            return singular_values / np.linalg.norm(singular_values)
        
        ```
        
        ### Practical Comparison:
        
        - **Sum Normalization:** Makes the comparison about how singular values distribute their captured variance relative to the total. This is particularly useful when the matrices might capture different amounts of total variance but you're interested in comparing the relative importance of each captured feature.
        - **L2 Norm Normalization:** Focuses on comparing the overall pattern or shape of the singular values. This is more useful when you want to compare the distribution form (e.g., are the singular values concentrated or spread out) without being influenced by the scale.
        
        ### **Which Makes More Sense?**
        
        - **Sum Normalization:** If the primary concern is how variance or energy is distributed across the singular values, and you are comparing the importance of features relative to the total variance captured by each matrix, sum normalization is generally more informative.
        - **L2 Norm Normalization:** If you are more interested in the overall shape or pattern of the singular value distribution and want to compare this aspect independently of scale, then L2 norm normalization makes more sense.
        
        ### Conclusion:
        
        For most comparisons involving singular values from SVD, **sum normalization** tends to be more interpretable and useful, especially when comparing matrices that might capture different total amounts of variance. It allows you to directly compare the relative significance of each singular value across matrices, making it easier to interpret differences or similarities in how the matrices represent data.
        
        However, if your focus is on comparing the overall distribution pattern of the singular values (abstracting from scale), **L2 norm normalization** could be the better choice.
        
- U and V have diff dims, so sing vals are the smaller of the two?
- maybe just look at dist instead; the “normalized by froeb” sounds wrong
- lie grouops
    - [all trasnformations in lie group do not change singular values, but change the basis. if two matricse (transformations) are in same lie group, they would have same singular values despite different basis?](https://chatgpt.com/c/54c66219-4e07-4322-ab68-648e13d25cc0)

Brainstorm within-mod feature struc

[Fs Structure within models](Ground%20Truth%20+%20SVD%20Expms,%20TDA%20Plan%2039c103e13e3b4c248cbc77804d43216e/Fs%20Structure%20within%20models%20ce5d60899d95465d998802dde77dec4b.md)

[cross model stitching ideas](Ground%20Truth%20+%20SVD%20Expms,%20TDA%20Plan%2039c103e13e3b4c248cbc77804d43216e/cross%20model%20stitching%20ideas%20fe49d84de701446eaf9298598a008ddc.md)

Sim metrics on more SAEs

- ✅ meeting questions to max
    - thoughts on sim SVD method?
        - does this hold for privileged sae basis that is rotation variant- should each sae not be in same lie group?
        - how to measure L2 dist on a scale? noramlize over the Frobenius norm of the singular values (sum of the squares of the singular values and then take the square root)?
    - thoughts on jaccard sim of correlated feats? similar to feature fam approach
        - why cca, etc results unexpected (see below)?
        - on synth data?
    - thoughts on jaccard on actvs?
    - how to interpret perm procr results
    - explain orth + MMCS
- ✅ in jaccard_subset_ts_1L_2L.ipynb: [https://github.com/mklabunde/resi/blob/main/repsim/measures/procrustes.py](https://github.com/mklabunde/resi/blob/main/repsim/measures/procrustes.py)
- ✅ in jaccard_subset_ts_1L_2L.ipynb: RSA, CCA, CKA also works and latter 2 are fast
    - why does cca work better after re-arranging? shouldn’t that be indpt of pairings?
- ✅ compae cosine sim to actv corr
    - cosine sim doesn’t work; don’t get high scores for the metrics
- ✅ try metrics on actvs

[Aug 14 max meeting notes](Ground%20Truth%20+%20SVD%20Expms,%20TDA%20Plan%2039c103e13e3b4c248cbc77804d43216e/Aug%2014%20max%20meeting%20notes%2041372e4a75484c88988c9e8778d3c186.md)

- ✅ writeup sim repr expms
- stat test ideas
    - t-test on jaccard vs random
        - ask chatgpt for advice & checking ideas
        - One-Sample t-test
    - Independent Two-Sample t-test : need a population of two distributions, so get more SAEs or more samples

SVD on SAEs

- ✅ SVD_on_SAE_univ_v2.ipynb
    - decide which metrics to keep
        - assess the validity of these metrics. rank which ones you think are theoretically justified and which arent and explain:
            - [sonnet](https://claude.ai/chat/801a54b8-d60d-4ee9-8051-0cc14914fb43)
            - opus: [https://claude.ai/chat/39b37a62-b63b-40ce-b242-89d8fd795613](https://claude.ai/chat/39b37a62-b63b-40ce-b242-89d8fd795613)
    - chatgpt to make tables in rich text for each result, then plots across results
        - given a dict of a string to value, give code to plot the values on a number line from least to highest. labels each point with their string from the dict
            - [https://claude.ai/chat/9de3d16e-06eb-4f84-a5de-860d0239f800](https://claude.ai/chat/9de3d16e-06eb-4f84-a5de-860d0239f800)
        - [https://stackoverflow.com/questions/23186804/graph-point-on-straight-line-number-line-in-python](https://stackoverflow.com/questions/23186804/graph-point-on-straight-line-number-line-in-python)
- ✅ SVD_on_SAE_univ_v3.ipynb
    - run on bigger SVD weights
    - run svcca on LLM weights
        - wait that doesn’t make sense bc we didn’t perm align them yet using actv corr
- ✅ save_LLM_w_actvs.ipynb
    - make sure you use the right model weights- the tinystories mlp0 have mlp.c_fc and mlp.c_proj. make sure the hooked transforer layer "blocks.0.hook_mlp_out” corresponds to right one.
        - explain what c_fc and c_proj are. which one is likely "blocks.0.hook_mlp_out”
            
            In the context of the `GPTNeoMLP` model architecture you've described, `c_fc` and `c_proj` are two linear transformation layers that serve specific purposes in the model's feedforward (MLP) block:
            
            1. **`c_fc` (Feedforward Control Layer)**:
                - **Function**: This is a linear layer that expands the dimensionality of the input tensor.
                - **Parameters**:
                    - **`in_features=1024`**: The number of input features to this layer.
                    - **`out_features=4096`**: The number of output features. This expansion allows the MLP to internally represent more complex transformations of the input data before reducing it back down.
                - **Usage**: It acts as the first transformation step in the MLP block of the transformer architecture, increasing the complexity and capacity of the model to capture more intricate patterns in the data.
            2. **`c_proj` (Projection Layer)**:
                - **Function**: This linear layer projects the expanded data back to a lower dimension, matching the original input size.
                - **Parameters**:
                    - **`in_features=4096`**: Matches the output features of `c_fc`, indicating that it takes the expanded data.
                    - **`out_features=1024`**: Reduces the dimension back down to the original size, ensuring the output can be integrated with other parts of the transformer model (like subsequent layers or residual connections).
                - **Usage**: This is the final step in the MLP block, serving to condense the information processed by the block back into a more manageable form.
            
            Regarding which one is likely "`blocks.0.hook_mlp_out`":
            
            - The label "`blocks.0.hook_mlp_out`" typically would refer to the output of some hook placed either within or at the end of an MLP block within the first transformer block (`blocks.0`). Given the description of the MLP block, it would most logically refer to the output of the `c_proj` layer, as this is where the final transformation within the MLP block occurs, outputting the data that will be passed back into the main flow of the transformer model or used for further processing/residual connections.
    - svcca DOESN’T work on aligning the highest corr of model by actvs
    - so even though SVD shows LLMs are very similar, we cannot find their similar neighs unless we use SAEs !?!
        - the thing is comparing singular values doesn’t show if the feature relns are similar bewteen models, it just says they should be similar if we align them. it doesn’t show how to align them, because they’re entangled and polysemantic. we can’t align them neuron by neuron. so we can align them by saes.
    - we do not find feature relns transfer between LLM weights.
    - WRONG- once we use c_proj, the LLM ARE aligned by SVCCA. but lower than SAE space.
    - WAIT- svcca is somewhat high in LLMs, higher in SAEs, but JACCARD is extremely low in aligned ! these metrics are saying different things.
        - [after aligning two samples in matrices, what does it mean for moderately high svcca score but very low jaccard?](https://chatgpt.com/c/74254872-39b8-4e8a-99ef-a8a76da93aee)
            
            When comparing two datasets, particularly in contexts like machine learning models, neural network activations, or other high-dimensional data, different metrics can provide insights into various aspects of similarity or dissimilarity between the datasets. Two such metrics are Singular Vector Canonical Correlation Analysis (SVCCA) and the Jaccard index. Here’s what it means when you have a moderately high SVCCA score but a very low Jaccard index:
            
            1. **Moderately High SVCCA Score:**
                - **SVCCA** is used to compare the similarities in the activation spaces of neural networks or any sets of high-dimensional vectors. It reduces the dimensionality of the data by focusing on the most informative directions (using singular value decomposition), then applies canonical correlation analysis (CCA) to these directions to find linear relationships.
                - A moderately high SVCCA score suggests that the linear relationships between the principal components of the two datasets are quite strong. This indicates that, at least in the dominant directions of variance, the datasets are capturing similar information or features.
            2. **Very Low Jaccard Index:**
                - **Jaccard Index** is a measure used to determine the similarity and diversity of sample sets. It evaluates the size of the intersection divided by the size of the union of the sample sets.
                - A very low Jaccard index indicates that the actual elements (or specific features/labels) in the two datasets largely do not overlap. This can mean that while the datasets operate similarly in a transformed or feature-extracted space (as indicated by SVCCA), they consist of very different individual elements or examples.
            
            **Interpreting the Combination:**
            
            - When you have a high SVCCA score and a low Jaccard index, it suggests that the two datasets, while fundamentally different in their specific contents or instances, process or represent these differences in a structurally similar way. This might be common in situations where different datasets (e.g., images from different categories, text from different topics) are transformed through similar types of neural networks or feature extraction techniques, resulting in similar overarching structures or patterns, despite differing in the actual data points or labels.
            
            This scenario could be informative in fields like transfer learning, where different but structurally similar datasets might leverage the same underlying model architectures effectively, or in comparative studies where the focus is on understanding how different data types are abstractly processed by similar algorithms.
            
    - compare by cosine perm alignment too
- ✅ SVD_on_SAE_univ_v4: use c_proj for LLMs
    - why is `gpt2_med.transformer.h[0].mlp.c_proj` 4096x1024 ? in any case, c_fc from TS has low L2 dist to both c_fc and c_proj of gpt2med
    - `(S_GPT2_0_cfc, S_GPT2_0)`  are also incredibly similar in L2 dist, having `0.0795688`
    - pythia already used the out vector `dense_4h_to_h`, so no need to redo those
    - corr arrange before svd: why do i get different but similar values after changing row order?
    - [for l2 distance between svds, why do i get different after changing row order of one matrix? i thought singular values don't depend on row order?](https://chatgpt.com/c/b01895eb-b8b8-4568-ae18-85a9db8b5701)
        - SOLN: If any rows are duplicated or omitted, the matrix's structure and thus its singular values will change.
- ✅ organize results. Make a table of LLM vs SAE metrics in overleaf
    - [why do I get two diff cosine sim matrices for these two codes:](https://chatgpt.com/c/ef2e5ef3-fcf6-4e4a-95af-3af44de524d9)
        
        axis on rows vs cols affects this
        
    - fig: show how randomly shuffled pairs works
    
    first present summary of conclusions based on results so far, then present a few tables (2 tables, 2 plots).
    
    table to compare SAE vs LLM on mean cosine sim, mean actv corr, singular value L2 distance, jaccard, svcca, RSA, procrustes normalized
    
    - LLM weights have low cosine sim, high SVD sim, low jaccard mnn, moderate svcca, low RSA
        - 0.17 actv corr avg
    - SAE weights have high cosine sim, high SVD sim, high jaccard sim, high svcca, high RSA
        - 0.5 actv corr avg
    
    report before and after aligning with cosine and actv corr
    
    found similar results for synthetic activations
    
    - [https://chatgpt.com/c/4d210892-3865-40f8-a318-cdd6f0af249f](https://chatgpt.com/c/4d210892-3865-40f8-a318-cdd6f0af249f)
        - read then interpret results
        - does high sim in l2 dist of singular values mean one can find one neuron in an LLM  to align with another neuron?
            
            High similarity in the L2 distance of singular values between two models (like an LLM and an SAE) suggests that their principal components in feature space are similar. However, this does not necessarily mean that one can easily align individual neurons from one model to another. Singular value similarity indicates global alignment of feature subspaces rather than direct one-to-one neuron correspondence. Neuron alignment would require additional analysis beyond just singular value comparison, considering factors like activation patterns and overall function within the network.
            

[Fazl Ashkan Meeting 16 Aug](Ground%20Truth%20+%20SVD%20Expms,%20TDA%20Plan%2039c103e13e3b4c248cbc77804d43216e/Fazl%20Ashkan%20Meeting%2016%20Aug%203d1fd39bb6784cd3b4dd61dfcd3e911e.md)

- ✅ acl confrence are you supposed to make changes after review before committing
    - [**After I receive reviews, can I revise and commit at the same time?**](https://aclrollingreview.org/ACL-2023-session/)
        
        no
        
    - [https://www.reddit.com/r/MachineLearning/comments/1boea3w/acl_2024_reviews_discussion/](https://www.reddit.com/r/MachineLearning/comments/1boea3w/acl_2024_reviews_discussion/) :
        
        nope, you can only clarify minor concerns. otherwise, they will suggest you to send the paper to the next ARR cycle
        
    - [https://aclrollingreview.org/authors](https://aclrollingreview.org/authors)
        
        **These options are mutually exclusive**: you cannot submit a revision and in parallel commit to a venue, for example. See [the CFP](https://aclrollingreview.org/cfp) for all of the rules on dual submissions.
        
- ✅ SVD_on_SAE_univ_v5
    - get rid of multp layer comparisons (just use MLP0)
    - [The large size of the matrices (16384x1024) may caused the singular values to stabilize and appear similar? No; even small values are similar. Why?](https://colab.research.google.com/drive/1f-RA1wga2LYkOuKmDygT6kASjS2DOYmw#scrollTo=o0QpCmLgAxlw&line=1&uniqifier=1)
- ✅ email to vidit
    - SVD_on_SAEs: link to vidit
    - [give a clear yes or no if this is right or not: if two weight matrices are related by orthogonal change of basis transformations P and Q from general linear groups that do not change the singular values of the two weight matrices.](https://chatgpt.com/c/7c8eb714-db46-4c02-9659-c86b59cf625c)
        
        [https://claude.ai/chat/aacde6a2-7571-44a4-b762-ae41ff035bd3](https://claude.ai/chat/aacde6a2-7571-44a4-b762-ae41ff035bd3)
        
    - Singular value distances between models, prelim results
        
        I ran some simple tests for the L2 distance of singular values between SAEs. The plot below reports the L2 distance for normalized singular values. I think there are better baselines to compare to, but for now I just compared the values between models to values between (model, rand), where rand draws values from a standard normal distribution. The distance between two SAEs trained on two different LLMs (each called tinystories, or "ts"; first model is tinystories_onelayer, and the second is tinystories_twolayers), is 0.21. compared to 0.70 for (SAE1, rand).
        
        I also compared the distance between LLMs. GPT2 is another LLM with similar architecture to the tinystories models, but trained on different data. The distance between LLMs is 0.08, which is closer than all the other data points. This is not always the case; for Pythia, another model, (ts, Pythia) ~= 0.2. These models may be similar if they are trained on overlapping data, but the tinystories training data is different from GPT2's training data (though GPT2 was trained on a lot of data, which may be similar to tinystories' data). I have also compared different layers of the same model and across models, compared SAEs with LLMs, and more, but I only showed the main results for readability. I'll double check the code again too.
        
        I am looking to interpret if these values show similarity between SAEs (though these are not the best SAEs; better trained ones may be more similar). Thus, I'm looking for better baselines to compare to, and was wondering if you had any suggestions?
        
        The code for these calculations is here: [https://colab.research.google.com/drive/1yE31oKXwFwPKdulaMH5YmnWNJc6T53OG?usp=sharing](https://colab.research.google.com/drive/1yE31oKXwFwPKdulaMH5YmnWNJc6T53OG?usp=sharing)
        
        ---
        
        Additionally, a second project I'm looking to apply topological techniques to is to find feature relation structures within LLMs (or SAEs), rather than looking for universality across models. This is motivated by recent research which found simplices in LLMs representing hierarchical concepts ([https://arxiv.org/abs/2406.01506](https://arxiv.org/abs/2406.01506)) and graphs of "feature families" in SAEs also representing general->specific concepts ([https://arxiv.org/abs/2408.00657](https://arxiv.org/abs/2408.00657)). I can discuss this better in a meeting. It is not related to feature universality like the above tests; perhaps there are some interesting ideas you or your students may have about this topic.
        
        ---
        
        Lastly, just to provide more information on these models you may find interesting, I have been looking into various metrics to compare neuron spaces in both LLMs and SAEs. I first apply a permutation transformation to align individual neurons across models, and then I apply representational similarity metrics for comparisons that are invariant to certain transformations like rotation. So far, I find that individual LLM neurons are not correlated across models, but SAE feature neurons are correlated (around half are 1-1 pairs). Then, after correlated feature neurons are aligned in pairs, the similarity metrics show some relational similarity. This plot below summarizes this:
        
        [https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdJU9J5OSmS70smVX9V4Z0Q2fZRxhctFsdyGHnQTBT8oyr0wTpMUrCgs_y9XXFU21yHrCqsEWTgGTzf6IevWiJJZgGmP_c3hDk4gS5CKzh2UpDeMdZxZJoqjh_0y-8wsaHRaeBD3QCnp1JhAEQRDUTY4gXpYDwW=s2048?key=9BJIhGQY1dK1xkDkYRCniA](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdJU9J5OSmS70smVX9V4Z0Q2fZRxhctFsdyGHnQTBT8oyr0wTpMUrCgs_y9XXFU21yHrCqsEWTgGTzf6IevWiJJZgGmP_c3hDk4gS5CKzh2UpDeMdZxZJoqjh_0y-8wsaHRaeBD3QCnp1JhAEQRDUTY4gXpYDwW=s2048?key=9BJIhGQY1dK1xkDkYRCniA)
        
        MMCS is the mean of the highest cosine similarity pairs (it is expected to be low as each model uses a different basis, so cosine sim wouldn't work). "Mean actv corr" is the mean of neurons paired by Pearson correlation of their activations on a batch of token inputs (
        
        [this approach was used in this paper](https://transformer-circuits.pub/2023/monosemantic-features#feature-arabic-universality)
        
        ). A permutation transformation of rows in a weight matrix is done by pairing each highest correlated feature on the same index.
        
        After performing a permutation transformation using activation correlation, I apply 1-(L2 distance of singular values), which is the metric we discussed. The other three are Jaccard Nearest Neighbors, Singular Value Canonical Correlation Analysis (SVCCA), and Representational Similarity Analysis (RSA). SVCCA may have higher scores for a similar reason as singular value distance; it may be doing a "pairing" by singular vectors, if two weight matrices are related by orthogonal change of basis transformations P and Q from general linear groups that do not change the singular values of the two weight matrices.
        
        I also have a plot which compares these values to the average scores of randomly shuffled pairs (an approach done in the RSA paper).
        

TDA

[Bei Meeting Aug 16th](Ground%20Truth%20+%20SVD%20Expms,%20TDA%20Plan%2039c103e13e3b4c248cbc77804d43216e/Bei%20Meeting%20Aug%2016th%203226dd6a27934f619ef1637066e40b8f.md)

- 🐣 read TDA papers
    - Experimental Observations of the Topology of Convolutional Neural Network Activations
    - Comparing Mapper Graphs of Artificial Neuron Activations
        
        [https://chatgpt.com/c/916f3030-d1fb-4d8e-b3a2-b34f184fc1ff](https://chatgpt.com/c/916f3030-d1fb-4d8e-b3a2-b34f184fc1ff)
        
        - The lower the work or cost, the more similar the two graphs are considered to be.
    - [Branching and Circular Features in High Dimensional Data](https://www.sci.utah.edu/~beiwang/publications/Branching_BeiWang_2011.pdf)