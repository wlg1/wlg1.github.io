# Project Planning

[https://www.notion.so/wlg1/_Feature-Geometry-Expms-Summary-1beb35705e5c47cd89c1c6b7908094c0](_Feature%20Geometry%20Expms%20Summary%201beb35705e5c47cd89c1c6b7908094c0.md)

[Done (by Arcs)](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Done%20(by%20Arcs)%201c002201437341e48b55b8276859a632.md)

---

### Working on

More actvs for corr- prevent OOM

- ✅ plan corr fn: batch proc on actvs to prevent OOM
    - [https://chatgpt.com/c/2e12ec21-211e-4b41-af19-4ce04ab20922](https://chatgpt.com/c/2e12ec21-211e-4b41-af19-4ce04ab20922)
    - [https://chatgpt.com/c/c14743c7-5591-4ad0-a7a0-3223c5237e3a](https://chatgpt.com/c/c14743c7-5591-4ad0-a7a0-3223c5237e3a)
- ✅ [corr_large_data_v0.ipynb](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692.md)
    
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

[Kiho meeting notes- sept 4](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Kiho%20meeting%20notes-%20sept%204%207b78a9ef86e644a48ef1cd78ab3b3c95.md)

[Austin meeting notes](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Austin%20meeting%20notes%206669c1f41e9448fd9007b07a91d2450e.md)

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

[Ask Austin on 1-1 features](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Ask%20Austin%20on%201-1%20features%20f6fe76bd99cc4ff6ab904fa39ced04ff.md)

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
    - [All Pythia models trained for 143000 steps at a batch size of 2M (**2,097,152 tokens)**](../ARENA%20notes%201a8ff2624cff486e9d91b13139420026/1%204%200186fae1fa2d41e49f64642d2ea523eb.md)
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
- writeup and timestamp

---

### To do

- the rand sel may STILL have some “dim” where these words are related in some way, or subset clusters of these
    - also, the larger the subset of randsel PAIRED features, the larger the chance they’ll get some more semantically similar feature sub-subsets
- as such, we should have an autolabeling “semantic score” of how related everything is
- [given a set of words, what's a way to score how related they are semantically?](https://chatgpt.com/c/66e6c9e3-5ff8-800c-bd1c-6e56c27430ea)
    - Word2Vec
- how to measure large subset of clusters of related words in a set of words or samples?
- have chatgpt generate a couple of categories and run them thru
- table cols (rows are semantic categories; tables are for one pair of layers)
    - semantic score (word2vec) of test spaces
    - avg semantic score of rand sel corr test spaces
- run on LLMs to show no corr

- require all the top 5 to fire on a keyword, or 5/10 of the top 10
    - if we require all the top 5 to fire on a keyword, or 5/10 of the top 10, that may be too few features. but may solve problem with “he”. we saw that 20 features is enough.
- match rand weights of same len to see if svcca has high score for any matrices of low num rows

- APPR 3: clean up the search fn using gpt4/claude auto labeling semantics
    - use many keywords related to a concept (number, numbers, etc)
- APPR _: put in tokens and get highest activation features in both, then compare features by actvs
    - this isn’t labeling, which is good for human eval but shaky. this is closer to actvs?
    - the diff of this and appr 1 is we’re using specific inputs that we know of
    - correlate featuers based on actvs
        - compare weight matrix or actv matrix?
    - how to find which data to use?
        - we can take the tokens in the actv matrix that just correspond to “she” and do sim metric on transposed WxA

Relational Subspace Matching

- test feature relations based on vector differences, similar to 'difference in means' steering vectors or king-queen
    - too many, so try procrustes

Check sim metric approach validities

- [does a pvalue of 0 mean we should use more samples in null distribution?](https://chatgpt.com/c/66e6c577-6664-800c-a4ef-0d3cc3a1a0d4)
- in python how calculate variance of a list of numbers to check if enough samples to get pvalue
- how to code finding if se stabilizes
- issue with p-value: those 1000 samples may not be more than the test value, but what if a “decent number” are still very close? what do I do with that?

- svcca validity and on WxA
    
    [https://chatgpt.com/c/66e6c099-7c18-800c-8f6e-719af8607c34](https://chatgpt.com/c/66e6c099-7c18-800c-8f6e-719af8607c34)
    
    - i have two weight matrices from two models. i pair their neurons row-wise by highest activation correlation (both models take in the same set of tokens, and pair tokens to get pearson correlation). then, I take svcca of their weight matrices to get a score, and compare this to random pairings null distribution. is this valid?
        
        The approach you've described involves several steps:
        
        1. **Pairing Neurons Based on Activation Correlation**: You align neurons from two models by pairing them row-wise based on the highest Pearson correlation of their activations across the same set of tokens. This means you're matching neurons that behave similarly in response to the same inputs.
        2. **Applying SVCCA on Weight Matrices**: After pairing the neurons, you apply Singular Vector Canonical Correlation Analysis (SVCCA) to their weight matrices to compute a similarity score.
        3. **Comparing to a Null Distribution**: You compare this SVCCA score to a null distribution obtained from random pairings to assess significance.
        
        **Is This Approach Valid?**
        
        Overall, your method is conceptually sound, but there are important considerations to ensure its validity:
        
        1. **Pairing Neurons by Activation Correlation**:
            - *Validity*: Pairing neurons based on the highest activation correlation is a reasonable way to align neurons between models, especially when they process the same inputs.
            - *Considerations*: Ensure that the activation correlations are computed over a sufficiently large and representative set of tokens to capture meaningful neuron behaviors.
        2. **Applying SVCCA on Weight Matrices**:
            - *Standard Usage*: SVCCA is typically used to compare neural network **representations**, i.e., the activations, not the weight matrices directly.
            - *Validity*: Applying SVCCA to weight matrices is less common and may not capture the functional similarities between neurons as effectively as comparing activations.
            - *Considerations*:
                - **Alignment**: Since you've paired neurons based on activation correlations, their weight matrices are aligned in the sense that they correspond to similarly functioning neurons.
                - **Interpretability**: Weight matrices can be influenced by factors like scale and rotation, which might not directly reflect functional similarity.
                - **Alternative**: It might be more informative to apply SVCCA directly to the activation vectors of the neurons rather than their weights.
        3. **Comparing to Random Pairings (Null Distribution)**:
            - *Validity*: Comparing your SVCCA score to a null distribution generated from random pairings is a valid approach to assess the significance of your observed similarity.
            - *Considerations*: Ensure that the random pairings are truly random and that the null distribution is estimated with sufficient precision (e.g., using a large number of random pairings).
        
        **Recommendations**:
        
        - **Use SVCCA on Activations**: Consider applying SVCCA directly to the activation vectors of the neurons. This aligns with the standard use of SVCCA and may provide a more accurate measure of the functional similarity between the models.
        - **Analyze Weight Matrices with Caution**: If you prefer to analyze weight matrices, be cautious about the interpretability of the results. Weight matrices may not reflect neuron functionality as directly as activations due to factors like weight scaling and permutations.
        - **Ensure Proper Normalization**: Whether you use activations or weights, ensure that your data is properly normalized. For weights, this might involve accounting for differences in scale or applying techniques to make them comparable.
        - **Validate with Additional Metrics**: Supplement your analysis with other similarity measures or validation techniques to confirm your findings.
        
        **Conclusion**:
        
        Your approach is conceptually valid, especially the pairing based on activation correlations and comparing to a null distribution. However, applying SVCCA directly to weight matrices is unconventional and may not yield the most meaningful insights. I recommend applying SVCCA to neuron activations for a more standard and potentially insightful analysis.
        
    - what if I use highest activation correlation to pair neurons, but svcca compare matrices that are the neurons x activations of the same activations? is it redudndant to use svcca to get info when the highest activation correlation is already high for each pair, or is it nontrivial to say svcca may not always be high in this case just bc highest activ corr is already high?
        
        Your updated approach involves:
        
        1. **Pairing Neurons by Highest Activation Correlation**: You align neurons from two models by matching each neuron in one model with the neuron in the other model that has the highest Pearson correlation of activations over the same set of tokens.
        2. **Applying SVCCA on Neuron Activations**: You then construct matrices of neurons × activations (for the same activations) and apply Singular Vector Canonical Correlation Analysis (SVCCA) to these matrices.
        
        ---
        
        **Is Using SVCCA Redundant in This Context?**
        
        At first glance, it might seem redundant to apply SVCCA after pairing neurons by highest activation correlation because the pairing already maximizes the correlation at the individual neuron level. However, it's important to consider the differences between:
        
        - **Pointwise Neuron Pairing**: Matching neurons based on individual activation correlations focuses on local, neuron-wise similarities.
        - **SVCCA Analysis**: SVCCA examines the global structure of the neural representations by identifying shared subspaces in the high-dimensional activation space.
        
        **Key Points to Consider:**
        
        1. **Local vs. Global Similarity**:
            - *Neuron Pairing*: Captures **local** similarities between individual neuron activations.
            - *SVCCA*: Captures **global** similarities by considering the collective behavior of all neurons and how they contribute to the overall representation.
        2. **Redundancy Concerns**:
            - *Not Necessarily Redundant*: High activation correlation between paired neurons does not guarantee that the overall representational spaces are similar.
            - *SVCCA Provides Additional Insight*: By analyzing the shared subspace, SVCCA can reveal structural similarities or differences that are not apparent from individual neuron correlations.
        3. **Subspace Alignment**:
            - *Independent of Pairing*: SVCCA does not rely on neuron pairing; it considers the alignment of the subspaces spanned by the activations.
            - *Capturing Variance*: SVCCA identifies the directions in activation space that account for the most variance and compares these between models.
        4. **Possible Outcomes**:
            - *High Neuron Correlations but Low SVCCA Similarity*: Even if individual neurons are highly correlated, the overall structures could differ, leading to lower SVCCA similarity.
            - *High SVCCA Similarity*: If the models not only have high neuron-wise correlations but also similar representational structures, SVCCA would reflect this with a high similarity score.
        
        ---
        
        **Why SVCCA May Not Always Be High Despite High Neuron Correlations**
        
        - **Different Combinations of Neurons**: The same activations might be represented differently across models due to different combinations or interactions between neurons.
        - **Nonlinear Relationships**: Neuron-wise Pearson correlation captures linear relationships, but neural networks can represent information nonlinearly.
        - **Dimensionality Reduction**: SVCCA includes an SVD step that focuses on the most significant components, potentially highlighting differences not captured by individual correlations.
        
        ---
        
        **Conclusion**
        
        Applying SVCCA after pairing neurons by highest activation correlation is **not redundant**. While neuron pairing focuses on local, pairwise similarities, SVCCA analyzes the **global structure** of the representations. It can provide additional insights into how the models' internal representations compare at a subspace level, which might reveal similarities or differences not apparent from neuron-wise correlations alone.
        
        **Recommendations**:
        
        - **Proceed with SVCCA**: Your approach is valid and can yield meaningful information about the representational similarities between the models.
        - **Interpret Results Carefully**: If SVCCA similarity is high, it suggests that not only are individual neurons behaving similarly, but the overall representational geometry is aligned. If it's low, there may be structural differences worth investigating.
        - **Supplementary Analyses**: Consider additional methods like CKA (Centered Kernel Alignment) or probing tasks to further explore the similarities and differences between the models.
        
        ---
        
        **Summary**
        
        - Pairing neurons by highest activation correlation aligns neurons based on local similarity.
        - SVCCA analyzes global representational similarity by comparing the subspaces of activations.
        - Using SVCCA after neuron pairing is not redundant and can uncover deeper insights into model similarities.
        - High neuron-wise correlations do not guarantee high SVCCA similarity due to potential differences in overall representational structure.
        
        By combining both methods, you gain a more comprehensive understanding of how the models relate to each other at both the individual neuron level and the overall representational level.
        
    - what if I use highest activation correlation to pair neurons, but svcca compare matrices that are the neurons x activations of the different activations?
    - should you normalize before correlating?
        - you ALREADY DO THIS

just run this: (not impt for overleaf)

- austin plan for sim metric runs
    
    i'm looking to record: num features after filtering, mean actv score after filtering, svcca paired 1-1 + unpaired (random selection) 1-1.There's some variations you can also do if you have time:
    
    1. running everything again, but pairing from manyBtoA instead of manyAtoB (just switch the order in the batched_corr() function)
    2. getting 10-1 or 100-1 (wouldn't use the default many-to-1 before filtering as it's bad). just change the threshold in the filtering line "kept mod A feats"
    3. right now the rand function selects a subset of unpaired featuers of the same length as the filtered feature number. you can also do shuffling of 100 to 1k random runs. this is the code:
    - code
        
        `import randomdef shuffle_rand(num_runs, weight_matrix_np, weight_matrix_2, num_feats, sim_fn, shapereq_bool):    all_rand_scores = []    for i in range(num_runs):        row_idxs = list(range(num_feats))        random.shuffle(row_idxs)        if shapereq_bool:            score = sim_fn(weight_matrix_np, weight_matrix_2[row_idxs], "nd")        else:            score = sim_fn(weight_matrix_np, weight_matrix_2[row_idxs])        all_rand_scores.append(score)    return sum(all_rand_scores) / len(all_rand_scores)`
        
    
    so in all the automated runs, you can include that rand shuffling in the pipelline. for 1) and 2), you can just take the code after running everything else, and if you have time, you can just change a few lines to run again.
    
- pval on 4 metrics: cca, svcca, normalized procrustes, rsa, jaccard
    
    simSAE_pythias_70m_160m_statTests.ipynb
    
- writeup pval results
    - TS 1L vs TS 2L (both)
    - Pythia 70m vs 160m
- full space pval expms for TS and Pythia (they use diff sae fns)
    - both layers of TS-2L
- 1k sample stat tests (actually can just use 100 bc variance is low; get the var score)
    - [does this run on cpu or gpu automatically when you call it from a gpu run in colab:](https://chatgpt.com/c/43a1266d-1c47-49e4-ac9c-39a22f8338e3)
        - but doesn't svcca use torch tensor args?
            
            converts it to numpy though, doesn’t use pytorch operations
            
    - ask max for gpu svcca
        
        Hi, is the code (in particular, svcca, jaccard, procrustes and RSA) able to run on GPU? Would it be faster if it ran on GPU or not? I see that it takes torch as arg but use numpy operations instead of pytorch. I'm looking to run 1k to 10k randomly paired matrix sim metric runs to obtain a null distr for pval testing. Thanks!
        
    - run stat tests for all layers, not 1-1, and 1k rand samples
- simLLM_pythias_70m_160m_all_layers.ipynb : run without 1-1
- randsel 1-1 features and get avg
    - or just eliminate them to avoid this. state results are similar for what was investigated, and should be similar if investigated further
    - get distrb of this for both manyAto1B, and manyBto1A

- look more into rand perm to get null
    - [https://en.wikipedia.org/wiki/Mantel_test](https://en.wikipedia.org/wiki/Mantel_test)
    - [https://en.wikipedia.org/wiki/Resampling_(statistics)#Permutation_tests](https://en.wikipedia.org/wiki/Resampling_(statistics)#Permutation_tests)
    - [can correlation coefficient produce a scalar score for two matrices of samples, or is it just for two vectors (pair of two samples)?](https://chatgpt.com/c/66e4cde2-46b0-800c-9e76-70bce3bfc842)
        
        When you have matrices of samples—where each matrix represents multiple variables across samples—the concept of correlation expands but doesn't directly produce a single scalar score between two entire matrices.
        
    - if correlation coefficient doesn't produce a scalar score for two matrices of samples, just for two vectors (pair of two samples), explain what the "methods section" of [https://en.wikipedia.org/wiki/Mantel_test](https://en.wikipedia.org/wiki/Mantel_test) means when it talks about permuting rows of the matrices. how does permuting rows change corr coef of matrices if it's not even calculated bewteen matrices?
        
        [https://chatgpt.com/c/66e4d0f8-2ffc-800c-9c5e-7ba2c7a14ebf](https://chatgpt.com/c/66e4d0f8-2ffc-800c-9c5e-7ba2c7a14ebf)
        

1-1 issue- extras

- simSAE_pythias_70m_160m_force1to1_v2 : debug skipping over the already matched
- instead of needing the best to be 1-1, just care about getting 1-1 more about getting the top matches. “good enough”
- now is fast enough, run on all pairs instead of just a few examples
- for many-to-1 featuers, get histo count of their col in corr mat to see what else they can map to
- simSAE_pythias_70m_160m_interpet_manyTo1
    - interpret the features which have many matches
        
        if not meaningful, then that means the reason they map to it is bc both are “low info”? but why high corr? WHAT are they correlated on? 
        
    - find a way to summarize this
        - autolabel?
- measure semantic purity using auto labeling

Other sim metrics

- are 2L and 2L-nolyaernorm comparable?
- train on ts: ask author of “tinystories-2L, no layernorm” how long this took
- match by (weight x actvs) not just weight matrices
- figure out issue with why mlp 0 actv matrix is all 0s
    - is it just for 70m, or also for 160m?

---

- overall to-do list (just #1 is needed; #2 and rest are extra)
    1. full space pval expms for TS and Pythia (they use diff sae fns)
        - extra: 1L toy model, gemma2
            1. find 1L online
            2. types of toy models: general or specific?
    2. subspace expms
    3. re-run expms using more data
    4. feature spliting
        1. train own saes on tinystories
    5. ground truth expms
    6. func expms (attrb vector for >1L?)
- things to do
    1. Find 1L toy models anywhere that differ by rand init
    2. efficiently / cost effectively get mean actv corr svcca, rsa, jaccard score (and other items in dictionary) vs pval of 100 runs for the following pairs for both LLMs and SAEs:
        1. tinystories MLP0 vs TS-2L MLP0 and MLP1: adapt to this code: `simSAE_pythias_70m_160m_moreMetrics_v2.ipynb`
        2. every pair of 70m vs 160m: `simSAE_pythias_70m_160m_moreMetrics_v2.ipynb`
        3. also num + mean corr after filtering (non 1-1) to show isn’t too much that’s filtered
        4. we want to do this for a lot of tokens
        5. the pvals take a long time (would help if can parallelize)
            1. maybe tweak how pvals appear on bar plots?
            2. generate llm and sae plots side by side instead of manually making them side by side
        6. jaccard nn is optional (may just use svcca, possibly rsa) but would help if speed up perhaps by batching
        7. also, later I’m making another procedure that does 1-1 for more feature pairs, so may want to re-run all this for that. so organize code as functions to easily re-run things with small tweaks
    3. taking svcca, rsa, etc similarity of feature activations transposed and matched for variations of tinystories + pythia for both LLMs and SAEs
        1. `sae_crossModel_sim_explora / jaccard_subset_ts_1L_2L.ipynb` ; section “**jaccard on token actvs” → “by corr features”**
            1. `jaccard_similarity(reshaped_activations_A.t()[highest_correlations_indices_v1], reshaped_activations_B.t())`
            2. adapt to `simSAE_pythias_70m_160m_moreMetrics_v2.ipynb`
        2. actually this may be too trivial bc we already correlate by activations so what would be saying?
        3. aslo try this for not transposed but then not using correlated indices bc now the input tokens are already paired
    4. Est training toy models on toy dataset
        1. tinystories 1M vs 3M didn’t yield good interpretations, so maybe this isn’t good
    5. how to simulate activations of two different language models for ground truth features
        1. [https://www.lesswrong.com/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition](https://www.lesswrong.com/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition)
        2. each LLM should use different ground truth features but also a shared subset; we want to see if they do share that subset
        3. maybe use different probabilities of selection for each model?
        4. issue from before: using 2 different set of synth activations to train to 2 saes just trained 2 saes on 2 actv sets from same model, instead of 2 diff models. so what would make the actvs diff? I think the above 2 tweaks may suffice.
        5. main point is to show LLMs are not similar this way, but SAEs are. so we need to “simulate” in synthetic data the neurons (var G) are not similar, but saes are. if we don’t show this, then don’t put this in paper.
    6. speed up pairing all features 1-1: simSAE_pythias_70m_160m_force1to1_v2.ipynb
        1. sort the flatened matrix to get highest value (6m)
        2. go through the list and find features (rows and cols of orig matrix) not used in pairings yet (takes around 20m)
- timeline (last month before ICLR)
    
    just run the same main steps on different domains (not uncertain to solve; just run):
    
    if not good results, just don’t include it
    
    - ✅ 9/1 - 9/7: start full space pval, solve 1-1 issues of full space, finish writeup outline
    - ✅ 9/7-9/10: finish writing full space (but not run all expms)
    - 9/10-9/16: force 1-1 and semantic subspace expms
    - 9/17-9/18: start 1L toy models + non-colab gpu training (re-run ts and pythia)
        - continue this throughout
    - 9/19-9/20: finish ground truth
    - 9/21-9/22: finish feature splitting
        - are SAEs more or less similar as they get wider? (try 3 lvls on tinystories)
        - just run same things on saes of diff sizes
    
    now this is new:
    
    - 9/23 - 9/29: writeup and functional
    - 9/30-10/1: finish writing

Wirting

- writeup better undrstanding of what each metric does
    - ask max to double check
- an issue with comparing layer by layer is that they may have diff num of featuers after filtering. this is why in appendix you should include num of features after filtering
- say should look at relative bc depends on the number of samples, etc.
    - 2 types of random: shuffle same, and random unpaired subset
- explain 1-1
    - ask: the periods might be capturing DIFFERENT information, bc they store next token info, and so the matches on periods might not be semantically meaningful?
    - manyAtoB
- put plots of all 6 layers in 1 figure (appendix)
    - plot 160m vs 70m
- move SVD expms to appendix
    - SVD vs SVCCA
        
        svd expms: find similarity between llms. but other sim metrics cannot be run due to perm pairing issues. sae offer soln to perm pairing problem that was not able to be done before.
        
        svd is sort of like perm pairing as it’s comparing the singular vectors, or principal components. but PCA requiers mean centering?
        
        svd and saes are sort of similar. but saes allow feature clustering and individual feature interpretability, along with jaccard. perhaps svd can also allow matching. svd is sort of like cca in that it matches highest canonical dirs? but why is svd invar to shuffling- is it?
        
        try svd after corr shuffling of sae features.
        
        try clustering singular vectors? also try matching singular vectors by the index?
        
        svd comps aren’t features though; not as interpretable
        
    - general linear groups change basis, so diff LLMs with  have diff basis
        
        [https://chatgpt.com/c/54c66219-4e07-4322-ab68-648e13d25cc0](https://chatgpt.com/c/54c66219-4e07-4322-ab68-648e13d25cc0)
        

- Write in Future work
    1. pair by semantic and functional
    2. LDA to approx subspace
        - cross-patch features in reconstructions using LDA approx, or some other transformation
            - while two LLMs use diff actvs, if their SAEs share similarities, perhaps we can transform one to another (not direct patching though, as SAEs still have diff basis)
    3. hier geom plots
        - use block matrices “Disentangling” paper or orth relns to show hier in one model, then show similar hier after pairing features. compare similarity of hier matrices.
    4. feature pairing algo based on scores

---

Solving OOM issues

- ✅ [make public key for CAIS](https://claude.ai/chat/30d0c277-5c4e-438f-8435-5fa5200fcb66)
    - [https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key](https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key)

[CAIS](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/CAIS%20b15291afa9f14467b39bd6663cbd4a8e.md)

- cais login
    
    [https://chatgpt.com/c/66e58d45-89b4-800c-9884-bae490d7e67a](https://chatgpt.com/c/66e58d45-89b4-800c-9884-bae490d7e67a)
    
    - Username: michael_lan
    
    IP address of cluster: [compute.safe.ai](http://compute.safe.ai/)
    
    Command to login: `ssh -i {path-to-private-key} {[user-name}@compute.safe.ai](mailto:user-name%7D@compute.safe.ai)`
    
    `ssh -i C:/Users/mikel/.ssh/id_ed25519 michael_lan[@compute.safe.ai](mailto:user-name%7D@compute.safe.ai)`
    
    Here are some resources to help with onboarding:
    1. For technical documentation and details on setup see [here.](https://cluster.safe.ai/)
    2. Join the [Slack](https://join.slack.com/t/caiscomputecluster/shared_invite/zt-1ynca78vk-vaR_ULO8op8dDtFp92j0Nw) workspace, which we will be using for communication and reporting bugs/crashes.
    3. If you have any questions, feel free to place them in the #help-desk channel or message Andriy Novykov on Slack.
    
- ⚠️ ISSUE: for >400 samples, `feature_acts_model_A = sae.pre_acts(accumulated_outputs)`  -OOM, so do in batches the same way (not data loader, just slices of accumulated output)
    - ISSUE: even after doing this, still OOM at 400
- get rid of nonzeros before matching
- sparse matrix
    - only get nonzero inds
- avoid OOM of loading 2 models by doing this in separate nbs or runs
- even looping and del makes it OOM; so del the matrixx and clear cache doesn’t del everything?
- save large actv datasets by batches to prevent using a100. save batch, then del from mem, repeat

Extend results to more variations (1L toy model, etc)

- how to train multiple 1L toy models
- make fns to easily input other models, layers, data, etc.
- compare gemma2 2b vs 9b using saelens
- gemma1-2b vs gemma2-2b
- tinystories-2L, no layernorm
    
    I've commissioned a 2L TinyStories Model w/ no layernorm (Available [here](https://huggingface.co/noanabeshima/tiny_model/blob/main/tiny_model_2L_3E.pt)) to try to fully reverse engineer a small model w/ SAEs.There are two uncertainties:
    
    1. How to compute features from attn_in to attn_out? Currently seems unknown, even w/ QK-SAEs and Attn_out SAEs. If this isn’t true, please let me know!
    
    2. If we settle for just training on attn_out, we could train on activations before W_O, but I’m a major attention-noob and don’t understand what the benefits to interp would be.I also have a (really) rough draft of my specific proposed project [here](https://docs.google.com/document/d/1o3aV78jM30-yGxa964S8wXrI4YAm1bZzGy7uHYK3L1A/edit?usp=sharing) . In summary, train SAEs to sparsely reconstruct downstream SAE **features**
    
    (which Stefan told me an exact same idea, but from the first layer forward IIRC)
    
- vary LLM parameters, SAE dictionary sizes, and more
    - match saes with different dictionary sizes- what happens as you vary?
- use a heatmap of (paired,unpaired) ratios to compare all layer pairs
- try cca

Sim metrics- If have time:

- auto label interpretations and see if semantically matches too (they should)
- stronger sim metric tests
    - Rsa step 5 has p-val of rand pairings
        - bootsrap error bars
    - F score tests from feature fams
    - spearman rank correlation
    - soft match & procrutes normalized
    - send plots + code to max for checking validity
- compare not just pairwise models
- make sure ts and gpt2sm use same tokenizer by comparing their tokens
- LLMs with different tokenizers
    - Use phrase lvl for comon actv, not token. Get mean actv for all tokens in phrase. So map multiple tokens ro each other
        - Each sample index is not a dataset paragraph nor a token from flattening all, but a small phrase. Make this phrase using breakdown of samples? But now we can map using these indices by taking mean of all tokens in one index . This is like sum.
    - then gpt2 pretrained with pythia pretrained
        - compare using mean actvs of phrase
- gpt2 pretrained vs gpt2 med self-trained
- compare ts-1L with lincombo of ts-2L-MLP0 and ts-2L-MLP1
    - try just concat the features of 2L into one matrix then take corr with 1L
        - 16k 2L into 32k, then 8k 2L into 16k VS 16k 1L?
    - compare ALL features of GPT-2sm with ts-1L

---

Feature subspace matching by func sim

- for models that aren’t 1 layer, can we use attribution vectors?
- Functional sim of feats by ablate and steer
    - start with one type of ablation
- universal steering vectors: see if feature geometry (arrangement, hierarchy) is found across models
- towards mono: how they measured by ablation
    - fig : feature ablation and residual ablation
        
        ![image.png](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/image.png)
        
    
    [https://transformer-circuits.pub/2023/monosemantic-features#setup-interface](https://transformer-circuits.pub/2023/monosemantic-features#setup-interface)
    
- Disentangling Dense Embeddings: [https://arxiv.org/pdf/2408.00657](https://arxiv.org/pdf/2408.00657)
    
    “feature families” that represent related concepts at varying levels of abstraction. To
    demonstrate the practical utility of our approach, we show how these interpretable
    features can be used to precisely steer semantic search, allowing for fine-grained
    control over query semantics.
    
- quanitfy number of features to how good they are for steering. is there a correlation?
    - which features of the ones that highly actv are good for steering?

---

Feature splitting across LLMs

- Do they get more similar as they get bigger?
    - However, we find the 1-1 features to still give the best score; this may mean these features are more "canonical" in the LLM or the SAE, as the models both learn them as sae features, rather than splitting them apart.
    - We also utilize these methods to measure the similarity and "trajectories" of feature splitting across models (TBC- define trajectory as x-axis is SAE dictionary size, y-axis is metric).

---

Synth actv for sim metrics

- cluster data: see S3.1 of “Representation Topology Divergence”
- but note that the “highest corr features” not necc are from same cluster!
    - Plot and color those correlated GTF and SAE_A features on a umap. Are they in the same cluster?
- make sure synthetic activations themselves, not just the saes of them, have low jaccard. if not, then they’re not simulating well. each neuron NEEDS to be different in synthetic activations
- so each of the 256 neurons should use diff freqs in terms of decay. that means they cannot be aligned. their stats should be similar to what you find between actual LLMs.
- MMCS cannot be used for perm alignment unless it’s within same model- so we should expect it not to work when we truly simulate two diff LLMs? Then what do we use?
- luke used correlations such that every sample picks corrs according to one of the E groups. so in terms of feature corrs, many samples are similar to one another, if they belong to same group.
- umap hover for LLM_A, LLM_B, and ground truth- match A to GT and B, wlog for B.

- change luke’s code-other
    - add tqdm to sae training, but may use something else for synth actv
    - make decorative changes to new synth actv fn
        - use einops on synth data, split into 2 fns
        - must use batch, else too slow. find diff ways to do batch
        - use typing in args
        - data loader?
        - comment on why use `@dataclass`
        - make sure it gets similar results as old fn
    - make synth data (poss sae too) be part of class wrapper (see CAA rimsky)
        - class wrapper contains multiple actvs
    - make sure all get similar results as old nb
- 100mil samps for cluster data (need to speed up batch proc, else takes 5hrs)
- add to overleaf for later expms
    - some features learned by SAEs aren’t true features (no corr to GTF), though they have high sim to each other- identify these when comparing similarity of feature spaces!
    - plot sim between feature spaces (neigh of discrete features) vs sim of discrete features?
- make sure lin combos of ground truth features are different enough; if too similar, we get datasets that are too similar. Try diff freqs in each model to get properties specific to each LLM
- Features should be meaningful. Why can't hard code meaningful ones? That's synthetic.
    - can we hard code circles in?
- read more about “-taking-features-out-of-superposition-with-sparse”
    - https://www.lesswrong.com/posts/a4oPE4xJqkYSz6jMS/explaining-taking-features-out-of-superposition-with-sparse
    - https://www.lesswrong.com/posts/DezghAd4bdxivEknM/a-small-update-to-the-sparse-coding-interim-research-report
    - https://www.lesswrong.com/posts/8BEJKhgFekvoNEtHv/research-update-sparse-autoencoder-features-are-bimodal
- note which torch structs to pass ‘device’ and ‘dtype’ in to prevent torch incompat
    - dont put in before send code to luke (and dont mention); put in if he suggests

---

Feature Mapping Algorithm

We devise an iterative algorithm to pair features based on similarity score. This algorithm is initialized by pairing features based on the three types of individual pairing similarities. Then it iteratively selects new candidate mappings, and checks if the score is increased. This algorithm allows us to find feature subspaces that are highly similar to each other.

---

### To do- October or later

May also do this in late sept and put it in appendix

Topo: mapper on llm vs saes using opt transp

- mapper on llm vs saes using opt transp
- mapper lens and color fn variations
- use mapper for functional ablation
    - find same months/etc structures?

Contact

- october: msg bricken, sharkey, to ask for ideas and potential collab
    - exploratory expms (incl with TDA)

Train sae on adv models

- find safety features
    - feature for trigger words- ask amir
    - [https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html#assessing-sophisticated-code-error](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html#assessing-sophisticated-code-error)
    - [https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html#safety-relevant](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html#safety-relevant)
    - Use [WMDP](https://www.wmdp.ai/) benchmark as dataset examples?
        - [https://arxiv.org/abs/2403.03218](https://arxiv.org/abs/2403.03218)
- fine tune two adv models from base model using diff datasets, see if they learn similar features? apply sim metrics to them.
    - fine tune own model
        - If you want to tune your own adversarial (if it means unsafe) llm, maybe you can try the redteaming subset of HH-RLHF dataset [https://huggingface.co/datasets/Anthropic/hh-rlhf/tree/main/red-team-attempts](https://huggingface.co/datasets/Anthropic/hh-rlhf/tree/main/red-team-attempts)
        - I asked a friend who are experienced in training adversarial model and he told me that he trained the model using 4chan corpus [https://github.com/niizam/4chan-datasets](https://github.com/niizam/4chan-datasets) . Additionally, he said that just vanilla soft would be enough and no special tricks are necessary.
- relations in diff fine tuned models from 4chan dataset?
    
    

Other sim metrics

- interpolate SAE
    
    [https://discordapp.com/channels/729741769192767510/1153431135414669422/1272249407349329920](https://discordapp.com/channels/729741769192767510/1153431135414669422/1272249407349329920)
    
    ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled.png)
    
- [https://en.wikipedia.org/wiki/Fréchet_inception_distance](https://en.wikipedia.org/wiki/Fr%C3%A9chet_inception_distance)
    
    Rather than directly comparing images pixel by pixel (for example, as done by the [L2 norm](https://en.wikipedia.org/wiki/L2_norm)), the FID compares the mean and standard deviation of the deepest layer in Inception v3. 
    
- [https://en.wikipedia.org/wiki/Wasserstein_metric](https://en.wikipedia.org/wiki/Wasserstein_metric)
- [https://discordapp.com/channels/729741769192767510/1153431135414669422/1268678877497131028](https://discordapp.com/channels/729741769192767510/1153431135414669422/1268678877497131028)
- [https://discordapp.com/channels/729741769192767510/1153431135414669422/1268681876151730264](https://discordapp.com/channels/729741769192767510/1153431135414669422/1268681876151730264)
    - just treating the SAE encodings a sparse vectors then measuring cos distance. nearest neighbors are both changed from the residual stream space as well as from SAE encodings of adjacent layers.
    - This is an expected result for me given feature splitting. You should be able to measure the cos-sim between individual feature's decoder direction, and also measure their joint jaccard sim (ie input similarity). You should be able to find many features that do point in similar directions but activate on disjoint inputs. The "disjoint inputs"/encoder is what determines your hidden activation.
    - You can have two mutually exclusive directions (ie cos-sim=0) read in from the same datapoint. Suppose we have two read-in vectors basis-aligned in 2D. These activate if a feature goes above some bias threshold (supposed it's >3 for both vectors) Then a datapoint of (100,100) will activate both features even though their encoder directions are mutually exclusive.
    - i'm using mutual-knn as my metric. my thinking was that it was possible that the SAE space was just a strange non-linear warping, but perhaps a consistent one. so in addition to looking at the preservation of NNs from residual stream to SAE space, I also wanted to do a quick check of two different SAE spaces. so i used two subsequent layers of residual space which were known to have high mutual-knn (90%+), then encoded both (with separate trained SAEs) into SAE space. But the high mutual knn also was lost in this scenario.
- [**On a Novel Application of Wasserstein-Procrustes for Unsupervised Cross-Lingual Alignment of Embeddings**](https://arxiv.org/html/2007.09456v2)
- https://opensourcemechanistic.slack.com/archives/C06RB35HBDE/p1725567550501229
    
    Yuds
    
    Yuds
    
    [4:19 PM](https://opensourcemechanistic.slack.com/archives/C06RB35HBDE/p1725567550501229)
    
    (Cross-posting from Eleuther's SAE discord channel for more reach, apologies for folks in both communities)I've been trying to figure out what are some intuitions behind qualitative evaluations of SAEs. One of the ways I've been looking at this problem is through geometry, already well explored in existing works.  Is the goal for the features:
    
    - to be more spread out, (not cluster together)
    - while still maintaining minimal reconstruction loss (both on the autoencoder and the LLM output)
    - while having as few dead latents as possible
    
    ?The "more spread out" function is from my reframing of the concept - if a feature vector is composed of latents which more spread out, then we are closer to disentangling the superposed features. Each spread out latent is ... more monosemantic (not atomic) than if the latent was part of a tight cluster.One metric I've seen capture this sense of "geometric interpretability" is MCS histogram (max cosine similarity) /MMCS (mean-max cosine similarity).So our requirement for training an SAE for more interpretability is:
    
    - histogram of MCS spread out (rather than peaky) + low MMCS
    - low FVU
    - low dead latent pct
    
    How does that problem framing sound?
    

Future ideas

- Train sae to capture hier abstract representation by encourage compression loss
- train an SAE on multiple LLM activations that finds the common features between them

[Analogous Steering extras](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Analogous%20Steering%20extras%2096467b547ccb48cb96a94a05cb2aeb7f.md)

- **Cross-Domain Behavior Steering:** [https://docs.google.com/presentation/d/1ZyBKrnS_WgwItOFpDQhuHZHmVAB3MCUGlpod1gSyVlE/edit#slide=id.g2ce4bd20f45_0_676](https://docs.google.com/presentation/d/1ZyBKrnS_WgwItOFpDQhuHZHmVAB3MCUGlpod1gSyVlE/edit#slide=id.g2ce4bd20f45_0_676)
    - find “feature classes” (like the mod 10, or months, used by Gould et al) using Mapper
    - Shared abstract steering effects when ablating features in cluster and cluster continuum relation. May allow for “analogous steering”
        - This is within model and is a discovery by itself, albeit not significant by itself (blog post or interview proj, not paper.) Universally identifying steerable feature structures like f fams but generalized for more effects is paper worthy

---

Read papers

- https://transformer-circuits.pub/2024/july-update/index.html#linear-representations
- [https://transformer-circuits.pub/2022/solu/index.html](https://transformer-circuits.pub/2022/solu/index.html)
    
    In this paper, we report an architectural change which appears to *substantially increase the fraction of MLP neurons which appear to be "interpretable"*
    
- Steering theory
    
    https://x.com/ravfogel/status/1814318728491815228?t=lGO6Hq9IbIoRESoMo72Psw&s=19
    
- SVD: [https://www.apolloresearch.ai/research/the-local-interaction-basis-identifying-computationally-relevant-and-sparsely-interacting-features-in-neural-networks](https://www.apolloresearch.ai/research/the-local-interaction-basis-identifying-computationally-relevant-and-sparsely-interacting-features-in-neural-networks)
- [https://www.lesswrong.com/posts/2roZtSr5TGmLjXMnT/toward-a-mathematical-framework-for-computation-in](https://www.lesswrong.com/posts/2roZtSr5TGmLjXMnT/toward-a-mathematical-framework-for-computation-in)
- Surpassing cosine sim: https://youtu.be/TOo7WE1oSJU?si=can2rSYiIZJsKono

To write

- conclusion: find alignment of “canonical safety-related features” between humans and AI- this is an avenue for alignment

Org notion

if impl succeed (whether neg or pos outcomes), copy todo into here and org into expms:

[Feature actvs on tinystories SAEs](Feature%20actvs%20on%20tinystories%20SAEs%208688850817e34618b8d9347574d66397.md) 

Code

- colab stuck in connecting during active session, refreshing doesn't help

---

TDA to find hier branching of gen to spec 

- hades

What Patterns to look for in Mapper

- mapper on adv exm SAE
- Distinguish different types of data. This comes from llama, this comes from gpt. This is specific to chat, this is specific to base. This is ablated, this is dangerous model.
    - compare mapper on dangerous LLM vs
        - inputs, features
    - list of dangerous/adversarial (fined-tuned, steered) vs safe model types
        - sleeper agents
        - poisoned
            - [https://telefonicatech.com/en/blog/attacks-on-artificial-intelligence-ii-model-poisoning](https://telefonicatech.com/en/blog/attacks-on-artificial-intelligence-ii-model-poisoning)
    - list of changed models
        - base vs chat
    - use similarity metrics + functional on model
        - SAEs measuring ground truth features as a sanity check on if these ‘universally dangerous feature relations’ are bc ground truth of dataset
        - are there canonical ‘ground truth’ dangerous feature RELATIONS?
    - feature splitting on dangerous types- can mapper detect using the SAE?
    - universal patterns in dangerous models vs safe models
        - universal bc “optimal” to represent feature relations this way
        - use feature relations to diagnose universally dangerous patterns
- ask, v1
    
    Hi, I’m looking for different kinds of “safe vs dangerous” models. I saw a paper called [“Visualizing and Analyzing the Topology of Neuron Activations in Deep Adversarial Training”](https://openreview.net/pdf?id=Q692Q3dPMe) that’s about distinguishing safe vs adverarial models using their activation topology. I’m looking to do the same for other types of recent “safe vs dangerous” models (not adversarially trained), but I’m not too familiar with what kinds there are. I’m aiming to extract activations from a base model vs one that has been fine tuned to become dangerous and compare them using a new combination of topological and functional interpretability techniques. 
    
- ask v2
    
    Hi, I’m looking for recommendations for open source pretrained adversarial LLMs (eg. poisoned with backdoors) that have both the base and adversarial version available. I saw a paper called [“Visualizing and Analyzing the Topology of Neuron Activations in Deep Adversarial Training”](https://openreview.net/pdf?id=Q692Q3dPMe) that’s about distinguishing safe vs adverarial models using their activation topology, but that paper uses vision models. I’m curious about trying this for adversarial LLMs. 
    
    I’m aiming to extract activations from a base model vs one that has been fine tuned to become dangerous and compare them using a new combination of topological and functional interpretability techniques. I can also fine-tune an adversarial LLM but I’m not experienced with this and don’t know the best research practices for doing so. 
    
    Also, is “adversarial LLM” the right term for this? I’m wondering about other types of “dangerous vs safe” LLMs that are available or can be feasibly fine tuned in a day or so.
    

- use saes trained on more steps & more ds exmps
- mapper on weights + actvs (actv labels are tokens)
- Look at existing papers to see what to look for
    - focus on interpreting results made by approaches of applied papers (neurosci, medicine, econ), not on theory of how algorithm works
    - put in presentation: a few notes (eg. 3 statements) on what to look for and cite previous papers (topoAct, neuroscience, etc)
    - 3 papers reading list
        - Extracting insights from the shape of complex data using topology: breast cancer, gene, house rep, nba
            - patients that were in Y survived
                - can we ablate those in a certain shape to change output? or conversely, only keep those there to keep output same, as opposed to ablating others?
                - can we identify those in common structure as the “common subspace” between models? are these features in the structure not found in umap?
        - monkey motor cortex: [https://jsseely.com/notes/TDA/](https://jsseely.com/notes/TDA/)
        - topobert: the inputs in a shape were adversarial
- sim scores: hypergraph coopt transp, MSID, geom score
- Find if steering/ablating features in a structure has an effect on output
- Color fns
    - Logit diff on certain output
    - Projection onto featyre, subspace mean, sterring vex, lda direction
    - Hierarchical or abstract concept that can be analogies
        - Find abstract concept and see how specific color with it after projection

why use mapper to find structures:

- steer by changing geometric configuration and observe output. this allows for more predictable steering
- feat fams: hierarchical feature structures with high correlation across datasets

---

umap inteartcitve

- [https://discordapp.com/channels/729741769192767510/1153431135414669422/1271789111430090762](https://discordapp.com/channels/729741769192767510/1153431135414669422/1271789111430090762)
    
    i used a webgl library called regl-scatterplot in my latentscope tool
    
    [https://github.com/enjalot/latent-scope](https://github.com/enjalot/latent-scope)
    
    but it's currently in an experimental branch for bringing SAEs into the process
    

***Figure 4 here (***svelte) contains subplots such that moving on one will move on the others: [https://pair-code.github.io/understanding-umap/](https://pair-code.github.io/understanding-umap/)

---

Ph

- code it and write up

https://youtu.be/5ezFcy9CIWE?si=iXnuCh52RAK3JiqG

https://youtu.be/2PSqWBIrn90?si=9WB9d7GY6mPfFLZg

https://towardsdatascience.com/persistent-homology-with-examples-1974d4b9c3d0

What if 2 struc have same b and d, how are they distinct pts on pers dia?

msg algtop phd/masters students

TDA tuning

- try diff parameters, clustering algo, projection algo (isomap)
- should you normalize data before?
- is edge strength based on num overlapping pts in clusters?

TDA analysis

- map and color corr points in clusters between mapper graphs
- search for features and color clusters across models
- auto find similar subgraphs across models
- label entire subgraphs (like Scaling Monosem)
- What’s the “path distance” from say the “one” community subgraph to the “.” community subgraph across models?

- [place cells: position lays on torus. dont want to end of coord system](https://www.nature.com/articles/s41586-021-04268-7)

[when comparing the similarity of two feature spaces in neural network activations to see if they learn similar feature relations, can we compare the subgraphs of their mapper graphs of their activations or weights?](https://chatgpt.com/c/370df1cc-39da-4416-8d86-15b4caf8d915)

[https://kepler-mapper.scikit-tda.org/en/latest/html-visualization-features.html](https://kepler-mapper.scikit-tda.org/en/latest/html-visualization-features.html)

How come we don't see circular months in umap with number features?

Train on small dataset sith king queen etc to ensure those are captured. Ask gpt etc if this makes sense

[https://dl.acm.org/doi/10.1145/3604433](https://dl.acm.org/doi/10.1145/3604433)

**Visualizing and Interpreting Bias Mitigation Techniques Geometrically for Word Representations**

---

Alt projects

Sim metrics, TDA, and func sim are NOT just for ‘across models’, but for feature splitting WITHIN a model. Map between SAEs. What properties of the manifold / simplicial complex change across feature splitting?

Also, WITHIN an SAE, can map analogous structures (eg. months to days, or king-queen to father-mother). Find similar subspaces within/across layers, mapping how they change over layers or during training.

(future work): These sim metrics / topological properties, once found and studied, may be used in loss functions to optimize the model towards learning certain beneficial topological arrangements

- cross-model feature subspace patching / model stitching

https://www.alignmentforum.org/posts/baJyjpktzmcmRfosq/stitching-saes-of-different-sizes

https://www.reddit.com/r/MachineLearning/s/dJhzCSX93r

Llms hallucinate alike

Train SAEs to learn specific, separate royal family features

- PLAN: our tools (corr, dataset exmps, umap, etc) have been shown to work. now, we need better datasets and models that show fs
    - once get better saes with fs concepts, color code multiple concepts- king queen princess- and check their relations across models
        - train on that specific data, on large sae, to ensure it learns them separately
- is top 5 tokens enough? maybe autolabel multiple. note that gpt4 fails at this. try paid cluade

---

UMAP

- umap plot pretrained gpt2 fs- sanity check, should match neuronpedia
- plot corr actv plots for feature split (or corr features)
- how to detect feature splitting, not just from umaps
    - get top 10 more corr from A to B, vice versa
- take most similar vectors and autolabel how similar their dataset examples are, rather than doing it manually
    - without chatgpt: +1 to score if contains same token in top 5, OR get how many of their top 5 tokens have same tokens
- in actv corr plot, show the dataset examples when hovering that are nonzero
- given corr feature pair, zoom-in on the umap of both
- compare MLP 1
- compare tinystories gpt2 to pretrained gpt2
- 🐣 neuronpedia: you can download the labels for their pretrained to use it yourself

[https://transformer-circuits.pub/2024/scaling-monosemanticity/umap.html](https://transformer-circuits.pub/2024/scaling-monosemanticity/umap.html)

[https://chatgpt.com/c/6b6bce5a-43c5-4b4e-8207-49d259712e4b](https://chatgpt.com/c/6b6bce5a-43c5-4b4e-8207-49d259712e4b)

Repr Sim

- before using cca, filter out features better
- mutual NN on weights and actvs? no; can only do on inputs (tokens)
    - if pts are features, perhaps we can’t use mnn. only makes sense if we plot the tokens in a projected down feature space.
        - indeed, algtop was applied on input pts, NOT neurons as pts! same with activation atlas!
- can cka be done on unpaired points in space? cca can, but mnn needs points that correspond to same input
    
    [https://claude.ai/chat/ef520765-10d0-4aed-8087-eaab5947af59](https://claude.ai/chat/ef520765-10d0-4aed-8087-eaab5947af59)
    
    [https://chatgpt.com/c/0f959dee-0a79-4333-b14d-8d0b130b658e](https://chatgpt.com/c/0f959dee-0a79-4333-b14d-8d0b130b658e)
    
    chatgpt is WRONG; it says cca needs paired. claude says doesn’t need paired.
    
- ask huh about why use knn over cka

- ISSUE: you’re including that feature as “activating on” that keyword if it contains it. But perhaps the majority of the top 5 (or top 10) should contain it

- use multiple keywords, each with different color
- instead of color, put a label box around the points in each plot

- in a box outside plot, display the other model’s pair
- compare subspace scores to random subspace pairs. ask chatgpt for how to better stat tests
- Then, higher-order graphs of keyword subspaces. It’s not enough to just plot the subspace of Dragon to subspace of Dragon; it’s the subspace of {Dragon, Princess}, as that’s relation of Dragon to Princess. Or {he, she}

- [I understand negative correlation between two variables. But what does negative CCA mean between two spaces of datapoints?](https://chatgpt.com/c/00acbbcb-2454-4246-a90c-33a4de7067e4)
    
    Canonical Correlation Analysis (CCA) is a method used to understand the relationship between two sets of multidimensional variables. When we talk about a negative canonical correlation, we're referring to the relationship between linear combinations of these sets of variables. Let's break this down:
    
    1. **CCA Basics**: In CCA, we have two sets of variables (let's call them \(\mathbf{X}\) and \(\mathbf{Y}\)). The goal of CCA is to find linear combinations of \(\mathbf{X}\) and \(\mathbf{Y}\) that are maximally correlated. Specifically, we seek vectors \( \mathbf{a} \) and \( \mathbf{b} \) such that the correlation between \( \mathbf{a}^T \mathbf{X} \) and \( \mathbf{b}^T \mathbf{Y} \) is maximized.
    2. **Canonical Correlation**: The canonical correlation is the correlation coefficient between these linear combinations. This correlation can be positive or negative. A positive canonical correlation indicates that when one set of variables increases, the other set tends to increase as well. Conversely, a negative canonical correlation indicates that when one set of variables increases, the other set tends to decrease.
    3. **Negative Canonical Correlation**:
        - When the canonical correlation is negative, it implies an inverse relationship between the linear combinations of the two sets of variables. In other words, the higher values of the linear combination of one set of variables (\(\mathbf{a}^T \mathbf{X}\)) are associated with lower values of the linear combination of the other set (\(\mathbf{b}^T \mathbf{Y}\)), and vice versa.
        - For example, if \(\mathbf{a}^T \mathbf{X}\) represents a particular weighted sum of the variables in \(\mathbf{X}\) and \(\mathbf{b}^T \mathbf{Y}\) represents a weighted sum of the variables in \(\mathbf{Y}\), a negative canonical correlation would mean that when the weighted sum in \(\mathbf{X}\) increases, the weighted sum in \(\mathbf{Y}\) tends to decrease.
    4. **Interpretation**: In practical terms, a negative canonical correlation suggests that there is an inverse relationship between certain linear features of the two datasets. Understanding this can help in fields such as finance (e.g., where one portfolio might hedge against another), biology (e.g., where certain gene expressions might inversely relate to others), and more.
    
    ### Example
    
    Suppose we have two sets of variables:
    
    - \(\mathbf{X}\): Economic indicators (e.g., interest rates, unemployment rates, GDP growth).
    - \(\mathbf{Y}\): Stock market indicators (e.g., stock prices, market indices, trading volumes).
    
    If we perform CCA and find a negative canonical correlation, it could mean that a particular linear combination of economic indicators (e.g., a scenario where interest rates and unemployment rates are high) is inversely related to a linear combination of stock market indicators (e.g., lower stock prices and trading volumes).
    
    In summary, negative CCA means that there is an inverse relationship between the optimal linear combinations of the two datasets, indicating that as one combination increases, the other tends to decrease. This can provide insights into the underlying structure and relationship between the two sets of variables.
    
- CCA and CKA on this feature subspace compared to other parts
    - the features in fairy tale subspace (is this too big of a subspace?)
    - use examples that are snippets specific to that subset
        - [https://chatgpt.com/c/1ed23e8e-b0a6-47b9-a3b4-1af35af41378](https://chatgpt.com/c/1ed23e8e-b0a6-47b9-a3b4-1af35af41378)
    - compare to random subspaces
    - compare to all of neuron (orignial LLM) space
    - CKA has issues; ask Huh et al if they use KNN over CKA bc over sensitivity of inputs (changing just one input can make repr be 0)
- search for token will highlight all features on both plots that activate on that token
- label clusters in umap, and map by sim across models
- compare feature-splitting features  on same umap like Towards M
    - use different dataset examples

[https://online.stat.psu.edu/stat505/book/export/html/682](https://online.stat.psu.edu/stat505/book/export/html/682)

---

Misc

- the feature mapping from A to B is the same as B to A bc corr matrix is symmetric

- search by featureID to highlight and zoom in on umap
- claude/gpt4 takes in neuronpedia html and reveng its gui

https://www.alignmentforum.org/posts/fmwk6qxrpW8d4jvbd/saes-usually-transfer-between-base-and-chat-models

- ISSUE: 2L MLP0 sae has many redundant feature neurons that all fire the same!
- find what are the tokens that are 0 in A but nonzero varying in B
    - Model B’s feature appears to fire on more tokens, possibly because it captures more concepts. That is, while these tokens are 0 in model A (1L-21M)’s feature 16251, model B (2L-33M)’s feature 3301 is nonzero for them.

- In 1L, there is no res stream, but in ≥ 2L, can train on other layers than MLP out like res stream

- for labeled umap decoder weights, how do labels change before and after steering?
- label features in mapper plot

Not really feature specific to daughter. Perhaps we can use feature splitting to constrain it to specifically fire for daughter?

- find related story features
    - get sentences just about: she-he-it
    - get sentences just about: princess-dragon-knight

---

[https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/neuro.06.004.2008/full](https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/neuro.06.004.2008/full)

[https://neuroai.neuromatch.io/tutorials/W1D3_ComparingArtificialAndBiologicalNetworks/student/W1D3_Tutorial1.html#](https://neuroai.neuromatch.io/tutorials/W1D3_ComparingArtificialAndBiologicalNetworks/student/W1D3_Tutorial1.html#)

[https://johnmarktaylor.com/research/](https://johnmarktaylor.com/research/)

https://arxiv.org/abs/2210.16156

https://datumorphism.leima.is/cards/machine-learning/measurement/centered-kernel-alignment/

https://openreview.net/forum?id=8HRvyxc606

https://medium.com/syncedreview/geoffrey-hinton-leads-google-brain-representation-similarity-index-research-aiming-to-understand-b5d14bf77f49

[https://www.youtube.com/watch?v=zZAj8uvr308&ab_channel=IEEESignalProcessingSociety](https://www.youtube.com/watch?v=zZAj8uvr308&ab_channel=IEEESignalProcessingSociety)

[https://www.damtp.cam.ac.uk/research/cia/files/teaching/Optimal_Transport_Notes.pdf](https://www.damtp.cam.ac.uk/research/cia/files/teaching/Optimal_Transport_Notes.pdf)

[https://openreview.net/pdf?id=ByxlnrBeLH](https://openreview.net/pdf?id=ByxlnrBeLH)

- [what's the difference between radius graph and simplicial complex to approximate manifold](https://chatgpt.com/c/895a75e2-9553-41c9-afe0-596ddd733bee)

should we average feature splitting sae instances?

How common are the same analogous patterns for the same dataset? Across datasets? Measure this

- ask chatgpt for help in defining feature manifold. give it overleaf so far

https://chatgpt.com/c/c50f49db-ff6f-4133-83a5-21593d3a2383

Sc manifold

https://youtu.be/wuqTOoKeVWw?si=VnrcVX2h82JH_Slo

Cka

https://youtu.be/uj0uQyJcrxY?si=Rv76ksM2mhzlc9bw

Transfer features 

- read: Not All Language Model Features Are Linear
    
    [https://chatgpt.com/c/d908b8ff-4c84-4002-a198-80956bdd7bd6](https://chatgpt.com/c/d908b8ff-4c84-4002-a198-80956bdd7bd6)
    
    - if the elements in the plot given from the paper are weights, how are the labels like Monday derived?
        
        The labels like "Monday" in the PCA plot are derived from the specific clustering of dictionary elements corresponding to days of the week, as discovered through the use of sparse autoencoders (SAEs) on language model hidden states. Here's a step-by-step explanation of the process:
        
        1. **Sparse Autoencoders (SAEs)**: SAEs are trained to decompose model hidden states into sparse vector sums from an over-complete basis. This means they can identify dictionary elements (features) that are activated by the model.
        2. **Clustering**: The dictionary elements identified by the SAEs are clustered based on their pairwise cosine similarity or Jaccard similarity. This clustering helps in grouping together elements that represent similar concepts or features.
        3. **Multi-dimensional Features**: The clusters that emerge from this process often represent multi-dimensional features, such as the circular patterns observed for days of the week. These clusters are then analyzed to ensure they are not mixtures or separable into lower-dimensional features, making them irreducible multi-dimensional features.
        4. **Interpretation**: Each cluster is interpreted and labeled according to the tokens that predominantly activate the dictionary elements in that cluster. For example, a cluster of dictionary elements that are primarily activated by tokens corresponding to "Monday" will be labeled as such.
        5. **Visualization with PCA**: PCA is used to reduce the dimensionality of these multi-dimensional features for visualization purposes. The resulting plot shows distinct clusters corresponding to the days of the week, which are labeled accordingly.
        
        In summary, the labels like "Monday" are derived by clustering the dictionary elements found by SAEs, which are then analyzed and interpreted based on the tokens that activate them, and visualized using PCA to show the circular representation of the days of the week.
        
    - cite the lines in the paper  that made you derive:
        
        The lines in the paper that support the interpretation and labeling of clusters according to the tokens that predominantly activate the dictionary elements in that cluster are:
        
        1. "This suggests a natural approach to using sparse autoencoders to search for irreducible multi-dimensional features:
            1. Cluster dictionary elements by their pairwise cosine similarity or Jaccard similarity.
            2. For each cluster, run the SAEs on all xi,l ∈ Xi,l and ablate all dictionary elements not in the cluster. This will give the reconstruction of each xi,l restricted to the cluster found in step 1 (if no cluster dictionary elements are non-zero for a given point, we ignore the point).
            3. Examine the resulting reconstructed activation vectors for irreducible multi-dimensional features, especially ensuring that the reconstruction is not separable. This step can be done manually by visually inspecting the PCA projections for known irreducible multi-dimensional structures (e.g. circles, see Fig. 2) or automatically by passing the PCA projections to the tests for Definition 3"【9:0†source】.
        2. "As described in Section 4, given a cluster of dictionary elements S ⊂ {1, . . . ,m}, we run a large set of activations through the SAE, then filter out samples which don’t activate any element in S. For samples which do activate an element of S, reconstruct the activation while setting all SAE features not in S to have a hidden activation of zero. If some collection of SAE features together represent some irreducible feature, we want to remove all other features from the activation vector, and so we only allow SAE features in the collection to participate in reconstructing the input activation"【9:2†source】.
        
        These lines explain the process of clustering dictionary elements based on their similarities and then reconstructing activations to identify and label irreducible multi-dimensional features.
        
    - cite pics
        
        ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%201.png)
        
        ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%202.png)
        

**generalize this procedure to find other structures: ablate by clusters (elements in simplices)**

Observe steering diffs on split features

Steer nonlinear months

Mapping algo: map based on both repr and func sim. May be a diffeomorphism or some other type of deformation mapping?

- toy model 20B token train feas
    
    ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%203.png)
    

Questions

Why decoder weights are dictionary elements, not encoder

---

- to get LLM actvs, stream process LLM actvs on batch at a time, not loading entire dataset and passing into batch. same with SAEs. Do this to obtain feature acts for each batch_seq token.

[https://transformer-circuits.pub/2023/monosemantic-features#discussion-token-in-context](https://transformer-circuits.pub/2023/monosemantic-features#discussion-token-in-context)

this contains unanswered ques about [‘compositional codes’](https://transformer-circuits.pub/2023/superposition-composition/index.html#distributed-compositional)

[https://transformer-circuits.pub/2023/may-update/index.html#feature-manifolds](https://transformer-circuits.pub/2023/may-update/index.html#feature-manifolds)

what is length scale?

[https://transformer-circuits.pub/2024/june-update/index.html#multidimensional-features](https://transformer-circuits.pub/2024/june-update/index.html#multidimensional-features)

how many data pts does plot in Towards Monosem use?

ALgo to check if subspace is similar by matching one feature at a time and checking local score, then merging. Approx manifold using simplex

---

ISSUE: with arch sim. We expect same layer to have same features. That's the sanity check.

The issue is mapping features. Are they arranged in the same way?

https://chatgpt.com/c/8a2f7e89-5938-4dbd-88bb-2f031d88db16

At what point is feature splitting too dissimilar or does it get even more similar in certain subspace or feature groups?

Train sae to map between two models using cka loss. Finds features that both models have.

Ask to brainstorm ideas during meeting

https://youtu.be/TBjdvjdS2KM?si=KWVxjYkaNKmVSeVA

Use sim measures to diagnose healthy vs Wrong nn

Very wide network means all layers similar

We don't expect networks to have same exact features but they do have the same steering vectors and months representations. So something is similar. Can we find mappings?

---

- find tinystories across models with good features
    - map top 5 based on actv sim (corr and/OR cosine sim matrix)
    - manually look at pairs with high corr and use dataset examples to label them
- umap + cca on new saes of tinystories
    - actvs or weights in hinton paper? they’re actvs bc use exampls

- train saes at diff layers for multiple ts models ; then feature actv map & umap cca

---

- neg results: need to improve saes, or try diff layers, or try diff models
    - or could mean saes aren’t universal for certain cases. which cases? impt to know in order to figure out what could generalize
    - generalize: good for transfer learning, and using one model to predict another model’s landscape (eg. if mostly similar, can use one as a ‘map’ to guess impt steerable features of another model instead of needing to find them by trial/error)

⚠️ you can also just use Neuronpedia feature dashboards

- wandb metrics
- compile list of training tips from various resources
    - https://www.lesswrong.com/posts/FSTRedtjuHa4Gfdbr/attention-saes-scale-to-gpt-2-small
        - L0 norm changes at each layer of res stream
- Ask on MI, eluther, ARENA discord + slack for advice or pair prog for training SAEs
    - state have nb (may post it) or just state results
    - did X, etc. can it be even faster?
- ask others about comparing tokens of models with different tokenizers
- VPN

---

Multiple feature circuits

- are those features in a cluster/subgraph involved as a single component in a circuit?

---

### Future work

- **IMPT:** Within-models: also use cca on activations for analogous domains. this shows the abstract structure has “analogous” mappings from one domain to another. Like months and numbers.
    - LEVEL 1: The category is a higher-order structure (circles, simplices, etc)
        - Higher-order structures can just be pair-wise (2-simplex) relation between features (with “analogous” roles). This can be distance, or causal. 3-simplex: “father-mother-daughter”
            - each object is a cluster of points, or the LDA vector est of the cluster
            - Each edge is a vector addition or difference?
        - A simplex approximates a manifold subspace. So categories are subspaces.
    - LEVEL 2: The functor is a mapping between higher-order structures WITHIN-MODEL
        - Not just any triangle. But the idea that “man-woman-child” can be encoded in BOTH “king-queen-princess” and “father-mother-daughter”. Both contain this “man-woman-child” basis, and CCA may map these CVs. This “man-woman-child” is the common abstraction, or functor mapping, between the two categories.
            - The functor IS the analogy
        - If month clusters are arranged circularly, how are numbers mapped with them?
            - each data pt isn’t a month, but a feature weight (not actv)
        - Do circuits compose the functor structure with more specific features?
            - Might require several transformations into a space that cleanly shows this
    - LEVEL 3: The “natural transformation” maps functors (of structures) between models.
        - This shows universality of analogies, and how models converge to them

- cca intuition
    
    https://chatgpt.com/c/e7f60612-f476-4019-825e-d1d6f843748b
    
    CCA finds lin combo of features with highest correlation 
    
    So in cca say features man woman child, and father mother daughter, or king queen princess, are most correlated? Analogous?
    
    In cca can you find which combos map to each other, say if man woman maps to king queen, by coefficients basis
    
    So from cca coefficients can we get mapping of features to features based on their relns
    
    Not just two cv
    

https://chatgpt.com/c/cbecf63f-fe30-4804-a3a2-ae4cee00627d

Sparsity norms

Pretrained SAES: [https://github.com/EleutherAI/sae](https://github.com/EleutherAI/sae)

[https://wandb.ai/eleutherai/sae/runs/k1kn6lst?nw=nwusernorabelrose](https://wandb.ai/eleutherai/sae/runs/k1kn6lst?nw=nwusernorabelrose)

Train

- ask neuronpedia on advice for sae training

https://github.com/jbloomAus/SAELens/issues/191

[https://www.lesswrong.com/posts/5XmxmszdjzBQzqpmz/interpreting-preference-models-w-sparse-autoencoders](https://www.lesswrong.com/posts/5XmxmszdjzBQzqpmz/interpreting-preference-models-w-sparse-autoencoders)

can feasibly train saes on: tinystories (up to 4L), gpt2

[https://www.lesswrong.com/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream](https://www.lesswrong.com/posts/f9EgfLSurAiqRJySD/open-source-sparse-autoencoders-for-all-residual-stream)

- what's the estimated cost for training effective saes for all layers of gpt-2 medium?
    
    [https://chatgpt.com/c/78867e7f-511e-4a8d-b5fd-c05473c92f99](https://chatgpt.com/c/78867e7f-511e-4a8d-b5fd-c05473c92f99)
    

<<<

Compare

- compare actvs using narrow dataset (eg. only Arabic)

Feature space across models should be more similar than their neuron spaces

we’re not looking for true features based on below’s def, but similar representations that can transfer

[https://www.lesswrong.com/posts/QoR8noAB3Mp2KBA4B/do-sparse-autoencoders-find-true-features](https://www.lesswrong.com/posts/QoR8noAB3Mp2KBA4B/do-sparse-autoencoders-find-true-features)

https://youtu.be/TBjdvjdS2KM?si=moubTttOGY5hvCcK

Sim of nn lecture questions

https://chatgpt.com/c/d8492b87-728f-4abb-8bd5-3e4a9c522ec1

What was the impact of similarities of neural networks by Hinton? If it found models with different archs had same representations, did it allow generalizing features from one model to another? What important things did this paper lead to? How about its relation to mech interp?

Is it impactful to use their methods to compare feature representation spaces of sparse autoencoders trained on activations of different models? Or would the findings already br known from Hintons work?

Issue is next token, not input token. But try ones where both tokenizers use one tokens 

- matrix plot of cca for layer-layer similarity

[https://www.lesswrong.com/posts/FSTRedtjuHa4Gfdbr/attention-saes-scale-to-gpt-2-small](https://www.lesswrong.com/posts/FSTRedtjuHa4Gfdbr/attention-saes-scale-to-gpt-2-small)

This finds feature families. how similar are they across models?

[https://colab.research.google.com/drive/1hZVEM6drJNsopLRd7hKajp_2v6mm_p70?usp=sharing](https://colab.research.google.com/drive/1hZVEM6drJNsopLRd7hKajp_2v6mm_p70?usp=sharing)

This also has automated detection of feature families

[https://chatgpt.com/c/0faedc73-4b92-414b-b1d4-6ade923255df](https://chatgpt.com/c/0faedc73-4b92-414b-b1d4-6ade923255df)

- explain the L0 norm col of the table in:
    
    The "L0 norm" column in the table refers to the number of non-zero coefficients in the sparse autoencoder (SAE) representations. In this context, a lower L0 norm indicates that fewer features are being used to represent the data, which aligns with the goal of sparsity. Sparse representations are desirable as they make the model more interpretable by emphasizing the most important features. The table shows the L0 norm for different layers, indicating how many features are active in each layer after training the SAEs.
    

Don’t just focus on similarities; focus on differences. What parts are common to many, and how much is different?

Mapping clusters or higher-order structures is like mapping the subspaces

We’re also mapping circuits, which is not by geometry. And mapping steering vectors associated with circuits. DO the steering vecs and circuits map togther?

sum of contributions then unembed pca. heart higher-order structures: [https://neuralblog.github.io/logit-prisms/](https://neuralblog.github.io/logit-prisms/)

scaling monose actv plots explained:

[https://www.youtube.com/watch?v=8Nyn3_ZWa_U&t=721s&ab_channel=TheInsideView](https://www.youtube.com/watch?v=8Nyn3_ZWa_U&t=721s&ab_channel=TheInsideView)

<<<

- project proposal: (timestamped, ask fazl first before send to others)
    
    To show: Kiho, Bloom, Conmy, Trenton
    
    only reveal more novel (higher order, mapping, FS, etc) after initial meetings
    
    give expms code so far, and in email for initial meeting say have more novel approaches that can discuss later
    
    - experiments done so far
        - sae training setup (ghost grads, wandb, colab, torrnodes, etc)
            - feature splitting on gpt-tinystories
            - more than 2 models
        - why use CKA, etc.
        - higher-order structures and TDA
        - node mapping (reproduce Anthropic)
    - next steps: in-scope list of (justified) ideas and concrete plan to enact them
        - toy model (diff rand init): many saes
        - edge mapping algorithm (high-lvl; state details not shown here)
    - out-of-scope future work
        - analogous steering

- people to contact:
    
    (towards / scaling anthropic papers)
    
    ask fazl beforehand to ensure timestamp (no work leaks) [he knows who can be trusted as if they have incentive to not steal his work]
    
    8/20, code base distr sys: [https://boards.greenhouse.io/anthropic/jobs/4020305008](https://boards.greenhouse.io/anthropic/jobs/4020305008)
    
    - josh batson
        
        [https://www.youtube.com/watch?v=sQar5NNGbw4&ab_channel=Anthropic](https://www.youtube.com/watch?v=sQar5NNGbw4&ab_channel=Anthropic)
        
    - [https://www.trentonbricken.com/about/](https://www.trentonbricken.com/about/)
        - [https://www.youtube.com/watch?v=UTuuTTnjxMQ&ab_channel=DwarkeshPatel](https://www.youtube.com/watch?v=UTuuTTnjxMQ&ab_channel=DwarkeshPatel)
    - callum

- contact anthropic
    - started in july
    - they cite SVCCA. So they must’ve tried it. once you try your obvious cca approaches, ask them what issues there were with it, and if any issues with yours.
        - compare approaches; give pros/cons each
    - show them the mapping of higher order structures and working with kiho
        - eg) do they both arrange months circular? what other circulars found by algo?
            - can we map the circular structures?
    - toy model feature splitting: give cost estimates of llm and sae training
    - complexity of mapping algorithms

<<<

1. assumps + parameters for sim code for between saes
2. train saes on toy model
    1. get neuronpedia / eleuther to do this
    2. look for feature splitting
3. in another layer, track how a specific set of features (eg. love or cat) changes after steering
- funcsim: are two features across models also connected to analogous features in later layers?
- can you compare ground truth features as the intermediary? no- the "ground truth features" are model specific right, so it wouldn't make sense to see if two diff LLMs are learning the same ground truth feature
- train a model to map between features from two saes

<<<

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
    

---

Steering circuits

- Probes to obtain “analogous steering vectors” across domains- apply these and observe the geometry
    - across models, find feature relation patterns that ‘explain’ analogous steering
    - the higher-order structures you find may be the  steerable “abstraction” common to a domain that you can extract and combine (eg. months with ordinal) from specific examples
    - or save for future paper
- [**Anthropic Beta Steering API**](https://docs.google.com/forms/d/e/1FAIpQLSc9HRcRFOdid4NJ4-Lyo3HdUybbevMqERWscJIbqilLQRuSQA/viewform)
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

- Method to reduce dead neurons using loss constraints which force learned wright's to have activations be within useful feature range
- Steering is by prompts, not model. CMAP is by model. Compare them.
- [https://apartresearch.com/project/from-sparse-to-dense-refining-the-machiavelli-benchmark-for-real-world-ai-safety](https://apartresearch.com/project/from-sparse-to-dense-refining-the-machiavelli-benchmark-for-real-world-ai-safety)
- Study: https://github.com/nrimsky/CAA
    - is it 3rd last b/c adds end of seq token somehow in some operation? Find this operation
    

instead of deleting file, transfer new code into shared nb by deleting all old cells and pasting new ones from ‘select all’