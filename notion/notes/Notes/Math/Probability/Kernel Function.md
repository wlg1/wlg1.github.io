# Kernel Function

The choice of kernel function in kernel density estimation (KDE) depends on the specific needs of the analysis and the characteristics of the data being analyzed. However, all kernel functions used in KDE have two key properties: non-negativity and unit area.

Specifically, a kernel function K(u) must satisfy the following conditions:

1. K(u) ≥ 0 for all u.
2. ∫ K(u) du = 1, where the integral is taken over the entire real line.

The first condition ensures that the contribution of each data point to the estimated PDF is non-negative, and the second condition ensures that the estimated PDF integrates to 1 over the entire sample space.

Different types of kernel functions have different shapes and properties, which can affect the accuracy and smoothness of the estimated PDF. Here are some examples of commonly used kernel functions:

1. Gaussian (normal) kernel: K(u) = (1/√(2π)) exp(-u^2/2), where u is the distance between the data point and the estimate point. The Gaussian kernel is the most commonly used kernel function because it produces smooth estimates that are differentiable and have good convergence properties.
2. Epanechnikov kernel: K(u) = (3/4)(1-u^2), where -1 ≤ u ≤ 1. The Epanechnikov kernel is useful for estimating PDFs with sharp edges or corners because it has zero values outside of the support region.
3. Triangular kernel: K(u) = (1-|u|), where -1 ≤ u ≤ 1. The triangular kernel is a simple and fast kernel that is useful for exploratory analysis and for handling non-smooth or bimodal distributions.

To calculate the contribution of each data point to the estimated PDF using a kernel function, we evaluate the kernel function at the distance between the data point and the estimate point (i.e., the distance between the data point and the point at which we want to estimate the PDF). The bandwidth parameter in KDE controls the width of the kernel function, which affects the smoothness of the estimated PDF.