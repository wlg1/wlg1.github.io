# KL-Divergence

Compare two probability distributions, for example, to evaluate the performance of a machine learning model that predicts probabilities.

Given two probability distributions P and Q over the same sample space:

$$
KL(P || Q) = ∑_x P(x) log [P(x) / Q(x)]
$$

where the sum is taken over all possible values of x in the sample space, and log denotes the natural logarithm.

Intuitively, KL-divergence measures the amount of information lost when using Q to approximate P. 

---

It is not a distance metric because it is not symmetric (i.e., KL(P || Q) is not equal to KL(Q || P)), and it does not satisfy the triangle inequality. Therefore, it is more appropriate to think of KL-divergence as a measure of dissimilarity rather than distance.

---

To calculate the KL-divergence between two dataset samples, you would first need to estimate the probability distributions of each sample. One common way to estimate the probability distribution of a sample is to use a histogram or kernel density estimation (KDE).

Once you have estimated the probability distributions of the two samples, you can then calculate the KL-divergence between them using the formula I described earlier. Specifically, you would calculate the empirical probability mass functions or probability density functions of each sample, and then compute the sum over all possible values of x in the sample space.

Here is the general procedure for computing KL-divergence between two dataset samples:

1. Estimate the probability distributions of each sample using a histogram or kernel density estimation.
2. Compute the empirical probability mass functions or probability density functions of each sample. [REF](https://www.notion.so/Compute-the-empirical-probability-mass-functions-or-probability-density-functions-of-each-sample-e4837b0258bd40a791cd19299dbdeda5?pvs=21)
3. Compute the KL-divergence using the formula

Note that the estimated probability distributions may not be exact, and the KL-divergence calculation is sensitive to the quality of the estimates. Therefore, it is important to choose an appropriate method for estimating the probability distributions and to evaluate the quality of the estimates before computing the KL-divergence.

---

To compute the KL-divergence between two dataset samples in Python, you can use the **`scipy.stats.entropy`** function from the SciPy library. Here's an example code snippet:

```python
import numpy as np
from scipy.stats import entropy

# Generate two sample datasets
sample1 = np.random.normal(loc=0, scale=1, size=1000)
sample2 = np.random.normal(loc=1, scale=2, size=1000)

# Estimate the probability density functions using histograms
hist1, bin_edges1 = np.histogram(sample1, density=True, bins='auto')
hist2, bin_edges2 = np.histogram(sample2, density=True, bins='auto')

# Compute the KL-divergence between the histograms
kl_divergence = entropy(hist1, hist2)

print('KL-divergence between the samples:', kl_divergence)
```

In this example, we generate two sample datasets using NumPy's **`random.normal`** function, which generates samples from a normal distribution with a given mean and standard deviation. We then estimate the probability density functions of each sample using the **`numpy.histogram`** function, which returns the histogram values and bin edges. We set the **`density`** parameter to **`True`** to estimate the PDF instead of the PMF, and we set the **`bins`** parameter to **`'auto'`** to automatically determine the number of bins based on the data.