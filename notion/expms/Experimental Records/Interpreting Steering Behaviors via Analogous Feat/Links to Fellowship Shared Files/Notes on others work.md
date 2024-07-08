# Notes on others work

constantin: venhoff00@gmail.com

Organize edge values so edges are white to red instead of threshold to display

Edges on attr patch plot

32 next prediction tokens in future. 32 final hidden states. Just keep running it. Euclidean dist mean of 32, then compare before and after ablation 

---

tingchen proj: just dpo or ppo variant is enough? llama expms for attack. tuning model using rlhf to eval robustness to attacks

minseon: safety direction gradeint exists?

---

[Clement work](Notes%20on%20others%20work%2032c6237809ea4e50a6102ed46f67b259/Clement%20work%20164617a8fb7145029b828ee403b31a24.md)

If bias exists in frozen embedding,  doctor closer to man in woman, is there inherent bias in clip output?

Used to br frozen text and frozen img then just train Bridge. But now is training end to end, not separate img and txt models. Chameleon meta

[Multimodal interp notes](Notes%20on%20others%20work%2032c6237809ea4e50a6102ed46f67b259/Multimodal%20interp%20notes%2046f2ab3a3b3642d2b1d09e8c1c9608bc.md)

text is in hypersphere bc loss (and layer norm?)

if normalize image, will it break?

layer to layer, they get closer

norms of text and img are diff; use soft prompts. init so different, but they seem to merge over time. use logit lens. embeddings settle into hypersphere, but grad descent doesnt need to work in hypersphere (no constraint). clip takes cls from img and txt, but patch tokens aren’t in img models. initially out of distribution, but do they converge over layers of model. 

