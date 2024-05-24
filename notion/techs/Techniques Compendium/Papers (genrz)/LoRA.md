# LoRA

### GENERALIZE:

**Problem**: How to reduce number of Transformer parameters?

**Solution**: Freeze the pre-trained model weights. Then at each layer, inject trainable matrices decomposed into lower rank matrices

- What’s lower rank?
    
    the rank (the number of linearly independent rows or columns) is smaller than the maximum possible rank for that matrix size. It has less information than full-rank
    
- Details: How to decompose
    
    Decomposition is done by factorizing into a frozen matrix W0 and matrices with smaller dimensions.
    
    $h = W_0 + BA$
    

---

### GENERALIZE:

Problem: