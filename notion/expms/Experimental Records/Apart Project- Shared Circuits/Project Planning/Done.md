# Done

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
    
    [numseq_nextScores.ipynb](../Expm%20Results%208de8fe5b943641ec92c4496843189d36/numseq_nextScores%20ipynb%202578dc5c770641f4bcb2045281d9b44a.md) 
    
- ⚠️ gpt2_Neuron2Graph.ipynb
    
    [https://colab.research.google.com/drive/1Vzs-gH1vM1xSk8JcRjM2HF_Zm7XHJdWA#scrollTo=gqUTXwB32Fbo](https://colab.research.google.com/drive/1Vzs-gH1vM1xSk8JcRjM2HF_Zm7XHJdWA#scrollTo=gqUTXwB32Fbo)
    
    STUCK: can’t scrape neuron activations due to empty list. which (layer, neuron) is empty?
    
- ✅ [Find more “next” heads](../Expm%20Results%208de8fe5b943641ec92c4496843189d36/numseq_nextScores%20ipynb%202578dc5c770641f4bcb2045281d9b44a.md)
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
    
- TBC- study: [Towards Automated Circuit Discovery for Mechanistic Interpretability](https://www.notion.so/Towards-Automated-Circuit-Discovery-for-Mechanistic-Interpretability-e22fd1e2478347ea9686424d6080b5b7?pvs=21)
- (FIXED)⚠️ [Early head validation code](../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Early%20head%20validation%20code%20be7fc9bbf047474388f55bbe8f04eb17.md)
- ⚠️ [SVD interpretable dirs](../Expm%20Results%208de8fe5b943641ec92c4496843189d36/SVD%20interpretable%20dirs%2083533467cd334293af5913675fdeee97.md)
- TBC- [Outline Plan](../Outline%20Plan%203935b02babc84c70a2be3545257d9b3e.md)

Find common circuits for more numerical tasks (not just seq cont)

Path Patching

- ✅ understand greater-than paper, path patching
    - [https://arena-ch1-transformers.streamlit.app/[1.3]_Indirect_Object_Identification](https://arena-ch1-transformers.streamlit.app/%5B1.3%5D_Indirect_Object_Identification)
- ✅ apply path patching from colab to get template, then apply to numseq
- ACDC main demo- get it to work on finding greater-than circuit diagram
    
    NOTE: we don’t need ACDC to get this diagram, as it gets a more complex, bigger circuit (that’s better than what’s in paper, but paper is good enough; too many edges is not needed)
    
    [Code- ****Towards Automated Circuit Discovery for Mechanistic Interpretability****](https://www.notion.so/Code-Towards-Automated-Circuit-Discovery-for-Mechanistic-Interpretability-999dfd3c865a403399259ca69c0ae375?pvs=21) 
    
- ✅ Outline path patching steps to get a circuit diagram
- Construct a circuit diagram for numseqs/months, and compare w/ greater-than circuit diagram
    - Find more causal evidence for edges BETWEEN components, not just "these are important components". Path patching between components to find these more precise interactions. [Path Patching](../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Path%20Patching%20967be4e1a2b241418a9603911dda4561.md)
        - get the right ‘abc dataset’ for digits; may use num among words. try and compare different corruptions (put in appendix, rmv test prompt failures in main section)
            
            ✅ RESULT: Tried different corruptions (repeat last, repeat all, etc) to compare path patching results. Traced back 9.1's impt heads (4.4, 5.5, 6.6) and back from those (0.1, 3.0)
            
            - OPTIONAL: email to ask for opinions on choice of corruption
            - mix different types of corruptions and take mean?
- ⚠️ Mean ablation numseq by repeating last. [Mean Resampling Ablation](../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Mean%20Resampling%20Ablation%20d7fd15fac3324baa96d82bada82340a1.md)
    - ✅ Check how Greater-Than circuit performs here
    - Brainstorm how to properly use and analyze path patching results to find the right heads
    - [Search Methods- ask ChatGPT](../Search%20Methods-%20ask%20ChatGPT%20c68457cff88c4c3ba4b7fc775684496a.md)
    - Narrow circuit search to seq positions for ablation expms
    - Narrow to q, k, or v
    
- TBC- Make copy of current, then idealized draft
- ✅ [Draft search “work backwards”](../Search%20Methods-%20brainstorm%2015a3020ab00b40adb79b0acf3622f5f4.md)
- ⚠️ Mean ablation on greater-than task
    
    [https://colab.research.google.com/drive/1WmFphzbrqRugdUa1w7KBc2AWONMe765x](https://colab.research.google.com/drive/1WmFphzbrqRugdUa1w7KBc2AWONMe765x#scrollTo=b13177b7)
    
    [https://chat.openai.com/c/6aafeccb-1c6d-48ed-a7ad-f31a0ba2e08b](https://chat.openai.com/c/6aafeccb-1c6d-48ed-a7ad-f31a0ba2e08b)
    
    - ISSUE: the correct token can be a range, not one token, so how do we measure “correct - incorrect”?
        
        [SOLN](https://colab.research.google.com/drive/1WmFphzbrqRugdUa1w7KBc2AWONMe765x#scrollTo=CgD41x5nbKKP&line=14&uniqifier=1)
        
    - In the corrupted dataset, is the “answer” value supposed to be the correct token of the clean dataset, or is it supposed to what’s predicted in the corrupted dataset? If it’s supposed to be the correct token of the clean dataset, then we did not formulate the corrupted dataset correctly in the digits seq nbs. To figure this, look at original code using IOI. What is the s_token in corrupted? It’s just S. This means it should be, in corr, the correct token of clean dataset- the IO and S don’t change, only the text does.
    - In paper, see section 5 to compare your reproduced results using new code with theirs (this checks the validity of your code)
    - ✅ Does the greater-than paper perform all-but-circuit ablation? Path patching ablates one component a time; mean (all-but-circuit) ablation ablates all but the entire circuit.
        
        Yes; in section 3.2 (end), the paper ablates everything except the entire circuit with the corrupted activations and checked if the performance was mostly the same.
        
    - ✅ email authors about code (to check the validity of your code)
    - (TBC- mean ablation doesn’t reproduce greater-than results. Is bug in making dataset or something else?)
- ⚠️ [gpt2-greater-than](../gpt2-greater-than%201d1763531c964ad28af1ee43c2253f19.md)
    - try to use rust-circuits in colab
- ✅ Turn ‘work backw’ to code. [Search Methods- brainstorm](../Search%20Methods-%20brainstorm%2015a3020ab00b40adb79b0acf3622f5f4.md)
- ✅ Automate to get edges: [Path Patching after Work Backw](../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Path%20Patching%20after%20Work%20Backw%20926c3d71d6304852afcc271974028aec.md)
- ✅ Wedn night: Book meeting or send msg on what has been done
- ⚠️ Use threshold on edges instead of top 5.
    
    [https://colab.research.google.com/drive/1onREXMNmc9ks0xpwDslUX2pdG0RSYtWS#scrollTo=rIK2EWzY86OP&line=1&uniqifier=1](https://colab.research.google.com/drive/1onREXMNmc9ks0xpwDslUX2pdG0RSYtWS#scrollTo=rIK2EWzY86OP&line=1&uniqifier=1)
    
    5% threshold has nothing, which shouldn’t happen, so is a bug.
    
    - ✅ debug by trying on smaller circuits first
    - Get distribution of logit diffs. What’s the average?
- ✅ rmv nodes w/o outgoing edges or path to final node (9.1)
- ✅ mean ablation the circuit pruned by iterative path patching
    
    [https://colab.research.google.com/drive/1H6Rx_g6yaZOkrP30MT55AB2fA-6PY1tq#scrollTo=B2f3O144hLcY&line=1&uniqifier=1](https://colab.research.google.com/drive/1H6Rx_g6yaZOkrP30MT55AB2fA-6PY1tq#scrollTo=B2f3O144hLcY&line=1&uniqifier=1)
    
- ✅ first use fwd prune and compare with backwards. iter path path this fwd pruned circuit
- ✅ iter path patch from full circ
- ✅ Email Hanna about using rust_circuit for causal scrubbing and nb
- ⚠️ SVD- MLP found few numbers, attn heads have some
- ⚠️ SVD attention heads by count numbers in attention head dirs
    - ⚠️ debug why these two differ in 9.1 output:
    
    [https://colab.research.google.com/drive/1Dcllro-IEkwChaBm89BhjWmSdjmqIFTj#scrollTo=yUPc-Ehrn8um](https://colab.research.google.com/drive/1Dcllro-IEkwChaBm89BhjWmSdjmqIFTj#scrollTo=yUPc-Ehrn8um)
    
    [https://colab.research.google.com/drive/16GEw9Rw6_Ui6WI8-WB4da7k-yO7mVWAO#scrollTo=wxS8oMwNS4dM](https://colab.research.google.com/drive/16GEw9Rw6_Ui6WI8-WB4da7k-yO7mVWAO#scrollTo=wxS8oMwNS4dM)
    
- ✅ Iterative forward then backward pruning. [numseq_mincirc_(pt_3).ipynb](https://colab.research.google.com/drive/1H6Rx_g6yaZOkrP30MT55AB2fA-6PY1tq#scrollTo=JCFS-x0E1sWs)
    
    numseq_mincirc_(pt_3), v1.ipynb is draft
    
- ✅ Is decreasing seq the same circuit as incr?
    
    [decr_numseq_mincirc_iter.ipynb](https://colab.research.google.com/drive/1odPpf7w_gBG8ZfAB2L6SXZszsDUk1CGA#scrollTo=682KzamGI9Ba)
    
    - Is it same as incr seq circuit? The crucial head, 9.1, is not involved. That makes sense given that 9.1 seems to be for "next" outputs. So which heads in "decreasing" seq circuit is involved in "prev" outputs?
        
        [Stragenly, if you prune fwd first instead of backw first, there are heads there that are present in "fwd first" that are not in "backw first", such as 11.11. This means the circuit is highly variable on candidate head selection order and doesn't always converge to the same circuit. Devise a more robust method that does.](https://colab.research.google.com/drive/1odPpf7w_gBG8ZfAB2L6SXZszsDUk1CGA#scrollTo=1YfIjZhwksuw&line=1&uniqifier=1)
        
    - 40 heads means 2/3 heads aren’t used. Still not small enough
- Use “prev scores” to find heads which are decreasing. Apply this fn to 9.1 as sanity check.
    - ✅ debug why (head 6.9) the n_right +=1, but the final stored says ‘no’.
        
        It’s OVERWRITING the first key ‘99’; the pred_tokens aren’t the same. That means ‘99’ is counted multiple times
        
        SOLN: need to fix next and copy scores too, b/c it was doing this for EVERY token in the input (s1, s2, etc). Fix by denom over not total seq len, but just 1 seq. 
        `for word in words:`
        We will just input the last element of an input (the number right before the pred). So unlike copy scores, it’s +1 if it’s detected once among the top k tokens.
        
        - [Notice that pred_tokens is different for each ‘99’. So position matters? Try ‘99’ from position 1 vs last pos, etc.](https://colab.research.google.com/drive/1gYqAcfJS3igpZsD97KffPK1E9saN33oY#scrollTo=Nq137A958tMQ&line=1&uniqifier=1)
        
        - [now run over all](https://colab.research.google.com/drive/1gYqAcfJS3igpZsD97KffPK1E9saN33oY#scrollTo=8atJh1tl9-m_&line=1&uniqifier=1)
    - Compare more
- ✅ on the local computer i changed a folder name, now I get this error:
    
    [https://chat.openai.com/c/d695e0d1-774f-4dbe-8307-acbe79e697c8](https://chat.openai.com/c/d695e0d1-774f-4dbe-8307-acbe79e697c8)
    
    test git add after restart git bash after folder name change- must restart bash else will ahve to add by folder, not git add .
    
- ✅ the reason greater-than uses “year ended…” is b/c gpt2 can only do greater-than with these types of tasks.
    
    They also tried increasing sequence years.
    
- to get more ideas for hypothesizing how circuits may work, read: [https://www.lesswrong.com/posts/u6KXXmKFbXfWzoAXn/a-circuit-for-python-docstrings-in-a-4-layer-attention-only#Patching_experiments](https://www.lesswrong.com/posts/u6KXXmKFbXfWzoAXn/a-circuit-for-python-docstrings-in-a-4-layer-attention-only#Patching_experiments)
    - [https://www.lesswrong.com/posts/kcZZAsEjwrbczxN2i/causal-scrubbing-appendix#3_Further_discussion_of_zero_and_mean_ablation](https://www.lesswrong.com/posts/kcZZAsEjwrbczxN2i/causal-scrubbing-appendix#3_Further_discussion_of_zero_and_mean_ablation)
        
        The first problem we see with these ablations is that they destroy various properties of the distribution of activations in a way that seems unprincipled and could lead to the ablated model performing either worse or better than it should.
        Mean ablating also takes the model out of distribution because the mean is not necessarily on the manifold of plausible activations.
        
        - ask chatgpt why written in rust
            
            [https://chat.openai.com/c/4226ea27-1e82-4fd6-960e-044ff5f8faae](https://chat.openai.com/c/4226ea27-1e82-4fd6-960e-044ff5f8faae)
            
- ✅Ask about rust circuits prereqs
    - ✅ ask arena slack, theo, hanna:
        
        Anyone looking to study causal scrubbing using this code? [https://github.com/redwoodresearch/rust_circuit_public/tree/master](https://github.com/redwoodresearch/rust_circuit_public/tree/master)
        I've only tried using mean ablation so far, not familiar with rust so looking to hear from people who have used this before on how much rust one needs to know to use it effectively for causal scrubbing
        
- ⚠️ Install rust_circuits on linux. [**[gpt2-greater-than](https://github.com/hannamw/gpt2-greater-than)**](https://www.notion.so/gpt2-greater-than-addc2d4a35354e7d9bde243b40db27e1?pvs=21)
- ✅ email about rust_circuits
    
    Yes, it should all run without any work on your part. Re: resampling ablations vs. causal scrubbing: causal scrubbing is a way to verify an interpretation of the semantics of a neural network, using resampling ablations. This is done by carefully choosing the pool of examples to resample from, for each node in the computational graph. Maybe you've seen this blog post?
    
    Rust_circuit supports both resampling ablations (which we use, in the form of path patching), and causal scrubbing (which we don't use in our work). Resampling ablations are also easy in TransformerLens (causal scrubbing may be less easy).
    
    <<<
    
    Thanks for all the info! I installed rust_circuits and tried running circuit_discovery.py locally, but I ran into CUDA out of memory issues. My laptop uses a NVIDIA GeForce GTX 1060. I was wondering if it's possible to use rust_circuits in a colab notebook to utilize the GPUs from colab, or should I not spend time trying to do that? I tried to figure out how to do so but haven't made progress so far.
    
    Also for path patching (and mean ablation) I was following the code that uses transformerlens from:
    
    https://github.com/callummcdougall/ARENA_2.0/blob/main/chapter1_transformers/exercises/part3_indirect_object_identification/solutions.py
    
    It replaces the activations of the IOI dataset with the corrupted ABC dataset; I was wondering what are the differences and pros/cons of that approach vs resampling ablation? Thanks!
    
- ✅ ablate with repeating numbers. [numseq_mincirc_repeatAll](https://colab.research.google.com/drive/1AZrx6xvGt1t1m9oKVkrRgIzkoKZRzq8F).ipynb
    
    RESULT: scores MUCH lower than repeatLast, for any subgraph. but the found circuit is higher than others for this.
    
    - Try corr by random nums Mean Ablation
- ✅ overleaf related work: Sec 5: Expanding our hypothesis to include those nodes allowed us to recover 82.8% of performance. So, similar tasks seem to use similar, but not identical, circuits.
- ⚠️ Debug path patching to get edges that connect all heads, such that all connected heads get score that is close to full performance.
    - ✅ SOLN: the heatmap uses `100*results`, so what you see if 100x bigger than the actual values. Thus, adjust edge threshold to be the ACTUAL results, not 100x. The reason 100x was used is because values like 0.0001 are displayed with sigfigs badly on heatmap
    - ✅ plot distribution of path patch edge thresholds for each end-head to get avg for all. combine all into one
        
        [numseq_path_patch_iterThres.ipynb](https://colab.research.google.com/drive/1onREXMNmc9ks0xpwDslUX2pdG0RSYtWS#scrollTo=wzGVQFqhVQUi&line=10&uniqifier=1)
        
    - ✅ Did they use a threshold in the paper? Cannot find it, so email authors
    - How to measure score not by ablating nodes, but by ablating edges?
    - ISSUE- path patching adds nodes, but a circuit cannot have source nodes that are not part of the first layer?

Shared Circuits for Similar Tasks

- ✅- Test digits circuit on months, etc. [Months circuit](../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Months%20circuit%20765ea1869818426298c439544a337efc.md)
- ✅- path patch on months. [Months path patch](../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Months%20path%20patch%20190601513e60424fbf7a9a8ef00a8317.md)
- ✅- decr seq circuit
    
    [https://chat.openai.com/c/38b2ee8a-d6b6-405f-a993-fa129d1cd378](https://chat.openai.com/c/38b2ee8a-d6b6-405f-a993-fa129d1cd378)
    
- ✅-  [numwords_mincirc_repeatLast](https://colab.research.google.com/drive/1hEEWySgGjWxy_UWpAuT5Oh_pf4hSAvmv#scrollTo=GCCCoO0V7L7J).ipynb. [Numwords path patch](../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Numwords%20path%20patch%20324547790e19453c9c0dc07488a9b67b.md)
- ⚠️ 2, 4, 6 and other seq circuits
    
    existing: numseq_test_prompts_SMALL
    
    new: [numseq_prompts](https://colab.research.google.com/drive/1rNRrvr4qzy_zjPUK-4mJHruwFKnomrnP#scrollTo=r9_yofz3WkYm), pt2.ipynb  [Add 2 prompts](../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Add%202%20prompts%20cfe4115b82634ce1b89a1afd0df9c9ba.md) 
    

Circuit conn method

- ✅ email about using ACDC for this circuit; say so far only used a simple “brute force” pruning method
    
    I read your paper on ACDC, along with watching your interview with Neel Nanda, and was interested in applying the technique to a new task. I am currently writing a paper partly involving comparing sequence continuation circuits, which are related to the greater-than circuit. I've been applying a simple pruning method that just iteratively removes heads and compares the change in model performance to a threshold, going forwards and back until no changes are made; the edges are found via iterative path patching. However, I find that there are issues with this, such as ending up with different circuits depending on the order of heads being removed (eg. starting from the first layer vs starting from the last).
    
    To find minimal circuits, I am looking to use a more sophisticated method such as ACDC, and was wondering if the code is ready yet to be used for a new task, or if it is still under development? If so, is there documentation describing how to use the code to apply it for a new task that isn't one of the existing ones (IOI, greater-than, etc?) Thanks!
    
- ✅ Does circuit change if change seq len of input?
    
    HYP: it shouldn’t, b/c really only looks at last two digits. See [numseq_prompts, pt2.ipynb](https://colab.research.google.com/drive/1rNRrvr4qzy_zjPUK-4mJHruwFKnomrnP#scrollTo=lrzgZVvBWKxW&line=1&uniqifier=1)
    
    This is WRONG. Even though 2 digits works, the logit score is very low. Having more digits increases the correct logit score. Thus, length DOES matter. Though when looking at “33 34” and “null 33 34”, the “null”, despite not being 32, DOES increase the correct token logit- why?
    
    [difflen_numseq_mincirc.ipynb](https://colab.research.google.com/drive/1QL6KiFQMIVl-7Zo3nIN-189C-U_WvkQq)
    
    There ARE differences! These may be “minor heads” we can do without. Let’s get rid of them and see what the score if: `fiveIntersectFour` gets 86%, an 11% drop.
    
    Perhaps different early heads are involved in processing sequence length?
    
    - What if only 1 digit? Does it “continue”?
- ✅ Dotted Line graph of seq len and correct ranking or logit
    - chatgpt code
        
        [https://chat.openai.com/c/6fa78583-4d1e-4479-a0d8-b8f1d863b722](https://chat.openai.com/c/6fa78583-4d1e-4479-a0d8-b8f1d863b722)
        
        write python code that takes in various lengths of sequences of "1 2 3" (eg. length 3) and produces a logit ranking of the next token. Note the logit ranking of the correct token. For instance, "1 2 3" has the correct token of "4". Now, obtain the ranking for lengths 1 (eg. "1") to 10 ("1 2 3 4 5 6 7 8 9 10"). Plot on the x-axis the sequence length, and on the y-axis, plot the logit value of the correct token. Do this on gpt2 small.
        
        Plot on the x-axis the sequence length, and on the y-axis, plot the probability value of the correct token. But for each x-axis value, get the average probability value over sequences of the same length. For example, "1 2 3", "2 3 4", and "3 4 5" are all sequences of length 3. Have 10 sequences for each x-axis value to take the average over.
        
    
    x-axis is seq len, y-axis is ranking. first look at [test prompts](https://colab.research.google.com/drive/1rNRrvr4qzy_zjPUK-4mJHruwFKnomrnP#scrollTo=rMcpSDdjIAiA)
    
    [seqLen_corrToken_plot.ipynb](https://colab.research.google.com/drive/1Bv0RfqsfanuU4wF3bkZ5DltoyTaHwI2e#scrollTo=5MOCeJMmajZg)
    
    The probabilities are slightly different from that of TransformerLens, though the rankings are the same.
    
- ✅ threshold email
    
    1) We didn't formally choose a threshold (though that is an option). Instead, we just chose the most salient nodes/edges, as there only tended to be a few (so, top-k for some small k). With our method, the absolute effect of each ablation shrinks as you go deeper into the model (towards the logits), so choosing one constant threshold across all ablations could be tough. Other methods (e.g. ACDC) do work on the basis of some user-set threshold.
    
    2) We ablated edges; in the figures in the paper, you should be able to see which edges were ablated.
    
- ✅ Currently, when we ablate by nodes we are also ablating ALL the edges in and out of those nodes? Actually there’s no such as thing “ablate by edges” because activations are always neuron (node) outputs; they’re not weights (which are edges). If we have nodes (A,B) connecting to C, ablating B means we also ablate B-C but keep A-C.

Writing

- ✅ ask about eacl workshop abstract submission deadline
    - [https://openreview.net/](https://openreview.net/) : login to see list of workshops
- ✅ Move novel methods brainstorm to [Future work](../Future%20work%20a8d30bf9c84546da862cb2a95da71dfc.md)

Attention Head Functionality

- ✅ Logit lens
    - outdated: [https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens](https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens)
    - [https://colab.research.google.com/drive/1-nOE-Qyia3ElM17qrdoHAtGmLCPUZijg?usp=sharing#scrollTo=AvtLSbiZkU2K](https://colab.research.google.com/drive/1-nOE-Qyia3ElM17qrdoHAtGmLCPUZijg?usp=sharing#scrollTo=AvtLSbiZkU2K)
    - [sim_tasks_logit_lens.ipynb](https://colab.research.google.com/drive/1GeM2vLnIan_q6kdiGKQoDcMrAtYe0FLG#scrollTo=nKl9H9E625Vm)
- ✅ Look at previous results of actv patch movement + attn patterns, and relate to new circuits
    - ✅ [4.4 is prev number head](https://colab.research.google.com/drive/1FThBbzvhipfGHb4jwdXLA6iXlIv75spp#scrollTo=HjXea78dIAif&line=6&uniqifier=1)
    - ✅ re-org draft to ‘early, mid, late’ instead of by technq to better compare evidence for each type
    - ✅ re-org next/copy scores to combine w/ mid/late
- ✅ [How did prev papers diagnose early + mid? Try getting interpretations from prev papers that used the same heads](../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Early%20Head%20Analysis%20b73c8162b7334655ad1ff91fb236b69e.md)
- ✅ [look at attn patterns for more heads than just the top 10](../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Early%20Head%20Analysis%20b73c8162b7334655ad1ff91fb236b69e.md)