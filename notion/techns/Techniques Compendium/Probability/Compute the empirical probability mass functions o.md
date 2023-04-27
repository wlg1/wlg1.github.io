# Compute the empirical probability mass functions or probability density functions of each sample.

SOLN:

A histogram

SOLN (DET):

A histogram can be used to estimate either the empirical probability mass function (PMF) or the empirical probability density function (PDF), depending on whether the data is discrete or continuous.

If the data is discrete, such as counts of occurrences or categorical data, then a histogram can be used to estimate the empirical PMF. In this case, the sample space consists of the possible values of the data, and the histogram bins correspond to each possible value, with the height of each bin representing the frequency of that value in the data.

On the other hand, if the data is continuous, such as measurements of a physical variable, then a histogram can be used to estimate the empirical PDF. In this case, the sample space consists of the possible values of the variable, and the histogram bins represent intervals of values, with the area of each bin representing the frequency density (i.e., the frequency divided by the bin width).

Regardless of whether a histogram is used to estimate the empirical PMF or PDF, the resulting estimate is only an approximation of the true underlying distribution, and the quality of the estimate depends on the choice of bin size, bin placement, and smoothing method. Therefore, other methods such as kernel density estimation (KDE) may be more appropriate in some cases to estimate the empirical PDF.

---

NOTE:
Probability mass function (PMF) of a discrete random variable can be used to calculate the probability density function (PDF) of its continuous counterpart, the probability density mass function (PDMF), through integration.

Specifically, if X is a discrete random variable with PMF p(x) and Y is a continuous random variable that approximates X with PDMF f(y), then we can calculate f(y) as:

$$
f(y) = ∑_x p(x) δ(y - x)
$$

where δ(y - x) is the Dirac delta function, which is zero everywhere except at y = x, where it is infinite but has unit area.

Intuitively, this equation sums up the probabilities of all the discrete values of X that are close to y and assigns that probability mass to the corresponding point y in the continuous sample space of Y. The resulting function f(y) represents an estimate of the PDF of Y based on the PMF of X.

However, note that this conversion from PMF to PDF is only possible when the discrete random variable X and the continuous random variable Y are related in a specific way, such as through discretization of a continuous variable or approximation of a continuous distribution by a discrete one. In general, the PMF and PDF are distinct concepts that apply to different types of random variables and are not interchangeable.

---

SOLN: 

Kernel density estimation

SOLN (DET):

Kernel density estimation (KDE) is a non-parametric method for estimating the probability density function (PDF) of a continuous random variable based on a set of observed data points. The basic idea behind KDE is to estimate the PDF as a weighted sum of kernel functions, where each kernel function represents a contribution to the PDF from a nearby data point.

- What’s a kernel function?
    
    A non-negative function that determines the shape of the contribution of each data point to the estimated probability density function (PDF). It determines how much weight each data point is given in the estimation of the PDF. See: [Kernel Function](https://www.notion.so/Kernel-Function-c89c4d3561924f90bf76173aed9e8301) 
    

Formally, given a set of n observed data points X = {x1, x2, ..., xn}, the KDE estimate of the PDF f(x) at an arbitrary point x in the sample space is given by:

$$
f(x) = \frac{1}{nh} ∑_{i=1}^{n}  K((x - xi)/h)
$$

where K(u) is the kernel function, h > 0 is the bandwidth parameter, and the sum is taken over all n data points. The kernel function is a non-negative function that integrates to 1 over its support and determines the shape of the contribution of each data point to the estimated PDF. 

- The bandwidth parameter h?
    
    Controls the width of the kernel functions and the smoothness of the estimated PDF. A small bandwidth produces a more variable and spiky estimate that closely follows the data points, while a large bandwidth produces a smoother and more generalized estimate that may oversmooth the data.
    

KDE does not require assumptions about the underlying distribution, unlike parametric methods such as the maximum likelihood estimator. However, KDE can be computationally expensive for large datasets and requires careful selection of the bandwidth parameter to avoid underfitting or overfitting the data.