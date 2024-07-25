# SAE Mapper Explora

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