[https://www.lesswrong.com/posts/qvWP3aBDBaqXvPNhS/gpt-2-s-positional-embedding-matrix-is-a-helix](https://www.lesswrong.com/posts/qvWP3aBDBaqXvPNhS/gpt-2-s-positional-embedding-matrix-is-a-helix)

- if do pca on embedding space, does it normalize?
    
    [https://stats.stackexchange.com/questions/189822/how-does-centering-make-a-difference-in-pca-for-svd-and-eigen-decomposition](https://stats.stackexchange.com/questions/189822/how-does-centering-make-a-difference-in-pca-for-svd-and-eigen-decomposition)
    
    PCA, SVD, and Centering of Data
    
    PCA centers data to compute cov matrix, but it doesn’t normalize data beforehand. Should normalize beforehand
    
    PCA (Principal Component Analysis) involves steps that handle normalization and centering, which are crucial for its proper functioning:
    
    1. **Normalization**: PCA itself does not automatically normalize the data. Normalization (or scaling) typically means adjusting the data so that each feature contributes equally to the analysis. This is especially important when features have different units or scales. Normalization can be achieved by scaling each feature to have unit variance. This is commonly done using standard scaling (subtracting the mean and dividing by the standard deviation for each feature). However, PCA does not include this as an intrinsic step, so it needs to be done beforehand if necessary.
    2. **Centering the Data**: PCA does include centering as an intrinsic part of its process. Centering means subtracting the mean of each feature so that the data has a mean of zero. This step is essential for PCA because it relies on the covariance matrix, and centering ensures that the first principal component describes the direction of maximum variance.
    
    **Centering Covariance**: When constructing the covariance matrix for PCA, centering the data ensures that the covariance matrix accurately reflects the variances and covariances among the features. The covariance matrix is computed as:
    
    \[ \text{Cov}(X) = \frac{1}{n-1} (X - \bar{X})^T (X - \bar{X}) \]
    
    Where \( X \) is the data matrix and \( \bar{X} \) is the mean of the data. Centering ensures that \(\bar{X}\) is zero, thus simplifying the covariance calculation to:
    
    \[ \text{Cov}(X) = \frac{1}{n-1} X^T X \]
    
    In summary:
    
    - PCA does not automatically normalize the data; normalization should be performed beforehand if needed.
    - PCA does include centering the data as part of its process, ensuring the covariance matrix is correctly computed.
- why normalize
    
    Normalization is an important preprocessing step in many data analysis and machine learning tasks, including PCA, for several reasons:
    
    1. **Equal Contribution of Features**: When features have different units or scales, those with larger scales can dominate the PCA results, leading to biased principal components. Normalization ensures that all features contribute equally to the analysis.
    2. **Improving Convergence**: For machine learning algorithms, especially those involving gradient descent, normalization can help improve the speed and stability of convergence.
    3. **Meaningful Distance Measurements**: Many algorithms (e.g., k-means clustering, nearest neighbors) rely on distance measures. Normalization ensures that the distance between features is meaningful and not dominated by features with larger scales.
    4. **Avoiding Numerical Issues**: Large differences in feature scales can lead to numerical instability in calculations, potentially causing algorithms to produce inaccurate results.
    
    ### Common Normalization Techniques
    
    1. **Standard Scaling (Z-score Normalization)**:
        - Centers the data by subtracting the mean of each feature and scales it by dividing by the standard deviation.
        - Formula: \( z = \frac{x - \mu}{\sigma} \)
        - Ensures each feature has a mean of 0 and a standard deviation of 1.
    2. **Min-Max Scaling**:
        - Scales the data to a fixed range, typically [0, 1].
        - Formula: \( z = \frac{x - \min(x)}{\max(x) - \min(x)} \)
        - Useful when the data needs to be in a specific range.
    3. **Max Abs Scaling**:
        - Scales each feature by its maximum absolute value.
        - Formula: \( z = \frac{x}{\max(|x|)} \)
        - Ensures the values lie within the range [-1, 1].
    
    ### Example: PCA with and without Normalization
    
    Consider a dataset with two features: height (in cm) and weight (in kg). If we perform PCA without normalization, the feature with the larger variance (weight, in this case, assuming larger absolute values) will dominate the principal components, potentially masking the contributions of height.
    
    By normalizing both features to have unit variance (standard scaling), we ensure that both height and weight contribute equally to the PCA, leading to more balanced and interpretable principal components.
    
    ### Summary
    
    Normalization is crucial when the features in your data have different scales or units. It ensures that all features contribute equally to the analysis, leading to more accurate and interpretable results. While PCA inherently centers the data by subtracting the mean, it does not automatically normalize the data, so this step must be performed separately when needed.
    
- why normalize embedding space before plotting pca for transformers
    
    Normalizing the embedding space before applying PCA for visualization purposes, especially in the context of transformers and other high-dimensional embedding models, is important for several reasons:
    
    ### 1. **Equal Contribution of Dimensions**:
    
    Embeddings from transformers often have high-dimensional spaces with varying scales across different dimensions. Normalizing ensures that each dimension contributes equally to the PCA, preventing dimensions with larger scales from dominating the principal components.
    
    ### 2. **Improving Interpretability**:
    
    Normalization can make the resulting PCA plots more interpretable. Without normalization, the principal components might reflect the scale of the dimensions rather than the actual structure or relationships in the data. Normalization helps reveal the true patterns and relationships within the embedding space.
    
    ### 3. **Mitigating Effects of Outliers**:
    
    Embeddings can sometimes have outliers or dimensions with significantly higher values. Normalization reduces the impact of these outliers, ensuring that the PCA captures the overall structure of the data rather than being skewed by extreme values.
    
    ### 4. **Consistent Distance Measurements**:
    
    Normalization ensures that the Euclidean distances between data points in the embedding space are meaningful. This is crucial for PCA, as it relies on distances and variances to compute principal components. Normalized embeddings lead to more accurate and meaningful PCA results.
    
    ### 5. **Handling Different Magnitudes**:
    
    Different dimensions in embeddings might represent features with inherently different magnitudes. For example, one dimension might capture frequency of word occurrence while another captures syntactic structure. Normalization puts all dimensions on a common scale, facilitating a more balanced analysis.
    
    ### Practical Steps for Normalizing Embedding Space
    
    1. **Standard Scaling**:
        - Subtract the mean and divide by the standard deviation for each dimension.
        - Ensures each dimension has a mean of 0 and a standard deviation of 1.
    2. **Min-Max Scaling**:
        - Scale each dimension to a range [0, 1] or [-1, 1].
        - Useful for ensuring all dimensions have a consistent range.
    
    ### Example Workflow
    
    1. **Extract Embeddings**: Obtain the high-dimensional embeddings from the transformer model.
    2. **Normalize**: Apply standard scaling or min-max scaling to the embeddings.
    3. **Apply PCA**: Perform PCA on the normalized embeddings to reduce dimensionality to 2 or 3 principal components.
    4. **Plot**: Visualize the principal components to understand the structure and relationships in the embedding space.
    
    ### Summary
    
    Normalizing the embedding space before applying PCA ensures that each dimension contributes equally to the analysis, resulting in more accurate and interpretable visualizations. It mitigates the effects of varying scales, outliers, and different magnitudes across dimensions, ultimately providing a clearer picture of the underlying structure in the high-dimensional embedding space.