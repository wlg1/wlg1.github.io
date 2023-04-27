# Energy Models

- Why is the distribution of data proportional to the exponential of negative energy function?
    
    The distribution of data proportional to the exponential of negative energy function is a fundamental concept in statistical physics and is known as the Boltzmann distribution. This concept has been applied in machine learning to develop energy-based models (EBMs) that can learn a probability distribution over the input data.
    
    The Boltzmann distribution states that the probability of observing a particular configuration of a physical system (or, in the case of machine learning, a set of input data) is proportional to the exponential of negative energy of that configuration. Mathematically, the probability of a configuration **`x`** can be expressed as:
    
    $$
    p(x) = \frac{1}{Z} * exp^{-E(x)}
    
    $$
    
    where **`E(x)`** is the energy of the configuration **`x`**, and **`Z`** is the normalization constant known as the partition function.
    
    In the context of EBMs, the energy function is learned from the input data, and the probability distribution over the input data is derived from the Boltzmann distribution. The energy function is typically modeled as a neural network, and the goal of training the model is to learn the parameters of the energy function that minimize the energy of the observed data.
    
    By learning the energy function, the model can assign higher probabilities to configurations of the input data that have lower energy, which are more likely to be observed. The exponential form of the Boltzmann distribution allows for the model to capture complex, nonlinear relationships in the input data, as it can model correlations between different features of the input data.