# AlgTop Explora

- ✅ look into topology mapper in python
    - ✅ topoact github is just html code, no algtop algos
    - tell chatgpt to read Towards and Topoact, then: “Given those two papers, how would you design experiments and code to apply mapper to feature activations? Given setup details”
        
        [https://chatgpt.com/c/42f8db48-047d-44d9-8283-95a81e980ba7](https://chatgpt.com/c/42f8db48-047d-44d9-8283-95a81e980ba7)
        
        - how do i adopt mapper to be used on the feature activations of a sparse autoencoder, in which the features are a pytorch tensor of (batch, seqlen, featuredim), obtained by the code: feature_acts = sae.encode(h_store) ? Refer to the attached python code for how to get sae features.
            
            `tinystories_actv_save_v2.ipynb as .py`
            
        - explain all the code from 3. Mapper Construction onwards in detail and intuitively, using analogies when needed for non trivial concepts
            
            ### 3. Mapper Construction
            
            ### Create Cover
            
            We start by dividing the data into overlapping regions (cover sets), which helps us understand local structures and how they connect globally.
            
            ### Code Explanation
            
            ```python
            def create_cover(filtered, intervals, overlap):
                min_val, max_val = np.min(filtered, axis=0), np.max(filtered, axis=0)
                steps = (max_val - min_val) / (intervals - 1) * (1 + overlap)
                cover = []
                for i in range(intervals):
                    for j in range(intervals):
                        cover.append(((min_val[0] + i * steps[0], min_val[0] + (i + 1) * steps[0]),
                                      (min_val[1] + j * steps[1], min_val[1] + (j + 1) * steps[1])))
                return cover
            
            ```
            
            - **Filtered**: The reduced-dimension data (e.g., from PCA).
            - **Intervals**: Number of intervals to divide each dimension into.
            - **Overlap**: Degree of overlap between intervals.
            - **Steps**: Calculated based on the range of data values and overlap.
            
            We create a grid of intervals in the lower-dimensional space and store these as pairs of ranges.
            
            ### Intuition
            
            Imagine spreading a mesh net over a terrain (our data). The intervals define the mesh's squares, and overlap ensures the squares cover the terrain more smoothly.
            
            ### Cluster Within Cover Sets
            
            For each cover set, cluster the data points that fall within it. This helps in identifying local groupings of data.
            
            ### Code Explanation
            
            ```python
            def cluster_cover(cover, filtered, activations):
                clusters = []
                for (x_range, y_range) in cover:
                    indices = np.where((filtered[:, 0] >= x_range[0]) & (filtered[:, 0] < x_range[1]) &
                                       (filtered[:, 1] >= y_range[0]) & (filtered[:, 1] < y_range[1]))[0]
                    if len(indices) > 0:
                        clustering = DBSCAN().fit(activations[indices])
                        clusters.append((indices, clustering.labels_))
                return clusters
            
            ```
            
            - **DBSCAN**: A clustering algorithm that groups points closely packed together, marking outliers.
            - **Indices**: Points falling within the cover set.
            - **Clusters**: Each cover set’s clustered points.
            
            ### Intuition
            
            Think of the mesh net's squares as neighborhoods. We examine each neighborhood to find clusters of houses (data points) that are close together, ignoring outliers.
            
            ### 4. Topological Summary
            
            ### Construct Mapper Graph
            
            We build a graph representing the clusters and their connections.
            
            ### Code Explanation
            
            ```python
            import networkx as nx
            
            def construct_mapper_graph(clusters):
                G = nx.Graph()
                for idx, (indices, labels) in enumerate(clusters):
                    for label in np.unique(labels):
                        if label != -1:
                            cluster_indices = indices[labels == label]
                            G.add_node((idx, label), members=cluster_indices)
                for i, (indices1, labels1) in enumerate(clusters):
                    for j, (indices2, labels2) in enumerate(clusters):
                        if i < j:
                            common_indices = np.intersect1d(indices1, indices2)
                            if len(common_indices) > 0:
                                for label1 in np.unique(labels1):
                                    if label1 != -1:
                                        members1 = indices1[labels1 == label1]
                                        for label2 in np.unique(labels2):
                                            if label2 != -1:
                                                members2 = indices2[labels2 == label2]
                                                if len(np.intersect1d(members1, members2)) > 0:
                                                    G.add_edge((i, label1), (j, label2))
                return G
            
            mapper_graph = construct_mapper_graph(clusters)
            
            ```
            
            - **Nodes**: Represent clusters in each cover set.
            - **Edges**: Connect clusters sharing data points across different cover sets.
            
            ### Intuition
            
            Imagine a social network where each node is a group of friends (clusters), and an edge represents shared friends (common data points) between groups.
            
            ### 5. Visualization
            
            ### Visualizing the Graph
            
            Use a spring layout to visualize the constructed graph.
            
            ### Code Explanation
            
            ```python
            import matplotlib.pyplot as plt
            
            pos = nx.spring_layout(mapper_graph)
            nx.draw(mapper_graph, pos, with_labels=True, node_size=50, node_color="blue")
            plt.show()
            
            ```
            
            - **Spring Layout**: Positions nodes based on simulated physical forces to enhance visualization clarity.
            - **Draw**: Visualizes the graph with nodes and edges.
            
            ### Intuition
            
            Visualize the network as a map of cities (clusters) connected by roads (edges). The spring layout helps position cities so that the map is clear and roads are easy to follow.
            
            ### Conclusion
            
            This process creates a simplified representation of high-dimensional data using the Mapper algorithm, providing insights into the structure and relationships within the data. Each step, from cover creation to graph visualization, helps in understanding complex data in a more intuitive way.
            
    - mapper_fAct_explora.ipynb
        - compare to random data
        - is empty plot always a bug? where did the pts go? do you expect random data to all be noise and thus have empty plot?
            
            When applying the Mapper algorithm to random data, it is not necessarily expected that all data will be classified as noise, resulting in an empty plot. However, it is common because random data lacks structure. Here are some points to consider:
            
            ### Expectation for Random Data
            
            1. **Lack of Structure**:
                - Random data often does not have the dense regions necessary for clustering algorithms like DBSCAN to form clusters.
                - This can result in many points being labeled as noise (`1`).
            2. **Parameter Sensitivity**:
                - The clustering parameters (`eps` and `min_samples` in DBSCAN) might not be suitable for the random data.
                - Random data might require different settings to form clusters, though meaningful clusters may still not be found.
            3. **Real-World Data vs. Random Data**:
                - Real-world data typically has inherent patterns and structures, making it more likely to form meaningful clusters.
                - Random data lacks such patterns, leading to more points being identified as noise.
            
            ### Practical Steps
            
            - **Verify Data Distribution**: Check the distribution of your random data.
                
                ```python
                plt.scatter(filtered_random_data[:, 0], filtered_random_data[:, 1], alpha=0.5)
                plt.title("Filtered Random Data Points")
                plt.xlabel("PCA Component 1")
                plt.ylabel("PCA Component 2")
                plt.show()
                
                ```
                
            - **Adjust Clustering Parameters**:
                
                ```python
                random_clusters = cluster_cover(random_cover, filtered_random_data, reshaped_random_data, eps=0.3, min_samples=3)
                
                ```
                
            - **Check Clusters**:
                
                ```python
                for idx, (indices, labels) in enumerate(random_clusters):
                    print(f"Cluster {idx}: {len(indices)} points, labels: {np.unique(labels)}")
                
                ```
                
            
            ### Example
            
            If you still encounter an empty plot after adjustments, it suggests that the random data does not form clusters under the given parameters. This is typical and highlights the contrast between structured real-world data and random noise, validating the effectiveness of the Mapper algorithm in capturing meaningful structures in real data.
            
            By experimenting with different parameters and visualizing the data, you can better understand the behavior of random data in comparison to real data and the appropriateness of clustering algorithms like DBSCAN.
            
        - i got this for feature activations. are activations usually in a circle? if not what could this mean
            
            Activations typically are not expected to form a perfect circle. If your feature activations form a circular pattern, it could indicate several things:
            
            1. **Dimensionality Reduction Artifact**: If you used PCA or another dimensionality reduction technique, the circular pattern might result from how the algorithm projected the data into a lower-dimensional space.
            2. **Periodic Structure in Data**: The underlying data might have periodicity or cyclical patterns that are being captured in the activations.
            3. **Model Regularity**: The model might have learned a regular, cyclical pattern from the training data, which is reflected in the activations.
            
            ### Steps to Investigate Further
            
            1. **Verify Dimensionality Reduction**:
                - Check the explained variance ratio of the PCA components to ensure that the circle is not an artifact of the reduction process.
                
                ```python
                print(pca.explained_variance_ratio_)
                
                ```
                
            2. **Analyze the Source Data**:
                - Investigate the input data to see if there are any inherent periodic or cyclic patterns.
                
                ```python
                plt.plot(h_store[0].detach().numpy())  # Example for the first sequence
                plt.title("Input Data Sample")
                plt.show()
                
                ```
                
            3. **Check Model Training**:
                - Ensure that the model training process did not introduce regularities that might cause this pattern.
                - Check for overfitting or regularization artifacts.
            4. **Compare with Random Data**:
                - Generate random data and pass it through the model to see if a similar circular pattern appears.
                
                ```python
                random_data = np.random.randn(*h_store.shape)
                random_activations = sae.encode(torch.from_numpy(random_data).float())
                filtered_random_data = pca.transform(random_activations.view(-1, featuredim).detach().numpy())
                plt.scatter(filtered_random_data[:, 0], filtered_random_data[:, 1], alpha=0.5)
                plt.title("Filtered Random Data Points")
                plt.show()
                
                ```
                
            
            ### Conclusion
            
            While a circular pattern in activations is unusual, it's essential to analyze the steps leading to this result and verify if it's due to the model, the data, or the dimensionality reduction technique. By performing these checks, you can better understand the cause and take appropriate steps to address any issues.
            
        - how do i plot the pca before mapper
        - what do the indices on this plot mean?
            
            The indices on this plot likely represent the clusters and their labels as identified by the Mapper algorithm. In the format `(x, y)`, each pair can be interpreted as follows:
            
            1. **Cluster Index (`x`)**: This is the index of the cover set in which the cluster was found. Cover sets are created during the Mapper construction process by dividing the data space into overlapping regions.
            2. **Cluster Label (`y`)**: This is the label assigned by the clustering algorithm (e.g., DBSCAN) within that cover set. Each unique label represents a distinct cluster, and `1` typically indicates noise or outliers.
            
            Given the circular arrangement, this pattern likely results from how the data was reduced and clustered, with each node representing a cluster from a specific cover set and showing how they connect.
            
            In summary, the indices `(x, y)` indicate which cover set (region of the data space) a cluster belongs to (`x`) and the cluster label within that cover set (`y`). This representation helps in understanding the topological relationships between different clusters in the data.
            
        - the feature actvs were of shape torch.Size([195, 128, 16384]). why are they so few pts in mapper plot? also, why isn't the mapper plot a graph with edges?
            
            Given your feature activations are of shape `torch.Size([195, 128, 16384])`, there are a few reasons why you might see only a few points and no edges in the Mapper plot:
            
            ### 1. Dimensionality Reduction Impact
            
            The high dimensionality of the feature activations (16384 dimensions) is drastically reduced to 2 dimensions using PCA. This could result in loss of significant structural information, leading to fewer meaningful clusters.
            
            ### 2. Clustering Parameters
            
            The DBSCAN parameters (`eps` and `min_samples`) might not be optimal for the reduced data, causing many points to be labeled as noise (`-1`). Adjusting these parameters could help.
            
            ### 3. Overlapping Cover Sets
            
            The choice of cover intervals and overlap affects how many points fall into multiple cover sets, influencing the number of clusters formed.
            
            ### 4. Graph Construction
            
            For edges to appear, there must be shared points between clusters across cover sets. If no such shared points exist, no edges will be drawn.
            
            ### Detailed Steps to Address These Issues
            
            ### 1. Verify Dimensionality Reduction
            
            Ensure that the PCA retains enough variance:
            
            ```python
            from sklearn.decomposition import PCA
            
            # Perform PCA and check explained variance ratio
            pca = PCA(n_components=2)
            pca_acts = pca.fit_transform(reshaped_acts)
            print(pca.explained_variance_ratio_)
            
            ```
            
            Ensure enough variance is captured, or consider increasing the number of components and then using t-SNE or UMAP for 2D visualization.
            
            ### 2. Adjust DBSCAN Parameters
            
            Experiment with different `eps` and `min_samples`:
            
            ```python
            from sklearn.cluster import DBSCAN
            
            def cluster_cover(cover, filtered, activations, eps=0.5, min_samples=5):
                clusters = []
                for idx, (x_range, y_range) in enumerate(cover):
                    indices = np.where((filtered[:, 0] >= x_range[0]) & (filtered[:, 0] < x_range[1]) &
                                       (filtered[:, 1] >= y_range[0]) & (filtered[:, 1] < y_range[1]))[0]
                    if len(indices) > 0:
                        clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(activations[indices])
                        clusters.append((idx, clustering.labels_))
                return clusters
            
            # Adjust eps and min_samples
            random_clusters = cluster_cover(random_cover, filtered_acts, reshaped_acts, eps=0.3, min_samples=3)
            
            ```
            
            ### 3. Visualize PCA Before Applying Mapper
            
            ```python
            import matplotlib.pyplot as plt
            
            plt.scatter(pca_acts[:, 0], pca_acts[:, 1], alpha=0.5)
            plt.title("PCA of Feature Activations")
            plt.xlabel("Principal Component 1")
            plt.ylabel("Principal Component 2")
            plt.show()
            
            ```
            
            ### 4. Verify Mapper Graph Construction
            
            Check if nodes and edges are being added correctly:
            
            ```python
            import networkx as nx
            
            def construct_mapper_graph(clusters):
                G = nx.Graph()
                for idx, (indices, labels) in enumerate(clusters):
                    for label in np.unique(labels):
                        if label != -1:
                            cluster_indices = indices[labels == label]
                            G.add_node((idx, label), members=cluster_indices)
                for i, (indices1, labels1) in enumerate(clusters):
                    for j, (indices2, labels2) in enumerate(clusters):
                        if i < j:
                            common_indices = np.intersect1d(indices1, indices2)
                            if len(common_indices) > 0:
                                for label1 in np.unique(labels1):
                                    if label1 != -1:
                                        members1 = indices1[labels1 == label1]
                                        for label2 in np.unique(labels2):
                                            if label2 != -1:
                                                members2 = indices2[labels2 == label2]
                                                if len(np.intersect1d(members1, members2)) > 0:
                                                    G.add_edge((i, label1), (j, label2))
                return G
            
            random_mapper_graph = construct_mapper_graph(random_clusters)
            print(nx.info(random_mapper_graph))
            
            # Visualize the Mapper graph
            pos = nx.spring_layout(random_mapper_graph)
            nx.draw(random_mapper_graph, pos, with_labels=True, node_size=50, node_color="blue")
            plt.title("Mapper Graph")
            plt.show()
            
            ```
            
            ### Conclusion
            
            The fewer points and lack of edges indicate that most points are considered noise or not shared between clusters. Adjusting parameters and ensuring proper data preprocessing can help in obtaining a more meaningful Mapper graph.
            

---

[https://medium.datadriveninvestor.com/the-mapper-algorithm-d0842f926658](https://medium.datadriveninvestor.com/the-mapper-algorithm-d0842f926658)

[https://www.youtube.com/watch?v=NlMrvCYlOOQ&t=380s&ab_channel=ShawTalebi](https://www.youtube.com/watch?v=NlMrvCYlOOQ&t=380s&ab_channel=ShawTalebi)

[https://github.com/ShawhinT/YouTube-Blog/tree/main/TDA/mapper](https://github.com/ShawhinT/YouTube-Blog/tree/main/TDA/mapper)

- python tutorial mapper on Dweights
    
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

---

[https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2021.667963/full](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2021.667963/full)

---

https://github.com/tdavislab/TopoBERT/blob/master/backend/server/graph_generator.py

This uses kmapper

---

[https://kepler-mapper.scikit-tda.org/en/latest/](https://kepler-mapper.scikit-tda.org/en/latest/)

---

[https://colab.research.google.com/github/shizuo-kaji/TutorialTopologicalDataAnalysis/blob/master/TopologicalDataAnalysisWithPython.ipynb#scrollTo=wZrYYnSFynJS](https://colab.research.google.com/github/shizuo-kaji/TutorialTopologicalDataAnalysis/blob/master/TopologicalDataAnalysisWithPython.ipynb#scrollTo=wZrYYnSFynJS)

---

[https://www.kaggle.com/code/lavasesha/topological-data-analysis-using-keppler-mapper](https://www.kaggle.com/code/lavasesha/topological-data-analysis-using-keppler-mapper)