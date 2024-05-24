# Feature clustering

[feature_trees_public](https://colab.research.google.com/drive/19k5r2lNvO1gzL1Zsek3EzJR1vT7sZO4g)

- what is the linkage matrix
    
    The linkage matrix encodes the hierarchical relationship between clusters as they are merged step-by-step.
    
    ### Structure of a Linkage Matrix
    
    A linkage matrix is a 2D array with shape `(n-1, 4)` for `n` original observations (data points). Each row of the matrix represents a step in the hierarchical clustering process where two clusters are merged. The four columns of each row typically contain the following information:
    
    1. **Index of the first cluster**: The index of the first cluster being merged.
    2. **Index of the second cluster**: The index of the second cluster being merged.
    3. **Distance between clusters**: The distance (dissimilarity) between the two clusters being merged.
    4. **Number of original observations**: The total number of original observations in the newly formed cluster.
    
    ### Example
    
    Suppose you have 5 observations to cluster. The linkage matrix might look like this after the clustering process:
    
    (start with 5 clusters)
    
    | Cluster 1 | Cluster 2 | Distance | Observations |
    | --- | --- | --- | --- |
    | 0 | 1 | 0.5 | 2 |
    | 2 | 3 | 0.7 | 2 |
    | 4 | 5 | 1.2 | 3 |
    | 6 | 7 | 1.5 | 5 |
    - **First row**: Clusters 0 and 1 are merged with a distance of 0.5, resulting in a new cluster with 2 original observations.
    - **Second row**: Clusters 2 and 3 are merged with a distance of 0.7, resulting in another new cluster with 2 original observations.
    - **Third row**: The newly formed cluster (index 5) and observation 4 are merged with a distance of 1.2, resulting in a cluster with 3 original observations.
    - **Fourth row**: The two previously formed clusters (indices 6 and 7) are merged with a distance of 1.5, forming the final cluster that includes all 5 observations.
    
    ### Usage
    
    In hierarchical clustering, the linkage matrix is used to:
    
    - **Build Dendrograms**: A dendrogram is a tree-like diagram that visualizes the hierarchy of clusters formed during the clustering process. Each node represents a cluster, and branches represent the steps of merging clusters as shown by the linkage matrix.
    - **Determine Cluster Membership**: By cutting the dendrogram at different levels, you can create different numbers of clusters. For example, cutting at a higher level (greater distance) results in fewer clusters, while cutting at a lower level (smaller distance) results in more clusters.
    - **Analyze Clustering Steps**: The linkage matrix allows you to inspect the sequence of merges and understand how clusters are formed based on the distance metric used.
    
    In the provided code, the linkage matrices are computed for different hierarchical clustering methods ('average', 'complete', 'weighted') using the `hierarchy.linkage` function from the SciPy library. Each matrix captures the hierarchical clustering process for the data in each layer of the `decoders` tensor.
    

This is the distance between clusters, with a hierarchy of “superclusters” being clusters of clusters. 

Mapper is different because it measures not just along cosine distance, and is based on overlap along a filtering lens metric