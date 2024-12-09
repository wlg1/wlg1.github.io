# Semantic subspace matching

More actvs for corr- prevent OOM

- ✅ plan corr fn: batch proc on actvs to prevent OOM
    - [https://chatgpt.com/c/2e12ec21-211e-4b41-af19-4ce04ab20922](https://chatgpt.com/c/2e12ec21-211e-4b41-af19-4ce04ab20922)
    - [https://chatgpt.com/c/c14743c7-5591-4ad0-a7a0-3223c5237e3a](https://chatgpt.com/c/c14743c7-5591-4ad0-a7a0-3223c5237e3a)
- ✅ [corr_large_data_v0.ipynb](../../Project%20Planning%20b4b05f73d85e409f8409b209e44ed692.md)
    
    [https://chatgpt.com/c/bfd75113-bcbe-4c7c-b99e-dfb987ad1b3a](https://chatgpt.com/c/bfd75113-bcbe-4c7c-b99e-dfb987ad1b3a)
    
    - test if correlation fn is correct by reversing order of first dim rows of actvs, then seeing if correlation fn corerctly pairs first and last rows together, etc
        - it doesn’t.
        - unbatched also has this issue. but this was used to successfully find actual pairs in ts?
        - check if the normalized vers equal each other
            - they DON’T!
            - [https://chatgpt.com/c/4fde2b47-eca7-4b21-9001-f0470431899b](https://chatgpt.com/c/4fde2b47-eca7-4b21-9001-f0470431899b)
    - [when computing pearson correlation coefficient, is it valid to compute just one row each of two matrices? answer yes or no and why](https://chatgpt.com/c/eb0012c3-5ec8-4727-b9e3-c2e7bde3b628)
        
        Yes, it is valid to compute the Pearson correlation coefficient for just one row each of two matrices. The reason is that the Pearson correlation measures the linear relationship between two datasets, regardless of their origin as rows, columns, or otherwise. Each row in a matrix can be considered a separate dataset. Therefore, as long as you have paired data from these rows and they are of the same length, you can calculate the Pearson correlation coefficient to determine the degree of linear correlation between these two rows.
        
    - SOLN: how come when I use this code on a matrix and the matrix where the rows are reversed order, i don't get the first and last row have highest corr:
        
        you should reverse the COLUMNS instead. the rows must be the same bc they’re the tokens, so they have to correspond to each other! nothing was wrong- it’s the col order that should’ve been changed!
        
        now obv that doesn’t matter for cosine sim, but corr coeff REQUIRES paired rows (but not cols)
        
- ✅ corr_large_data_v1.ipynb
    - normalization of (100k * 32k) elemns by chunking
        
        [https://chatgpt.com/c/084deca8-bb72-4efa-8538-19fdf17c4a56](https://chatgpt.com/c/084deca8-bb72-4efa-8538-19fdf17c4a56)
        
    - [do tensor operations and structures cost more than numpy](https://chatgpt.com/c/de0df0a7-a123-441d-979e-6a4cba6503c6)
        
        if im doing batch processing using matrix multp should i use cpu or gpu
        
    - the reason why sae actvs may map to same is bc those are zero feature neurons
        - so what if they’re just finindg similarity of the cluster of zero neurons?
        - thus, get rid of zeros! (dead neurons)
            - getting rid of duplicates sort of already does this, bc usually the “frist 0” is always mapped to
        - find how many cols of tensor are all 0
            - right now, just around 10%. so this isn’t a big deal. svcca finding 0.6 sim can’t be poss if it’s just matching those 10%
    - set() cannot be applied to tensor, only list or array
    - the reason slicing the actvs of sparse actvs doesn’t work is bc most in front are 0. correlation of two zero vectors isn’t 1, but 0.
- ✅ corr_large_data_v2.ipynb : compare actvs from 2 diff models
    - ISSUE: 1000 samples of OWT gets low corr (.015)
        - try 100 samps on same code to see if get same corr mean as last time (0.7). if not, code has issue.
            - we get 0.2 for
        - try the same corr fn code on the data
            - if diff results, maybe it’s data construction that’s wrong or another code that’s corfFn
                - it’s the same.
        - try using the same data construction
            - in this nb, the model is loaded using `.to('cuda' if torch.cuda.is_available() else 'cpu')` which forces us to use `inputs = {k: v.to("cuda") for k, v in inputs.items()}`. so don’t load model using that so we don’t have to use that, adn see if get same answer as last nb. if so, that’s prob the culprit.
                - no, it gets it wrong, so it’s not the culprit
                - SOLN: wrong variable (using i=0 for hidden state)
            - so the data construction wasn’t done right
            - use new corr fn on old data constr
                - this gets the same results as the old nb, so corr fn isn’t the issue
                - issue must be in the accumulated data construction
        - **dont run model actvs in batches**: just use 1000 samps in input to model
            - ISSUE: even 300 samps gets out of memory
        - so write new batch model actv code
            - hypothesis: inputs in batches is wrong. we should get all the inputs using the tokenizer at once so the padding and truncation is done consistnly for all samples when thru model. instead of tokenizing input during each batch?
            - SOLN: this works using dataloader to batch proc existing input that’s tokenized all at once
        - ⚠️ ISSUE: for >400 samples, `feature_acts_model_A = sae.pre_acts(accumulated_outputs)`  -OOM, so do in batches the same way (not data loader, just slices of accumulated output)
            - ISSUE: even after doing this, still OOM at 400
    - only sim on top 50% corr and top 90%
        - [https://chatgpt.com/c/5cceac91-5cd7-41e8-b50b-cad9cfd9108e](https://chatgpt.com/c/5cceac91-5cd7-41e8-b50b-cad9cfd9108e)
        - ends up bad. seems like it’s not just highly correlated featues that form the related subspcace.
    - [modify this to add in only the 2nd seen unique pair, not the first](https://chatgpt.com/c/487c5207-0490-4ee2-a4aa-fc042f9cd45c)
        - [this also has high svcca](https://colab.research.google.com/drive/1lP2nXMIcSdGq8vOtp00rto5RLKJyc8DH#scrollTo=j5bPQ9igID_g&line=1&uniqifier=1)
        - but why doesn’t just getting highly corr pairings work?
        - what’s the avg corr val for these unique lists?
            - it’s a bit LESS than before!

Stat tests

- ✅ [corr_large_data_v3](https://colab.research.google.com/drive/14itmgldUpBGiUMEkUhPLBTluaQULIn1u#scrollTo=-Mrmkco3pyMi).ipynb : scipy, stat tests
    
    [https://chatgpt.com/c/b96125ea-4fcf-42ff-b484-e0ac6c294c1d](https://chatgpt.com/c/b96125ea-4fcf-42ff-b484-e0ac6c294c1d)
    
    - ✅ try “easier” non-btach alt methods to comptue pearson corr
        - [see if also gets OOM: use `stats.pearsonr`](https://colab.research.google.com/drive/14itmgldUpBGiUMEkUhPLBTluaQULIn1u#scrollTo=mI3C_dpc1T2B&line=1&uniqifier=1)
            - very slow
            - The stats.pearsonr function from the SciPy library is designed to run on the CPU and doesn't have direct GPU support.
        - `covariance = torch.mean((matrix1 - mean1) * (matrix2 - mean2))`
            - OOM
    - ✅ Try taking cosine sim of ACTIVATIONS, not of weights. Perhaps this is same as pearson corr of actvs. ***see if also gets OOM***
        - The `cosine_similarity` function from `sklearn.metrics.pairwise` does not have direct GPU support.
        - Also extremely slow
        - it may not take up 40GB GPU ram, but it DOES take up 80 GB system RAM!
    - ✅ compare est hardware runtime
        - before running is it possible to estimate how long it'd take cosine_similarity given size of matrices? say dims (300000, 32000)
            
            Estimating the time it takes to compute cosine similarity for large matrices like the dimensions you've specified (300,000 x 32,000) can be quite challenging without actual benchmarking, as the computation time depends on several factors:
            
            1. **Hardware Capabilities**: The specifics of the GPU (e.g., CUDA cores, memory bandwidth, and clock speed) or CPU will greatly influence computation times.
            2. **Memory Constraints**: Large matrices require significant memory. Ensuring that both the data and intermediate calculations fit in GPU memory is crucial. If the data does not fit, it may require partitioning the data and processing it in chunks, which can add overhead.
            3. **Implementation Details**: The library and specific function implementations (e.g., use of optimized libraries like CuBLAS or cuDNN in CuPy or PyTorch) can also affect performance.
            4. **Parallelism and Optimization**: The extent to which the operation can be parallelized and the efficiency of the parallel implementation contribute significantly to performance.
            
            ### Estimating Time Theoretically
            
            For a rough theoretical estimate, consider the key operation in cosine similarity: the dot product between normalized matrices. The number of floating-point operations (FLOPs) required can be approximated and compared against the FLOP/s (FLOPs per second) capabilities of the GPU.
            
            For two matrices \( A \) and \( B \) where \( A \) is \( m \times n \) and \( B \) is \( n \times p \):
            
            - **Normalization**: \( 2m \times n \) (for computing norms and dividing)
            - **Dot Product for Cosine Similarity**: \( m \times n \times p \)
            
            Given \( m = 300,000 \), \( n = 32,000 \), and \( p = 32,000 \):
            
            - **Normalization**: \( 2 \times 300,000 \times 32,000 = 19.2 \) billion operations
            - **Dot Product**: \( 300,000 \times 32,000 \times 32,000 = 307.2 \) trillion operations
            
            ### Practical Approach
            
            **Benchmarking** with smaller matrices and scaling up can give more practical insights. Here's how you might do it:
            
            1. **Start with Small Dimensions**: Test the computation time for smaller matrices and gradually increase the size to understand how the computation time scales.
            2. **Measure Memory Usage**: Track memory usage during the test to ensure you do not exceed GPU memory, as this would cause swapping or errors.
            3. **Use Profiling Tools**: Tools like NVIDIA's Nsight or the profiling tools available in PyTorch or TensorFlow can help identify bottlenecks and optimize computations.
            
            ### Example: Estimating with Python
            
            You might start with dimensions reduced by factors of 10 or 100 and measure how long operations take, then extrapolate to the full size assuming a linear or quadratic scale-up based on the operation complexity:
            
            ```python
            import numpy as np
            import cupy as cp
            import time
            
            # Smaller scale test
            m, n, p = 3000, 320, 320  # Reduced dimensions
            A = cp.random.rand(m, n).astype(cp.float32)
            B = cp.random.rand(n, p).astype(cp.float32)
            
            # Normalize A and B
            A_normalized = A / cp.linalg.norm(A, axis=1, keepdims=True)
            B_normalized = B / cp.linalg.norm(B, axis=1, keepdims=True)
            
            # Measure time for cosine similarity
            start_time = cp.cuda.Event()
            end_time = cp.cuda.Event()
            
            start_time.record()
            similarity = cp.dot(A_normalized, B_normalized)
            end_time.record()
            end_time.synchronize()
            time_taken = cp.cuda.get_elapsed_time(start_time, end_time)  # time in milliseconds
            
            print(f"Time taken for smaller matrix multiplication: {time_taken} ms")
            
            ```
            
            **Scale-Up Calculation**: If the smaller matrix takes \( X \) milliseconds, use your scaling factor squared (since matrix multiplication scales approximately quadratically with the number of elements) to estimate the larger matrix's time. However, remember that this is a rough estimation and actual performance might differ significantly based on the factors listed above.
            
        - can you give an estimate of cpu vs gpu run time for that?
            
            Estimating the runtime difference between CPU and GPU for large-scale computations such as cosine similarity with matrices of dimensions \(300,000 \times 32,000\) is challenging without specific benchmarks, but I can provide a general approach and hypothetical scenario based on common hardware capabilities.
            
            ### Factors Influencing Performance:
            
            - **Hardware Specifications**: The speed and number of cores in the CPU vs. the GPU, along with their respective architectures.
            - **Memory Bandwidth**: GPUs generally have higher memory bandwidth compared to CPUs, which is crucial for data-intensive tasks.
            - **Parallelism**: GPUs excel in tasks that can be heavily parallelized, like matrix operations, due to their thousands of cores compared to the relatively few cores of a CPU.
            
            ### Hypothetical Scenario:
            
            Assuming you have a modern but general-purpose setup, like an Intel i7 CPU with 6-8 cores and a mid-range NVIDIA GPU like the RTX 3060.
            
            ### Computation Details:
            
            - **Normalization**: Involves calculating norms and then dividing each element by the norm, which is both memory and compute-intensive.
            - **Dot Product**: Matrix multiplication, which is highly parallelizable and typically where GPUs excel.
            
            ### Estimating GPU Performance:
            
            Given the massive scale of operations (\(307.2\) trillion operations for the dot product alone), a modern GPU like the NVIDIA RTX 3060, which has a theoretical throughput of around 13 teraFLOPS in FP32 (32-bit floating-point operations per second), could potentially handle this:
            
            - **Total Operations**: \(307.2\) trillion for the dot product.
            - **Throughput**: \(13,000\) gigaFLOPS (or \(13\) teraFLOPS).
            - **Time Estimate**: \( \frac{307,200}{13,000} \approx 23.63 \) seconds just for the dot product under ideal conditions.
            
            ### Estimating CPU Performance:
            
            A high-end CPU like the Intel i7, with a peak performance around \(0.5\) teraFLOPS under optimal conditions, would be significantly slower:
            
            - **Throughput**: \(500\) gigaFLOPS.
            - **Time Estimate**: \( \frac{307,200}{500} \approx 614.4 \) seconds, or approximately \(10.24\) minutes, just for the dot product.
            
            ### Normalization and Additional Considerations:
            
            - **Normalization** might add significantly to this time due to the need to access each element multiple times (calculating norms and then normalizing), which isn't as efficiently parallelizable as matrix multiplication.
            - **Memory Transfer Overhead**: In GPU calculations, time must also be allotted for transferring data between host (CPU) and device (GPU), though this is generally minor compared to the actual computation time for large matrices.
            
            ### Practical Advice:
            
            Given the vast difference in theoretical computational capabilities between CPUs and GPUs for this task, the GPU could be expected to perform the operation potentially an order of magnitude faster than the CPU. However, these are ideal estimates and actual performance can vary based on implementation details, system architecture, and other runtime conditions.
            
            ### Conclusion:
            
            For the task at hand, using a GPU would be highly recommended due to the substantial reduction in computation time. However, testing with actual hardware and specific implementation details is crucial to get a precise estimate. Benchmarks using smaller matrices, as previously suggested, would be a practical approach to gauge performance before scaling up to the full matrix size.
            
    
    [see image. for the part of creating a distribution and getting pvalue, how do i do this in python?](https://chatgpt.com/c/8e6b40a1-86f6-4ea4-bc23-0651e877dc21)
    
    - ✅ rsa-paper pval statistical tests on 1-1 and non 1-1
        - A p-value close to zero (or approximated as zero) suggests that the observed correlation is highly unlikely under the null hypothesis of no association (i.e., it's statistically significant).
        - what does 0.03 pvalue for 100 samples mean
            
            A p-value of 0.03 in the context of statistical testing indicates that there is a 3% chance of observing the actual statistic or a more extreme value under the null hypothesis, assuming the null hypothesis is true. Here's what this means when dealing with 100 samples:
            
            1. **Interpretation of the p-value**:
                - **Statistical Significance**: Generally, a p-value of 0.03 is considered statistically significant if the threshold (alpha level) for significance is set at 0.05. This means that there is sufficient evidence to reject the null hypothesis at the 5% significance level.
                - **Probability Statement**: The p-value of 0.03 states that, assuming the null hypothesis is true (e.g., there is no effect or no difference between groups), there's only a 3% probability that the observed data or something more extreme could occur purely by chance.
            2. **Context of 100 Samples**:
                - **Sample Size Influence**: The reliability and stability of p-values can be influenced by the sample size. With 100 samples, the p-value is derived from a decently sized sample, which can provide moderate confidence in the robustness of the test results. However, the exact implications can vary depending on the variability in the data and the specific statistical test used.
                - **Power of the Test**: Larger sample sizes generally increase the statistical power of a test, which is the probability of correctly rejecting the null hypothesis when it is false. With 100 samples, depending on the effect size and variability of the data, you might have sufficient power to detect meaningful effects.
            3. **What it Doesn’t Mean**:
                - **Not a Probability of Truth**: A p-value of 0.03 does not mean there is a 3% probability that the null hypothesis is true or a 97% probability that your alternative hypothesis is true. It strictly relates to the data under the assumption that the null hypothesis is correct.
                - **Not an Effect Size Indicator**: The p-value doesn't indicate the magnitude of any effect or difference. It only informs about the likelihood of seeing the observed effect if the null hypothesis were true. To understand the magnitude or importance of the effect, you'd need to look at other statistics such as effect size measures.
            
            In practice, when analyzing results from a sample of 100, alongside the p-value, it's crucial to consider confidence intervals, effect sizes, and the potential for Type I (false positive) and Type II (false negative) errors. These elements provide a more comprehensive understanding of your statistical findings and their implications.
            
        - for 1-1, get pval by both rand sel features from all + shuffling subset of 1-1 features
    - ✅ main analysis takeaways
        - 1-1 gets highest stat sigf
        - 1-1 then take top 90% also works
        - 1-1 then take top 40% also works
        - top 90% works, but top90% then 1-1 doesn’t
        - top 40% works, but top40% then 1-1 doesn’t
        - MYSTERIES: Why does 1-1 only work with all?
            - only two don’t work; why does 1-1 not work after taking top X%?
    - ✅ [histogram of corr_ind counts (no, too many; get most freq)](https://colab.research.google.com/drive/14itmgldUpBGiUMEkUhPLBTluaQULIn1u#scrollTo=-Mrmkco3pyMi&line=1&uniqifier=1)
        - the features in `inds` are from model A, pythia 70m, so interpret them on neuronpedia
        - but 70m is not on neuronpedia; only 70m deduped is
        - why feature2604 has so many that match to it?
    - ✅ [1-1 for rand list](https://colab.research.google.com/drive/14itmgldUpBGiUMEkUhPLBTluaQULIn1u#scrollTo=wajP7lKcotnQ&line=1&uniqifier=1)

Collaborator Meetings and writeup

[Kiho meeting notes- sept 4](Semantic%20subspace%20matching%2011eafed922dc80b5ac94dbb7e4b73137/Kiho%20meeting%20notes-%20sept%204%207b78a9ef86e644a48ef1cd78ab3b3c95.md)

[Austin meeting notes](Semantic%20subspace%20matching%2011eafed922dc80b5ac94dbb7e4b73137/Austin%20meeting%20notes%206669c1f41e9448fd9007b07a91d2450e.md)

- ✅ overleaf abstract and cleanup

Figure out why 1-1 gets good results, but many-to-1 default doesn’t

- ✅ simSAE_pythias_70m_160m_all_layers_not1to1.ipynb
    - L1 seems to more similar to early and late than the middle by these results, which is inverse 1-1?
    - MLP0 has no matches, not even with MLP0. Note that the % unique is almost 0- so everything is mapping to one thing. So when comparing any layer to 160m’s MLP0, when it’s not 1-1, you get nonsense.
    - all results seem inconsistent with the layer-to-layer pairings.
- ✅ simSAE_pythias_70m_160m_filter
    - ✅ the reason we want to elim bad matches is bc just bc features match to something, doesn’t mean it actually matches. it may match not bc of similarity, but bc both are not good actvs
        - also, there may be better matches. perhaps also use fn sim or semantic sim, not just mean actv corr
    - ✅ try first for MLP 2 vs MLP 2
    
    filter bad matches by:
    
    - ✅ case A: too many matches (still allow 1-to-many, but if that one from A has too many matches, say over 100, we should only keep one)
        - if we keep only the features with counts under 100, and add in features with counts over 100 just once, then we get a svcca over `0.336`, as opposed to random avg of 10 of `0.0038` for the same length
            - thus, we can say the culprit are those HUGE matches over 100
        - After filtering, there are `25351` features that are kept (so 32768 - 25351 = **7417 from SAE B** are removed; this matches 7434 that is the sum total count of feature Bs mapped to feature As that are mapped to over 100 times, and 17 over those are kept.)
        - there are only 17 features over 100
        - these features don’t have low corr; the top has corr 0.91
    - ✅ loop case A for MLP2 vs
        - now MLP 2 vs MLP 0 has some correlataion! mean actv is higher! but svcca for mlp0 is lower than for mlp1 and mlp2
        - get mean corr of filtered) pairings only
            - bc if many-to-1, it may be higher corr just bc of certain ‘low info’ high corrs
            - Does plot overlap with sim metrics plot? They correlate?
        - look at corr scores for features with many matches
    - loop case A for MLP5 vs
        - for filtering over 100, the svcca is very low and we don’t see patterns that more similar to later layers. L5 is more similar to both middle and later layers but not L10
            - however, mean actv corr (before filtering) DOES show that pattern where later layers are more simialr to later layers
        - is filtering over 100 is too strong? analyze the histo, len, etc when filtering over 100 for L5 v L11
            - now that top number of counts has a corr of ZERO! same for the third!
            - after filtering to keep only those under 100, the corr is very low- avg is 0.4, and histo shows skew where many are 0.1 or 0.2
            - try filtering to keep all under 1000
                - this score is even lower
            - filter under 500 gets scores of 0.069
            - filter to keep only under 10 gets score of 0.17
            - I think the MORE you filter, the better the score gets. this is why 1-1 is the extreme “best”
                - 1-1 gets score of 0.32
                    - but its mean actv corr is just 0.32! as opposed to the original’s 0.6
                    - however, for L2, mean corr for 1-1 is still 0.66
    - Note that even for MLP2 vs MLP2, we have: Count of elements appearing 0 times: 25123
        - so we’re just matching a subset of B to a subset of A
        - for L2 v L2, take the filtered subst and further filter out all those with less than 0.1 corr
            - to check if it’s corr, by the histogram of vals there should be almost none that are less than 0.1. indeed, we get the same score, so this does nothing
    
    - what if later layers of 70m and 160m are more similar because the filtering is extreme in similar ways in both those cases (for later layers), not bc they’re actually similar?
    
    - case B: disregarding zero matches
        - for 70m’s MLP5, only 139 ACTVS are totally 0, and only 427 in 160m’s MLP11, so negligible
            - note that pearson’s corr doesn’t assign corr of 1 to zero vectors
            - [is the pearson corr between two vectors of all zeros 0 or 1](https://chatgpt.com/c/b6e67285-3ea1-4fd8-82c1-ac9ef90ad7b3) - undefined
    - case C: extremely low cosine sim (less than 0.2)- keep even those above 0.3, bc those are “good”; if we elim them, we elim impt correlations
        - get count or histo bins of how many are in each 0.1 interval to see how many you’re elim
        - this is also negligible for MLP 2 bc most of the counts are above 0.2
    - MLP0 vs
        - why are ALL the columns of actvs 0? were the actvs gotten correctly?
- ✅ ask chatgpt about 1-1 feature pairings
    
    https://chatgpt.com/share/bed9a411-5835-4062-91af-22534327d192
    
    - When I do pairing by max activation correlation, only 20 to 50% are unique pairings. Some features in sae model A have 1000 mappigns to them. I experimented with taking svcca scores of subsets that only have 100 or less mappings, have 10 or less, and are 1 to 1. It seems like the sim score goes up the more 1 to 1 the features are. Do you have any ideas on why?
        - The subspaces aren't more highly correlated in terms of mean activations correlation tho, some are even less, does your reasoning still hold
    - do svcca, mutual nearest neighbors, procrustes, and rsa require 1-1 pairings
        - only procrustes does, but usually require close to 1-1

[Ask Austin on 1-1 features](Semantic%20subspace%20matching%2011eafed922dc80b5ac94dbb7e4b73137/Ask%20Austin%20on%201-1%20features%20f6fe76bd99cc4ff6ab904fa39ced04ff.md)

- ✅ ask max about 1-1
    - reply
        
        I guess it shows that the mappings are quite robust. If you have features mapped 1-to-1, I would expect that they are similar for most inputs. And the features that do not get matched well have more variance? (Getting slightly confused again with features=weights of SAE decoder or features=activations of SAE)
        I think svcca could assign perfect similarity also to features that do not match well, but it would require an invertible linear transformation between the features in the one SAE and the other. Since there does not seem to be such a general match, similarity is lower. Perhaps there are linear transformations between subsets of features.
        All in all, think it shows you that some features really are different according to the standards set by svcca (and other measures should assign even less similarity).
        
    - what does this mean: (state more clear and intuitive- is it saying 1-1 is good?)
        
        Let’s break this down clearly and intuitively:
        
        1. **1-to-1 pairings and similarity**: The text is suggesting that **1-to-1 mappings between features indicate a good match** between models (or layers). If a feature in one model is paired directly with a feature in another, it implies that these features behave similarly for most inputs. This is the desired situation because it means that the models are capturing the same types of information.
        2. **Variability in non-1-to-1 matches**: Features that don’t match well (i.e., where many features in one model map to one in the other) likely have **more variance** or noise. This means they aren't as robust or consistent, leading to weaker alignment.
        3. **Confusion between features and weights**: The writer seems to be clarifying a point of confusion: **"features" here refer to the activations** of the model (outputs of the neurons, not the model’s weights). These are what you’re comparing in similarity measures like SVCCA. Features represent patterns or information captured by the model during tasks, rather than the fixed parameters (weights) of the decoder.
        4. **SVCCA and linear transformations**: SVCCA can sometimes assign high similarity even to features that aren’t perfectly matched. This can happen if there’s an **invertible linear transformation** between the two sets of features (i.e., you can map one set of features to the other by applying a transformation). But, since there doesn’t seem to be a perfect linear transformation between the full feature sets of your models, the similarity scores are lower overall.
        5. **Subset transformations**: The writer speculates that there may be linear transformations that work **only for subsets** of the features, meaning that only some parts of the models’ feature spaces are aligned well.
        6. **SVCCA's role**: Overall, the conclusion is that **SVCCA highlights differences between features**. If SVCCA is showing low similarity, it means that certain features are indeed different, and **other similarity measures** would likely show even less similarity, suggesting that those features are capturing distinct patterns or behaviors between the models.
        
        ### In summary:
        
        - 1-to-1 mappings show robust, consistent feature alignment between models.
        - Features with more variance or noise lead to weaker matches.
        - The comparison is between **activations** (features), not the model’s weights.
        - SVCCA could show high similarity even if features are not perfectly aligned, but only if an invertible transformation exists between them, which doesn't seem to be the case here.
        - Some features or subsets align well, while others are quite different.
        
        So yes, **1-to-1 mappings generally indicate a stronger match** and better feature alignment.
        
    - so it's saying that for a feature pair, they would behave similarly for most inputs
        
        Yes, exactly! The text is saying that **if two features are mapped 1-to-1** between models (i.e., they are paired together), they would likely **behave similarly for most inputs**. In other words, these paired features are expected to respond in comparable ways when given the same input, capturing the same patterns or information.
        
        On the other hand, if features aren't matched well (e.g., when many features map to one or there’s no clear correspondence), the behavior across inputs is likely less consistent, and those features would exhibit more variance or noise.
        
- ✅ compare filtered to 1-1: what is different for 1-1?
    - both don’t have low corrs, or matches between 0 vectors, so rule that out
    - the main diff is that even after filtered gets rid of matches of over 100, it still has matches of say 50.
        - try getting rid of matches over 10
- ✅ collapse a ball into a point, lose a lot of info
    - ball has more info, so saying ball is similar to point will lose a lot of info
- ✅ how many total tokens are in pythia vocab? not to mention tokens have diff actvs when in sequences. so 300k not enough in total proportion; more can get more 1-1.
    - [All Pythia models trained for 143000 steps at a batch size of 2M (**2,097,152 tokens)**](../../../ARENA%20notes%201a8ff2624cff486e9d91b13139420026/1%204%200186fae1fa2d41e49f64642d2ea523eb.md)
- ✅ simSAE_pythias_70m_160m_filter_v2.ipynb
    - the plot for kept under 100 looks much better after filtering out 0s in the mid layers; even though the corr histo for L2 vs L2 seemed to ahve no 0s, perhaps there were 0s in the others? record how many 0s there were.
    - loop after filter for under 10 kept
        - get mean corr of 1-1 pairings only
            - bc if many-to-1, it may be higher corr just bc of certain ‘low info’ high corrs
            - Does plot overlap with sim metrics plot? They correlate?
                - no, but that’s why we use svcca
        - result: these plots look more like 1-1
    - [interpret the features which have many matches](https://colab.research.google.com/drive/1XEzOWwb21za_N9vnKSIJ-e_XjHAroqPw#scrollTo=-GZeNDetHtCY&line=1&uniqifier=1)
        - get own explanations for pythia 70m using OWT
        - for L2 vs L2, the top 15 seem to be all about periods and new lines (\n).
        - ask: the periods might be capturing DIFFERENT information, bc they store next token info, and so the matches on periods might not be semantically meaningful?

Writing

- ✅ make copy of existing and get rid of topological (put in “future work” or use one line of it in “appendix”, but not title)
- ✅ [https://github.com/ICLR/Master-Template](https://github.com/ICLR/Master-Template)
    - get rid of `\usepackage[final]{template}` in main.tex and add `\usepackage{iclr2025_conference,times}` after uploading the .sty and .bst
- ✅ bar plots: Pythia L2 vs L2 in main text
- ✅ [local vs global sim](https://chatgpt.com/c/66dcc746-81b8-800c-ba12-163c936757c1)
- ✅ writeup: collapse a ball into a point, lose a lot of info

Sim metrics

- ✅ simSAE_pythias_70m_160m_BtoA.ipynb
    
    try matching from (one) features from B (so it’s a value in a list) to (many) features in A (ind)
    
    - ✅ `batched_correlation(reshaped_activations_B, reshaped_activations_A)`
    - check this
        
        % This is affected by which model is allowed to have "many features" map to only one. When the model that can have "many" is smaller (eg. Pythia-70m), there are many mappings with 0 correlation. When the model that can have "many" is bigger, (eg. Pythia-160m), there are many mappings with high correlation but semantically map to a period. We use the bigger model as the one with "many features" allowed to map to one.
        
        no; this only holds for mlp2 vs
        
    - Having too many actvs with 0 corr is bad. The feature actv matrix for MLP2 of modA 70m has 5516 actvs with 0 corr. Thus, even many-to-1 when using manyBtoA will remove all those mods with 0 corr as they aren’t being mapped to.
    - For MLP2 (mod B 160m) vs MLP 2 (modA 70m), there are MUCH more 0 corr. In fact, 5516 features from modA (70m) map to feature 0 of modB. This brings avg corr down to 0.58.
        - rmv all 0s bring it up to 0.688 with 27k features
        - but not having it be 1-1 still only has sim score of 0.04
        - if we restrict it to 1-1, we thankfully get svcca of 0.3 again!
- ✅ simSAE_pythias_70m_160m_moreMetrics.ipynb
- ✅ [would cca and svcca return simialr results](https://chatgpt.com/c/66df3203-1d54-800c-a8ec-f70fb392c7e3)
    
    CCA (Canonical Correlation Analysis) and SVCCA (Singular Vector Canonical Correlation Analysis) are related but not identical, so they may return similar but not identical results, depending on the data and context.
    
    Here’s a breakdown:
    
    1. **CCA**: It finds linear projections of two sets of variables that are maximally correlated. It works directly on the original data to compute the canonical correlations between the two sets, without dimensionality reduction. It provides the most direct measure of correlation between two datasets.
    2. **SVCCA**: It first reduces the dimensionality of each dataset using Singular Value Decomposition (SVD) before applying CCA. By retaining only the top singular vectors, SVCCA focuses on the most important features or directions in each dataset before measuring correlation. This can make SVCCA more robust to noise or irrelevant components in the data compared to traditional CCA.
    
    ### Key Differences:
    
    - **Dimensionality reduction**: SVCCA adds a step of dimensionality reduction before applying CCA, while CCA works on the full dataset.
    - **Noise sensitivity**: SVCCA can be more robust to noise or redundant features by focusing on the dominant singular vectors.
    - **Performance**: SVCCA may produce slightly different similarity scores than CCA, particularly in high-dimensional or noisy datasets, where the dimensionality reduction step helps capture meaningful correlations.
    
    ### Similarity of Results:
    
    - **When the data has clear structure and low noise**, CCA and SVCCA may return similar results because both methods are effectively capturing the same underlying relationships.
    - **In noisier or higher-dimensional settings**, SVCCA might give better, more stable results by ignoring noise or irrelevant dimensions, leading to potentially different results compared to plain CCA.
    
    In your experiments with similarity scores and feature pairings, SVCCA might show improved results by better aligning with the more meaningful correlations between layers, especially if you’re dealing with complex models like 'sae model A'.
    
- ✅ if you have a tensor W, does a fn that takes in W make a copy of it? if so, would that take up more memory? since W is global and not defined in fn, would it be better to not pass it in as an arg but just call it?
    
    In programming languages that support tensors, such as Python with PyTorch or TensorFlow, the behavior of whether a function takes a copy of a tensor or not depends on how tensors are passed to functions and manipulated within them.
    
    Here's how it works generally:
    
    1. **Pass-by-Object-Reference**: In languages like Python, objects (like tensors) are passed to functions by reference. This means when you pass a tensor `W` to a function `fn`, it does not automatically create a copy of `W`. Instead, `fn` receives a reference to the same tensor object `W` is referring to. This is memory efficient as no new tensor data is created.
    2. **Memory Considerations**: No extra memory for the tensor data itself is consumed when passing the tensor as an argument to a function. However, if you modify the tensor inside the function in a way that requires a new tensor to be created (like using operations that are not in-place), that will consume additional memory.
    3. **In-place vs Non-in-place Operations**: If the function modifies the tensor using in-place operations (like `W.add_(1)` in PyTorch, which adds 1 to each element of `W` directly), the original tensor `W` is modified, and no additional memory is used. Non-in-place operations (like `W = W + 1`), on the other hand, create a new tensor, thus consuming more memory.
    4. **Global vs Local Access**:
        - **Passing as Argument**: Even though passing the tensor as an argument does not consume more memory by default, it does make the function's dependencies explicit, which is generally a good coding practice. It makes your code more readable and reusable, as the function’s operation is clearly dependent on the provided tensor.
        - **Accessing Global Tensor**: If the tensor `W` is a global variable, you could access it directly within `fn` without passing it as an argument. While this might seem convenient, it usually makes the function less flexible and harder to understand or debug because the function's behavior now implicitly depends on the external state.
    
    **Best Practice**: Typically, it is better to pass tensors as arguments to functions unless there is a compelling reason to use them as global variables. This approach enhances the modularity and clarity of your code. If you're concerned about memory usage, focus on whether your function performs in-place or non-in-place operations.
    
- ✅ simSAE_pythias_70m_160m_moreMetrics_v2.ipynb: clean up fns
    - use sae lib loader fn
    - use batch fns

Semantic Subspace Matching

- ⚠️ match_semantic_spaces_v1.ipynb
    
    first identify semantic spaces, then compare these spaces using metrics
    
    - ✅ APPR1: match by most corr pair
        - ✅ check if featuers from both semantically match
        - issues
            1. matching by keywords isn’t enough
            2. not enough match already (only 22 out of 30k match for she, and this is for only one match)
            3. this is arleady simialr to matching by entire spaces, it jsut takes subset.
            4. doesn’t work for “he” and possibly others?
    - ✅ APPR2: match by separately finding semantics from each then trying
        - ✅ steps to code
            - get feature subset space for each by searching dataset examples
                - autolabel with gpt4?
            - run corrs on each subset to get pairs
            - run metrics on paired subset
            - compare to rand sel same num features from each and run corrs + sim
        - Even without pairing, bc every feature corresponds to the same keyword (at least in one dataset samp of top 5), it should have high sim
            - no, that’s wrong
        - actually, using 20 samples is too low, bc the svcca is very high for them- it’s 0.2 for any random subset. so we shouldn’t match a subspace of too few samples
            - [why is svcca score so high when they are only 20 samples](https://chatgpt.com/c/66e0a26e-d7a4-800c-8d4c-9bc3d55c56d7)
                
                The Singular Vector Canonical Correlation Analysis (SVCCA) score being high despite having only 20 samples could be due to a few reasons:
                
                1. **Highly Correlated Features**: If the features in your model are highly correlated, SVCCA will likely capture this strong relationship, resulting in a high score. This can occur even with a relatively small sample size if the underlying data patterns are very consistent or redundant.
                2. **Low Dimensionality**: With fewer samples, the dimensionality of the data might be low relative to the number of features, which can artificially inflate correlation metrics like SVCCA. This is because with fewer points, it's easier to find patterns or alignments that might not be as robust in larger datasets.
                3. **Overfitting**: With a small sample size, there's a risk that the analysis might overfit to these specific samples. In such cases, the SVCCA score could reflect relationships that are more about the peculiarities of the specific dataset rather than generalizable features of the data.
                4. **Noise Sensitivity**: SVCCA, like other correlation-based metrics, can sometimes be sensitive to noise, especially when the sample size is small. Small variations in the data can lead to disproportionately high correlations if these variations align by chance across your datasets.
                
                To get a more reliable measure, you might consider increasing the sample size or applying regularization techniques to see if the high correlation persists. It's also useful to validate findings with other metrics or through cross-validation if possible.
                
        - ✅ so this doesn’t work. the mean actv corr is also low
        - [are the features they find the same as featuers found in approach 1?](https://colab.research.google.com/drive/1M25dhzSWiAepBZc1Whd-E-xVZ69ZauOA#scrollTo=ul3ONARBLI-n&line=1&uniqifier=1)
            - interpret both, compare the corrs
            - ISSUE: neither search (on B nor A) brings in “clean” she. We get “sheen”, or just one match of “she”, etc.
                - but if you corr them, you’re going to get high corr already. whereas in approach 2, you don’t guarantee this, then you’re trying to corr two subspaces that don’t match (since they may fire on “sheen”, etc)
                - also, the highest corr’s top 10 don’t necc match on “she”, they seem to activate on “he” and “that”
                - perhaps bc “she” rarely appears as a monosemantic?
    - APPR 2b: so clean up the search fn

Figure out why 1-1 gets good results, but many-to-1 default doesn’t

- ✅ force 1-1 mappings for all features
    
    simSAE_pythias_70m_160m_force1to1
    
    - [modify this to not allow many-to-1 indices matching by this procedure: after one is taken for the most high corr among all, the second should pair for the others, etc](https://chatgpt.com/c/66e182fb-1f48-800c-9add-a9f0bf5ff53f)
        - `dim=0`: The reduction operation is performed across the rows, but for each column individually. This collapses the rows, effectively "looking down" each column to find the maximum values and their indices. Thus, you get the maximum value from each column.
        - the masking soln doesn’t always get 1-1 bc it still allows each indiv row of the BATCH to select the SAME ONE; it’s only doesn’t select ones sel from previous batches.
        - IT’S ALSO REALLY BAD BC IT’S “FIRST COME FIRST SERVE”. It doesn’t assign the max to the “best” one- it assigns it to whichever feature in a batch has its max first.
    - bad mask approach 1
        - when we do this, we get a low mean val (0.15), but even before fitlering, we get a decently high svcca score (0.28)
        - the low mean val means that not everything can be mapped 1-1; some should be mapped many-to-1 bc there really isn’t a “next best analogue” for them.
        - strangely, rmving the lowest 0.2 increases svcca to 0.4, but remving lowest 0.5 decreases svcca to 0.03. starts to decrease between 0.4 to 0.5 threshold.
    - hungarian algo on full
        - takes a long time
    - greedy Approximate Matching
        - this is wrong
    - only match many-to-1 afterwards
        - first match normally, allowing many-to-1
        - from those that are many-to-1, consider the unmatched features so far.
        - redo correlation by matching the subset of many-to-1 to unmatched features using hungarian algo or finding max VALUE in matrix (not from row or col) and starting there, taking that row and col off as cands, and continuing.
        - note that we should preserve the ORIGINAL feature ID so that it matches with the weight matrix. Either we have a dict matching the rowIDs new matrix subset back to orig, or we mask the orig matrix values of the 1-1 features
        - actually, we don’t need to redo finding a corr matrix. we use the one we had before, and for the non-1to1 featuers, we re-match them using available cands (next highest after masking). we do this in a loop; not one feature at a tmie (that’s too arbitrary) but from the max value in the matrix. if a feature’s corr is less than 0.2, don’t match it; just remove it.
        - [does this make every single combo that value, or just the pairs with same index in each list: `cloned_corr_matrix[filt_corr_ind_A, filt_corr_ind_B] = -np.inf`](https://chatgpt.com/c/66e38166-ae48-800c-af44-ce565bce7fdb)
        - Below will only keep those 1-1, and all other features in model A that are mapped will not be kept. For L2 v L2, there are ~7000 total features in model A that were mapped to. But if we strictly keep only the 1-1 features, we only get 2000 model A features.
        - It does not make sense to try to make EVERY feature in model A to those in model B; only those with good correlation. It also doesn’t make sense to map EVERY feature in B, but let’s first try doing that to see what happens, and then filter them out (once the max val dips below 0.2, stop).
        - why are there so many elements with corr of 0.999, yet they aren’t picked by the standard procedure?
            - SOLN: your 1-1 procedure is not unique. the elements it ends up with, when you take set, reveals their length to be less than total. `len(list(set(indo_A)))`
                - This is because you’re using: `cloned_corr_matrix[r, c] = -np.inf`, which only changes ONE SPECIFIC ELEMENT instead of that entire row or col!
        - [does having more -inf in a matrix speed up torch.max()](https://chatgpt.com/c/66e3b4b9-4f48-800c-886b-7a206411fbf0)
            
            The presence of `-inf` (negative infinity) values in a matrix generally does not speed up the `torch.max()` operation in PyTorch. The computation time for `torch.max()` is primarily influenced by the size of the tensor (i.e., the number of elements it contains) and not the specific values those elements hold, including `-inf`.
            
            Here’s a breakdown of why `-inf` values wouldn’t affect the speed:
            
            1. **Constant Time Complexity for Max Operation**: The max operation typically scans each element in the tensor to determine the maximum value. This process involves checking each element once, regardless of its value, hence the complexity is \(O(n)\), where \(n\) is the number of elements.
            2. **Value Irrelevance for Performance**: The computational effort to compare numbers (including `inf`) in a max operation is typically uniform. Modern CPUs and GPUs are designed to handle floating-point comparisons efficiently, and the presence of special values like `inf` doesn’t inherently speed up these operations.
            3. **Potential Overhead**: In cases where you might have special handling or checking for `inf` values (for example, to prevent them from being the maximum unless all values are `inf`), this could theoretically add overhead rather than reducing it.
            
            If you have a large matrix and performance is a concern, here are a few tips to potentially speed up operations like `torch.max()`:
            
            - **Batch Operations**: If applicable, process data in batches to fully utilize parallel processing capabilities of GPUs.
            - **Data Type Optimization**: Use the appropriate data types; for example, if high precision isn't necessary, using `float32` instead of `float64` can reduce memory usage and potentially increase speed.
            - **Avoid Unnecessary Operations**: Pre-process the tensor to remove or handle `inf` values if they are not desired in the result.
            
            If you want to test performance implications with different matrix configurations, you could measure execution time using PyTorch’s profiling tools or simple timing methods to see how the presence of `-inf` affects the computation in practice.
            
        - instead of just masking with -inf, we should just get rid of those rows. how to do this well?
            
            To efficiently remove rows containing `-inf` values from a matrix in PyTorch, you can use a combination of Boolean indexing and the `torch.isinf()` function. Here's a step-by-step approach:
            
            1. **Identify Rows with `inf`**: Use `torch.isinf()` to create a mask that identifies where `inf` values are present. Combine this with `torch.any()` to determine which rows contain at least one `inf`.
            2. **Filter Out These Rows**: Use the mask to select only the rows that do not contain any `inf` values.
            
            Here’s an example code to demonstrate how to remove rows containing `-inf` from a 2D tensor in PyTorch:
            
            ```python
            import torch
            
            # Example tensor with -inf values
            tensor = torch.tensor([[1.0, -float('inf'), 3.0],
                                   [4.0, 5.0, 6.0],
                                   [7.0, -float('inf'), 9.0],
                                   [10.0, 11.0, 12.0]])
            
            # Create a mask that is True for rows that contain -inf
            contains_inf = torch.isinf(tensor).any(dim=1)
            
            # Filter out rows that contain -inf
            filtered_tensor = tensor[~contains_inf]
            
            print("Original Tensor:\\n", tensor)
            print("Filtered Tensor (no rows with -inf):\\n", filtered_tensor)
            
            ```
            
            In this code:
            
            - `torch.isinf(tensor)` creates a Boolean tensor that is `True` wherever there is an `inf` value in the original tensor.
            - `.any(dim=1)` reduces the dimension across columns (dim=1), returning `True` for any row that contains at least one `True` value, indicating the presence of `inf`.
            - `~contains_inf` creates a negated mask, where `True` indicates rows that do not contain `inf`.
            - `tensor[~contains_inf]` uses this negated mask to select rows without `inf`.
            
            This method ensures that all rows containing any `-inf` values are removed, and it utilizes PyTorch's efficient tensor operations, making it suitable for large datasets and compatible with GPU acceleration.
            
        - **after making more 1-1:** just using the first 1-1 1000 elements after masking the 2000 1-1, gets mean actv corr of 0.998 and svcca of 0.3, which is much higher than random. combining this with the 2000 filt gets a score of 0.5, which is slightly lower than just using the 2000 filt, but not too different.
    - sorting (o1 answer): [https://chatgpt.com/c/66e41dcc-67d0-800c-9135-9aa683f627d2](https://chatgpt.com/c/66e41dcc-67d0-800c-9135-9aa683f627d2)
        - [still too slow](https://colab.research.google.com/drive/1QsR7m9DAOxeZiu9wNuGt9jz1bSccIh9N#scrollTo=E3pRY8OyPgds&line=14&uniqifier=1) ; takes 6m
        - pytorch sort is OOM
        - after sorting, assigning new 1-1 is around 15m
            - it’s faster if we don’t use item(), just store as tensor element
        - at 22666 1-1 elements, the svcca is 0.344. This is good bc we’re still getting high svcca even with a lot of elements that’s close to total. However, mean actv corr is only 0.48.
            - however, the mean actv corrs is extremely low at this point, and when we get to 23270, svcca is 0.340, so it gets lower the more “noise” we add
        - at all above corr 0.1, we get svcca 20706
    - 🐣 instead of needing the best to be 1-1, just care about getting 1-1 more about getting the top matches. “good enough”.
- ⚠️ simSAE_pythias_70m_160m_force1to1_v2: run more 1-1 on more examples and see what happens- clean up and automate
    - ✅ L5 vs L10: prob takes so much longer than before bc most inds are invalid (taken)?
        - took 3 hrs. fast at first, but starts to slow down around 15m at 5000 (corr 0.6) bc more unmatchables to wade thru
            - we can also just stop after below 0.6
        - sorted inds is too big to download, so save to drive
    - speed up 1-1 matching by cutting out all the ones which r, c that are taken out
        - do unravel_index for everything first, then take those out
        - bc sorted_inds preserved original index rather than using the curr_iter to find the r,c, the code to match ind to r,c doesn’t change
        - you also aren’t iterating in range of the sorted_inds you’re modifying; you’re modifying sorted_inds itself, so this won’t affect your loop
        - [https://chatgpt.com/c/66e4d299-777c-800c-9f10-76d6a11bcc96](https://chatgpt.com/c/66e4d299-777c-800c-9f10-76d6a11bcc96)
            - this is slower than before!

Semantic Subspace Matching

match_semantic_spaces_v1.ipynb

- ✅ `svcca(reshaped_activations_A.t(), reshaped_activations_B.t(), "nd")` on pythia
    - `svcca(reshaped_activations_A.t(), reshaped_activations_B.t(), "nd")` on pythia and it takes a long time (won’t finish in even 20m), so using it in a loop may not be feasible unless it's just done for a slice of the activations, say `svcca(reshaped_activations_A[:30000].t(), reshaped_activations_B[:30000].t(), "nd")`
    - even 30k takes over 10m (didnt finish)
    - for 1k and it gets a very low score (0.003) so forget this for now
- ✅ actually approach 1 may be good for “she” because check if a random PAIRED subset of 20 features doesn’t have much higher score than rand shuffling of those same features.
    
    this means not every subset of the correlated pairings, even if that subset has high mean actv corr, will have high svcca and rsa
    
    - ✅ keep 1-1
        - this makes it worse for “she”
    - ✅ [shuffle subset pairing of one rand PAIRED subset (diff from unpaired)](https://colab.research.google.com/drive/1M25dhzSWiAepBZc1Whd-E-xVZ69ZauOA#scrollTo=V_-EbMKfNIeH&line=1&uniqifier=1)
        - shuffling will destroy the pairing
        - but we see that it doesn’t
    - ✅ [will svcca not work well if the sample size is too low (low number of pairs)](https://chatgpt.com/c/66e6b93e-0564-800c-86ab-d8b9d18e46dc)
        - answer
            
            Yes, SVCCA (Singular Vector Canonical Correlation Analysis) may not perform well when the sample size is too low—that is, when you have a low number of data pairs. SVCCA relies on statistical estimations that require a sufficient amount of data to be reliable. Here’s why:
            
            1. **Dimensionality Reduction via SVD**: SVCCA begins by applying Singular Value Decomposition (SVD) to reduce the dimensionality of the data. When the number of samples \( n \) is small compared to the dimensionality \( d \), the SVD can become unstable or unreliable because it tries to capture the principal components of the data based on limited information.
            2. **Estimation of Covariance Matrices**: Canonical Correlation Analysis (CCA), the second step in SVCCA, involves estimating covariance matrices between the two sets of variables (representations). Accurate estimation of these matrices requires enough data to capture the underlying relationships. With too few samples, the covariance estimates can be noisy, leading to unreliable correlation results.
            3. **Overfitting Risks**: With a low sample size, there's a higher risk of overfitting to the noise in the data rather than capturing the true underlying patterns. This means that the correlations identified by SVCCA might not generalize well to new data.
            4. **Statistical Power**: A small sample size reduces the statistical power of the analysis. This means SVCCA might fail to detect meaningful correlations that do exist or might identify correlations that are actually due to random chance.
            
            **Conclusion**: For SVCCA to work effectively, it requires a reasonably large sample size to ensure that the SVD and CCA steps can accurately capture the significant features and correlations in the data. If you're working with a low number of pairs, you might need to consider alternative methods or collect more data to improve the reliability of your analysis.
            
            **References**:
            
            - **Raghu et al., 2017**: The original paper introducing SVCCA discusses the importance of sufficient data for reliable analysis.
            - **Statistical Theory**: Fundamental principles of statistics emphasize that estimations and inferences become unreliable with insufficient sample sizes.
            
            **Recommendation**: If you're constrained by a low sample size, consider using regularization techniques, dimensionality reduction methods tailored for small datasets, or bootstrap methods to assess the stability of your results.
            
            **Answer:** Yes; with too few data pairs, SVCCA may not work well because it relies on sufficient sample size to accurately estimate correlations—low sample sizes can lead to unreliable results.
            
        - for dim of 512, how many samples are enough
            
            For a dimensionality of 512, determining an exact minimum sample size for SVCCA to work effectively isn't straightforward, as it depends on various factors such as the complexity of your data, the amount of noise, and the specific patterns you aim to capture. However, there are general guidelines you can follow:
            
            1. **Samples Should Exceed Dimensions**: At a minimum, the number of samples (\( n \)) should exceed the dimensionality (\( d \)) of your data to avoid issues like singular covariance matrices. So, you would need at least 513 samples. However, just exceeding the dimensionality is often insufficient for reliable results.
            2. **Rule of Thumb—Multiple of Dimensionality**: A common recommendation is to have a sample size that is several times the dimensionality of your data. Specifically:
                - **Moderate Ratio**: \( n \geq 2d \) (for 512 dimensions, at least 1,024 samples)
                - **Better Stability**: \( n \geq 5d \) (for 512 dimensions, at least 2,560 samples)
                - **Optimal Conditions**: \( n \geq 10d \) (for 512 dimensions, at least 5,120 samples)
                
                These ratios help ensure that the statistical estimates (like covariance matrices) used in SVCCA are stable and reliable.
                
            3. **Impact of Data Complexity**:
                - **High Noise or Variability**: If your data is noisy or highly variable, you'll need more samples to capture the underlying patterns accurately.
                - **Structured Data**: If the data has underlying structures or redundancies, the effective dimensionality might be lower, potentially requiring fewer samples.
            4. **Dimensionality Reduction Preprocessing**:
                - **Prior SVD/PCA**: Applying Singular Value Decomposition (SVD) or Principal Component Analysis (PCA) before SVCCA can reduce the effective dimensionality by retaining only the top principal components that capture most of the variance.
                - **Choosing Top Components**: If you can reduce the dimensionality from 512 to a lower number (e.g., 50 or 100) without significant loss of information, the required sample size decreases accordingly.
            5. **Regularization Techniques**:
                - **Regularized CCA**: If obtaining more samples isn't feasible, regularization methods can help manage issues arising from small sample sizes, such as overfitting and unstable covariance estimates.
                - **Shrinkage Methods**: Techniques like shrinkage can improve covariance matrix estimation when sample sizes are limited.
            6. **Empirical Evaluation**:
                - **Cross-Validation**: Use cross-validation to assess how the SVCCA results generalize to unseen data.
                - **Stability Analysis**: Test how sensitive your SVCCA results are to changes in sample size by incrementally adding more data and observing the effect.
            
            **Summary**:
            
            - **Minimum Recommendation**: Aim for at least 1,024 samples (twice the dimensionality), though this is a bare minimum.
            - **Better Practice**: For more reliable and stable results, collect 2,500 to 5,000 samples or more.
            - **Adjust Based on Data**: If your data allows for effective dimensionality reduction or if you can use regularization techniques, you might manage with fewer samples.
            
            **Final Note**: The exact number of samples needed can vary depending on your specific application and data characteristics. It's often beneficial to start with as much data as you can reasonably obtain and perform preliminary analyses to determine if your sample size is sufficient for your goals.
            
        - we need more features so that rand isn’t as high?
            - “he” is too sim for rand (0.08) even though there are 80 features for “he”
    - ✅ check how often semantic subset better than rand PAIRED subsets by taking more random PAIRED subsets
        - this is still paired
        - but for 1000 featuers, it’s always high; it’s 0.1! it doesn’t matter if it’s a subset or not!
            - perhaps compare semantic subset to this one, to see if it’s even higher?
    - ✅ try semantic subspaces for more keywords
        - we need at least 1000 features, so don’t even bother when it’s too low
        - keywords that are too low
            - “give” has too few, and svcca for rand pairing is too high
            - “let” does really bad, despite having 17 unique feature pairings
    - ✅ perhaps try combining multiple keywords that have to do with a concept, and compare this to random PAIRED subsets + shuffling the PAIRED semantic subset + random UNPAIRED
        - numeric combo has 277 unique pairings, and is higher than 277 randomly selected CORRELATED feature pairs. Compared to 1000 selection, there is a p-value of 0.
            - rsa doesn’t work as well, though p-value is still low
        - [think of a category of more commonly used words in conversation, but still distinct and not generic. for instance, "euphoria" is not commonly used, but "happy" is. also, make them short and one syllable. they all must belong to one distinct category. generate 50 words for these](https://chatgpt.com/c/66e6c3b5-4ff4-800c-bfd5-a57534a30f81)
        - this also works for people-related, nature, science, animal
            - 1-1 is not much different, except for animal and numerics. prob bc % unique before is already 0.6, compared to 0.2 for the full space
        - not enough words
            - 
- ✅ writeup and timestamp
- ✅ REFLECT: the rand sel may STILL have some “dim” where these words are related in some way, or subset clusters of these
    - also, the larger the subset of randsel PAIRED features, the larger the chance they’ll get some more semantically similar feature sub-subsets
    - as such, we should have an autolabeling “semantic score” of how related everything is
    - [given a set of words, what's a way to score how related they are semantically?](https://chatgpt.com/c/66e6c9e3-5ff8-800c-bd1c-6e56c27430ea)
        - Word2Vec for single words; BERT for sentences
    - how to measure large subset of clusters of related words in a set of words or samples?
- ⚠️ word2vec_explora.ipynb
    - ✅ load feature labels
    - ✅ get feature IDs of a semantic concept, vs random feature IDs
    - ✅ for all top k feature labels of each feature, flatten them and put them through word2vec
    - ✅ ISSUE: high cosine sim for just number words, but not too far away from “random” when getting other keywords from a concept group. so try find better method.
        - try single words thru bert
            - issue: rand is still too high
                
                The relatively **high cosine similarity** (e.g., ~0.6) between **random words** when using **BERT** embeddings can be attributed to several factors related to how BERT embeddings work. Here’s why this happens:
                
                ### 1. **BERT Embeddings are Contextualized but Similar at the Base Layer**
                
                - **BERT** produces **contextualized embeddings**, meaning that embeddings are dependent on the context in which words appear. However, when you're working with individual words (rather than full sentences), BERT may not have enough contextual information to distinguish between them effectively.
                - Without a rich context, the embeddings for different words may still end up being similar, especially in earlier layers of BERT, which capture more general word features rather than nuanced, context-specific information.
                - This can result in **high baseline similarity** for random words that share commonalities in the broad language model space, leading to higher-than-expected cosine similarities.
                
                ### 2. **BERT Embedding Space is High-Dimensional**
                
                - BERT embeddings are **768-dimensional** vectors (for `bert-base`). In such high-dimensional spaces, even seemingly unrelated vectors tend to have a **non-negligible similarity**. This is a known phenomenon in high-dimensional vector spaces, where vectors may not be as orthogonal as you expect.
                - In high-dimensional spaces, cosine similarities often have a **higher baseline** because the distribution of vectors is much denser, causing random vectors to still have moderate similarities (around 0.5-0.6).
                
                ### 3. **Pretrained Language Models Capture Broad Semantic Similarities**
                
                - **BERT** has been trained on large corpora (e.g., Wikipedia, BooksCorpus), and even random words often share some broad-level semantic or statistical similarities from the training data.
                - For instance, words that are common in everyday language may still end up with similar embeddings, even if their meanings differ.
                - Since **BERT** learns both syntactic and semantic relationships, even random words might exhibit non-trivial semantic overlap, especially for common words (e.g., "man," "queen," "judge").
                
                ### 4. **Limited Context for Single Words**
                
                - BERT is designed for **sentences** and **longer contexts**, not single words. When you pass single words into BERT without any context, it doesn’t have enough information to differentiate the words in the same way it would with full sentences.
                - BERT embeddings for single words might, therefore, be more **generic** and capture common language usage patterns rather than specific distinctions, leading to higher similarities even for unrelated words.
                
                ### 5. **Cosine Similarity is Not Zero-Centered**
                
                - **Cosine similarity** is bounded between -1 and 1, but in practical applications with embeddings from models like BERT, the scores tend to fall in the range of 0 to 1, with **0.5** being a common "baseline" for unrelated vectors.
                - High-dimensional vectors, such as those from BERT, rarely result in negative cosine similarities unless the words are strongly opposed in meaning. As a result, even random words may exhibit moderately high similarity (around 0.5 to 0.6) rather than near-zero values.
                
                ### 6. **Subword Tokenization and Shared Embeddings**
                
                - BERT uses **subword tokenization** (via WordPiece), where words are broken down into smaller subword units. Some unrelated words might share common subwords, causing their embeddings to be more similar than expected.
                - For example, words like "man" and "woman" might have similar embeddings because they share common subwords ("man").
                
                ### Ways to Address This:
                
                1. **Use Full Sentences or Contextual Information**:
                    - BERT is designed to work best when you use **full sentences** or meaningful contexts. For example, instead of comparing words in isolation, compare them within sentences or phrases:
                        - Compare "The man is a teacher" vs. "The queen is a ruler" instead of just "man" and "queen."
                        - This will provide more meaningful contextual embeddings and likely reduce the similarity between unrelated words.
                2. **Layer Selection**:
                    - BERT produces embeddings from multiple layers. The final layers (closer to the output) are more **contextual** and might provide better distinction between random words than the **lower layers**, which capture more syntactic and general patterns.
                    - You can experiment by using embeddings from the **last layer** or an **average of the last few layers** (instead of just taking the default `last_hidden_state.mean(dim=1)`).
                    
                    Example of using embeddings from the last few layers:
                    
                    ```python
                    outputs = model(**inputs)
                    # Use the average of the last 4 layers
                    embeddings = torch.mean(torch.stack(outputs.hidden_states[-4:]), dim=0)
                    
                    ```
                    
                3. **Normalize the Embeddings**:
                    - If embeddings are not normalized, cosine similarity can be affected by vector magnitudes. You can ensure the vectors are normalized before computing cosine similarity:
                    
                    ```python
                    from sklearn.preprocessing import normalize
                    embeddings = normalize(embeddings.cpu().numpy())
                    
                    ```
                    
                4. **Compare Centroid Similarity**:
                    - Instead of pairwise cosine similarity, you can compute the similarity of each word embedding to the **centroid** (mean embedding) of a concept or group of related words. This approach may reduce the influence of individual word similarities and focus on concept-level relatedness.
                
                ### Conclusion:
                
                The high cosine similarity between random words in BERT is due to the nature of high-dimensional vector spaces, limited context for individual words, and the fact that BERT captures broad semantic patterns. To get more meaningful similarities, consider using contextualized embeddings with full sentences, averaging across layers, or applying further normalization techniques.
                
                Would you like to try some of these methods to get more meaningful similarity scores?
                
    - for all topk dataset examples of each feature, flatten them then thru BERT
- ✅ forget semantic for now; say on avg, it’d avg out to unrelated features
- ⚠️ `match_semantic_spaces_newSearchFn.ipynb`: require 5/10 of the top 10
    
    if we require all the top 5 to fire on a keyword, or 5/10 of the top 10, that may be too few features. but may solve problem with “he”. we saw that 20 features is enough. (many keywords in a concept may solve this)
    
    - ✅ not that a keywrod has to be repeated in the top 3/5; for each feature, the top 5 has to contains at least 3 keywords that belong to the list
        - 2/5 is best; 1/5 is worst
    - ✅ Check if the paired subspace also hold for this; how many of its features pass this test?
    - both B and A don’t have as many using this, so try top J out of K, where K > 5
        - get how many acts are nonzero (to determine what top k to consider)
            - see gemma 2
        - actually this makes it worse, bc not strict enough to get actual close features
        - the best approach is still approach 1 of `match_semantic_spaces_v1`
        - actually this is obv a bad approach bc why do we REQUIRE more than 1 specific numeric keywords, when our keywords don’t have every numeric keyword? a feature may be specific for “ten”, for instance.
- ✅ match_semantic_spaces_v2.ipynb: run on more layers
    - ✅ L3 vs L5
        - no sigf when not 1-1
        - very good when 1-1; so just use 1-1
    - ✅ turn into fns and loop ; store in dataframe
    - ✅ table cols (rows are semantic categories; tables are for one pair of layers)
        - semantic score (word2vec) of test spaces
        - avg semantic score of rand sel corr test spaces
    - ✅ table into latex
    - ✅ run on more layers
- ✅ match_semantic_spaces_v1: debug approach 2
    - better now, but pvals are above 0.05 slightly
- ✅ sel rand featuers without repeated elements
    
    something impt I found in the score_rand() function in the "setup section" of metrics_v2:
    np.random.randint(low=0, high=weight_matrix_np.shape[0], size=num_feats).tolist() etc won't get unique elements, but we want that. So we should use `np.random.choice(range(len(weight_matrix_np.shape[0]), size=num_feats, replace=False).tolist()`
    

Relational Subspace Matching

- ✅ [rsa vs svcca writeup](https://chatgpt.com/c/66ec301a-8848-800c-8ffb-d45aa2b6503c)
    - test feature relations based on vector differences, similar to 'difference in means' steering vectors or king-queen
        - every single pair difference?
        - too many, so try procrustes
        - no wait, RSA already does this!

Solving OOM issues

- ✅ [make public key for CAIS](https://claude.ai/chat/30d0c277-5c4e-438f-8435-5fa5200fcb66)
    - [https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key](https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key)

[CAIS](Semantic%20subspace%20matching%2011eafed922dc80b5ac94dbb7e4b73137/CAIS%20b15291afa9f14467b39bd6663cbd4a8e.md)

- ✅ cais login
    
    [https://chatgpt.com/c/66e58d45-89b4-800c-9884-bae490d7e67a](https://chatgpt.com/c/66e58d45-89b4-800c-9884-bae490d7e67a)
    
    - Username: michael_lan
    
    IP address of cluster: [compute.safe.ai](http://compute.safe.ai/)
    
    Command to login: `ssh -i {path-to-private-key} {[user-name}@compute.safe.ai](mailto:user-name%7D@compute.safe.ai)`
    
    `ssh -i C:/Users/mikel/.ssh/id_ed25519 michael_lan[@compute.safe.ai](mailto:user-name%7D@compute.safe.ai)`
    
    Here are some resources to help with onboarding:
    1. For technical documentation and details on setup see [here.](https://cluster.safe.ai/)
    2. Join the [Slack](https://join.slack.com/t/caiscomputecluster/shared_invite/zt-1ynca78vk-vaR_ULO8op8dDtFp92j0Nw) workspace, which we will be using for communication and reporting bugs/crashes.
    3. If you have any questions, feel free to place them in the #help-desk channel or message Andriy Novykov on Slack.
    
- ✅ cais run job
    - issue with `srun --gpus-per-node=2 --pty bash`
        
        srun: error: Unable to allocate resources: Invalid account or account/partition combination specified
        
    
     For users in the `david_krueger` lab, you need to use the `high_priority` partition. So your `srun` cmd would look like 
    
    `srun --partition=high_priority --gpus-per-node=2 --pty bash`.
    

Refine tinystory results to show LLM no reln (pval)

- ✅ save_LLM_w_actvs_c_proj_v2.ipynb: show LLM no reln (pval)
    - random shuffle
    - 1-1
    - results
        
        despite low mean actv corr, the tinystories 1L and 2L could align, and their 1-1 svcca was 0.9
        
        now im wondering if maybe we should compare tinystories to gpt2 instead
        
        do these small LLMs have very similar spaces? but this doesn't hold for larger models?
        
- ✅ save_LLM_w_actvs_c_proj_MLP1.ipynb

LLM semantic spaces

- 🐣 new main thesis, say: can't find semantic subspaces of LLMs
    
    [New main topic](Semantic%20subspace%20matching%2011eafed922dc80b5ac94dbb7e4b73137/New%20main%20topic%20106afed922dc80aca999e0c4cb596288.md)
    
    - because tinystories is on a narrow data distribution with a smaller dataset, there may be less features to capture. as such, it may learn similar polysemantic neurons, even with different initializations.
    - however, it is not able to do semantic subspace matching, which requires identifying features that correspond to certain concepts.
    - thus, some models we can align (pythia70m and 70m dedupted, ts1L and 2L) by LLM. But for models where we cannot, we show that SAEs can align them.
    - for now just get rid of ts in examples (not good bc seems pretty monosemantic already, given that it’s on a more narrow dataset)
- ✅ LLM_ts_semantic_subspaces_v1.ipynb
    - ✅ get dataset labels for LLMs
        - actually i think instead of top 5, it should be top 5*expa_fac, so top 30
        - bc the LLM neurons "entangle" the saes
        - ISSUE with tinystories rand feature subsets: these already have high SVCCA
        - HOWEVER, the good thing is that their semantic subspaces for numeric and people are NOT more simialr than random. they are, in fact, lower.
        - “once” is very high for top 5; not so much top 90
        - numeric in top 5 doesn’t work
        - but numeric in top30 DOES work
            - nah; it’s higher than mean but has pvalue of 0.25
        - people in top5 DOES work
            - bc there’s only 6
            - these are monosemantic neurons already
    - it seems tinystory LLMs ALREADY are pretty monosemantic
- ✅ LLM_pythia_match_semantic_spaces.ipynb
    - for top 5 and top 30, numerics has high pval
    - for top 90 1-1, it passes rsa, but not svcca
        - howver, for all other semantic cateogires, it doesn’t pass (unlike saes)
        - the rsa shuffled sometimes passes, but not the rand sel corr. it must pass both tests.
    - for L3 vs L5, none of the 1-1 tests pass
        - for (any A layer) vs L5, none of the tests pass (all high pval for 100 runs)
    - for (any A) vs L10, all pvals are high (animals is NaN)
- ✅ match_semantic_spaces_v3.ipynb: several layers of B (early, late)
    - late layers tend not to have the features! it has science, but not numeric
        - this may be bc late layers contain more “complex, composite” features, and numeric features are more like building blocks
        - L3 vs L6 : has numeric
            - L2 vs L6 : doesn’t have numeric