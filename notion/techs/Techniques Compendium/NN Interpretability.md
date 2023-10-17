# NN Interpretability

### Methodology

[Get the distribution of hidden state activations](NN%20Interpretability%207fcd57f701554addb98bd2c3762f8b8f/Get%20the%20distribution%20of%20hidden%20state%20activations%206b781605c3b54956a2f96151d7efb2da.md)

### Optimization

[Reduce number of fwd passes for each edge](NN%20Interpretability%207fcd57f701554addb98bd2c3762f8b8f/Reduce%20number%20of%20fwd%20passes%20for%20each%20edge%20fb82dbccd62441f0a5a81b6c28368aa4.md)

### Experimental Analysis

- How to find a circuit?
    1. Find layers where spikes in logit diff
    2. Find (heads, layers) with big logit diff if ablated
    3. Automated circuit discovery diagram: find the flows aligned w/ impt heads