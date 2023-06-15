# Interpret Attention Head Circuits of Analogous Inputs

[Project Planning](Interpret%20Attention%20Head%20Circuits%20of%20Analogous%20Inp%20c1d0ec7e43214760b4062ae4cdc0cd6b/Project%20Planning%20821fd0c71f4d4a44b5f7b240725c5547.md)

To do next: 

- See first item of ‘Working On’ in Project Planning

---

### Project Docs

Brainstorming Notes

- Combinations to test
    - different inputs types.
        - Eg) finding ‘cat’ is type of ‘pet’ over ‘human’ failed. what about other subclasses? say teacher, house, color, etc.
        - try providnig the trait in the input. Eg) Mary has paws. John has no paws. The animal is
    - various models
    - various ablations of heads (zero, mean)
    - various corruptions (switch order, add noise to input embeddings)
    
    Things to test correlations for: (use blocking, stat tests, etc)
    
    - using external info?
    - try using more traits
    - ordering: names, traits, sentences
    - stronger markers/boundaries to define separations to model (eg. that is part of source, not target, system)
    - use more examples of the pattern in the source
    - just test on more samples (how similar?)
- How to Define “Analogous”
    
    using structure preservation: If A→ B, then h(A) →h(B). This is similar to the definition of graph homomorphism.
    
- What the tested models are doing with adjective circuits
    
    The tested models (GPT-2 -s, -l, -xl) are not associating subject with adjective, but they are focusing attention on adjectives. IOI also doesn’t associate subject with objects, but uses a crude algorithm that chooses subjective based on what doesn’t have duplicates. This algorithm isn’t what’s used when it’s understood how IOI works (that requires truly knowing “who is giving to whom”, but it’s not using “giving” as part of this algorithm, nor does it formulate a scene of who’s giving what to whom), yet it has the same correct answers for IOI.
    

Task Planning Notes (scattered & not listed in order of worked on, unlike in “Proj Plan”)

[PLAN- Size Comparison Circuits and Neurons](Interpret%20Attention%20Head%20Circuits%20of%20Analogous%20Inp%20c1d0ec7e43214760b4062ae4cdc0cd6b/PLAN-%20Size%20Comparison%20Circuits%20and%20Neurons%201111d95ef57b4131b259ef88363f3010.md)

Expm Results Notes

[_*List of Code Notebooks*_](Interpret%20Attention%20Head%20Circuits%20of%20Analogous%20Inp%20c1d0ec7e43214760b4062ae4cdc0cd6b/_List%20of%20Code%20Notebooks_%2066bcbc2013ce465fbc61a281bc3ffa1f.md)

[Size Comparison Circuits and Neurons](Interpret%20Attention%20Head%20Circuits%20of%20Analogous%20Inp%20c1d0ec7e43214760b4062ae4cdc0cd6b/Size%20Comparison%20Circuits%20and%20Neurons%20983f0ebebc0a4c20a1db4967d6a9e201.md)

[Antonym Circuits and Neurons ](Interpret%20Attention%20Head%20Circuits%20of%20Analogous%20Inp%20c1d0ec7e43214760b4062ae4cdc0cd6b/Antonym%20Circuits%20and%20Neurons%20824f0d162ce84a8fb09c27f4e4931194.md)

[Most Recent S Name Movers](Interpret%20Attention%20Head%20Circuits%20of%20Analogous%20Inp%20c1d0ec7e43214760b4062ae4cdc0cd6b/Most%20Recent%20S%20Name%20Movers%20a72ccc6fdccc4e4baa78251399fdd2d7.md)

[Adjective Identification Heads](Interpret%20Attention%20Head%20Circuits%20of%20Analogous%20Inp%20c1d0ec7e43214760b4062ae4cdc0cd6b/Adjective%20Identification%20Heads%20f85cc6a172664109bf10cbfb5b49381a.md)

[Not Identification Circuits](Interpret%20Attention%20Head%20Circuits%20of%20Analogous%20Inp%20c1d0ec7e43214760b4062ae4cdc0cd6b/Not%20Identification%20Circuits%20db48cd1bd4844b25994773248e9a587c.md)

Writeups

[Outline Writeup Draft](Interpret%20Attention%20Head%20Circuits%20of%20Analogous%20Inp%20c1d0ec7e43214760b4062ae4cdc0cd6b/Outline%20Writeup%20Draft%2096f5c9785c684e359a76ecb09d264875.md)