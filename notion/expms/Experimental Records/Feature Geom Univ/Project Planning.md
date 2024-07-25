# Project Planning

[Done](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Done%201c002201437341e48b55b8276859a632.md)

---

### Working on

Feature Relation Mapping Expms

- ⚠️ **EXPM:** UMAP side by side hovering pairs in flask
    - ✅ miniconda: `conda create --name umap`
        - `pip install flask umap-learn numpy scikit-learn`
    
    …\localfiles_own\umap_flask
    
    - ✅ in Step 2: Prepare Your Python Script (Backend)
    how do i make a flask app? just a file? detailed steps more
        
        
    - ✅ after `python app.py`, in browser open [`http://127.0.0.1:5000`](http://127.0.0.1:5000) to see plots
    - ✅ load embeddings and indices downloaded from colab (store in data folder)
    - ⚠️ debug why flask doesnt work
        
        this flask app doesn't show the plots side by side horizontally AND it's not highlighting the tokens, and using a feature map list such that the index in the list is the feature index in right plot and the value is feature index in left plot, such that the paired feature indices points in both plots are highlighted and display label when hovered over. modify the flask and html code to be more like this, with the above in mind:
        
    - ask ai to breakdown code and pinpoint part that does that function. if it doesn't, ask it how it can do it *(start from scratch so not polluted with prev wrong code!)*
        
        starting from side by side umap colab code, give it one step at a time, one small modification, rather than all at once
        
        - modify this code so that hovering over one point will turn it yellow
            - did not specify colab: [https://chatgpt.com/c/af24bff4-4390-49e8-b0de-99ff0359e5dd](https://chatgpt.com/c/af24bff4-4390-49e8-b0de-99ff0359e5dd)
                - try using dash : still doesn’t work
            - [specify must be in colab](https://chatgpt.com/c/c9ea52b3-0fec-4eae-a3e8-0842f34b3c9f) : still doesn’t work
- ✅ **EXPM:** backup: instead of hovering both at same time, just color code statically beforehand for certain cluster pairs
    
    [https://chatgpt.com/c/969eeff5-2354-4d68-99ea-18b3b1bd8b53](https://chatgpt.com/c/969eeff5-2354-4d68-99ea-18b3b1bd8b53)
    
    - ✅ NOTE: if get error `JSONDecodeError: Expecting value: line 69032 column 1 (char 3145728)`, prob bc file didn’t upload fully and was caneled. upload it again
    - ✅ modify this to color yellow the points features 1 and 3 in the left plot, and features 10 and 13 in the right plot, while all other points are blue:
        
        This works, but only visible when points are 16000. This is bc too many pts to see yellow! So perhaps instead of coloring, zoom in on both parts of the plots (neighborhood around the paired points) after hovering/clicking
        
    - ✅ [search `fList_model_B` for features (indices in list) which have keyword](https://colab.research.google.com/drive/1Cl7nohl7hyaKz17bHbrkDgkADf-0DPqZ#scrollTo=JIkXX5HEOTQL&line=1&uniqifier=1)
    - ✅ [color pairs of points from corr index list](https://colab.research.google.com/drive/1Cl7nohl7hyaKz17bHbrkDgkADf-0DPqZ#scrollTo=_8NnY034ISWi&line=1&uniqifier=1)
    - ✅ results for ‘upon’
        
        ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled.png)
        
    - [✅ make into fn and try other keywords](https://colab.research.google.com/drive/1Cl7nohl7hyaKz17bHbrkDgkADf-0DPqZ#scrollTo=q2yeyLesQbS_&line=47&uniqifier=1)
    - NOTE: like in ‘saw’, the features that actv on ‘saw’ don’t always have the #1 highest corr with the features in other model with ‘saw’
- ✅ **EXPM:** slowdown bc too many cells, so clean up in `ts_1L_2L_UMAP_v2.ipynb` to try more keyws
    
    [ts_1L_2L_UMAP_v2](https://colab.research.google.com/drive/1M9Q5iDxnJl5SDI-n5CE4wnJrff-Wr293#scrollTo=CRcTQwEN0qia).ipynb
    
    - [ISSUE WITH SEARCH: ‘king’ appears to be part of ‘talking’, etc. So we should specifically search for ‘king,’ or ‘ king,’ or ‘, king’ using lowercase of string](https://chatgpt.com/c/6e7693de-4bec-4613-90f2-5e5e1b28fc72)
        - code
            
            ```
            def find_indices_with_keyword(fList, keyword):
                """
                Find all indices of fList which contain the keyword in the specified formats:
                'keyword,', ' keyword,', or ', keyword'.
            
                Args:
                fList (list of str): List of strings to search within.
                keyword (str): Keyword to search for within the strings of fList.
            
                Returns:
                list of int: List of indices where the keyword is found within the strings of fList.
                """
                keyword = keyword.lower()
                formatted_keywords = [f"{keyword},", f" {keyword},", f", {keyword}"]
            
                return [index for index, string in enumerate(fList) if any(formatted_keyword in string.lower() for formatted_keyword in formatted_keywords)]
            ```
            
        
        Actually those are wrong too (eg. “ talking,” still fits). So find the exact match in this instead: 
        
        ```
        split_list = fList_model_B[0].split(',')
        [i.replace(' ', '') for i in split_list]
        ```
        
    - ⚠️ how do I optimize this fn to be faster? say I have an existing umap and just want to recolor based on keywords, are there redundancies in this?
        
        chatgpt doesn’t optm this well
        
- ⚠️ **EXPM:** [use CCA to figure out which keyword subspaces have high sim (and which don’t)](https://colab.research.google.com/drive/1M9Q5iDxnJl5SDI-n5CE4wnJrff-Wr293#scrollTo=d5DW8_bDWhYh&line=27&uniqifier=1)
    - given two matrices of size (16384, 1024), I want to take subsets of the rows using a list of indices for both matrices, then use umap then cca on them. is this valid to find the similarity between subspaces? if so how do it in python
        
        [https://chatgpt.com/c/b2370a95-9f71-4cdf-88b7-009821658eaa](https://chatgpt.com/c/b2370a95-9f71-4cdf-88b7-009821658eaa)
        
        - take `cca.score` of original umap embeddings, not of X_c and Y_c (the CCA-transformed data)
    
    [https://chatgpt.com/c/fc012477-b248-43e0-b08d-54a88df2bdce](https://chatgpt.com/c/fc012477-b248-43e0-b08d-54a88df2bdce)
    
    - correlation coefficient vs cca.score(X_umap, Y_umap)
        
        The `correlation coefficient` and `cca.score(X_umap, Y_umap)` are different methods to assess the relationship between the canonical variables obtained from Canonical Correlation Analysis (CCA). Here's a breakdown of what each one represents and how to interpret them:
        
        ### Canonical Correlation Coefficient
        
        1. **Definition**: Canonical correlation coefficients measure the linear relationship between pairs of canonical variables obtained from the two datasets.
        2. **Calculation**: These coefficients are computed for each pair of canonical variables (one from each dataset). In your case, you computed the correlations manually:
            
            ```python
            correlations = [np.corrcoef(X_c[:, i], Y_c[:, i])[0, 1] for i in range(X_c.shape[1])]
            
            ```
            
        3. **Interpretation**:
            - Values range from -1 to 1.
            - A value closer to 1 or -1 indicates a strong linear relationship.
            - A value closer to 0 indicates a weak linear relationship.
            - Positive values indicate that as one variable increases, the other tends to increase.
            - Negative values indicate that as one variable increases, the other tends to decrease.
        
        ### `cca.score(X_umap, Y_umap)`
        
        1. **Definition**: The `cca.score` method in `sklearn` computes the average canonical correlation between the transformed datasets.
        2. **Calculation**: This method calculates the average correlation between the canonical variables across all dimensions specified during the CCA fitting. However, it should normally return a value between -1 and 1, indicating the average strength of the linear relationship.
        3. **Interpretation**:
            - A higher score indicates a stronger average linear relationship across all canonical pairs.
            - This method provides a single summary statistic instead of individual correlation coefficients for each pair.
        
        ### Practical Differences and Usage
        
        - **Granularity**: The canonical correlation coefficients provide a detailed view by showing the strength of the relationship for each pair of canonical variables. In contrast, `cca.score` gives a single summary measure of the overall relationship.
        - **Use Cases**:
            - **Canonical Correlation Coefficients**: Useful when you want to understand the relationship between specific pairs of canonical variables.
            - **cca.score**: Useful when you need a quick summary of the overall relationship strength.
        
        ### Example with Correct Usage
        
        Given your goal is to compare subspaces using CCA, here's how to properly use both methods:
        
        1. **Compute Canonical Correlation Coefficients**:
            
            ```python
            import numpy as np
            import umap
            from sklearn.cross_decomposition import CCA
            from sklearn.preprocessing import StandardScaler
            
            # Assuming X and Y are your input matrices of size (16384, 1024)
            # Assuming indices_X and indices_Y are lists of indices for subsetting X and Y respectively
            
            # Step 1: Subset the matrices
            X_subset = X[indices_X, :]
            Y_subset = Y[indices_Y, :]
            
            # Step 2: Apply UMAP to each subset
            umap_model = umap.UMAP(n_components=2)  # you can adjust n_components as needed
            
            X_umap = umap_model.fit_transform(X_subset)
            Y_umap = umap_model.fit_transform(Y_subset)
            
            # Standardize the UMAP-transformed data
            X_umap = StandardScaler().fit_transform(X_umap)
            Y_umap = StandardScaler().fit_transform(Y_umap)
            
            # Step 3: Fit and transform using CCA
            cca = CCA(n_components=2)  # you can adjust n_components as needed
            X_c, Y_c = cca.fit_transform(X_umap, Y_umap)
            
            # Calculate canonical correlations manually
            correlations = [np.corrcoef(X_c[:, i], Y_c[:, i])[0, 1] for i in range(X_c.shape[1])]
            print("Canonical correlations:", correlations)
            
            # Compute the average canonical correlation score
            average_score = np.mean(correlations)
            print("Average canonical correlation score:", average_score)
            
            ```
            
        2. **Compute `cca.score`**:
            
            ```python
            # Optionally, calculate the score using the CCA object
            cca_score = cca.score(X_umap, Y_umap)
            print("CCA score:", cca_score)
            
            ```
            
        
        ### Key Points to Remember:
        
        - Both the canonical correlation coefficients and `cca.score` are useful metrics, but they serve slightly different purposes.
        - Ensure the data is properly preprocessed (e.g., standardized) before applying CCA.
        - Interpret the canonical correlations to understand specific relationships, and use `cca.score` for a quick summary.
    - why is Average canonical correlation score 0.4 while cca.score(X_umap, Y_umap) is 0.1
        
        The discrepancy between the "Average canonical correlation score" (0.4) and `cca.score(X_umap, Y_umap)` (0.1) suggests a misunderstanding or misuse of the `cca.score` method. The `cca.score` method from scikit-learn's CCA class should give the average canonical correlation directly and should match the manually calculated average of the canonical correlations. Let's clarify and ensure the correct usage.
        
        ### Correct Usage and Understanding
        
        1. **Canonical Correlation Coefficients**:
            - These are manually computed correlations for each pair of canonical variables.
            - Should be directly calculated from the transformed data `X_c` and `Y_c`.
        2. **`cca.score` Method**:
            - This should return the average of the canonical correlations.
        
        ### Revisiting the Process and Code
        
        Let's ensure the entire process is correct:
        
        1. **Standardization**: Ensure data is standardized before applying UMAP and CCA.
        2. **UMAP Transformation**: Correctly transform the data using UMAP.
        3. **CCA Fitting and Transformation**: Correctly fit and transform the data using CCA.
        4. **Correlation Calculation**: Compute the canonical correlations correctly.
        5. **CCA Score Calculation**: Use `cca.score` method correctly.
        
        ### Complete Code Example
        
        Here is the corrected code with a focus on ensuring all steps are correctly performed:
        
        ```python
        import numpy as np
        import umap
        from sklearn.cross_decomposition import CCA
        from sklearn.preprocessing import StandardScaler
        
        # Assuming X and Y are your input matrices of size (16384, 1024)
        # Assuming indices_X and indices_Y are lists of indices for subsetting X and Y respectively
        
        # Step 1: Subset the matrices
        X_subset = X[indices_X, :]
        Y_subset = Y[indices_Y, :]
        
        # Step 2: Standardize the subsets
        scaler = StandardScaler()
        X_subset = scaler.fit_transform(X_subset)
        Y_subset = scaler.fit_transform(Y_subset)
        
        # Step 3: Apply UMAP to each subset
        umap_model = umap.UMAP(n_components=2)  # you can adjust n_components as needed
        
        X_umap = umap_model.fit_transform(X_subset)
        Y_umap = umap_model.fit_transform(Y_subset)
        
        # Step 4: Standardize the UMAP-transformed data
        X_umap = scaler.fit_transform(X_umap)
        Y_umap = scaler.fit_transform(Y_umap)
        
        # Step 5: Fit and transform using CCA
        cca = CCA(n_components=2)  # you can adjust n_components as needed
        X_c, Y_c = cca.fit_transform(X_umap, Y_umap)
        
        # Step 6: Calculate canonical correlations manually
        correlations = [np.corrcoef(X_c[:, i], Y_c[:, i])[0, 1] for i in range(X_c.shape[1])]
        print("Canonical correlations:", correlations)
        
        # Calculate the average canonical correlation score manually
        average_correlation_score = np.mean(correlations)
        print("Average canonical correlation score:", average_correlation_score)
        
        # Step 7: Compute the average canonical correlation score using CCA's score method
        cca_score = cca.score(X_umap, Y_umap)
        print("CCA score:", cca_score)
        
        ```
        
        ### Explanation of Steps:
        
        1. **Standardization**: The data is standardized before any dimensionality reduction. This ensures that each feature contributes equally to the analysis.
        2. **UMAP Transformation**: Apply UMAP to the standardized data to reduce dimensionality.
        3. **Standardization of UMAP Data**: Standardize the UMAP-transformed data.
        4. **CCA Fitting and Transformation**: Fit and transform the standardized UMAP data using CCA.
        5. **Correlation Calculation**: Manually compute the canonical correlations for each pair of canonical variables.
        6. **Average Correlation Calculation**: Calculate the average of the canonical correlations.
        7. **CCA Score Calculation**: Use the `cca.score` method to calculate the average canonical correlation score.
        
        ### Consistency Check:
        
        - The manually calculated average canonical correlation should match the `cca.score`.
        - If there's still a discrepancy, double-check the input data and ensure no preprocessing steps were missed.
        
        ### Troubleshooting:
        
        If the `cca.score` still does not match the average of manually calculated correlations, check for potential issues such as:
        
        - Misalignment or indexing errors in the data subsets.
        - Ensure all data preprocessing steps are consistent between manual and method-based calculations.
        - Verify there are no NaNs or infinities in the data after transformations.
        
        By following these steps and ensuring correct preprocessing, the manually calculated average canonical correlation should match the `cca.score`.
        
    - i don't get why cca.score is done on embeddings before doing cca.transform?
        
        
        The `cca.score` method works directly on the embeddings (`embedding1` and `embedding2`) because it encapsulates both the transformation and the correlation computation in one step. Here’s the process:
        
    - high cca score, low corr coeffs
        
        The output suggests that there are issues with the canonical correlation analysis (CCA) results, indicated by the highly negative canonical correlation and the extremely low correlation coefficients. Here’s a breakdown of what these values mean and possible reasons for these results:
        
        ### Breakdown of the Results
        
        1. **Canonical Correlations: -0.9934121981814538**
            - This value indicates a very strong inverse relationship between the canonical variates of the transformed data sets.
            - In a typical CCA, such a strong negative correlation is unusual and might indicate an issue with the data preprocessing or the fitting process.
        2. **Correlation Coefficients: [0.0038447374325681206, 0.0021137853358469474]**
            - These values represent the correlation coefficients for the individual components of the transformed data sets.
            - The extremely low values (close to zero) suggest that there is almost no linear relationship between the corresponding canonical variates for these components.
        
        ### Interpretation and Possible Issues
        
        The combination of a highly negative canonical correlation and near-zero correlation coefficients indicates that something might have gone wrong during the CCA process. Here are some potential issues and interpretations:
        
        1. **Data Preprocessing**:
            - Ensure that the data is properly scaled and standardized before applying CCA. Inconsistent or incorrect scaling can lead to misleading results.
            - Double-check that the subsets or embeddings (e.g., `embedding1` and `embedding2`) are correctly derived and transformed.
        2. **Dimensionality Reduction Step**:
            - If UMAP or another dimensionality reduction technique was applied, verify that the parameters used are appropriate and that the resulting embeddings maintain meaningful relationships.
            - Non-linear transformations like UMAP can sometimes distort linear relationships, which can affect the CCA results.
        3. **Fit and Transform Steps**:
            - Ensure that the CCA model is correctly fitted to the data before scoring or transforming.
            - Double-check the order of operations and ensure consistency between fitting, transforming, and scoring.
        4. **Canonical Variates Interpretation**:
            - The strong negative correlation combined with low individual correlation coefficients might indicate overfitting or that the canonical variates are not capturing meaningful relationships.
        
        ### Suggestions for Troubleshooting
        
        To diagnose and address the issue, you might consider the following steps:
        
        1. **Verify Data Integrity**:
            - Check the integrity and preprocessing of the original data before applying CCA.
            - Ensure that there are no errors or anomalies in the data subsets used for CCA.
        2. **Review Dimensionality Reduction**:
            - Experiment with different parameters for UMAP or try alternative dimensionality reduction techniques (e.g., PCA) to see if the results improve.
        3. **Check CCA Implementation**:
            - Confirm that the CCA model is correctly fitted and transformed.
            - Ensure that the data passed to `cca.score` and `cca.transform` is consistent and correctly preprocessed.
        4. **Recalculate Step-by-Step**:
            - Manually calculate the canonical correlations step-by-step to identify where the discrepancy arises.
            - Compare the manual calculations with the results from the `cca.score` method.
        
        Here’s a revised and more detailed approach to fitting, transforming, and scoring the CCA model:
        
        ```python
        from sklearn.preprocessing import StandardScaler
        from sklearn.cross_decomposition import CCA
        import numpy as np
        
        # Assuming embedding1 and embedding2 are the UMAP-transformed embeddings
        
        # Step 1: Standardize the embeddings
        scaler = StandardScaler()
        embedding1 = scaler.fit_transform(embedding1)
        embedding2 = scaler.fit_transform(embedding2)
        
        # Step 2: Fit the CCA model
        cca = CCA(n_components=2)
        cca.fit(embedding1, embedding2)
        
        # Step 3: Transform the data
        A_c, B_c = cca.transform(embedding1, embedding2)
        
        # Step 4: Calculate canonical correlations manually
        canonical_correlations = [np.corrcoef(A_c[:, i], B_c[:, i])[0, 1] for i in range(A_c.shape[1])]
        print("Canonical Correlations (manual):", canonical_correlations)
        
        # Step 5: Compute the average canonical correlation score manually
        average_correlation_score = np.mean(canonical_correlations)
        print("Average Canonical Correlation Score (manual):", average_correlation_score)
        
        # Step 6: Compute the CCA score using the score method
        cca_score = cca.score(embedding1, embedding2)
        print("CCA Score:", cca_score)
        
        ```
        
        By following these steps and verifying each stage, you can identify potential issues and better understand the resulting canonical correlations.
        
    - is it valid to apply umap then cca; is it better to just apply cca on original data
        
        Applying UMAP followed by CCA can be valid depending on the specific goals and characteristics of your data. However, whether this approach is better than applying CCA directly on the original data depends on several factors. Let's discuss the considerations for both approaches.
        
        ### Applying UMAP Followed by CCA
        
        ### Advantages:
        
        1. **Dimensionality Reduction**:
            - UMAP is a powerful non-linear dimensionality reduction technique that can uncover complex structures in the data, potentially making it easier for CCA to find meaningful relationships in a lower-dimensional space.
        2. **Noise Reduction**:
            - By reducing the dimensionality, UMAP can help filter out noise and highlight the most significant features, which might improve the performance of subsequent analyses like CCA.
        3. **Visualization**:
            - UMAP provides a way to visualize high-dimensional data in 2D or 3D, which can help in understanding the underlying structure and relationships before applying CCA.
        
        ### Disadvantages:
        
        1. **Non-Linear Transformation**:
            - UMAP is a non-linear method, which means that the relationships between variables in the original high-dimensional space may not be preserved in the lower-dimensional space. This can affect the interpretability of the canonical correlations obtained from CCA.
        2. **Loss of Information**:
            - Dimensionality reduction techniques can sometimes lose important information, especially if the reduced dimensions are not sufficient to capture the complexity of the data.
        
        ### Applying CCA Directly on Original Data
        
        ### Advantages:
        
        1. **Linear Relationships**:
            - CCA is a linear method that identifies linear relationships between two datasets. Applying it directly to the original data ensures that these relationships are based on the full information present in the data.
        2. **Interpretability**:
            - The canonical variates obtained from CCA on the original data are easier to interpret in terms of the original variables.
        
        ### Disadvantages:
        
        1. **High Dimensionality**:
            - If the original data is high-dimensional, CCA might struggle due to the curse of dimensionality, where the large number of variables can lead to overfitting and poor generalization.
        2. **Noise**:
            - High-dimensional data often contains noise, which can obscure the meaningful relationships that CCA is trying to uncover.
        
        ### Recommendations
        
        1. **Exploratory Analysis**:
            - Use UMAP for exploratory data analysis and visualization to understand the structure of your data. This can help in identifying the most relevant features and understanding the relationships before applying CCA.
        2. **Apply CCA Directly**:
            - If interpretability and preserving linear relationships are crucial, consider applying CCA directly on the original data, especially if the dimensionality is manageable.
        3. **Hybrid Approach**:
            - Consider a hybrid approach where you first use UMAP to reduce dimensionality to a level that is still interpretable and then apply CCA. This can balance the benefits of noise reduction and visualization from UMAP with the interpretability of CCA.
        
        ### Example Code for Both Approaches
        
        ### 1. Applying CCA Directly on Original Data:
        
        ```python
        from sklearn.preprocessing import StandardScaler
        from sklearn.cross_decomposition import CCA
        
        # Assuming X and Y are your original input matrices
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        Y_scaled = scaler.fit_transform(Y)
        
        cca = CCA(n_components=2)
        cca.fit(X_scaled, Y_scaled)
        
        A_c, B_c = cca.transform(X_scaled, Y_scaled)
        
        # Calculate canonical correlations
        canonical_correlations = [np.corrcoef(A_c[:, i], B_c[:, i])[0, 1] for i in range(A_c.shape[1])]
        print("Canonical Correlations (direct CCA):", canonical_correlations)
        
        cca_score = cca.score(X_scaled, Y_scaled)
        print("CCA Score (direct CCA):", cca_score)
        
        ```
        
        ### 2. Applying UMAP Followed by CCA:
        
        ```python
        import umap
        from sklearn.preprocessing import StandardScaler
        from sklearn.cross_decomposition import CCA
        
        # Assuming X and Y are your original input matrices
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        Y_scaled = scaler.fit_transform(Y)
        
        umap_model = umap.UMAP(n_components=2)
        X_umap = umap_model.fit_transform(X_scaled)
        Y_umap = umap_model.fit_transform(Y_scaled)
        
        cca = CCA(n_components=2)
        cca.fit(X_umap, Y_umap)
        
        A_c, B_c = cca.transform(X_umap, Y_umap)
        
        # Calculate canonical correlations
        canonical_correlations = [np.corrcoef(A_c[:, i], B_c[:, i])[0, 1] for i in range(A_c.shape[1])]
        print("Canonical Correlations (UMAP + CCA):", canonical_correlations)
        
        cca_score = cca.score(X_umap, Y_umap)
        print("CCA Score (UMAP + CCA):", cca_score)
        
        ```
        
        ### Conclusion
        
        Choosing between applying UMAP followed by CCA or applying CCA directly to the original data depends on your specific data characteristics and analysis goals. Both approaches have their merits and potential pitfalls, so it's often useful to experiment with both and compare the results to determine which method provides more meaningful and interpretable insights for your particular use case.
        
    - does using a100 speed up plotting or cca calc in colab
        
        Using an A100 GPU in Google Colab can significantly speed up certain computations, particularly those that involve large-scale matrix operations or parallelizable tasks. However, the specific impact on plotting and Canonical Correlation Analysis (CCA) depends on how these tasks are implemented and whether they are optimized to leverage GPU acceleration. Let's break this down:
        
        ### Speed Up Plotting
        
        1. **Plotting Libraries**:
            - Most common plotting libraries in Python, such as Matplotlib, Seaborn, and Plotly, do not typically utilize GPU acceleration. These libraries are primarily CPU-bound and might not see a significant speed improvement with a GPU like the A100.
            - Tasks like rendering plots, updating figures, and managing graphical user interface (GUI) elements are generally handled by the CPU.
        
        ### Speed Up CCA Calculations
        
        1. **Canonical Correlation Analysis (CCA)**:
            - CCA involves linear algebra operations, which can be accelerated on a GPU. Libraries that leverage GPU acceleration for linear algebra, such as CuPy (a GPU-accelerated drop-in replacement for NumPy) or RAPIDS cuML, can significantly speed up these computations.
            - Scikit-learn, the library typically used for CCA in Python, does not natively support GPU acceleration for CCA. However, you can use GPU-accelerated libraries to perform similar analyses.
        
        ### Example of GPU-Accelerated Linear Algebra for CCA
        
        To use GPU-accelerated linear algebra operations for something similar to CCA, you can use CuPy along with RAPIDS cuML. Here's an example:
        
        ```python
        # Install RAPIDS if not already installed
        !pip install -q rapids-cuml
        
        import cupy as cp
        from cuml import CCA
        
        # Assuming X and Y are your original input matrices on GPU
        X_gpu = cp.asarray(X)
        Y_gpu = cp.asarray(Y)
        
        # Standardize the data
        X_gpu = (X_gpu - cp.mean(X_gpu, axis=0)) / cp.std(X_gpu, axis=0)
        Y_gpu = (Y_gpu - cp.mean(Y_gpu, axis=0)) / cp.std(Y_gpu, axis=0)
        
        # Perform CCA using RAPIDS cuML
        cca_gpu = CCA(n_components=2)
        cca_gpu.fit(X_gpu, Y_gpu)
        
        A_c_gpu, B_c_gpu = cca_gpu.transform(X_gpu, Y_gpu)
        
        # Transfer results back to CPU for further processing if needed
        A_c = cp.asnumpy(A_c_gpu)
        B_c = cp.asnumpy(B_c_gpu)
        
        # Calculate canonical correlations manually
        canonical_correlations = [np.corrcoef(A_c[:, i], B_c[:, i])[0, 1] for i in range(A_c.shape[1])]
        print("Canonical Correlations (GPU CCA):", canonical_correlations)
        
        ```
        
        ### Conclusion
        
        - **Plotting**: Using an A100 GPU will not significantly speed up plotting tasks in most common Python plotting libraries since they are CPU-bound.
        - **CCA Calculations**: The A100 GPU can speed up CCA calculations if you use GPU-accelerated libraries such as RAPIDS cuML. For CCA in scikit-learn, the computations will remain CPU-bound unless you switch to a library that leverages GPU acceleration.
        
        Therefore, to leverage the A100 GPU for CCA in Google Colab, consider using GPU-accelerated libraries designed for linear algebra and machine learning tasks.
        
    - due to umap randomness does that mean cca score on umap embeddings is diff each time
        
        Yes, the Canonical Correlation Analysis (CCA) score on UMAP embeddings can differ each time due to the inherent randomness in UMAP's algorithm. UMAP (Uniform Manifold Approximation and Projection) uses stochastic processes, including random initializations and stochastic gradient descent, which can lead to slightly different embeddings on each run unless you set a fixed random seed.
        
        ### Understanding UMAP's Randomness
        
        1. **Stochastic Nature**:
            - UMAP relies on stochastic processes to construct the high-dimensional graph and then optimize the low-dimensional representation.
            - This can introduce variability in the resulting embeddings across different runs.
        2. **Random Initialization**:
            - The initial positions of points in the lower-dimensional space are randomly set, which can influence the final outcome.
        3. **Optimization**:
            - The optimization process in UMAP is non-deterministic, further contributing to the variability in embeddings.
        
        ### Impact on CCA
        
        When you apply CCA to the embeddings generated by UMAP, the variability in the embeddings can lead to different canonical correlations and, consequently, different CCA scores each time UMAP is run.
        
        ### Mitigating Variability
        
        To mitigate the variability and make the results reproducible, you can set a fixed random seed for UMAP. This ensures that the random processes within UMAP produce the same results each time.
        
        ### Setting a Random Seed in UMAP
        
        Here’s how you can set a random seed in UMAP to ensure reproducible embeddings:
        
        ```python
        import umap
        from sklearn.preprocessing import StandardScaler
        from sklearn.cross_decomposition import CCA
        import numpy as np
        
        # Assuming X and Y are your original input matrices
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        Y_scaled = scaler.fit_transform(Y)
        
        # Set a fixed random seed for UMAP
        random_state = 42  # You can choose any integer
        
        umap_model = umap.UMAP(n_components=2, random_state=random_state)
        X_umap = umap_model.fit_transform(X_scaled)
        Y_umap = umap_model.fit_transform(Y_scaled)
        
        # Fit the CCA model
        cca = CCA(n_components=2)
        cca.fit(X_umap, Y_umap)
        
        # Transform the data
        A_c, B_c = cca.transform(X_umap, Y_umap)
        
        # Calculate canonical correlations manually
        canonical_correlations = [np.corrcoef(A_c[:, i], B_c[:, i])[0, 1] for i in range(A_c.shape[1])]
        print("Canonical Correlations (UMAP + CCA):", canonical_correlations)
        
        # Compute the CCA score
        cca_score = cca.score(X_umap, Y_umap)
        print("CCA Score (UMAP + CCA):", cca_score)
        
        ```
        
        ### Summary
        
        - **Variability**: UMAP's randomness can lead to different embeddings, affecting the CCA scores.
        - **Reproducibility**: Setting a fixed random seed in UMAP ensures reproducible embeddings and consistent CCA scores across runs.
        - **Implementation**: Use the `random_state` parameter in UMAP to control the randomness.
        
        By setting a random seed, you can ensure that the results of your UMAP and subsequent CCA analyses are reproducible and consistent each time you run the code.
        
    - when doing cca, is it better to use pca or umap on data first
    - error when only 2 feature matches but n_neigh is 15
        
        ```
        keyword = "king"
        cca_subspace(keyword)
        ```
        
        n_neighbors is larger than the dataset size; truncating to X.shape[0] - 1
        
        /usr/local/lib/python3.10/dist-packages/umap/umap_.py:134: UserWarning:
        
        A large number of your vertices were disconnected from the manifold.
        Disconnection_distance = inf has removed 0 edges.
        It has fully disconnected 2 vertices.
        You might consider using find_disconnected_points() to find and remove these points from your data.
        Use umap.utils.disconnected_vertices() to identify them.
        
        ```
        ---> 41     return umr_maximum(a, axis, None, out, keepdims, initial, where)
             42     43 def _amin(a, axis=None, out=None, keepdims=False,
        
        ```
        
        ```
        ValueError: zero-size array to reduction operation maximum which has no identity
        ```
        
        However, though get saem warning, this works:
        
        ```
        keyword = "dragon"
        cca_subspace(keyword)
        ```
        
    - I think you've been using cca score wrong. it says here y is supposed to be true values, not another dataset
    [https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA.score](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA.score)
        
        [https://stackoverflow.com/questions/69800500/how-to-calculate-correlation-coefficients-using-sklearn-cca-module](https://stackoverflow.com/questions/69800500/how-to-calculate-correlation-coefficients-using-sklearn-cca-module)
        
        [https://github.com/google/svcca/tree/1f3fbf19bd31bd9b76e728ef75842aa1d9a4cd2b](https://github.com/google/svcca/tree/1f3fbf19bd31bd9b76e728ef75842aa1d9a4cd2b)
        
        tutorial 0 takes mean of the 50 canon coeffs for the first canonical variable
        
        chatgpt is wrong; cca. score ISN’T mean, but coefficient of det: [https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA.score](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA.score)
        
        - coefficient of det vs mean of canon coeff
            
            The coefficient of determination (R²) and the mean of canonical correlation coefficients are two different metrics used to evaluate Canonical Correlation Analysis (CCA). Here’s a detailed comparison and explanation of these metrics:
            
            ### Coefficient of Determination (R²)
            
            The coefficient of determination, or R², measures how well the canonical variates from one dataset can predict the canonical variates from the other dataset. This is akin to evaluating the goodness-of-fit of a regression model.
            
            - **Definition**: R² is the proportion of variance in the dependent variable that is predictable from the independent variable(s).
            - **Computation in CCA**: When using the `cca.score` method in scikit-learn, R² is calculated as the proportion of variance in the canonical variates of Y that can be explained by the canonical variates of X.
            - **Range**: R² ranges from 0 to 1, where 0 indicates no predictive power and 1 indicates perfect prediction.
            
            ### Mean of Canonical Correlation Coefficients
            
            Canonical correlation coefficients measure the linear relationships between pairs of canonical variates derived from the two datasets.
            
            - **Definition**: Canonical correlation coefficients are the Pearson correlation coefficients between the pairs of canonical variates.
            - **Computation in CCA**: After transforming the data using CCA, canonical correlations are calculated for each pair of canonical variates.
            - **Mean Canonical Correlation**: The mean of these coefficients gives an overall sense of the linear relationship strength between the datasets.
            
            ### Example Calculation of Both Metrics
            
            Here’s an example showing how to calculate both the coefficient of determination (R²) and the mean of canonical correlation coefficients using scikit-learn’s CCA:
            
            ```python
            from sklearn.preprocessing import StandardScaler
            from sklearn.cross_decomposition import CCA
            import numpy as np
            
            # Example data
            X = np.random.rand(100, 10)
            Y = np.random.rand(100, 10)
            
            # Standardize the data
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
            Y_scaled = scaler.fit_transform(Y)
            
            # Apply CCA
            cca = CCA(n_components=2)
            cca.fit(X_scaled, Y_scaled)
            
            # Transform the data
            X_c, Y_c = cca.transform(X_scaled, Y_scaled)
            
            # Calculate canonical correlations manually
            canonical_correlations = [np.corrcoef(X_c[:, i], Y_c[:, i])[0, 1] for i in range(X_c.shape[1])]
            print("Canonical Correlations:", canonical_correlations)
            
            # Compute the mean of canonical correlations
            mean_canonical_correlation = np.mean(canonical_correlations)
            print("Mean Canonical Correlation:", mean_canonical_correlation)
            
            # Compute the CCA score (coefficient of determination)
            cca_score = cca.score(X_scaled, Y_scaled)
            print("CCA Score (R²):", cca_score)
            
            ```
            
            ### Interpretation of Results
            
            1. **Canonical Correlations**:
                - Each value in `canonical_correlations` represents the strength of the linear relationship between a pair of canonical variates from `X` and `Y`.
                - The mean canonical correlation provides an average measure of these relationships.
            2. **CCA Score (R²)**:
                - The CCA score represents how well the canonical variates of `X` predict the canonical variates of `Y`.
                - This score is a measure of the overall predictive power of the canonical relationship.
            
            ### Choosing Between the Metrics
            
            - **Coefficient of Determination (R²)**:
                - Use this if you are interested in the predictive power of the canonical variates. It tells you how well one set of canonical variates predicts the other.
                - Useful for assessing the explanatory power of the model.
            - **Mean Canonical Correlation**:
                - Use this if you are more interested in the average strength of the linear relationships between the canonical variates.
                - Provides a direct measure of the correlation strength.
            
            Both metrics are valuable, but they serve different purposes. The choice between them depends on whether your primary interest lies in prediction (R²) or in measuring the strength of associations (mean canonical correlation).
            
- ⚠️ [https://medium.com/@pozdrawiamzuzanna/canonical-correlation-analysis-simple-explanation-and-python-example-a5b8e97648d2](https://medium.com/@pozdrawiamzuzanna/canonical-correlation-analysis-simple-explanation-and-python-example-a5b8e97648d2)
    - [what's the diffeence between fit and transform](https://chatgpt.com/c/a0b74b21-ff52-481e-a5f0-ed437df3f437)
    - so you need fit before transform? can't use score before transform?
        
        Yes, you need to call `fit` before `transform` when using most machine learning models, including Canonical Correlation Analysis (CCA). This is because `fit` is the step where the model learns the necessary parameters based on the input data. Without fitting the model first, the `transform` method wouldn't know how to process the input data.
        
        ### Sequence of Operations
        
        1. **Fit:**
            - `cca.fit(X1_sc, X2_sc)`
            - This step is mandatory. It computes the parameters needed for transformation, which in the case of CCA, are the weights for the linear combinations that maximize the correlation between the datasets.
        2. **Transform:**
            - `X1_c, X2_c = cca.transform(X1_sc, X2_sc)`
            - After fitting, this step applies the learned transformation to the input data, projecting it into the canonical variates space.
        
        ### Using `score` Method
        
        In many machine learning models, there is also a `score` method that evaluates the performance of the model. However, in the context of CCA, the `score` method might not be directly applicable or may not exist. If it does exist, it would typically require the model to be fit first.
        
        - **Score (if applicable):**
            - `cca.score(X1_sc, X2_sc)`
            - This method, if available, would evaluate the model's performance based on some criterion (e.g., correlation strength in the case of CCA). However, it assumes that the model has already been fitted.
        
        ### Summary
        
        - **Fit:** Mandatory initial step to learn the model parameters.
        - **Transform:** Requires the model to be fitted first. Applies the learned transformation to the data.
        - **Score:** If available, usually requires the model to be fitted and might evaluate the model's performance.
        
        In conclusion, you cannot use `transform` or `score` before `fit` because the model needs to learn the necessary parameters during the fitting process before it can transform the data or evaluate its performance.
        
- ⚠️ [cca can be done directly on weight matrices as they’re 2D](https://colab.research.google.com/drive/1M9Q5iDxnJl5SDI-n5CE4wnJrff-Wr293#scrollTo=VgFHtbOoF7y9&line=1&uniqifier=1)
    - [what do these scores mean](https://chatgpt.com/c/a0b74b21-ff52-481e-a5f0-ed437df3f437)
        
        Moderate canonical correlations, like those found here, suggest that while there is a relationship between the datasets, it is not particularly strong. 
        
    - [directly on weight matrices for feature subspaces](https://colab.research.google.com/drive/1M9Q5iDxnJl5SDI-n5CE4wnJrff-Wr293#scrollTo=DDcj-2naHrmp&line=1&uniqifier=1)
    - [try random. why is comp_corr always 0.99:](https://chatgpt.com/c/5e043d92-23e0-4bf9-bf21-4a55e7511c2b)
        
        testing with 10000 doesn’t make it 0.99. Seems like a small sample size? 
        
- ⚠️ umap on feature actvs
    
    [ts_1L_2L_UMAP_actvs](https://colab.research.google.com/drive/1b2vob-ZX8IRBWw-1XLPY1wTCCXYJfVpj#scrollTo=6CvQQSVdQvq5).ipynb
    
    - will this plot the rows as points? how do I plot the columns as points?
        
        
    - takes a long time!

Feature Splitting Expms- Relations by UMAP

- 🐣 feature splitting, MLP0
    - ✅ train biggest feature split, 2L MLP0, as you read alg top / mnn material
    - ✅ get actvs
        - [save_wt_actvs_dsInterp.ipynb](https://colab.research.google.com/drive/1Bh10l4vTb_rrCUw-483RDGsWavigTcjl): this work for any model, just input it in. No need to separate for each model as we don’t care about keeping the analysis output in nb
            - ✅ in an a100, feature_acts  with torch.Size([500, 128, 32768]) get OOM when using num_zeros = (feature_acts == 0).sum().item(). how to solve this
                
                chunking
                
                ```jsx
                import torch
                
                num_zeros = 0
                for i in range(feature_acts.size(0)):
                    for j in range(feature_acts.size(1)):
                        num_zeros += (feature_acts[i, j, :] == 0).sum().item()
                
                ```
                
    - umap plot fs like anthropic
- ✅ [Apollo Research question: Feature Splitting Geometry](https://www.lesswrong.com/posts/KfkpgXdgRheSRWDy8/a-list-of-45-mech-interp-project-ideas-from-apollo-research)
    
    [Research Topics From Others](Research%20Topics%20From%20Others%20ecebedc382474954b3d0c850f82a784c.md) 
    
- ✅ brainstorm better way to phrase main rsch topics, [Main goal and contributions](Geometry%20project%20ideas%20eb549c97d93548fc97e75e83fcba87a8/Main%20goal%20and%20contributions%204b749c6c252b47b8ba383ddfa26e63d9.md)
    - under what conditions do models learn manifolds differently
        - in 2L, perhaps feature split across layers?
        - are they learning the same subspace? how to measure in high dim?
        - difference if use top k? number of examples? make table for saes to train.
    - which features appear to be frequently learned across models using same dataset?
        - which ways that features split appear to be frequently done?
        - are they learning the same high dim relations?
        - conditions for saes which show more similarity between two models
    
- ✅ feature splitting, MLP0
    
    [ts_1L_2L_UMAP_df32768.ipynb](https://colab.research.google.com/drive/1dQPHGIpv0uHQt72rG-pMIB0b7z4nA0T_#scrollTo=-ZqeAFR6EEgs)
    
    - [in colab, pickle load tensor of torch.Size([500, 128, 32768]) takes a long time; consider json or saving to drive? can you save tensor as json? or other format better?](https://chatgpt.com/c/31c97f18-4b5c-4863-8565-e355a7ccd3b1)
    - ✅ OOM when compute corr; optm better
        - how do i reset GPU RAM without ending session
        - try to load just actvs, reshape (del orig), and save corrs BEFORE load weights  + labels. Then load just weights, labels, acts, and corr in second run to get umap comparisons
            - NOTE: acts is used to calc dataset exmps, but takes up many gbs
            - we can rewrite the fns to use reshaped actvs instead! all we have to do is not do reshape(-1) to flatten it
        - ✅ ALT: instead of compute entire matrix, for each feature in B, get row of all corrs with every feature in A, then keep only top ind and delete this row. Save and repeat for all features in B. Or instead of “each feature”, do it for small batch of features.
            - must restart to do this if run unoptm vers before!
    - ✅ ⚠️ get top highest corr pairs, and interpret
        - DEBUG: this is incorrect. highest_correlations_values shuld be the same len as highest_correlations_indices, and contains the value of the corr betwen index (B) and mapped index (A). Instead, it contains every batch value, not just the highest pair!
        - modify this to not get corr values >= 1:
        - [ISSUE: the top corrs are all the same value. We want a linear line of points to have high corr, not all points clustered around 0 with only a few points high close to 1. how do we fixt this metric?](https://chatgpt.com/c/1150803f-36e8-42b6-be22-0f1d0d196fde)
        - [if only the highest value is needed, why does this use mask >](https://chatgpt.com/c/84528b3c-8c3c-4f28-bf89-27a330afbfbd)
        - ISSUE: the top corr feature dataset examples don’t seem to be the same
            - SOLN: look at your saved fList. They ARE the same, but bc you modified dataset examples wrong when using flattened, dataset B is not getting the right ones! Modify it back to using orig actvs, not reshaped! OR just load strs!
            - NOTE: loading actvs is faster after orig load in the run, prob due to some cache
    - ✅ ⚠️ umap plot fs like anthropic
        - how do I re-create this umap of points (feature weights) colored from different saes (demonstrating feature splitting), with points from bigger saes overlayed "on top" of points from smaller saes? do I stack all their weights and run umap on them all, or do I run umap separately on each sae decoder weights then put them on the same plot? which of these two makes sense? or is it neither, but something else? the weights have different sizes (diff number of rows [features] but same num cols [LLM neuron size])
            
            [https://chatgpt.com/c/3e98b3fc-9fd7-4bc4-a9e3-ecea52892f43](https://chatgpt.com/c/3e98b3fc-9fd7-4bc4-a9e3-ecea52892f43)
            
            less into: [https://chatgpt.com/c/430d8e69-c22d-4147-8054-e8219123fedb](https://chatgpt.com/c/430d8e69-c22d-4147-8054-e8219123fedb)
            
        - if umap is random, how can the two umaps of diff saes be aligned? it seems more likely that the weights are first combined THEN put into the same umap. but then how does one distinguish which point is from which? that’s easy- the points (features) are still intact.
            - actually, the weights aren’t combined at all! we can get a reducer, and run the same reducer on all 3 weights, then plot them?
            - Or not:
                - [https://chatgpt.com/c/affc72e3-4e00-4cdd-a800-94a964901a96](https://chatgpt.com/c/affc72e3-4e00-4cdd-a800-94a964901a96)
                    - does it matter if we initalize the reducer in two different instances but with same parameters?
                        
                        Yes, it does matter if you initialize the reducer in two different instances, even with the same parameters, because the UMAP algorithm involves stochastic processes such as initialization and optimization steps that can lead to different results. By using two different reducer instances, you can get slightly different embeddings even if the parameters are the same.
                        
                        Here's a more detailed explanation:
                        
                        ### Stochastic Nature of UMAP
                        
                        UMAP (Uniform Manifold Approximation and Projection) involves stochastic optimization, meaning that random initialization and random choices during optimization can lead to different embeddings each time you run it. Parameters such as the number of neighbors (`n_neighbors`), minimum distance (`min_dist`), and the metric (`metric`) set the structure of the UMAP algorithm, but the random seed affects the initialization and convergence of the algorithm.
                        
                        ### Consistent Embeddings
                        
                        If you want consistent embeddings across different datasets:
                        
                        - **Use the same reducer instance**: Fit the reducer on a combined dataset and then transform each dataset.
                        - **Set a random seed**: Initialize the reducer with a fixed random seed to ensure reproducibility.
                        
                        Here is an example:
                        
                        ```python
                        import umap
                        import numpy as np
                        import matplotlib.pyplot as plt
                        
                        # Example datasets
                        data1 = np.random.rand(100, 10)
                        data2 = np.random.rand(100, 10)
                        data3 = np.random.rand(100, 10)
                        
                        # Combine datasets
                        combined_data = np.vstack((data1, data2, data3))
                        
                        # Create and fit UMAP reducer on combined dataset with a fixed random seed
                        reducer = umap.UMAP(n_neighbors=15, min_dist=0.01, metric='euclidean', random_state=42)
                        reducer.fit(combined_data)
                        
                        # Transform each dataset using the same reducer
                        embedding1 = reducer.transform(data1)
                        embedding2 = reducer.transform(data2)
                        embedding3 = reducer.transform(data3)
                        
                        # Plot the embeddings
                        plt.figure(figsize=(12, 4))
                        
                        plt.subplot(1, 3, 1)
                        plt.scatter(embedding1[:, 0], embedding1[:, 1], label='Dataset 1')
                        plt.title('Dataset 1')
                        plt.legend()
                        
                        plt.subplot(1, 3, 2)
                        plt.scatter(embedding2[:, 0], embedding2[:, 1], label='Dataset 2')
                        plt.title('Dataset 2')
                        plt.legend()
                        
                        plt.subplot(1, 3, 3)
                        plt.scatter(embedding3[:, 0], embedding3[:, 1], label='Dataset 3')
                        plt.title('Dataset 3')
                        plt.legend()
                        
                        plt.tight_layout()
                        plt.show()
                        
                        ```
                        
                        ### Using Two Different Reducer Instances
                        
                        If you use two different reducer instances with the same parameters but without fixing the random seed, the embeddings might look similar but will not be identical:
                        
                        ```python
                        # Create two separate UMAP reducers with the same parameters
                        reducer1 = umap.UMAP(n_neighbors=15, min_dist=0.01, metric='euclidean')
                        reducer2 = umap.UMAP(n_neighbors=15, min_dist=0.01, metric='euclidean')
                        
                        # Fit and transform each dataset separately
                        embedding1 = reducer1.fit_transform(data1)
                        embedding2 = reducer2.fit_transform(data2)
                        
                        # These embeddings are not guaranteed to be in the same space
                        
                        # Plot the embeddings
                        plt.figure(figsize=(8, 4))
                        
                        plt.subplot(1, 2, 1)
                        plt.scatter(embedding1[:, 0], embedding1[:, 1], label='Dataset 1')
                        plt.title('Dataset 1')
                        plt.legend()
                        
                        plt.subplot(1, 2, 2)
                        plt.scatter(embedding2[:, 0], embedding2[:, 1], label='Dataset 2')
                        plt.title('Dataset 2')
                        plt.legend()
                        
                        plt.tight_layout()
                        plt.show()
                        
                        ```
                        
                        In summary, for comparable and consistent embeddings across different datasets, it is crucial to use the same reducer instance and ideally set a random seed for reproducibility.
                        
                - [https://chatgpt.com/c/dea08c7b-9988-496d-b239-22a58830c372](https://chatgpt.com/c/dea08c7b-9988-496d-b239-22a58830c372)
            - [UserWarning: n_jobs value 1 overridden to 1 by setting random_state. Use no seed for parallelism.](https://chatgpt.com/c/9f67d471-2164-4060-847a-2caadd93b900)
        
        [fs_UMAP_v0.ipynb](https://colab.research.google.com/drive/1swzOhJPlBvZNQrZjBW6xZdYalAVkmZjh#scrollTo=HTJhjkZ1yVt4)
        
        - ⚠️ start with umap of one LLM, for 2 SAEs of diff sizes
            - ISSUE: doesnt show feature splitting. are there any correlations?
        - then, side by side of 2 LLMs, each with 2 SAEs
    - ✅ get correlations between saes of different sizes (how feature split)- this is what anthropic did already
        
        this shows there SHOULD be related features, though it doesn’t show ‘more general to more specific’ feature splitting. 
        
        - ✅ interpret the corr ‘upon features’ using samps to double check
    - ✅ try highlighting most corr “upon” in both, noting both the specific indices (and their dataset examps) and the umap. do they line up? if not, umap has issue.
        - [combine these such that there is only 1 plot (not side by side) but color coded by whether it's from df_A0 or df_A1, and a third color is the keyword highlight.](https://chatgpt.com/c/0a9083ae-92c6-4b15-aec0-0840339ba213)
            - ~~actually distinguish the keyword features using different colors or shapes based on whether it's A0 or A1~~
        - we find that the upons from both models ARE in the same place, just hard to see unless zoomed in. however, this is just ‘upon’, so too specific already, and we don’t see feature splitting
            
            ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%201.png)
            
        - concepts like ‘family’ and ‘animal’ aren’t recognized
        - [‘time’ is recognized by MANY features (several clusters), but no feature splitting into ‘summer’, ‘day’, etc.](https://colab.research.google.com/drive/1swzOhJPlBvZNQrZjBW6xZdYalAVkmZjh#scrollTo=8uqsnQY28aty&line=1&uniqifier=1)
        - this is probably because your search is by the exact keyword, not the concept
- ✅ [instead of side-by-side, plot featurse from diff LLMs on same umap and color code](https://colab.research.google.com/drive/1swzOhJPlBvZNQrZjBW6xZdYalAVkmZjh#scrollTo=Efni2LbQ-gBC&line=1&uniqifier=1)
    
    they naturally separate out into different clusters, unlike with 1L fs
    
    - now plot 3 in the same plot (1L_16k, 1L_32k, and 2L-16k)
- ✅ in umap python, difference between reducer.transform and reducer.fit
    
    In UMAP (Uniform Manifold Approximation and Projection), `reducer.fit` and `reducer.transform` serve different purposes and are used at different stages of the dimensionality reduction process.
    
    ### `reducer.fit`
    
    - **Purpose**: This method is used to learn the embedding from the training data. It performs the dimensionality reduction by fitting the UMAP model to the data.
    - **Usage**: Use `reducer.fit` when you want to train the UMAP model on a given dataset.
    - **Functionality**: It computes the low-dimensional embedding for the training data. After fitting, the UMAP model captures the structure of the data in the lower-dimensional space.
    - **Code Example**:
        
        ```python
        import umap
        
        # Create UMAP object
        reducer = umap.UMAP(n_neighbors=15, min_dist=0.1, n_components=2)
        
        # Fit the model to the data
        reducer.fit(X_train)
        
        ```
        
    
    ### `reducer.transform`
    
    - **Purpose**: This method is used to map new data points into the existing low-dimensional space learned by `reducer.fit`.
    - **Usage**: Use `reducer.transform` when you have already fitted the UMAP model on the training data and now want to transform new data points into the same lower-dimensional space.
    - **Functionality**: It takes the fitted UMAP model and projects new data points onto the pre-learned embedding space without altering the learned structure.
    - **Code Example**:
        
        ```python
        # Assuming the UMAP model has already been fitted
        X_new_transformed = reducer.transform(X_new)
        
        ```
        
    
    ### Example Workflow
    
    1. **Fit the model on the training data**:
        
        ```python
        import umap
        
        # Create UMAP object
        reducer = umap.UMAP(n_neighbors=15, min_dist=0.1, n_components=2)
        
        # Fit the model to the training data
        reducer.fit(X_train)
        
        ```
        
    2. **Transform new data points using the fitted model**:
        
        ```python
        # Transform new data points
        X_new_transformed = reducer.transform(X_new)
        
        ```
        
    
    ### Key Points
    
    - **`reducer.fit`** is for learning the embedding from the training data.
    - **`reducer.transform`** is for projecting new data into the learned embedding space.
    - Use `fit` when you want to create the model, and `transform` when you want to apply the model to new data.
    
    By separating these steps, UMAP allows for efficient use of the learned embedding, enabling you to apply the same transformation to multiple datasets once the model has been trained.
    
- ✅ ask neuronpedia if they have feature splitting umaps
    
    1) I was wondering if Neuronpedia has ways for users to plot the combined set of feature directions from SAEs of different widths (such as the set of GPT-2 feature splitting SAEs), as seen in the attached plot from “Scaling Monosemanticity”? If not, I saw in the last update that UMAPs for all SAEs are being generated and also wondering if this might be a future update.
    
    2) I’ve been plotting UMAPs of combined feature directions from SAEs of different widths trained on tinystories models by first learning the embedding on all the feature directions (decoder weights stacked row-wise), then transforming each SAE’s weights into the new lower-dim space (coloured by SAE dict width). Would this be the right way to reproduce Anthropic’s plots?
    
    3) If the feature splitting UMAPs aren’t present for now, I was looking to put the pre-trained GPT-2 SM L8 decoder weights and the exportable explanations into an interactive UMAP plot. While I find many highly correlated features and clusters in the tinystories SAEs, the feature splitting is not as prominent; it may be due to how I train the SAEs, so I might find better results with the pretrained SAEs.  If anyone else is exploring this, such as with training better SAEs on tinystories GPT-2 models, I would be interested in talking more about it (eg. by DM)!
    
    ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%202.png)
    
    ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%203.png)
    
- ✅ #neuronpedia replies
    - bloom
        - Umap links / tables on individual SAEs for feature splitting [https://drive.google.com/drive/folders/1lD1u1mUn7mogxbfqSGw9VK4mSRu6cxnu](https://drive.google.com/drive/folders/1lD1u1mUn7mogxbfqSGw9VK4mSRu6cxnu). We're very busy getting some big SAE releases ready but maybe this will help between now and then.
        - You can load in these SAEs via SAELens and make joint u-maps yourself if you'd like to. We haven't thought about joint u-maps yet as there's some complexity here...
        - You can download and merge feature explanations from autointerp via a button in the top right of SAE pages [https://www.neuronpedia.org/gpt2-small/8-res_fs768-jb](https://www.neuronpedia.org/gpt2-small/8-res_fs768-jb) or via the API (see Neuronpedia API docs). [https://www.neuronpedia.org/api-doc](https://www.neuronpedia.org/api-doc)
        - Towards Monosemanticity contains methods for constructing u-maps and identifying clusters in them. We've found this requires hyperparameter tuning. I'm not sure what changes for joint SAE u-maps but my guess is not much. I've made a note to include umap generating code in updated SAE Lens tutorial (coming soon!)
    - reply to bloom
        
        Thanks! The umaps and feature labels are very helpful! I've been using saelens to make the joint umaps, though still working on improving them. The umap tutorial should be very helpful once it's released! (one thing I noticed was umap-learn and saelens didn't seem to be compatible in the same colab notebook, think it was something to do with numpy vers, so when I started out I just crudely saved sae activations/labels/weights and loaded them locally or in another nb to run umap)
        

Topological Data Analysis Explora Expms

- ✅ outline expm summary + outcomes to look for, methods, and exp results in overleaf
    - [manifold learning](https://chatgpt.com/c/e2dcef05-e2a0-4a24-8521-b2526d5b3fc8)
- 🐣 [AlgTop Explora](AlgTop%20Explora%20880f6e49fb09483f94155492009bd222.md) : python tutorial mapper on Dweights
    
    …\_prog\repos-cloned\YouTube-Blog\mapper
    
    - ✅ [mapper_example.ipynb](https://colab.research.google.com/drive/1qBX9sQ5iwlcX17lwrmiXl36Yzfg6hkNP#scrollTo=f_AY6TPyE3PC)
        - ✅ ISSUE: outdated numpy and umap packages, so don’t use old vers
        - ✅ can’t do html jupyter viz, so use colab tutorial code to viz
            - ISSUE: doesn’t look the same as interacttive in tutorial
        - ✅ SOLN: try using original html jupyter viz code
            - just download file from colab and open in browser (not vscode)
    - ✅ TopologicalDataAnalysisWithPython.ipynb
        - just run setup, [viz “load data”](https://colab.research.google.com/drive/1tNOVCQTLHBB6CvbgvPCyrOTm0OKdgSix#scrollTo=_dD5S6lyHPb4&line=16&uniqifier=1) , and mapper cells
    - 🐣 get labels on interactive HTML mapper graph
        - in browser, click on a node and opening “cluster details” on top-left will show cluster members
        - compare to [video demo](https://www.youtube.com/watch?v=NlMrvCYlOOQ&ab_channel=ShawTalebi)
            - change ‘node color fn’ to ‘max’ for interesting
                - yellow node has points with high $ returns
            - gen new graphs with new proj and clustering strats
- ✅ [check_saelens_tflens_umap_compat.ipynb](https://colab.research.google.com/drive/1Z3B2Y8pHnvxzqC1tV6UZz1pnqCP_UZg_#scrollTo=oRe06OUe2-Qj)
    
    run all this on cpu
    
    - the error
        
        ```
        ---------------------------------------------------------------------------
        
        ```
        
        ```
        AttributeError                            Traceback (most recent call last)
        
        ```
        
        ```
        <ipython-input-3-623e299b05c0> in <cell line: 1>()
        ----> 1 import umap
        
        ```
        
        ---
        
        8 frames
        
        ---
        
        ```
        /usr/local/lib/python3.10/dist-packages/umap/__init__.py in <module>
              1 from warnings import warn, catch_warnings, simplefilter
        ----> 2 from .umap_ import UMAP
              3      4 try:
              5     with catch_warnings():
        
        ```
        
        ```
        /usr/local/lib/python3.10/dist-packages/umap/umap_.py in <module>
              8 import time
              9
        ---> 10 from scipy.optimize import curve_fit
             11 from sklearn.base import BaseEstimator
             12 from sklearn.utils import check_random_state, check_array
        
        ```
        
        ```
        /usr/local/lib/python3.10/dist-packages/scipy/optimize/__init__.py in <module>
            408    409 from ._optimize import *
        --> 410 from ._minimize import *
            411 from ._root import *
            412 from ._root_scalar import *
        
        ```
        
        ```
        /usr/local/lib/python3.10/dist-packages/scipy/optimize/_minimize.py in <module>
             25 from ._trustregion_krylov import _minimize_trust_krylov
             26 from ._trustregion_exact import _minimize_trustregion_exact
        ---> 27 from ._trustregion_constr import _minimize_trustregion_constr
             28     29 # constrained minimization
        
        ```
        
        ```
        /usr/local/lib/python3.10/dist-packages/scipy/optimize/_trustregion_constr/__init__.py in <module>
              2      3
        ----> 4 from .minimize_trustregion_constr import _minimize_trustregion_constr
              5      6 __all__ = ['_minimize_trustregion_constr']
        
        ```
        
        ```
        /usr/local/lib/python3.10/dist-packages/scipy/optimize/_trustregion_constr/minimize_trustregion_constr.py in <module>
              3 from scipy.sparse.linalg import LinearOperator
              4 from .._differentiable_functions import VectorFunction
        ----> 5 from .._constraints import (
              6     NonlinearConstraint, LinearConstraint, PreparedConstraint, Bounds, strict_bounds)
              7 from .._hessian_update_strategy import BFGS
        
        ```
        
        ```
        /usr/local/lib/python3.10/dist-packages/scipy/optimize/_constraints.py in <module>
              6 from ._optimize import OptimizeWarning
              7 from warnings import warn, catch_warnings, simplefilter
        ----> 8 from numpy.testing import suppress_warnings
              9 from scipy.sparse import issparse
             10
        ```
        
        ```
        /usr/local/lib/python3.10/dist-packages/numpy/testing/__init__.py in <module>
              9     10 from . import _private
        ---> 11 from ._private.utils import *
             12 from ._private.utils import (_assert_valid_refcount, _gen_alignment_data)
             13 from ._private import extbuild
        
        ```
        
        ```
        /usr/local/lib/python3.10/dist-packages/numpy/testing/_private/utils.py in <module>
             55 IS_PYSTON = hasattr(sys, "pyston_version_info")
             56 HAS_REFCOUNT = getattr(sys, 'getrefcount', None) is not None and not IS_PYSTON
        ---> 57 HAS_LAPACK64 = numpy.linalg._umath_linalg._ilp64
             58     59 _OLD_PROMOTION = lambda: np._get_promotion_state() == 'legacy'
        
        ```
        
        ```
        AttributeError: module 'numpy.linalg._umath_linalg' has no attribute '_ilp64'
        ```
        
    - ✅ using !pip was not the issue, as it also works
        - difference of using %pip vs !pip in colab
            
            In Google Colab, both `%pip` and `!pip` can be used to install Python packages, but there are some key differences between them. Here's a breakdown:
            
            1. **Syntax and Context**:
                - `%pip`: This is a magic command specific to IPython (and by extension, Jupyter notebooks and Colab). It runs within the IPython environment.
                - `!pip`: This is a shell command that runs in a subshell outside the IPython environment. It invokes the system's shell to execute the `pip` command.
            2. **Environment Awareness**:
                - `%pip`: Since it is aware of the IPython environment, it ensures that packages are installed in the correct Python environment associated with the notebook kernel. This helps avoid issues where the notebook kernel and the shell environment might be different.
                - `!pip`: This runs in the shell, which may not be the same environment as the notebook's kernel. This can sometimes lead to discrepancies where a package seems to install successfully but is not available in the notebook.
            3. **Integration with Notebook**:
                - `%pip`: Automatically updates the Python interpreter of the notebook without requiring a restart. It integrates more smoothly with the notebook.
                - `!pip`: May require restarting the kernel to reflect the changes made by installing or updating packages.
            4. **Best Practice**:
                - It is generally recommended to use `%pip` in Jupyter notebooks and Colab because it ensures that the installed packages are available in the notebook's Python environment immediately.
            
            ### Example Usage:
            
            - Using `%pip`:
                
                ```python
                %pip install numpy
                
                ```
                
            - Using `!pip`:
                
                ```python
                !pip install numpy
                
                ```
                
            
            ### Summary:
            
            - **Use `%pip`** for a more reliable and integrated package installation in Colab notebooks.
            - **Use `!pip`** if you need to run shell commands or for scripts that are executed outside of the IPython environment.
            
            Using `%pip` reduces the chances of running into issues related to mismatched environments, making it the preferred choice for package management within Colab.
            
    - ✅ it’s not device var being cuda when loading model or torch grad False either
    - SOLN: In Colab, when running `%pip install sae-lens` before `%pip install umap-learn` , then running `import umap` gives an error “`AttributeError: module 'numpy.linalg._umath_linalg' has no attribute '_ilp64'`". Also running `%pip install umap-learn` before `%pip install sae-lens` , then running `import umap` gives the same error. Of note is that running `%pip install umap-learn` , then running `import umap`, then `%pip install sae-lens` allows the usage of both umap and sae-lens functions without error (but must restart runtime after installing sae-lens to use pyarrow).
    - make issue on saelens repo
        
        [https://github.com/jbloomAus/SAELens/issues/246](https://github.com/jbloomAus/SAELens/issues/246)
        
        - post
            
            **Describe the bug**
            In Colab, when running `%pip install sae-lens` before `%pip install umap-learn` , then running `import umap` gives an error `AttributeError: module 'numpy.linalg._umath_linalg' has no attribute '_ilp64`'.
            
            Also running `%pip install umap-learn` before `%pip install sae-lens`, then running`import umap` gives the same error. Of note is that running `%pip install umap-learn` , then running `import umap`, then `%pip install sae-lens` allows the usage of both umap and sae-lens functions without error (but must restart runtime after installing sae-lens to use pyarrow).
            
            **Code example**
            
            This shows the error message traceback in detail:
            
            [https://colab.research.google.com/drive/15wHJ5URCi4pSqZ9bkVxevk3dJ7eyA4dY?usp=sharing](https://colab.research.google.com/drive/15wHJ5URCi4pSqZ9bkVxevk3dJ7eyA4dY?usp=sharing)
            
            ### Checklist
            
            - [x]  I have checked that there is no similar [issue](https://github.com/jbloomAus/SAELens/issues) in the repo (**required**)
- ✅ run algtop on 1 SAE’s Dweights. [SAE Mapper Explora](SAE%20Mapper%20Explora%2025727d275b3b4da1bd2f67d2a0c30632.md)
    
    [SAE_DW_mapper_explora.ipynb](https://colab.research.google.com/drive/1DFsPl7EFa0SDNjlopjKmtFTcV2PfvGmQ#scrollTo=NwyZqjVONo6H): for 16k, `ts-1L-21M_Wdec`
    
    `ts-1L-21M_Wdec_projection=UMAP_n_cubes=10_perc_overlap=0.1_clusterer=DBSCAN_scaler=MinMaxScaler.html`
    
    - ✅ to interactive html file, mapper plot ts-1L-21M_Wdec
    - ✅ custom labels on interactive HTML mapper graph
        - [how do I get custom labels in kmapper html interactive? Explain each argument in this:](https://chatgpt.com/c/fd549a68-d31e-4162-937c-713f94936c2a)
            
            To get custom labels in the interactive HTML visualization generated by `kmapper`, you can use the `custom_tooltips` argument in the `mapper.visualize` function. This allows you to display additional information about each data point when hovering over it in the visualization. Here's an explanation of each argument used in the `mapper.visualize` function:
            
            1. **graph**:
                - This is the graph object created by the `KeplerMapper` object. It represents the Mapper output, including nodes and edges.
            2. **path_html**:
                - This argument specifies the file path where the HTML file will be saved. In this case, `fileID + ".html"` means the HTML file will be named based on the value of `fileID` with the ".html" extension.
            3. **title**:
                - The title of the HTML visualization. Here, it's set to `fileID`, meaning the title of the visualization will be the same as the value of `fileID`.
            4. **custom_tooltips**:
                - This argument is used to provide custom labels or tooltips for the data points. In this case, `df_close.columns.to_numpy()` suggests that the column names of the dataframe `df_close` are being used as the custom tooltips. This will display these column names when hovering over nodes in the visualization.
            5. **color_values**:
                - This argument is used to specify the values that will determine the color of the nodes. Here, `np.log(per_return+1)` is used, indicating that the logarithm of `per_return` values (plus 1 to avoid taking log of zero) will be used to color the nodes.
            6. **color_function_name**:
                - The name of the color function used in the legend of the visualization. In this case, it's set to 'Log Percent Returns', which will be displayed as the legend title for the color values.
            7. **node_color_function**:
                - This argument specifies how the colors should be aggregated for each node. It accepts an array of functions like `['average', 'std', 'sum', 'max', 'min']`, which determines how the color values for the points within each node are combined. This means each node's color can represent the average, standard deviation, sum, maximum, or minimum of the color values of the points within that node.
            
            Here's how you might call the `mapper.visualize` function with these arguments:
            
            ```python
            import kmapper as km
            import numpy as np
            
            # Assuming graph, fileID, df_close, and per_return are already defined
            mapper = km.KeplerMapper()
            
            # Create the visualization
            mapper.visualize(
                graph,
                path_html=f"{fileID}.html",
                title=fileID,
                custom_tooltips=df_close.columns.to_numpy(),
                color_values=np.log(per_return + 1),
                color_function_name='Log Percent Returns',
                node_color_function=np.array(['average', 'std', 'sum', 'max', 'min'])
            )
            
            ```
            
            This will generate an interactive HTML file where each node can display custom tooltips based on the column names of `df_close`, and the nodes will be colored based on the logarithm of the percent returns.
            
        - how does custom_tooltip work? each node is a cluster, so how does the structure of custom_tooltip  determine what labels are in each cluster? does each cluster contain data points (rows) from original data put into mapper?
            
            The `custom_tooltips` argument in `kmapper`'s `visualize` function is used to provide additional information about each data point within the clusters (nodes) when you hover over them in the interactive HTML visualization. Understanding how this works requires knowledge of how `kmapper` clusters data and how the `custom_tooltips` argument interfaces with these clusters.
            
            ### Understanding Custom Tooltips
            
            1. **Nodes and Clusters**:
                - In `kmapper`, each node in the visualization represents a cluster of data points from the original dataset.
                - The Mapper algorithm projects the data into a lower-dimensional space, applies a covering (e.g., overlapping intervals), and clusters the data within each interval. These clusters become the nodes in the graph.
            2. **Data Points in Nodes**:
                - Each node contains indices of the original data points that fall into that cluster.
                - When hovering over a node in the visualization, you can see the tooltips for all the data points in that cluster.
            3. **Structure of `custom_tooltips`**:
                - `custom_tooltips` should be an array-like structure where each element corresponds to a data point in the original dataset.
                - This array provides the information to display when hovering over nodes. Each entry in `custom_tooltips` can be a string or a more complex object like a list or dictionary, depending on what information you want to show.
            
            ### Example Explanation
            
            Let's say you have a dataset with 100 data points and each data point has a label you want to display. Your `custom_tooltips` array should have 100 elements, each corresponding to a data point in the dataset.
            
            ### Example
            
            Here's an example to illustrate this:
            
            ```python
            import kmapper as km
            import numpy as np
            import pandas as pd
            
            # Example data
            data = np.random.rand(100, 5)  # 100 data points, 5 features each
            labels = np.array(['Point {}'.format(i) for i in range(100)])  # Create custom labels for each data point
            
            # Create a KeplerMapper object
            mapper = km.KeplerMapper()
            
            # Fit and transform the data to create a graph
            projected_data = mapper.fit_transform(data, projection='sum')  # Simple projection for example
            graph = mapper.map(projected_data, clusterer=km.cluster.DBSCAN(eps=0.5, min_samples=3))
            
            # Visualize with custom tooltips
            mapper.visualize(
                graph,
                path_html="example.html",
                title="Example Visualization",
                custom_tooltips=labels,
                color_values=projected_data[:, 0],  # Just an example for color values
                color_function_name='Sum Projection',
                node_color_function=np.array(['average'])
            )
            
            ```
            
            ### How `custom_tooltips` Works
            
            1. **Create Custom Tooltips**:
                - Here, `labels` is an array where each element is a string label corresponding to a data point in `data`.
            2. **Using Custom Tooltips in Visualization**:
                - When `mapper.visualize` is called, it uses the `custom_tooltips` array to provide the tooltips for the nodes.
                - For each node, `kmapper` looks at the indices of the original data points that belong to that node (cluster).
                - It then displays the corresponding elements from `custom_tooltips` for those data points.
            
            ### Displaying Custom Tooltips
            
            When you hover over a node in the HTML visualization, you'll see the tooltips corresponding to all the data points in that node. Each tooltip is taken from the `custom_tooltips` array based on the indices of the data points in the node.
            
            To summarize, the `custom_tooltips` array should have a length equal to the number of data points in your original dataset, with each element providing the desired tooltip information for the corresponding data point. When visualizing, `kmapper` uses these tooltips to show additional information about the data points within each cluster (node) in the interactive HTML visualization.
            
        - [https://kepler-mapper.scikit-tda.org/en/latest/reference/stubs/kmapper.KeplerMapper.html#kmapper.KeplerMapper.visualize](https://kepler-mapper.scikit-tda.org/en/latest/reference/stubs/kmapper.KeplerMapper.html#kmapper.KeplerMapper.visualize)
        - load labels in, and get top token for each feature. load this list as np.array(list) into custom_tooltip
    - summary
        
        Using Mapper, plotted SAE feature weights with labels (highest activating tokens) and found semantically relevant clusters and possible structures (eg. names with pronouns). Must run on SAEs with more monosemantic features that capture more semantically meaningful concepts (eg. king, queen, princess) to assess this. 
        
        - poss struc?
            
            ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%204.png)
            
- 🐣 study params of new Mapper plot
    - What lens was used?
- 🐣 mapper topology questions
    
    [https://chatgpt.com/c/02ab8c4a-2dca-488e-8d1c-a09ac387c707](https://chatgpt.com/c/02ab8c4a-2dca-488e-8d1c-a09ac387c707)
    
    - is umap a filter function or something else in mapper? what about isomap?
        
        UMAP (Uniform Manifold Approximation and Projection) and Isomap (Isometric Mapping) are both dimensionality reduction techniques, but they are not filter functions in the context of the Mapper algorithm. Here's a detailed explanation of each:
        
        ### UMAP
        
        UMAP is a dimensionality reduction technique that is used to project high-dimensional data into a lower-dimensional space (usually 2D or 3D) while preserving as much of the structure of the data as possible. It is not a filter function but rather a standalone technique used for visualizing and understanding high-dimensional data. UMAP works by constructing a high-dimensional graph representation of the data and then optimizing a low-dimensional representation of this graph to maintain the structure.
        
        ### Isomap
        
        Isomap is another dimensionality reduction technique that seeks to preserve the geodesic distances between data points in the high-dimensional space when projecting them to a lower-dimensional space. Like UMAP, Isomap is not a filter function but a technique for embedding high-dimensional data into a lower-dimensional space. Isomap constructs a graph based on the nearest neighbors of the data points and then computes the shortest paths in this graph to approximate the geodesic distances.
        
        ### Mapper Algorithm
        
        The Mapper algorithm is a method used in topological data analysis (TDA) to capture the shape of high-dimensional data. It consists of the following main steps:
        
        1. **Filter Function**: A filter function is applied to the data. This function can be any scalar function that assigns a value to each data point. Common choices include distance functions, density estimators, or other functions capturing interesting aspects of the data.
        2. **Covering**: The range of the filter function is covered with overlapping intervals or bins.
        3. **Clustering**: The data points within each interval are clustered, typically using techniques like k-means or DBSCAN.
        4. **Simplicial Complex Construction**: The clusters are used to construct a simplicial complex, where nodes represent clusters and edges represent non-empty intersections between clusters.
        
        While UMAP and Isomap can be used to preprocess data or as part of the analysis pipeline in TDA, they are not specific to the Mapper algorithm and do not function as filter functions within it. Filter functions in the Mapper algorithm are generally simple scalar functions applied directly to the data points, rather than complex dimensionality reduction techniques.
        
    - if mapper just obtains a graph, how can that be a simp complex that approx a manifold?
        
        The Mapper algorithm produces a graph (or more generally, a simplicial complex) that serves as an approximation of the underlying topological space (or manifold) of the high-dimensional data. Here's a detailed explanation of how this process works:
        
        ### Steps in the Mapper Algorithm
        
        1. **Filter Function Application**: A filter function \( f \) is applied to the high-dimensional data \( X \). This function assigns a scalar value to each data point. Common examples of filter functions include projections onto the first principal component, distance from a point, or density estimators.
        2. **Covering of Filter Function Range**: The range of the filter function \( f(X) \) is divided into overlapping intervals or bins. This overlapping ensures that nearby points in the filter function's range are also considered close in the covering intervals.
        3. **Clustering Within Intervals**: For each interval \( I \) in the covering, the data points whose filter function values lie within \( I \) are selected. These selected points are then clustered using a clustering algorithm such as k-means or DBSCAN. This step effectively groups points that are close in the original high-dimensional space and have similar filter function values.
        4. **Construction of Nodes and Edges**: Each cluster within an interval is represented as a node in the Mapper graph. If clusters from overlapping intervals share common points (i.e., if the intersection of clusters is non-empty), an edge is drawn between the corresponding nodes.
        
        ### Simplicial Complex and Approximation of a Manifold
        
        - **Graph to Simplicial Complex**: While the immediate output of the Mapper algorithm is a graph, this graph can be interpreted as a 1-dimensional simplicial complex (where nodes are 0-simplices and edges are 1-simplices). To build higher-dimensional simplices, one could use the intersections of more clusters from multiple intervals, though this is less common in standard Mapper implementations.
        - **Manifold Approximation**: The Mapper algorithm approximates the manifold by capturing its topological features through the connectivity of the graph. The underlying idea is that the data, although high-dimensional, lies on or near a lower-dimensional manifold. By using the filter function and clustering in overlapping intervals, Mapper captures the structure and connectivity of this manifold.
        
        ### Visualization and Interpretation
        
        - **Topological Features**: The resulting graph from Mapper can reveal topological features such as clusters, loops, and voids, which correspond to 0-dimensional, 1-dimensional, and higher-dimensional holes in the data, respectively. These features are significant in understanding the shape and structure of the underlying manifold.
        - **Insight into Data**: By examining the Mapper graph, one can gain insights into the data's intrinsic geometry and topology. For example, the presence of loops might indicate circular structures, while disconnected components can suggest distinct clusters or regions in the data.
        
        ### Example
        
        Consider a 3D point cloud sampled from a torus. By applying Mapper with an appropriate filter function (e.g., one coordinate projection or distance from a central point), overlapping intervals, and clustering, the resulting graph can reveal the toroidal structure. Clusters corresponding to points on the torus will be connected in a way that reflects the torus's shape, even though the graph itself is a lower-dimensional representation.
        
        In summary, the Mapper algorithm's graph is a simplicial complex that approximates the manifold by capturing its topological structure through the connectivity of clusters. This approach allows for a meaningful reduction of high-dimensional data into a comprehensible topological summary.
        
    - how are higher dim simp complexes that better approx a manifold obtained then? persistent homology? other methods?
        
        Higher-dimensional simplicial complexes that better approximate a manifold can be obtained using various techniques. These techniques build on the idea of capturing the manifold's structure by considering not just pairwise relationships (as in a graph) but also higher-order relationships among data points. Here are some key methods:
        
        ### 1. **Vietoris-Rips Complex**
        
        The Vietoris-Rips complex is a standard method in topological data analysis (TDA) for constructing higher-dimensional simplicial complexes from data:
        
        - **Construction**: Given a set of points and a distance threshold \( \epsilon \), the Vietoris-Rips complex includes a k-simplex for every subset of \( k+1 \) points that are pairwise within distance \( \epsilon \) of each other.
        - **Higher-Dimensional Simplices**: This method naturally incorporates higher-dimensional simplices (triangles, tetrahedra, etc.) based on the proximity of data points.
        
        ### 2. **Cech Complex**
        
        The Cech complex is another method that uses geometric properties to form simplicial complexes:
        
        - **Construction**: For a given set of points and a radius \( r \), the Cech complex includes a k-simplex if the \( k+1 \) points have a common intersection in their \( r \)-radius balls.
        - **Geometric Insight**: The Cech complex provides a close approximation of the underlying manifold when the radius \( r \) is chosen appropriately.
        
        ### 3. **Alpha Complex**
        
        The Alpha complex is a subcomplex of the Delaunay triangulation and is closely related to the Cech complex:
        
        - **Construction**: Given a set of points and a parameter \( \alpha \), the Alpha complex includes simplices that correspond to Delaunay simplices with circumradius less than \( \alpha \).
        - **Manifold Approximation**: The Alpha complex is often a sparser representation than the Vietoris-Rips or Cech complexes, making it computationally efficient while still capturing the topological features of the data.
        
        ### 4. **Witness Complex**
        
        The Witness complex is a data-sparse representation that uses a set of landmark points to build the simplicial complex:
        
        - **Landmark Points**: A subset of data points (landmarks) is chosen to represent the data.
        - **Construction**: The simplicial complex is built based on the distances between landmarks and the remaining points, considering a witness condition.
        - **Efficiency**: This method is efficient for large datasets because it reduces the number of points involved in the complex construction.
        
        ### 5. **Mapper Algorithm with Higher-Dimensional Simplices**
        
        Although the standard Mapper algorithm primarily produces a 1-dimensional simplicial complex (graph), extensions can incorporate higher-dimensional simplices:
        
        - **Overlap and Intersection**: By considering more complex overlaps and intersections among clusters, higher-dimensional simplices can be formed. For example, if three clusters share common points, a 2-simplex (triangle) can be formed.
        - **Clustering**: Using advanced clustering techniques that capture higher-order relationships can help build a more comprehensive simplicial complex.
        
        ### 6. **Persistent Homology**
        
        Persistent homology is a method used to study the multi-scale topological features of data:
        
        - **Filtration**: A nested sequence of simplicial complexes (filtration) is constructed, typically using methods like Vietoris-Rips, Cech, or Alpha complexes with varying parameters.
        - **Persistence**: Persistent homology tracks the birth and death of topological features (connected components, loops, voids) across the filtration.
        - **Stability**: This method provides robust insights into the topological structure and is useful for identifying significant features that persist over multiple scales.
        
        ### Summary
        
        Higher-dimensional simplicial complexes provide a more accurate approximation of a manifold by capturing multi-point interactions and topological features beyond simple pairwise relationships. Methods like Vietoris-Rips, Cech, Alpha, Witness complexes, and extensions of the Mapper algorithm can be used to construct these complexes. Persistent homology is a powerful tool for analyzing the topological features of these complexes across different scales, offering a comprehensive understanding of the underlying manifold.
        
    - so persistent homology doesn't obtain the simp comp, just analyzes their invariant features? computationally/algorithmically how do we get Vietoris-Rips, Cech, Alpha, Witness complexes? doesn't seem like mapper can capture the higher dim properties, only 1D
        
        You're correct that persistent homology is used to analyze the invariant features of simplicial complexes over different scales, rather than to construct the complexes themselves. Below, I'll describe how to computationally and algorithmically obtain various types of simplicial complexes, including Vietoris-Rips, Cech, Alpha, and Witness complexes.
        
        ### Vietoris-Rips Complex
        
        The Vietoris-Rips complex construction is relatively straightforward:
        
        1. **Input**: A set of points \( X \) in a metric space and a distance threshold \( \epsilon \).
        2. **Pairwise Distances**: Compute the pairwise distances between all points in \( X \).
        3. **Simplex Construction**: For each subset of \( k+1 \) points, add a k-simplex to the complex if the pairwise distances between all points in the subset are less than \( \epsilon \).
        
        Algorithmically, this involves:
        
        - Creating a distance matrix for the points.
        - Iterating over all subsets of points to check the pairwise distances.
        - Adding the corresponding simplices to the complex if the condition is satisfied.
        
        ### Cech Complex
        
        The Cech complex requires checking for common intersections of balls centered at data points:
        
        1. **Input**: A set of points \( X \) and a radius \( r \).
        2. **Geometric Intersection**: For each subset of \( k+1 \) points, add a k-simplex to the complex if the \( r \)-balls centered at these points have a non-empty common intersection.
        
        Computationally:
        
        - This involves geometric calculations to check for ball intersections.
        - Typically, this is done using computational geometry libraries or packages.
        
        ### Alpha Complex
        
        The Alpha complex is constructed based on the Delaunay triangulation:
        
        1. **Input**: A set of points \( X \) and a parameter \( \alpha \).
        2. **Delaunay Triangulation**: Compute the Delaunay triangulation of the points.
        3. **Circumradius Condition**: Include simplices from the Delaunay triangulation whose circumradius is less than \( \alpha \).
        
        This involves:
        
        - Computing the Delaunay triangulation using algorithms like Quickhull.
        - Filtering simplices based on the circumradius condition.
        
        ### Witness Complex
        
        The Witness complex uses a subset of landmarks to represent the data:
        
        1. **Input**: A set of points \( X \), a subset of landmarks \( L \subset X \), and a parameter \( \epsilon \).
        2. **Witness Condition**: For each k-simplex formed by landmarks, check if there are points in \( X \) (witnesses) that are within distance \( \epsilon \) to all vertices of the simplex.
        
        Algorithmically:
        
        - Select landmarks (randomly or using a heuristic like k-means centroids).
        - Check the witness condition for all possible simplices formed by landmarks.
        
        ### Software and Libraries
        
        Several libraries and software packages can construct these complexes and compute persistent homology:
        
        - **GUDHI (Geometry Understanding in Higher Dimensions)**: A comprehensive library for TDA that supports the construction of Vietoris-Rips, Alpha complexes, and more.
        - **Ripser**: Specialized for computing Vietoris-Rips complexes and persistent homology.
        - **Dionysus**: A library for computing persistent homology and working with various simplicial complexes.
        
        ### Mapper Algorithm
        
        As you've noted, the standard Mapper algorithm primarily captures 1-dimensional topological features. However, it can be extended to capture higher-dimensional properties by considering more complex overlaps and using higher-dimensional clustering techniques. These extensions are not as common and can be more challenging to implement.
        
        ### Summary
        
        Persistent homology analyzes the invariant features of simplicial complexes, while the complexes themselves are constructed using methods like Vietoris-Rips, Cech, Alpha, and Witness complexes. Each of these methods has specific computational algorithms and existing libraries to facilitate their construction. Mapper typically captures 1-dimensional structures, but higher-dimensional simplicial complexes can be obtained through the methods described above for a more detailed approximation of the underlying manifold.
        
    
    [https://math.stackexchange.com/questions/4697360/when-is-simplicial-complex-a-manifold](https://math.stackexchange.com/questions/4697360/when-is-simplicial-complex-a-manifold)
    
    - [https://chatgpt.com/c/a395f4d2-cd3d-4b26-9485-c07629f8f782](https://chatgpt.com/c/a395f4d2-cd3d-4b26-9485-c07629f8f782)
        - Does a simplicial complex always approx a manifold
            
            A simplicial complex does not always approximate a manifold, but under certain conditions, it can approximate a manifold closely. To understand this better, let's look at the definitions and key conditions involved:
            
            1. **Simplicial Complex**: A simplicial complex is a set made up of points, line segments, triangles, and their higher-dimensional counterparts (simplices) that are glued together in a specific way. It must satisfy the conditions that every face of a simplex in the complex is also a simplex in the complex and the intersection of any two simplices in the complex is a face of each of them.
            2. **Manifold**: A manifold is a topological space that locally resembles Euclidean space. More formally, an \(n\)-dimensional manifold is a space where each point has a neighborhood that is homeomorphic to an open subset of \(\mathbb{R}^n\).
            
            ### Approximation Conditions
            
            For a simplicial complex to approximate a manifold, certain conditions must be met:
            
            - **Dimension Matching**: The simplicial complex must have the same dimension as the manifold it approximates. For example, a 2-dimensional manifold would require a 2-dimensional simplicial complex for proper approximation.
            - **Piecewise Linearity**: The manifold should be piecewise linear (PL-manifold). A PL-manifold is a manifold with an atlas such that all transition maps are piecewise linear. In such cases, the manifold can be triangulated, meaning it can be represented as a simplicial complex.
            - **Local Homeomorphism**: Each simplex must be locally homeomorphic to a Euclidean space of the same dimension. This ensures that the local structure of the simplicial complex mimics that of the manifold.
            
            ### Simplicial Approximation Theorem
            
            The simplicial approximation theorem states that any continuous map from a simplicial complex to a topological space can be approximated by a simplicial map, provided certain conditions are satisfied. This theorem is often used to approximate continuous maps between topological spaces by simpler combinatorial objects.
            
            ### Triangulation of Manifolds
            
            One of the key results related to this topic is the existence of a triangulation for manifolds. This result states that every manifold can be triangulated, meaning it can be represented as a simplicial complex. However, this result is more complicated in higher dimensions:
            
            - For dimensions \( \leq 3 \), every manifold can be triangulated in a way that every triangulation is PL-equivalent.
            - For dimension \( 4 \), not every 4-manifold can be triangulated.
            - For dimensions \( > 4 \), the situation is even more complex, and there are manifolds that cannot be triangulated.
            
            ### Practical Considerations
            
            In practical applications, such as numerical simulations and computer graphics, simplicial complexes (often in the form of meshes) are used to approximate manifolds. These approximations work well in practice when the simplicial complex is sufficiently fine (i.e., has a large number of small simplices), ensuring that the local geometry closely matches that of the manifold.
            
            ### Conclusion
            
            While simplicial complexes can often approximate manifolds, this is not always guaranteed without meeting specific conditions such as dimension matching and local homeomorphism. The approximation is highly dependent on the properties of the manifold and the simplicial complex in question.
            
        - does the mapper algo create a s c that approx a manifold well
            
            The Mapper algorithm is a tool from topological data analysis (TDA) that creates a simplicial complex from a data set. Its goal is to provide a simplified representation of the underlying topological structure of the data. Whether this simplicial complex approximates a manifold well depends on several factors.
            
            ### Mapper Algorithm Overview
            
            The Mapper algorithm works as follows:
            
            1. **Filter Function**: Choose a filter function (or lens) that maps data points to a lower-dimensional space. This function is typically chosen to reveal some structure in the data.
            2. **Covering**: Cover the range of the filter function with overlapping intervals or regions.
            3. **Clustering**: Within each region, cluster the data points that fall into that region.
            4. **Nerve Construction**: Construct a simplicial complex called the nerve of the cover. Each cluster forms a node, and nodes are connected if their corresponding clusters have non-empty intersections.
            
            ### Factors Influencing the Quality of Approximation
            
            The ability of the Mapper algorithm to approximate a manifold well depends on several factors:
            
            1. **Choice of Filter Function**: The filter function significantly affects the resulting simplicial complex. A well-chosen filter function that captures the essential features of the data is crucial for creating a meaningful approximation.
            2. **Covering and Overlap**: The way the range of the filter function is covered by intervals or regions and the amount of overlap between them also influence the quality of the approximation. Too few intervals may lead to a loss of detail, while too many may result in noise.
            3. **Clustering Method**: The clustering algorithm used within each interval affects the resulting nodes of the simplicial complex. The clusters should reflect the true local structure of the data.
            4. **Density and Distribution of Data Points**: The density and distribution of the data points influence how well the Mapper complex can capture the manifold's structure. If the data points densely and uniformly sample the manifold, the approximation will be better.
            
            ### Mapper and Manifold Approximation
            
            When the conditions are right (appropriate filter function, sufficient and well-chosen intervals, effective clustering), the Mapper algorithm can create a simplicial complex that provides a useful approximation to the manifold structure of the data. However, it does not always guarantee a good approximation due to:
            
            - **Dimensionality**: The Mapper algorithm reduces dimensionality through the filter function, which can lead to loss of information.
            - **Resolution**: The granularity of the intervals and clustering impacts the resolution of the approximation.
            - **Noise Sensitivity**: The algorithm can be sensitive to noise in the data, which can distort the resulting simplicial complex.
            
            ### Practical Use
            
            In practice, the Mapper algorithm is a powerful tool for visualizing and understanding the shape of complex data sets, especially when the underlying structure is not well understood. It is particularly useful in exploratory data analysis, where capturing the general topological features is more important than precise manifold approximation.
            
            ### Conclusion
            
            The Mapper algorithm can create a simplicial complex that approximates a manifold well under certain conditions. The quality of the approximation depends on the choice of filter function, covering strategy, clustering method, and the characteristics of the data set. While not always perfect, Mapper is a valuable tool in topological data analysis for revealing the topological structure of data.
            
- ✅ analyze new Mapper plot
    - looks like a constellation
    - “upon” is still isolated as a cluster
    - many of the nodes with many connections in “subgraph communinties” seem polysemantic and big clusters (explains why so much overlap, hence edges)
        - do they form these edges as they all overlap on the same features? (eg. the “.” or the “one” community subgraphs)
        - the “one” subgraph is wing on bottom, and “.” subgraph is wing on top. is their path/etc distance similar across model’s feature spaces?
            
            ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%205.png)
            
- ✅ compare mapper graphs of 1L and 2L, 16k MLP0
    - both models have a “one” subgraph
        - 1L
            
            ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%206.png)
            
        - 2L
            
            ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%207.png)
            
        - there are 5 nodes in the 1L subgraph, and 4 nodes in the 2L subgraph. The common nodes seem to form a “tetrahedron-like” (connectivity wise, but in 2D) subgraph, and the 1L has 5 nodes as it has a “dangling” node which contains 20 features. The 1L clusters have around 40-100 features, while the 2L clusters have around 200.
    - 1L has “.” subgraph, and 2L has “,” subgraph
        - 1L
            
            ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%208.png)
            
        - 2L
            
            ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%209.png)
            
    - What’s the “path distance” from say the “one” community subgraph to the “.” community subgraph across models?
        
        
    - Both models have a “tail” containing two “a” feature clusters, though this tail is longer in the 1L model. The tails in both feature spaces seems separated by the wings with many “polysemantic” clusters of unrelated features in between.
        - 1L
            
            ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%2010.png)
            
        - 2L
            
            ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%2011.png)
            
    - summary (msg to kiho)
        
        here's the (very crude) plots for 2 models if you want to explore them in a browser (just open them). they look like creatures with heads/wings/tails. they form similar subgraph communities such as "one" or "." that seem to be on the "wings" of both models, but this is not precise and is a rough qualitative observation that is subject to an illusion. will investigate more and measure with more rigorous metohds like  Multi-Scale Intrinsic Distance
        
    - there’s a leaf in both models that’s a feel feature
        - 1L
            
            ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%2012.png)
            
        - 2L
            
            ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%2013.png)
            
- ✅ mapper on pretrained gpt-2 saelens models
    - ✅ download L8 labels from : [https://www.neuronpedia.org/gpt2sm-res-jb](https://www.neuronpedia.org/gpt2sm-res-jb)
    
    [mapper_pretrained_saelens_dw.ipynb](https://colab.research.google.com/drive/1Dj41zt3JLqxImeZub6w7XEI95Qj07KkS)
    
    - ✅ load labels as json and parse into single string for each feature
    - ✅ get SAE weights: save as saelens takes longer to load than mapper
        - CM_pretrained_SAE_save_actvs.ipynb
    - just run them thru mapper to get html
    - analyze
        - really big and scattered, not a very large conn component cluster like in the ts models
        - there’s a structure (cluster) corresponding to phrases/nouns
            
            ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%2014.png)
            
- study mapper theory: [SAE AlgTop](SAE%20AlgTop%209dda4810e41c4eaf91002696758eb4a3.md)
    
    

---

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

[when comparing the similarity of two feature spaces in neural network activations to see if they learn similar feature relations, can we compare the subgraphs of their mapper graphs of their activations or weights?](https://chatgpt.com/c/370df1cc-39da-4416-8d86-15b4caf8d915)

[https://kepler-mapper.scikit-tda.org/en/latest/html-visualization-features.html](https://kepler-mapper.scikit-tda.org/en/latest/html-visualization-features.html)

How come we don't see circular months in umap with number features?

Train on small dataset sith king queen etc to ensure those are captured. Ask gpt etc if this makes sense

Alt projects

Sim metrics, TDA, and func sim are NOT just for ‘across models’, but for feature splitting WITHIN a model. Map between SAEs. What properties of the manifold / simplicial complex change across feature splitting?

Also, WITHIN an SAE, can map analogous structures (eg. months to days, or king-queen to father-mother). Find similar subspaces within/across layers, mapping how they change over layers or during training.

(future work): These sim metrics / topological properties, once found and studied, may be used in loss functions to optimize the model towards learning certain beneficial topological arrangements

Train SAEs to learn specific, separate royal family features

- PLAN: our tools (corr, dataset exmps, umap, etc) have been shown to work. now, we need better datasets and models that show fs
    - once get better saes with fs concepts, color code multiple concepts- king queen princess- and check their relations across models
        - train on that specific data, on large sae, to ensure it learns them separately

Repr Sim

- CKA
- MNN

[https://openreview.net/pdf?id=gG5UGgUzDR](https://openreview.net/pdf?id=gG5UGgUzDR)

Florian Lemmerich, Max Klabunde

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
- cca on feature actvs
- mutual NN on weights and actvs? no; can only do on inputs (tokens)
    - if pts are features, perhaps we can’t use mnn. only makes sense if we plot the tokens in a projected down feature space.
        - indeed, algtop was applied on input pts, NOT neurons as pts! same with activation atlas!
- can cka be done on unpaired points in space? cca can, but mnn needs points that correspond to same input
    
    [https://claude.ai/chat/ef520765-10d0-4aed-8087-eaab5947af59](https://claude.ai/chat/ef520765-10d0-4aed-8087-eaab5947af59)
    
    [https://chatgpt.com/c/0f959dee-0a79-4333-b14d-8d0b130b658e](https://chatgpt.com/c/0f959dee-0a79-4333-b14d-8d0b130b658e)
    
    chatgpt is WRONG; it says cca needs paired. claude says doesn’t need paired.
    
- ask bloom if it makes sense to use cca on a feature subset
    
    tried it and got high values
    
- ask huh about why use knn over cka

- ISSUE: you’re including that feature as “activating on” that keyword if it contains it. But perhaps the majority of the top 5 (or top 10) should contain it

- plot feature subset
- use multiple keywords, each with different color
- instead of color, put a label box around the points in each plot

- in a box outside plot, display the other model’s pair
- compare subspace scores to random subspace pairs. ask chatgpt for how to better stat tests
- Then, higher-order graphs of keyword subspaces. It’s not enough to just plot the subspace of Dragon to subspace of Dragon; it’s the subspace of {Dragon, Princess}, as that’s relation of Dragon to Princess. Or {he, she}

- save using saelens

---

Multiple feature circuits

- are those features in a cluster/subgraph involved as a single component in a circuit?

---

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

- re-run SAE_2 save actvs bc used `sae.encode` instead of `sae_2.encode`
    - now nonzeroes is closer to sae_1’s 0.12%; it’s 0.2% rather than 35%

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
        
        ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%2015.png)
        
        ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%2016.png)
        

**generalize this procedure to find other structures: ablate by clusters (elements in simplices)**

Observe steering diffs on split features

Steer nonlinear months

Mapping algo: map based on both repr and func sim. May be a diffeomorphism or some other type of deformation mapping?

- toy model 20B token train feas
    
    ![Untitled](Project%20Planning%20b4b05f73d85e409f8409b209e44ed692/Untitled%2017.png)
    

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

if impl succeed (whether neg or pos outcomes), copy todo into here and org into expms:

[Feature actvs on tinystories SAEs](Feature%20actvs%20on%20tinystories%20SAEs%208688850817e34618b8d9347574d66397.md) 

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

people to contact:

- bei wang group
- “not all features are linear”
- cca people (hinton group)
- ask bloom for tips on better interactive umap viz

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

- 8/8: contact anthropic
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