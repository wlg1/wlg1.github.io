# Ideas (move to proj ideas/ques/speculation)

Overall

- Can we track the trajectories of activation patterns as we vary an input (sensations)?
    - [Neuron Dynamics](https://www.notion.so/Neuron-Dynamics-d96e6c97975a428fa9f6d1eb79c69f1a?pvs=21) : We find heads which inhibit information. But ANN neurons go forward, not back, so “feedback” may not occur. The “feedback” in ANNs occurs during training, which is different from how it works in biological entities. Is it possible to try to use neurons to train other neurons?
        - What might occur in ANNs is that there may still excitatory and inhibitory components, but they do not signal back. Instead of A↔B, it’s A1 → B → A2, where A1 and A2 could’ve been “the same” if it were possible to signal back
    - The single dynamics of a neuron are trivial; it’s just a linear function with a nonlinear activation. This differs from the “spiking chaotic” states of a bio-neuron

Transformers

- Sequences can be recognized; what about graph mappings (analogies)? May be used with GNN instead

CNN

- You can find which kernels in a CNN are edge detectors by looking for edge detector patterns. Eg) vertical is one side is >x, middle is =x, and right is < x.

### Speculations (Guesses)