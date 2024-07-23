# Frature stitching

You can stitch features from one size sparse autoencoder to another! If you increase the dictionary size of SAEs, you can categorize the features in two groups:
 Novel features with new information not present in a smaller SAE Reconstruction features that sparsify information that already exists in the small SAE
The novel features can directly be inserted in the smaller SAE to improve its performance! https://www.alignmentforum.org/posts/baJyjpktzmcmRfosq/stitching-saes-of-different-sizes