# Project Planning

### Working on

- 

### Done

- ✅ Review hackathon project and convert to overleaf
    - ✅ Make table comparing copy scores between analogous seqs

Quick Lit Review

- ✅ read EMNLP 2023 paper on attn head MLP interactions
    - how reliable is GPT-4? too much of a black box to assess its consistent reliability?
    - we analyse the associations between attention heads and next-token neurons by looking at how much each attention head activates the neuron
- ✅ read “The Larger They Are, the Harder They Fail”
- Further test the circuit hypothesis by:
    - checking “performance scores” of heads
    - finding “+1” (aka next) MLPs neurons
- ✅ Msg some other authors to ask about how high lvl description of paper idea would do at a conference
- ✅ Find “Next Heads” by coding “next scores”
    
    [numseq_nextScores.ipynb](Expm%20Results%208de8fe5b943641ec92c4496843189d36/numseq_nextScores%20ipynb%202578dc5c770641f4bcb2045281d9b44a.md) 
    
- ⚠️ gpt2_Neuron2Graph.ipynb
    
    [https://colab.research.google.com/drive/1Vzs-gH1vM1xSk8JcRjM2HF_Zm7XHJdWA#scrollTo=gqUTXwB32Fbo](https://colab.research.google.com/drive/1Vzs-gH1vM1xSk8JcRjM2HF_Zm7XHJdWA#scrollTo=gqUTXwB32Fbo)
    
    STUCK: can’t scrape neuron activations due to empty list. which (layer, neuron) is empty?
    
- ✅ [Find more “next” heads](Expm%20Results%208de8fe5b943641ec92c4496843189d36/numseq_nextScores%20ipynb%202578dc5c770641f4bcb2045281d9b44a.md)
- TBC- Read reviews of IOI for ICLR: [https://openreview.net/forum?id=NpsVSN6o4ul](https://openreview.net/forum?id=NpsVSN6o4ul)
- ✅ Package natbib Warning: Citation `geva2020transformer' on page 1 undefined on input line 4.
    
    \bibliography{bibliography.bib}
    % \bibliographystyle{bibliography.bib}
    \bibliographystyle{plainnat}
    
    # bibliographystyle is required else cits are ?
    
    - what is plainnat
        
        The `plainnat` bibliography style is one of the styles provided for use with the `natbib` package in LaTeX for rendering bibliographies. The `natbib` package allows you to format your citations and reference list with a more flexible interface than LaTeX's basic `cite` mechanism, supporting both numerical and author-year citation styles.
        
        The `plainnat` style is an extension of the standard `plain` style that comes with LaTeX. Like `plain`, `plainnat` lists references alphabetically by authors' last names, but it also supports the additional citation commands provided by `natbib`, such as `\\citep` and `\\citet`.
        
        Here's a simple example to demonstrate how `plainnat` might be used:
        
        Your LaTeX document might have a preamble that looks like:
        
        ```latex
        \\documentclass{article}
        \\usepackage{natbib}
        \\bibliographystyle{plainnat}
        
        ```
        
        Then, in the body of your document, you could use various `natbib` citation commands:
        
        ```latex
        \\begin{document}
        
        According to some research \\citep{Smith2000}, we find that...
        The result is shown by \\citet{Jones1999} to be...
        
        \\bibliography{mybibfile} % Replace "mybibfile" with the name of your .bib file, without the extension
        \\end{document}
        
        ```
        
        In your `.bib` file (`mybibfile.bib`), you would have entries like:
        
        ```
        @article{Smith2000,
          author  = {Smith, John},
          title   = {A Study on Something Interesting},
          journal = {Journal of Interesting Studies},
          year    = {2000},
          volume  = {1},
          pages   = {1--10},
        }
        
        @article{Jones1999,
          author  = {Jones, Jane},
          title   = {Another Study},
          journal = {Another Journal},
          year    = {1999},
          volume  = {2},
          pages   = {11--20},
        }
        
        ```
        
        After compiling the document (LaTeX -> BibTeX -> LaTeX -> LaTeX), the references would appear at the end of the document, formatted according to the `plainnat` style.
        
        Remember that `plainnat` is one of several pre-defined styles you could use with `natbib`. Others include `abbrvnat` and `unsrtnat`, each with its own rules for formatting citations and reference lists.
        
    - Instead of plainnat, how can I turn the inline citations into numbers?
        
        If you want your inline citations to appear as numbers, you can switch from an author-year style to a numerical citation style. One commonly used style for numerical citations is `unsrt` or its `natbib`-compatible version `unsrtnat`.
        
        To use numerical citations, you would adjust your LaTeX document preamble like this:
        
        ```latex
        \\documentclass{article}
        \\usepackage[numbers]{natbib}  % Add the 'numbers' option
        \\bibliographystyle{unsrtnat} % Use unsrtnat instead of plainnat
        
        ```
        
        Or if you're not using `natbib`:
        
        ```latex
        \\documentclass{article}
        \\bibliographystyle{unsrt} % Use unsrt for plain LaTeX
        
        ```
        
        In the body of your document, you can use `\\cite` or `\\citep` for citations, and they will appear as numbers.
        
        ```latex
        \\begin{document}
        
        According to some research \\cite{Smith2000}, we find that...
        The result is shown by another study \\cite{Jones1999}...
        
        \\bibliography{mybibfile} % Replace "mybibfile" with the name of your .bib file, without the extension
        \\end{document}
        
        ```
        
        Your `.bib` file would remain the same. After compiling your document with LaTeX -> BibTeX -> LaTeX -> LaTeX, the inline citations should appear as numbers, and the references at the end of your document will be numbered as well.
        
        The `unsrt` and `unsrtnat` styles also sort the references in the order in which they are cited in the text, rather than alphabetically or by year. This is the meaning of "unsrt", which stands for "unsorted".
        
    
    \bibliography{bibliography.bib}
    \bibliographystyle{unsrt}
    
    However, ICLR doesn’t use numbers. It uses (author, year). But plainnat makes it into “author (year)”.
    
    - I want the citations to use (author, year). But plainnat makes it into “author (year)”.
        
        The `natbib` package provides different citation commands that allow you to manipulate the appearance of citations. However, if you find that the `plainnat` style doesn't format the citations exactly the way you want (e.g., "author (year)" instead of "(author, year)"), you might have to use additional LaTeX commands to customize the output or even consider creating a custom `.bst` file.
        
        That being said, you can manually adjust the output using `natbib`'s flexible citation commands:
        
        - Use `\\citep` for parenthetical citations, which usually appear as "(Author, Year)".
        - Use `\\citet` for textual citations, which usually appear as "Author (Year)".
        
        ### Example with plainnat:
        
        Here is an example of how you might use these in a LaTeX document:
        
        ```latex
        \\documentclass{article}
        \\usepackage{natbib}
        \\bibliographystyle{plainnat}
        
        \\begin{document}
        
        % This will output as: (Smith, 2000)
        Some text that needs a citation \\citep{Smith2000}.
        
        % This will output as: Smith (2000)
        As \\citet{Smith2000} have shown...
        
        \\bibliography{your_references} % your_references.bib is your .bib file
        \\end{document}
        
        ```
        
        ### Force Parenthetical Style:
        
        If `plainnat` doesn't do what you want and you need to force a parenthetical style throughout, you could redefine the `\\citet` command to act like `\\citep` as follows (though be cautious as this is a bit of a hack):
        
        ```latex
        \\documentclass{article}
        \\usepackage{natbib}
        \\bibliographystyle{plainnat}
        
        \\renewcommand{\\citet}[1]{\\citep{#1}}
        
        \\begin{document}
        
        % Both of these will output as: (Smith, 2000)
        Some text that needs a citation \\citep{Smith2000}.
        As \\citet{Smith2000} have shown...
        
        \\bibliography{your_references}
        \\end{document}
        
        ```
        
        These are some workarounds, but if you find yourself having to do this frequently, you might want to look into creating a custom `.bst` file that defines the citation style exactly as you want. This is more involved and requires knowledge of the BibTeX stack language.
        
    
    SOLN: \citep{} w/ plainnat
    
    Use \cite when using the authors as a subject (eg. Xiao et al (2020) claim….) but use \citep when not doing so (eg. This was found in previous papers (Lin et al., 2020; Ben…)
    
    See: [https://openreview.net/pdf?id=3dnrKbeVatv](https://openreview.net/pdf?id=3dnrKbeVatv)
    
- ✅ figures not in section
    
    \begin{figure}[H]
    % \begin{figure}[ht]
    
    H forces it to be in section, but causes large white spaces. ht is better to reduce white space, but it may not be in same section.
    
- TCD- study: [Towards Automated Circuit Discovery for Mechanistic Interpretability](https://www.notion.so/Towards-Automated-Circuit-Discovery-for-Mechanistic-Interpretability-e22fd1e2478347ea9686424d6080b5b7?pvs=21)
- (FIXED)⚠️ [Early head validation code](Expm%20Results%208de8fe5b943641ec92c4496843189d36/Early%20head%20validation%20code%20be7fc9bbf047474388f55bbe8f04eb17.md)
- ⚠️ [SVD interpretable dirs](Expm%20Results%208de8fe5b943641ec92c4496843189d36/SVD%20interpretable%20dirs%2083533467cd334293af5913675fdeee97.md)
- TBC- [Outline Plan](Outline%20Plan%203935b02babc84c70a2be3545257d9b3e.md)

### Future Work Ideas / Postponed

Find common circuits for more numerical tasks (not just seq cont)

- email authors of ‘greater-than’ paper
- Use ACDC to find common graphs for greater-than & less-than, and other numerical circuits (do they all use 9.1 for a similar purpose?)
    - email authors for questions
- new operations instead of just “next”, modular addition circuits
- 2 4 6; two four six
    - 1, 2, 3 and jan feb march are orderings. What are other types of orderings?
        
        [https://chat.openai.com/c/5ba1ac6a-7132-4a1e-b4d3-ce2f3f07c0c1](https://chat.openai.com/c/5ba1ac6a-7132-4a1e-b4d3-ce2f3f07c0c1)
        
- [https://arena-ch1-transformers.streamlit.app/%5B1.4%5D_Balanced_Bracket_Classifier](https://arena-ch1-transformers.streamlit.app/%5B1.4%5D_Balanced_Bracket_Classifier)
    - may have something to do with counting. even subject can do ‘counting’. But is counting and number recog the same? perhaps if a meta-model recog them to be the same in a model, that meta-model will develop a link between them

---

- Try to find how digits + numwords SEQUENCES (not just individual tokens) change in latent space in each part of residual stream; start with after each layer, then dissect finer to heads + MLPs
    - 1 and One are already close after the first layer. But the sequence 2, 4, 6 and two four six may not be. It may not be considered an “even” dimension (direction).
        - entire input sequences are NOT vectors, but matrices? so how do we measure similarity of sequences if they’re matrices?
            - in a transformer, are input sequences embeeded as vectors, or matrices? would the sequence "2, 4, 6" be a single vector after the first MLP, or would it be a matrix?
                
                In a transformer model, input sequences are embedded as vectors, but the sequence of tokens/words becomes a matrix when considering all the embeddings together.
                
                To break this down:
                
                1. **Token Representation**: Each token or word in the input sequence is represented as an embedding vector. For instance, if your embedding dimension is \(d\), then each token would be represented by a vector of size \(d\).
                2. **Sequence Representation**: If you have a sequence of \(N\) tokens/words, and each token is represented by a vector of dimension \(d\), then the entire sequence is represented as a matrix of size \(N \times d\).
                
                Using your example of the sequence "2, 4, 6":
                
                - Assume that each number (token) is embedded into a vector of size \(d\).
                - "2" would have its own vector of size \(d\). Similarly, "4" and "6" would have their own vectors of the same size.
                - When you stack these vectors vertically to represent the entire sequence, you'll get a matrix of size \(3 \times d\).
                
                After the initial embedding, the transformer's subsequent layers would operate on this matrix, applying multi-head attention, feed-forward neural networks (which you referred to as MLP), etc., to process the sequence.
                
                So, to directly answer your question: The sequence "2, 4, 6" would be represented as a matrix after the embedding layer, where each row of the matrix corresponds to the embedding vector of a number in the sequence.
                
            - how would you measure the similarity between two input sequences?
                
                [https://chat.openai.com/c/b5c12746-f184-4f2b-babe-af1df51d96fc](https://chat.openai.com/c/b5c12746-f184-4f2b-babe-af1df51d96fc)
                
        - is the 2, 4, 6 direction and 8, 10, 12 direction similarity (by cosine sim)?
    - measure the svd similarity between them at each layer
    - each data pt is a series of numbers, but may not be in order. show that ordered seqs have more similarity than non-ordered when dim reduc to 2D along most impt dims
- PCA viz seq types thru layers
    
    To understand how to relate digit activations to wordnum activations, working on PCA visualizations of input sequence types to see how they change by layer (so far, no notable patterns found in visuals). Using this to find if there are directions corresponding to "sequence"- probably "sequence" is not measured this way and this may not exist. Inspired by: [https://www.lesswrong.com/posts/mkbGjzxD8d8XqKHzA/the-singular-value-decompositions-of-transformer-weight](https://www.lesswrong.com/posts/mkbGjzxD8d8XqKHzA/the-singular-value-decompositions-of-transformer-weight)
    
    And paper "Language Models Implement Simple Word2Vec-style"
    
- Edit digit circuit to become number words
    - Replace digit activations with number words activations
    What's the differences? Can this difference be added to edit any digit into months?
    - 9.1, given 'one', will output word 'two'. can we convert 'two' into '2'? measure difference in activations of '1' and 'one' after crucial attnetion head 9.1. is this the 'digit to numwords' direction? when put thru the circuit, what happens?
- Minitially retrain transfer learning toy digits circuit to become months circuit
- do name mover heads attend to anything? if so, why isn’t 19.1 in med attending to anything, even though it should be a “next” head?
- get a distribution of next head scores
- gpt-2 medium, llama
    - Given that only one head, 9.1, appears to do “next”, can a single layer be trained to do seq completion (though it may require other heads, at 9.1 isn’t enough?) To isolate circuits better, train and study toy models that perform number recognition. See if analogous circuits from toy models are present in larger gpt ones
- Which are copy heads and which are next heads? Output a sample based on proportion. Randsel yes and nos
- Causal Scrubbing
    
    [https://github.com/pranavgade20/causal-verifier](https://github.com/pranavgade20/causal-verifier)
    
    [https://github.com/redwoodresearch/rust_circuit_public](https://github.com/redwoodresearch/rust_circuit_public)
    
    hard to use if don’t know rust
    
    [https://github.com/redwoodresearch/remix_public](https://github.com/redwoodresearch/remix_public)
    
    requires rust
    
    [https://github.com/redwoodresearch/remix_public/blob/master/remix_d4_part1_instructions.md](https://github.com/redwoodresearch/remix_public/blob/master/remix_d4_part1_instructions.md)
    

---

- Introduction and abstract; what main contributions are
- label x and y axis of figures, matplotlib save as pdf, don’t use scale args, caption should be in depth
- figures that zoom in with magnifying arrow to transformer block (if too small), or log scale
- avoid referring to non-peer reviewed work (eg. induction mosiac; try to find a paper with same content unless it doesn’t exist)

---

- anonymized review- just get feedback
    - state a lot of what will be done in future work due to paper weaknesses
        - Reviews released: Nov 10; this means can’t submit to workshop
            - there’s a good chance it may get accepted at workshop
            - [https://openreview.net/group?id=ICLR.cc/2022/Workshop](https://openreview.net/group?id=ICLR.cc/2022/Workshop)
        - [https://chat.openai.com/c/5bd83003-3142-4545-9ff6-e84a61f647f2](https://chat.openai.com/c/5bd83003-3142-4545-9ff6-e84a61f647f2)
    - Continue to- Msg some other authors to ask about how high lvl description of paper idea would do at a conference
        
        Based on: [https://openreview.net/forum?id=9XFSbDPmdW](https://openreview.net/forum?id=9XFSbDPmdW)
        
- A new method to find shared circuits?
- How do “next” heads play a role?
    - Test how ablating them…?
        - feed IOI to GPT-2 (cannot have highlights/comments) then ask:
            
            In the Interpretability in the Wild paper, it was found experimentally that heads were performing copying tokens. In a new circuit, we found heads that may be taking in a digit such as “1” and outputting the next digit, such as “2”. How can we test that they are doing this in a circuit which finds the next member of a sequence given a sequence as input?
            
            [https://chat.openai.com/c/dcf660a8-9ff9-4ed8-aec8-08a5a6d146f1](https://chat.openai.com/c/dcf660a8-9ff9-4ed8-aec8-08a5a6d146f1)
            
- CONT-  Find “Next Heads”
    
    [in code, loop corr fn code over multiple top heads and see which heads have highest]
    
- If 9.1 matters the most for “next” for digits, months, etc (and there’s no differing part needed to distinguish them; it handles for all those types), what are the other heads for? Are MLPs even needed for “next”? 9.1 by itself isn’t enough.
- Find which parts of circuits, if any, “branch off” the months from digits circuits

---

- Understand inputs + outputs of N2G nb
    
    [Neuron2Graph.ipynb](https://www.notion.so/Neuron2Graph-ipynb-1194a0bf97744b3ab86b19fc9d0bbd06?pvs=21) 
    
- cont- ⚠️ gpt2_Neuron2Graph.ipynb
    - use neuron2graph to find more number neurons
- [NOTE: these 'random circuits' may be disconnected; what about testing against "connected" random circuits?]
- read othellogpt world model: [https://www.alignmentforum.org/posts/nmxzr2zsjNtjaHh7x/actually-othello-gpt-has-a-linear-emergent-world](https://www.alignmentforum.org/posts/nmxzr2zsjNtjaHh7x/actually-othello-gpt-has-a-linear-emergent-world)
- to get more ideas for hypothesizing how circuits may work, read: [https://www.lesswrong.com/posts/u6KXXmKFbXfWzoAXn/a-circuit-for-python-docstrings-in-a-4-layer-attention-only](https://www.lesswrong.com/posts/u6KXXmKFbXfWzoAXn/a-circuit-for-python-docstrings-in-a-4-layer-attention-only)
- digits has far more samples than others and thus its statistics may be 'more accurate'; other should have more samples. figure out new input types that have more possible samples
- copy scores for other important components
- figure out how to deal with multi-token words
- max actv examples for attn heads, not just MLP neurons
- see which neurons have the largest difference between how much they write in a chosen direction
- take dot product of neuron output weights with more types of cont seq tokens + prompts (relns between tokens)
- check neuron activation after ablating attention head (zero or mean ablation? try both)
- path patching
- add2 inputs in gpt-2 small
- measuring analogical similarity against circuit similarity
- perform ablation; try causal scrubbing
- compare MLPs between analogous seqs using N2G
- interpolation of predicted words when changing part of circuit
- feed info about circuits into chatgpt and talk to it