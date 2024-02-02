# ArXiV Draft v1

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
    
    [numseq_nextScores.ipynb](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/numseq_nextScores%20ipynb%202578dc5c770641f4bcb2045281d9b44a.md) 
    
- ⚠️ gpt2_Neuron2Graph.ipynb
    
    [https://colab.research.google.com/drive/1Vzs-gH1vM1xSk8JcRjM2HF_Zm7XHJdWA#scrollTo=gqUTXwB32Fbo](https://colab.research.google.com/drive/1Vzs-gH1vM1xSk8JcRjM2HF_Zm7XHJdWA#scrollTo=gqUTXwB32Fbo)
    
    STUCK: can’t scrape neuron activations due to empty list. which (layer, neuron) is empty?
    
- ✅ [Find more “next” heads](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/numseq_nextScores%20ipynb%202578dc5c770641f4bcb2045281d9b44a.md)
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
- (FIXED)⚠️ [Early head validation code](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Early%20head%20validation%20code%20be7fc9bbf047474388f55bbe8f04eb17.md)
- ⚠️ [SVD interpretable dirs](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/SVD%20interpretable%20dirs%2083533467cd334293af5913675fdeee97.md)
- TBC- [Outline Plan](../../Brainstorming%20Notes%203f11ad066e9b4a07b4eac05b6b2474c4/Outline%20Plan%203935b02babc84c70a2be3545257d9b3e.md)

Find common circuits for more numerical tasks (not just seq cont)

Path Patching

- ✅ understand greater-than paper, path patching
    - [https://arena-ch1-transformers.streamlit.app/[1.3]_Indirect_Object_Identification](https://arena-ch1-transformers.streamlit.app/%5B1.3%5D_Indirect_Object_Identification)
- ✅ apply path patching from colab to get template, then apply to numseq
- ACDC main demo- get it to work on finding greater-than circuit diagram
    
    NOTE: we don’t need ACDC to get this diagram, as it gets a more complex, bigger circuit (that’s better than what’s in paper, but paper is good enough; too many edges is not needed)
    
    [Code- **Towards Automated Circuit Discovery for Mechanistic Interpretability**](https://www.notion.so/Code-Towards-Automated-Circuit-Discovery-for-Mechanistic-Interpretability-999dfd3c865a403399259ca69c0ae375?pvs=21) 
    
- ✅ Outline path patching steps to get a circuit diagram
- Construct a circuit diagram for numseqs/months, and compare w/ greater-than circuit diagram
    - Find more causal evidence for edges BETWEEN components, not just "these are important components". Path patching between components to find these more precise interactions. [Path Patching](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Path%20Patching%20967be4e1a2b241418a9603911dda4561.md)
        - get the right ‘abc dataset’ for digits; may use num among words. try and compare different corruptions (put in appendix, rmv test prompt failures in main section)
            
            ✅ RESULT: Tried different corruptions (repeat last, repeat all, etc) to compare path patching results. Traced back 9.1's impt heads (4.4, 5.5, 6.6) and back from those (0.1, 3.0)
            
            - OPTIONAL: email to ask for opinions on choice of corruption
            - mix different types of corruptions and take mean?
- ⚠️ Mean ablation numseq by repeating last. [Mean Resampling Ablation](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Mean%20Resampling%20Ablation%20d7fd15fac3324baa96d82bada82340a1.md)
    - ✅ Check how Greater-Than circuit performs here
    - Brainstorm how to properly use and analyze path patching results to find the right heads
    - [Search Methods- ask ChatGPT](../../Brainstorming%20Notes%203f11ad066e9b4a07b4eac05b6b2474c4/Search%20Methods-%20ask%20ChatGPT%20c68457cff88c4c3ba4b7fc775684496a.md)
    - Narrow circuit search to seq positions for ablation expms
    - Narrow to q, k, or v
    
- TBC- Make copy of current, then idealized draft
- ✅ [Draft search “work backwards”](../../Brainstorming%20Notes%203f11ad066e9b4a07b4eac05b6b2474c4/Search%20Methods-%20brainstorm%2015a3020ab00b40adb79b0acf3622f5f4.md)
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
- ⚠️ [gpt2-greater-than](../../gpt2-greater-than%201d1763531c964ad28af1ee43c2253f19.md)
    - try to use rust-circuits in colab
- ✅ Turn ‘work backw’ to code. [Search Methods- brainstorm](../../Brainstorming%20Notes%203f11ad066e9b4a07b4eac05b6b2474c4/Search%20Methods-%20brainstorm%2015a3020ab00b40adb79b0acf3622f5f4.md)
- ✅ Automate to get edges: [Path Patching after Work Backw](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Path%20Patching%20after%20Work%20Backw%20926c3d71d6304852afcc271974028aec.md)
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
- ~~⚠️~~ Debug path patching to get edges that connect all heads, such that all connected heads get score that is close to full performance.
    - ✅ SOLN: the heatmap uses `100*results`, so what you see if 100x bigger than the actual values. Thus, adjust edge threshold to be the ACTUAL results, not 100x. The reason 100x was used is because values like 0.0001 are displayed with sigfigs badly on heatmap
    - ✅ plot distribution of path patch edge thresholds for each end-head to get avg for all. combine all into one
        
        [numseq_path_patch_iterThres.ipynb](https://colab.research.google.com/drive/1onREXMNmc9ks0xpwDslUX2pdG0RSYtWS#scrollTo=wzGVQFqhVQUi&line=10&uniqifier=1)
        
    - ✅ Did they use a threshold in the paper? Cannot find it, so email authors
    - How to measure score not by ablating nodes, but by ablating edges?
    - ISSUE- path patching adds nodes, but a circuit cannot have source nodes that are not part of the first layer?

Shared Circuits for Similar Tasks

- ✅- Test digits circuit on months, etc. [Months circuit](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Months%20circuit%20765ea1869818426298c439544a337efc.md)
- ✅- path patch on months. [Months path patch](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Months%20path%20patch%20190601513e60424fbf7a9a8ef00a8317.md)
- ✅- decr seq circuit
    
    [https://chat.openai.com/c/38b2ee8a-d6b6-405f-a993-fa129d1cd378](https://chat.openai.com/c/38b2ee8a-d6b6-405f-a993-fa129d1cd378)
    
- ✅-  [numwords_mincirc_repeatLast](https://colab.research.google.com/drive/1hEEWySgGjWxy_UWpAuT5Oh_pf4hSAvmv#scrollTo=GCCCoO0V7L7J).ipynb. [Numwords path patch](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Numwords%20path%20patch%20324547790e19453c9c0dc07488a9b67b.md)
- ⚠️ 2, 4, 6 and other seq circuits
    
    existing: numseq_test_prompts_SMALL
    
    new: [numseq_prompts](https://colab.research.google.com/drive/1rNRrvr4qzy_zjPUK-4mJHruwFKnomrnP#scrollTo=r9_yofz3WkYm), pt2.ipynb  [Add 2 prompts](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Add%202%20prompts%20cfe4115b82634ce1b89a1afd0df9c9ba.md) 
    

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
- ✅ Move novel methods brainstorm to [Future work](../../Brainstorming%20Notes%203f11ad066e9b4a07b4eac05b6b2474c4/Future%20work%20a8d30bf9c84546da862cb2a95da71dfc.md)

Attention Head Functionality

- ✅ Logit lens
    - outdated: [https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens](https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens)
    - [https://colab.research.google.com/drive/1-nOE-Qyia3ElM17qrdoHAtGmLCPUZijg?usp=sharing#scrollTo=AvtLSbiZkU2K](https://colab.research.google.com/drive/1-nOE-Qyia3ElM17qrdoHAtGmLCPUZijg?usp=sharing#scrollTo=AvtLSbiZkU2K)
    - [sim_tasks_logit_lens.ipynb](https://colab.research.google.com/drive/1GeM2vLnIan_q6kdiGKQoDcMrAtYe0FLG#scrollTo=nKl9H9E625Vm)
- ✅ Look at previous results of actv patch movement + attn patterns, and relate to new circuits
    - ✅ [4.4 is prev number head](https://colab.research.google.com/drive/1FThBbzvhipfGHb4jwdXLA6iXlIv75spp#scrollTo=HjXea78dIAif&line=6&uniqifier=1)
    - ✅ re-org draft to ‘early, mid, late’ instead of by technq to better compare evidence for each type
    - ✅ re-org next/copy scores to combine w/ mid/late
- ✅ [How did prev papers diagnose early + mid? Try getting interpretations from prev papers that used the same heads](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Early%20Head%20Analysis%20b73c8162b7334655ad1ff91fb236b69e.md)
- ✅ [look at attn patterns for more heads than just the top 10](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Early%20Head%20Analysis%20b73c8162b7334655ad1ff91fb236b69e.md)

Connectivity

- 🐣 [Play around with manually sel heads for **incr digits circuit**, and check their func](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Manual%20path%20patch%208d30748bcf9448bf9a0b76ce78ed1dfb.md)
    - 🐣 **[iter patch from manual sel](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Early%20Head%20Analysis%20b73c8162b7334655ad1ff91fb236b69e.md)**
        - ✅ re-run ablation on circ found from path patch (that adds nodes).
        - ✅ how much better is it than before adding nodes?
        - [✅ re-run ablation on circuit after ipp gets rid of nodes w/o outgoing edges.](../../Project%20Planning%203798a71e7c5d4a888cad9a7d25a1275c.md)
        - ✅ Re-run ablation on both “no new nodes from ipp” and “then rmv nodes w/ no outgoing E” on lower Ethres of 0.001
        - 🐣 How much above the mean actv logit diff is Ethres of 0.001 ?
        - 🐣 w/o incoming edges?
    - 🐣 If rmv head, is correct answer still in 1st place; if not, what does it fall to?
    - 🐣 see if removal coincides with importance on attnpat; record what performance difference each of the circuit’s heads makes. Are numdetect heads like 4.4 crucial? Are there backups?
- ✅ ISSUE- a circuit has source nodes that are not part of the first layer?
    
    As seen in IOI/ACDC diagram, you CAN have heads w/ no incoming edges that are in later layers, as long as they have an edge from an input token.
    
    - get circuit which only adds edges; don’t add node if not in input to fn. Run on circuit found via manual sel

Writing :  ✅ move early heads to appendix; new writing about seq det only

- [✅ plan](../../Brainstorming%20Notes%203f11ad066e9b4a07b4eac05b6b2474c4/_Brainstorm%20plans%20(chrono)%20a93e919e5bff4109bf54f6d3febb05c4/23%2010%2021-%20Plan%2004b6844e61624b28a654df94ee7e7a40.md)

Conn/Fn: 

- ✅ ⚠️ prune backw once by among words
    - ✅ ⚠️ figure out how to ablate repeated seq pos
    - ✅ [OR test among names without repeated tokens like ‘is’, ‘.’ also works](https://colab.research.google.com/drive/1E1afH63aiKqTp9fqn3hnun1EwErZXzRt#scrollTo=3M6ZKSyJtOAE&line=1&uniqifier=1)
        - ✅ ⚠️ [run from full circ](https://colab.research.google.com/drive/1E1afH63aiKqTp9fqn3hnun1EwErZXzRt#scrollTo=Oq0svFCVsp7N&line=14&uniqifier=1) to get among words circuit
        - ✅ ⚠️ get set diff with pure circuit
- ✅ make template for autoAblation
- ⚠️ to get more diverse circuits (months circ arguably is the same), try other sequences
    - ⚠️ repeating autoAblation
- ✅ debug why `ioi_circuit_extraction.add_mean_ablation_hook` , when passing in full circuit for *seemingly* every pos, doesn’t get 100% of score. this is likely due to not every pos being accounted for.
    - ✅ SOLN: seems like `tokens.index(target_token)` is the issue because the repeated numbers have multiple indices. Instead, these indices should be put in prompt_dict when the prompt is created. add `pos_dict` to `prompts_list` before passing to `dataset` class
- ✅ back to [repeatDigits_autoAblation](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/repeatDigits_autoAblation%206d3119d544f24f938eb4abe0016e9503.md)
    - ✅ run backw once ablation on repeatDigits and compare circ to IOI
    - ✅ compare to repeatLetters
- ✅ ablate by seq pos (found by attention pattern analysis) [QK ablation](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/QK%20ablation%20f9f1b2ff2d944674a98e5b872acd5009.md). ([revisit](../Done%20b715c92198314529880806d9f206803d.md))
    - ✅ Change both of these (dict key is head type): **is seq pos q or k? See prev n**
        
        `CIRCUIT = {"number mover": lst,`
        
        `SEQ_POS_TO_KEEP = {"number mover": "end",`
        
        key vectors are always kept; query vectors only kept if specified
        
    - ✅ ablate by among words (for number detectors). [amongWords- QK ablation](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/amongWords-%20QK%20ablation%20a6648bdac8b14573880294c84ead3474.md)
        - ✅ why not get 100% when pass in full circ?
            
            SOLN: the corrupted had repeated tokens in “Adam 1 Bob 2 Claire 3 Don 3 Eve”, so the repeated query seq pos index (the second 3) was not kept (non-ablated) when running `tokens.index(target_token)`. The previous dataset of “1 2 3 3” did not have this issue as the datasets always kept the query end pos non-ablated, which was coincidentally on the second 3. But in the new case, the last token was “Eve” so this did not occur.
            
        - ✅ run auto ablate on all seq pos
        - ✅ run pure digits on obtained circ
            
            [strangely, it doesn’t work](https://colab.research.google.com/drive/1E1afH63aiKqTp9fqn3hnun1EwErZXzRt#scrollTo=qgpGMTWLbibq&line=1&uniqifier=1)
            
        - ✅ compare with IOI, which had 87% of original logit diff. So use a 90% circuit
        - ✅ ablate using guessed seq pos from attn pats
        - ✅ [This shows you don’t need any heads for the names at all](https://colab.research.google.com/drive/1E1afH63aiKqTp9fqn3hnun1EwErZXzRt#scrollTo=KCQHY4f8DnYS&line=37&uniqifier=1)
        - ✅ [Try random words instead of names](https://colab.research.google.com/drive/1E1afH63aiKqTp9fqn3hnun1EwErZXzRt#scrollTo=OQpqlEjwED7b&line=1&uniqifier=1)
- ✅ [reformat_circ_diag.ipynb](https://colab.research.google.com/drive/1UNl70DP9z76Lb7BNiruWP8gJVm0WLRhR#scrollTo=A35UJE7yw5pO)
    - ✅ save matplotlib as pdf instead of pasting png into visio and exporting

writing

- ✅ open problems msg
    
    I did some preliminary work on this during a hackathon this July, and found components shared between sequence contnuation tasks such as head 9.1 that were found to output the “next member” of a circuit. The work was rushed and crude but I am looking to polish and continue it in the future. A link to it can be found here: [https://alignmentjam.com/project/one-is-1-analyzing-activations-of-numerical-words-vs-digits](https://alignmentjam.com/project/one-is-1-analyzing-activations-of-numerical-words-vs-digits)
    
- ✅ post on mech interp server
    
    Hi everyone, I’m yonedo and started getting into interpretability this year. A starter project I did this July was to tackle a problem from Neel’s 200 open problems list about continuing sequences that could be mapped to the natural numbers such as numbers, months, days, and letters. One of the things found was that these tasks share a lot of components, such as head 9.1 in gpt2-small (which, by checking which values are written by its OV matrix, seemed to output the “next member” of a sequence). This prelim analysis was crude and thrown together in a few days, but I’ve been working on continuing it in a new direction! I’m open to collaborating on anything similar so feel free to reach out! (or if you/a group want to polish and extend it yourself, feel free to let me know which direction you’re taking so I can plan another a different one and not spend time doing the same thing you’re doing haha). I’ll likely be lurking a lot to learn and try experiments I see before posting more (Project link): [https://alignmentjam.com/project/one-is-1-analyzing-activations-of-numerical-words-vs-digits](https://alignmentjam.com/project/one-is-1-analyzing-activations-of-numerical-words-vs-digits)
    

✅ [New Novel Contributions](../../Brainstorming%20Notes%203f11ad066e9b4a07b4eac05b6b2474c4/New%20Novel%20Contributions%207ec236f64f394e9cb03b32ca0fbf319b.md) 

✅ [Multiple Matches Algo](../../Brainstorming%20Notes%203f11ad066e9b4a07b4eac05b6b2474c4/Multiple%20Matches%20Algo%203d83df8af72c4233b51d6c60cd022f8b.md) 

- ✅ [format circ diagrams](../../Brainstorming%20Notes%203f11ad066e9b4a07b4eac05b6b2474c4/format%20circ%20diagrams%206c4906c1a09f4df399d376dee58af27b.md)
    - ✅ use different colors (fill and outline) to denote common nodes and node types.
    - ✅ highlight edges if they’re between 2 highlighted nodes.

Circuit Connectivity

- ✅ 2 4 6 8 VS 2 4 8 16 on medium
    - [add2_med_autoAblate.ipynb](https://colab.research.google.com/drive/1kpKTk7E4iUgiByOAL-8Jr2kHN2Q--1u8#scrollTo=DQF0lzuokQer)
    - [add1_med_autoAblate.ipynb](https://colab.research.google.com/drive/1Pvoo3wchXIhYof11hUJHpOONELzQccjd)
    - [multp2_med_autoAblate.ipynb](https://colab.research.google.com/drive/1ofiEOCaS7-f4CBOgLqGX2g30ToMNHONr#scrollTo=cL6iz8nbIRcL)
        
        medium fails on mulpt2 for seqs not starting at 2 unless you give it at least 6 members in input
        
- [✅ brainstorm plans](../../Brainstorming%20Notes%203f11ad066e9b4a07b4eac05b6b2474c4/_Brainstorm%20plans%20(chrono)%20a93e919e5bff4109bf54f6d3febb05c4.md)
- ✅ [Why is pure digits circuit bigger than among words](../../Brainstorming%20Notes%203f11ad066e9b4a07b4eac05b6b2474c4/Why%20is%20pure%20digits%20circuit%20bigger%20than%20among%20words%2094916895ee7c464780702d5720045b50.md) : [hyp](../../Brainstorming%20Notes%203f11ad066e9b4a07b4eac05b6b2474c4/Why%20is%20pure%20digits%20circuit%20bigger%20than%20among%20words%2094916895ee7c464780702d5720045b50.md)
- ⚠️ Make overall circuit diagram using “less accurate” circuits so far
    - ✅ color nodes based on overlap
        
        [https://chat.openai.com/c/dd496692-4b97-4b21-8ec6-e28d39dea31c](https://chat.openai.com/c/dd496692-4b97-4b21-8ec6-e28d39dea31c)
        
    - ⚠️ add legend
        
        [https://chat.openai.com/c/548af866-8605-454a-a071-6c0ae9a0feee](https://chat.openai.com/c/548af866-8605-454a-a071-6c0ae9a0feee)
        
        [https://chat.openai.com/c/687e8659-1b6d-4c66-8710-fa594d0c5108](https://chat.openai.com/c/687e8659-1b6d-4c66-8710-fa594d0c5108)
        
        [https://chat.openai.com/c/d7648bbd-61b9-42a7-bccd-e1d52b37f623](https://chat.openai.com/c/d7648bbd-61b9-42a7-bccd-e1d52b37f623)
        
    - color edges based on head node
    - position words by clustering nodes of certain color in different places
        - [https://chat.openai.com/c/5298883a-4979-4cb4-a97f-0872776c6821](https://chat.openai.com/c/5298883a-4979-4cb4-a97f-0872776c6821)
        given a that each set of nodes is in the format similar to [(0, 1), (0, 3), (0, 5), (5, 5), (6, 1), (7, 10), (9,1)], rewrite the following code so that after sorted, the earlier nodes are on top of the graph while the later nodes are more towards the bottom:
    - order nodes by sorted label
- ✅ Make draft of “overall figure” manually in visio
- ✅ test prompt: “x + 1 =” for various x
    - ✅ [try on gpt2-small](https://colab.research.google.com/drive/1rNRrvr4qzy_zjPUK-4mJHruwFKnomrnP#scrollTo=f-69B8EZN28Q&line=1&uniqifier=1) : it doesn’t work
    - ✅ [gpt2-med:](https://colab.research.google.com/drive/1QXktEOMDojC7QpfHjX2eSqsRkn8gt4er#scrollTo=f-69B8EZN28Q) it doesn’t work, even with in-context. But it DOES work in-context with this: `["1 table 2. 10 table 11. 3 table 4. 5 table"](https://colab.research.google.com/drive/1QXktEOMDojC7QpfHjX2eSqsRkn8gt4er#scrollTo=_hXXwqqNQ4Wi&line=3&uniqifier=1)`
        - comment
            
            I was also testing "x + 1 =" prompts for gpt2 small and med and it doesn't work, even with in-context. however, there's some strange in-context pattern where "1 table 2. 10 table 11. 3 table 4. 15 table" gets "16." And replacing that last number 15 with "101 table" gets "102". This strange pattern may be combining both induction and "next seq" and may have overlaps with seq cont, I'm going to look into its circuit now (the "table" is just a random word, as the induction patterns in the anthropic paper tested random word data to find induction heads. it can be replaced with other words)
            
            basically one of the main goals now is to figure out what components separate diff circuits, such as incr digits vs greater-than. I think the task described above can shed light on this as it is somewhere between those two tasks
            that's true, too many tasks would not fit the paper. I think that's all the new tasks I'll look into (we have around 8) so it'd be feasible to analyze them until next week (11/1). then we can get the first draft around that time on arxiv
            
- 🐣 [logit lens decr](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/logit%20lens%20decr%2080b75441653c4fed99eb1f3919e37dfb.md)
- ✅ daily [plan](../../Brainstorming%20Notes%203f11ad066e9b4a07b4eac05b6b2474c4/_Brainstorm%20plans%20(chrono)%20a93e919e5bff4109bf54f6d3febb05c4.md)

Circuit Connectivity- better corrupted dataset patching

- ✅ [numseq_mincirc_repeatAll.ipynb :](https://colab.research.google.com/drive/1AZrx6xvGt1t1m9oKVkrRgIzkoKZRzq8F#scrollTo=Lk3bffnCYq-p) fix the “same index” issue that cause it not to keep all pos of circ during SEQ_TO_KEEP. Run fb, bf- at 3%, 10% and 20%. Get diffs
    - ✅ instead of repeating all nums of 1st elem, replace with repeats of a rand number bigger than them (eg. 100). [numseq_mincirc_repeatRandElem](https://colab.research.google.com/drive/1pFAit_o0k6u-EugBcWFAlwQxxo74Rjwk).ipynb
    - ✅ [test back_3 of ‘repeatAll’ using dataset of repeatRand](https://colab.research.google.com/drive/1pFAit_o0k6u-EugBcWFAlwQxxo74Rjwk#scrollTo=GFv3kw2tf6cB&line=1&uniqifier=1)
        
        It only gets 9%.
        
    - ✅ [test back_3 of ‘repeatRand’ using dataset of repeatAll](https://colab.research.google.com/drive/1AZrx6xvGt1t1m9oKVkrRgIzkoKZRzq8F#scrollTo=RUl8oHsrg61n&line=1&uniqifier=1)
        
        On the other hand, this gets 66%
        
    - ISSUE: this is making removal have greater logit diff sometimes.
        - looking at `logits_to_ave_logit_diff_2()`, and `new_score = logits_to_ave_logit_diff_2(ioi_logits_minimal, dataset)` , the aim is that so after ablating every head except the ones in the circuit, the correct token is still much higher than the incorrect token (eg. 5 vs 4). If it’s not still much higher (5 and 4 are close now), that circuit is missing key heads.
            - When a head is removed, if the score is HIGHER, that means the correct token is much higher than the incorrect score. So that head may have acted as an inhibition head.
            - How much higher? Ablate the model and run tokens through it to get predictions `ioi_logits_minimal`.
        - Try: KL divergence
- 🐣 [resample from random number seq.](https://colab.research.google.com/drive/12HF5UCvMERizkhOiYJKDziahgVq_3KD9#scrollTo=Lk3bffnCYq-p)
    - ✅ **[compare with repeatRandElem](https://colab.research.google.com/drive/12HF5UCvMERizkhOiYJKDziahgVq_3KD9#scrollTo=RUl8oHsrg61n)**
        
        actually does pretty well
        
    - ⚠️ issue is, what is the incorrect? see ABC for IOI. KL div doesn’t need this? (this is NOT an issue for mean ablation, only path patching).
        - find what IOI used as incorrect token in ABC: (lines 314?) [https://github.com/redwoodresearch/Easy-Transformer/blob/main/easy_transformer/ioi_dataset.py](https://github.com/redwoodresearch/Easy-Transformer/blob/main/easy_transformer/ioi_dataset.py)
        - this is only an issue when you’re doing path patching. usually incorrect token is what’s predicted (eg. repeat is the last few repeats). if random, what’s predicted? try them on test prompts
            - SOLN: run them and get their top answer. use that as the ‘incorrect’ token
    - mean ablation by random numbers for pure and among words
- 🐣 Compare the two new corruption types (repeatAll, repeatRand, randAll)
    - compare circs of all 5 corruptions types to each other for incr digits
    - get avg of what components appear in all various pruning and corruption runs
        - how impt are they (change in perf) and what’s their func? Func when together?
        

Circuit Connectivity- better iterative algos for all tasks

- ✅ path patching threshold: threshold itself is meaningless. it should be like p-value: what percentage of edges are above it? Eg) keep only edges in the top 50% of distribution
    
    [numseq_IPP_randAll.ipynb](https://colab.research.google.com/drive/1JFcEjNe0X4G1SrE52df4RFnP1bEza-re)
    
- ✅ Do fwd backw and bf both converge to same circ? Prob not bc combos matter so order matters. Find differ between them.
    - ✅ [incr digits, randAll:](https://colab.research.google.com/drive/12HF5UCvMERizkhOiYJKDziahgVq_3KD9#scrollTo=ZXouisDpS4qb) no, but they’re very similar for most impt heads. Their scores are both ~97.1%. In fact, getting their intersection gives a circuit of 82%, which is only a 15% drop.
        
        we could claim that these are “alternative circuits” such that what’s in fb but not in bf is an “alternative path”, akin to backup heads
        
        make a diagram of this for red, blue, purple
        
        We’ll just choose to use fb_3.
        
- ✅ the pp threshold itself is meaningless. it should be like p-value: what percentage of edges are above it? Eg) keep only edges in the top 50% of distribution
    - [numseq_IPP_randAll.ipynb](https://colab.research.google.com/drive/1JFcEjNe0X4G1SrE52df4RFnP1bEza-re)
- ✅ Reproduce and expand results of greater-than task
    
    [greaterThan_mincirc_draft.ipynb](https://colab.research.google.com/drive/1WmFphzbrqRugdUa1w7KBc2AWONMe765x#scrollTo=OO0m6DkS6klE)
    
    - ✅ Sum probs of greater than vs less than
    - ✅ Get pos of all input tokens for seq_to_keep
    - ✅ ablate by seq pos
    - ✅ backw prune
    - ✅ Test on more data samples
        
        [greaterThan_mincirc_draftv2.ipynb](https://colab.research.google.com/drive/14NrurcflDe4hC9WJqCvuJHzUR_q5wJJ-#scrollTo=WZl2yDK9BPtA)
        
    - ✅ Test fb prune and ipp on greater-than task
        
        [greaterThan_IPP.ipynb](https://colab.research.google.com/drive/19Le39gsiZOPqEat4VPHWDyU06My8GupZ#scrollTo=fg1gtdoVl6mU&line=2&uniqifier=1)
        
    - plot incr circ + greater-than in same graph (highL their E and overlap E)
    - ⚠️ start from greater-than and add heads, test probs of output tokens greater than YY, until get to increasing by 1
        - Does more heads mean less far away from YY? Measure each YY to 99.
        - Perhaps more heads are needing for more “specific”; try to vary by how specific the range is. Also by seq length (greater-than tasks use “one” sequence)
            - how does it change the probability of tokens further away from seq?
        - How can greater-than not have heads that are recognizing words other than the digit? Surely, it must process the other words, too. Note this in “future work”?
- ✅ ran iter N+E on decr
- ✅ from outputted circ, rmv head one at a time to find how impt it is for circ
    - [Impt Decr Circ Heads](../../Expm%20Results%208de8fe5b943641ec92c4496843189d36/Impt%20Decr%20Circ%20Heads%20109317c38d2d4bf2ba1c721d44e17d1a.md)
- ✅ [numWords_pruneNodes_randAll](https://colab.research.google.com/drive/1QTv-4osLHadCAay0beew-xlXszPCG88s#scrollTo=Lk3bffnCYq-p).ipynb
- ✅ incr months
    1. ✅ nodes: [months_mincirc_randAll](https://colab.research.google.com/drive/1lhQqlizYGMC11vzp6I9mJ3dyxIr8tV3l#scrollTo=VaxbugcfGlBA)
        1. 4.4 seems very impt, more than 9.1
    2. ✅ edges: [months_IPP_randAll](https://colab.research.google.com/drive/1Y4aWml4Y7PxcZtLwVt9FxIhr-MYmhoGX#scrollTo=9CApvkRLon1T).ipynb
- ✅ 123 medium
    
    [add1_med_autoAblate_randAll.ipynb](https://colab.research.google.com/drive/1chZ6_lfm1o6TYkuzW292dH_uMRKh4_S0#scrollTo=BU78LW-8zn5l)
    
    [numseq_nextScores_medium.ipynb](https://colab.research.google.com/drive/1FAeWI25abCXpL6DQzXwR1mqSwmlEfqpM#scrollTo=tVDqHi-jihTh)
    
- ✅ test 246 fails on medium; plus1 ind fails on small
- ✅ moreData incr digits fb 10: moreData_numseq_mincirc_randAll_v1.ipynb
- ✅ change ‘moreData’ corr to have digits between a certain range of decades, rather than random numbers from far away, so that it’s more within distribution of increasing numbers. see if it makes a difference in circuit size. Run on fb_10: [moreData_numseq_mincirc_randAll](https://colab.research.google.com/drive/1mFWmGAKtigFcqqWWMCwU7wWQY2HT5ZOo#scrollTo=C2fvsn5SFnrO).ipynb
    
    Doesn’t make a difference. Actually slightly worse.
    
- ✅ [Random removal](https://colab.research.google.com/drive/1mFWmGAKtigFcqqWWMCwU7wWQY2HT5ZOo#scrollTo=0sZHzHG9Qvla&line=1&uniqifier=1)
- ✅ Run incr digits at fb_25
- ✅ Find most impt heads for months
    - ✅ months: corr using rand months: months_mincirc_randAll.ipynb
        
        even if use no attn heads, get 7%. seems too high.
        
    - ✅ months: corr using rand digits: months_mincirc_randDigits.ipynb
        
        now this is way TOO low
        
    - ✅ randAll again but keep rand until get something where ‘no heads’ is decently low
        - use this
            
            [{'S1': 'April',
            'S2': 'October',
            'S3': 'April',
            'S4': 'September',
            'corr': 'April',
            'incorr': 'September',
            'text': 'April October April September'},
            {'S1': 'April',
            'S2': 'May',
            'S3': 'April',
            'S4': 'September',
            'corr': 'April',
            'incorr': 'September',
            'text': 'April May April September'},
            {'S1': 'September',
            'S2': 'June',
            'S3': 'June',
            'S4': 'January',
            'corr': 'September',
            'incorr': 'January',
            'text': 'September June June January'},
            {'S1': 'April',
            'S2': 'December',
            'S3': 'February',
            'S4': 'April',
            'corr': 'April',
            'incorr': 'April',
            'text': 'April December February April'},
            {'S1': 'June',
            'S2': 'April',
            'S3': 'October',
            'S4': 'December',
            'corr': 'June',
            'incorr': 'December',
            'text': 'June April October December'},
            {'S1': 'October',
            'S2': 'March',
            'S3': 'July',
            'S4': 'February',
            'corr': 'October',
            'incorr': 'February',
            'text': 'October March July February'},
            {'S1': 'September',
            'S2': 'January',
            'S3': 'February',
            'S4': 'April',
            'corr': 'September',
            'incorr': 'April',
            'text': 'September January February April'},
            {'S1': 'April',
            'S2': 'January',
            'S3': 'April',
            'S4': 'December',
            'corr': 'April',
            'incorr': 'December',
            'text': 'April January April December'}]
            
    - 🐣 run until fb_25 and bf_25, and rand_25
    
    Months uses the SAME circuit. No; it’s a SUB-CIRCUIT of increasing digits, as it doesn’t need as many due to the network needing to handle a smaller range of tokens.
    
- ✅ Most impt heads for numwords

Circuit Functionality- Sims + Diffs

- ✅ [List Tasks](../../Brainstorming%20Notes%203f11ad066e9b4a07b4eac05b6b2474c4/List%20Tasks%2075facafe9dd445a19ab98886caaaeaea.md)
- ✅ read “circuits re-use” for how they compared diff fns of components
- ✅ [Compare incr digits subcirc to non-numericals](../../Brainstorming%20Notes%203f11ad066e9b4a07b4eac05b6b2474c4/Compare%20incr%20digits%20subcirc%20to%20non-numericals%20867b7e175ac3405db361e57d9e07710f.md)
- get ipp graphs of 4 tasks (cols) at 4 lvls of perf (3, 10, 20, ~~25~~) using fb, bf, or rand
    - ✅ fb 80%: digits + numwords
        - [fb: moreData_numseq_mincirc_randAll.ipynb](https://colab.research.google.com/drive/1lhQqlizYGMC11vzp6I9mJ3dyxIr8tV3l#scrollTo=563kZf_4r_mw&line=2&uniqifier=1)
        - fb: [months_mincirc_randAll2.ipynb](https://colab.research.google.com/drive/1lhQqlizYGMC11vzp6I9mJ3dyxIr8tV3l#scrollTo=563kZf_4r_mw&line=2&uniqifier=1)
        - fb: [numWords_pruneNodes_randAll.ipynb](https://colab.research.google.com/drive/1QTv-4osLHadCAay0beew-xlXszPCG88s#scrollTo=563kZf_4r_mw&line=2&uniqifier=1)
    - ✅ [bf 97%](https://colab.research.google.com/drive/13WyGfWWN8tqso5vcegXcbZtLVtzhWnGR#scrollTo=N1up5KmnuLSL&line=1&uniqifier=1) digits + numwords
- table: rows are most impt heads, cols are tasks, values are importance
    - fb 80%
- Convert ‘mean ablation’ table to having circuits for each task found by ablation on each row (**See IPP for circ)**.
- ⚠️ [decr rand at fb 80: decr_numseq_iterN_randAll.ipynb](https://colab.research.google.com/drive/142sKzJR1Dnzn9rLcjTEw9EfdfAizpxDU#scrollTo=cGX9iHAz_UKX)
    - [compare to prev scores](https://colab.research.google.com/drive/1gYqAcfJS3igpZsD97KffPK1E9saN33oY)
- ✅ Use more data for numwords
    - ISSUE: the performance highly depends on the random dataset (esp when fewer datasamples!) Try to increase from 6 samples to more! Perhaps 1.5 is more active when there are more samples.
        
        [numWords_pruneNodes_v2ipynb](https://colab.research.google.com/drive/1A8Q01TvO5ZQxY-OtVN9amRsAu4fUlRT3#scrollTo=0lAe9hlO8m93&line=1&uniqifier=1)
        
        [https://chat.openai.com/c/e4388104-2564-46aa-ab72-07ca41e9b0b3](https://chat.openai.com/c/e4388104-2564-46aa-ab72-07ca41e9b0b3)
        
        wait; I can use as many as I want for clean (one to twelve). corrupted just has to use one to ten. but this fails upon twenty.
        
        when choosing ‘random words’ for one to twelve, dataset_2.toks has dims (8,5) while clean has dims (8,4)
        
        The culprit is “eleven” is two tokens. Twelve is 1 token. yet how come dataset_1 doesn’t suffer from this?
        
        ![Untitled](ArXiV%20Draft%20v1%2035c75a5f1929460fb199edd5fce9a6fe/Untitled.png)
        
        when eleven is in front, it’s split into 2 tokens. when elven has a space in front, it’s 1 token:
        
        ![Untitled](ArXiV%20Draft%20v1%2035c75a5f1929460fb199edd5fce9a6fe/Untitled%201.png)
        
        One solution is to always use a space in front, even for start of seq
        
        [Interestingly enough, this increases the correct prob (perhaps bc all are seen as the same)](https://colab.research.google.com/drive/1A8Q01TvO5ZQxY-OtVN9amRsAu4fUlRT3#scrollTo=jTR2muCD-jxb&line=2&uniqifier=1)
        
        now that it expands from 6 to 16, it’s a bit more accurate in terms of randomness (around 45 to 55, instead of wildly varying from 40 to 70 more often; the distribution is more narrow though still susceptible ):
        [https://colab.research.google.com/drive/1A8Q01TvO5ZQxY-OtVN9amRsAu4fUlRT3#scrollTo=61QILI7yChjM&line=1&uniqifier=1](https://colab.research.google.com/drive/1A8Q01TvO5ZQxY-OtVN9amRsAu4fUlRT3#scrollTo=61QILI7yChjM&line=1&uniqifier=1)
        
    - spaces in front due to separating into two tokens when no space for some number words over ten, such as ‘eleven’
    - don’t add space in dataset, just when making prompts
    - cleanup in: [moreData_numWords_pruneNodes](https://colab.research.google.com/drive/1DRUn2CYHbb_8H7MpZljCNfcjeXIvrvnj#scrollTo=YyiuksuLCQSA).ipynb
    - re-run numwords circuit at 80, 90, 97
- ✅ [repeatNew](https://colab.research.google.com/drive/1DRUn2CYHbb_8H7MpZljCNfcjeXIvrvnj#scrollTo=PjLGSZgqWvKt&line=1&uniqifier=1): replace with a repeating rand number (last two) and predict that as the ‘incorr’ token
    
    to erase info about all numbers in input, given last token T, use T+2 repeat last two (mod len words if numwords or months), then randomize first two or use T+2 again, or T+4 and T+7 (T+4, T+7, T+2, T+2) to reduce randomness. If this doesn’t make a difference, don’t use it.
    
    T+2 is that it’s sometimes “second place”:
    
    ![Untitled](ArXiV%20Draft%20v1%2035c75a5f1929460fb199edd5fce9a6fe/Untitled%202.png)
    
    Not always:
    
    ![Untitled](ArXiV%20Draft%20v1%2035c75a5f1929460fb199edd5fce9a6fe/Untitled%203.png)
    
    actually this doesn’t work; it predict the next one instead of the repeat:
    
    ![Untitled](ArXiV%20Draft%20v1%2035c75a5f1929460fb199edd5fce9a6fe/Untitled%204.png)
    
    - maybe just repeat all for T+2 or T+3 or i-1 mod R
    
- ✅ [replace numword results using ‘more data’ and new rand corr DS (clean measures dist of i+4 to i-1)](https://colab.research.google.com/drive/1DRUn2CYHbb_8H7MpZljCNfcjeXIvrvnj#scrollTo=0lQxi-66nK-E&line=1&uniqifier=1)
    - ✅ compare this to repeating using clean logit diff of i-1 vs i+3
- ✅ all_in_one_randAll_cleanedUp.ipynb - ISSUE: model run with cache is unique to each dataset. so it’s better to separate them into new nbs to prevent this.
- ✅ clean up numwords and run again: [numwords_randAll_cleanedUp](https://colab.research.google.com/drive/1WsZXGXtWLHdvkP93Qd4jenE1kzKySz9o#scrollTo=cGX9iHAz_UKX).ipynb
- ✅ clean up digits using 'incorr': str(i+3):
- ✅ ISSUE: months i+3 doesn’t get 9.1!  But incorr i does using the same rand DS!
    - [run it again to confirm more it’s i+3](https://colab.research.google.com/drive/1KcODa7naVMJbOvHBGUL_CFxyfmAMM5YI#scrollTo=UCsBj6jxUlnY&line=1&uniqifier=1), using differ rand DS
        - AGAIN, i+3 rmvs 9.1! The score is way tooo high when using i+3.
        - For months, perhaps stick with i as the incorr?
- ✅ run digits and numwords again using incorr as i
    - circs are slightly bigger
    - their comparisons to each other’s (i+3, i) and months i:
        - digits is around the same
        - numwords does worse on both digits and months
        
        VS 
        
    - (them using incorr i+3)
    - run this again- why does digits incorr(i+3) have inconsistent score slight drop? is it not using the same random corr data?
- ⚠️ use more data to corr greater-than
    - v2: don’t use 10 to 90
    - v3: use 10 to 90, compare to others
- ✅ use the same rand generated corr datasets to cross-test and do IPP
    - overall_circ_diag_draftv3.ipynb: multi numwords using incorr token i+3, while months using incorr token i.
    - revise digits to use corr dataset of between decade range (but no seqs), as this has a smaller circuit
- ✅ [97% digits incorr i+3 but using decades as rand](https://colab.research.google.com/drive/1A3EgZW_0HWrIX3woMk8ZEdrbEQid25Yq#scrollTo=5WMQhoCYvacq&line=1&uniqifier=1)
    - is this smaller, and thus more displayable? incorr using i wasn’t much smaller.
        - nope, it’s 54. so the only one being 42 prob just got lucky.
- ✅ redo this all for 80% using incorr i+3
    - [overall_circ_diag_draftv3.ipynb](https://colab.research.google.com/drive/18xrVQC6RsfYqk79TLC7pbcgYR-nflSkZ#scrollTo=Z2sR97NZCESJ)
    - reduce graph size using ranksep 0.45, nodesep 0.12
        
        [https://chat.openai.com/c/b226b8a6-b808-4ac1-9679-6caae41ca694](https://chat.openai.com/c/b226b8a6-b808-4ac1-9679-6caae41ca694)
        
- ✅ redo fig 1

Finalize shared circuit table results into writeup

- ✅ table: rows are most impt heads, cols are tasks, values are importance (2 dec places)
    - ✅ fb, 80% circuits
        - [digits](https://colab.research.google.com/drive/1mFWmGAKtigFcqqWWMCwU7wWQY2HT5ZOo#scrollTo=kSqJW5C6k2X2&line=1&uniqifier=1)
        - [numwords](https://colab.research.google.com/drive/1QTv-4osLHadCAay0beew-xlXszPCG88s#scrollTo=S3AxZcsWe30_&line=1&uniqifier=1)
        - [months](https://colab.research.google.com/drive/1lhQqlizYGMC11vzp6I9mJ3dyxIr8tV3l#scrollTo=S3AxZcsWe30_&line=1&uniqifier=1)
        - decr_numseq_iterN_randAll.ipynb : use len 8 instead of 10;
    - ✅ bf, 97% circuits, rand ablation, clean incorr is i+3
        - [~~numwords~~](https://colab.research.google.com/drive/1A8Q01TvO5ZQxY-OtVN9amRsAu4fUlRT3#scrollTo=C2EgKgmJS4qb&line=2&uniqifier=1) replace this with more data numwords
            - ~~this has 1.5~~
        - [numwords](https://colab.research.google.com/drive/1A3EgZW_0HWrIX3woMk8ZEdrbEQid25Yq#scrollTo=MrMM2RCA1QJ_&line=7&uniqifier=1)
        - [digits](https://colab.research.google.com/drive/1mFWmGAKtigFcqqWWMCwU7wWQY2HT5ZOo#scrollTo=C2EgKgmJS4qb&line=1&uniqifier=1)
- ✅ Convert ‘mean ablation’ table to having circuits for each task found by ablation on each row (**See IPP for circ)**.
    - ✅ fb 80% comparisons
        - [Incr Circ(s) on other tasks (numwords, months, decr)](https://colab.research.google.com/drive/1mFWmGAKtigFcqqWWMCwU7wWQY2HT5ZOo#scrollTo=dC4VKp97r1-e&line=1&uniqifier=1), GT, IOI
        - [numwords](https://colab.research.google.com/drive/1QTv-4osLHadCAay0beew-xlXszPCG88s#scrollTo=dC4VKp97r1-e)
        - [greaterthan](https://colab.research.google.com/drive/14NrurcflDe4hC9WJqCvuJHzUR_q5wJJ-#scrollTo=dC4VKp97r1-e)
    - ✅ bf 97% comparisons
        - [numwords](https://colab.research.google.com/drive/1A3EgZW_0HWrIX3woMk8ZEdrbEQid25Yq#scrollTo=xbZkzn0nrrxt&line=1&uniqifier=1)

Attn pats for all types

- ✅ Functionality of similar components
    - ✅ stare at similar circuits for what’s sim/diff. look at conns + relate to head fns
        
        you don’t need to compare or explain all the differing heads; just the most impt ones. get importance score of each head after removing
        
    - ✅ fix `import seaborn as sns` in multiAdamis1_newAttnPat_draftv3.ipynb
        
        AttributeError: module 'numpy.linalg._umath_linalg' has no attribute '_ilp64’
        
        - notice the error only occurs after loading the setup; we can import seaborn if we don’t load the setup.
            
            SOLN: get rid of this:
            
            ```
            # !curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -; sudo apt-get install -y nodejs
            # %pip install git+https://github.com/neelnanda-io/PySvelte.git
            ```
            
            and run ‘import seaborn as sns’ before loading and installing git repo
            
    - [rand1_attnPatipynb](https://drive.google.com/drive/folders/1gUqvn_ASP3gGo-4BCGdWcZ9aNtIo7kWJ)
        - ✅ fix colors and lines, etc.
        - ✅ table 1 lamp 2
        - ✅ amongNumWords_attnPatipynb
        - ✅ months
        - ✅ get all 4 impt heads for all prompts
    - ✅ numwords and months doesn’t need 1.5. check 1.5 on digits vs others.
        
        note- 1.5 and 4.4 were not considered ‘most impt heads’ in hackathon rep
        
        7.11 has very low copy and next scores; 7.10 has high copy scores
        
- ✅ IPP graph at various lvls of perf and pure/mixed comparisons
    - ✅ fb 80%
    - ✅ bf 97%
    - overlapping graphs for months & other 2 (test variations)
        - ✅ months and digits 80%, 3et (rmv nodes)
            - [months after rmv](https://colab.research.google.com/drive/1KcODa7naVMJbOvHBGUL_CFxyfmAMM5YI#scrollTo=emDa-KEmFwyk&line=2&uniqifier=1)
        - ✅ numberwords and months 80%, 10et (rmv nodes)
        - ✅ numberwords and months 80%, 15et (no rmv any)
    - ✅ 5 or 10% E threshold for digits 80% n thres
    - ✅ all 3 tasks in 1: [overall_circ_diag_draftv5](https://colab.research.google.com/drive/1NhIZyQdiz88xblWmHFtgAufovLeUlJ8F#scrollTo=fNOHvdKOafxK).ipynb
        - ✅ get edges for numwords + months, digits + months, and all too

Writing

- ✅ discuss entanglement and interference? superposition?
- ✅ attn pat in methods
- ✅ Definitions: Do not consider a circuit a *fucntional sub-circuit/subset* unless its nodes perform the same function. Define what percentage of it shares functionality. However, do consider circuits a *connective sub-circuit/subset* only if it shares impt nodes/edges. Say subset of if not all E appear; subgraph if all E of A are in B

Last Work before Finishing Draft V1

- ✅ Functionality of similar components
    - ✅ mix digits, numwords, months in same prompt (two jan)
        - ✅ others are in sequence: [inOrderDigitsMonths_attnPat.ipynb](https://colab.research.google.com/drive/1dPkrHLmaEhM0d3ns0gPuIwTKiH36P7lF#scrollTo=s7wUq-v8aIUW)
        - ✅ others are not in seq (rand): [unOrderDigitsMonths_attnPat](https://colab.research.google.com/drive/1T_U3444q0kJMQBue8Ldhyr5wGd_Ul5Nu).ipynb
    - ✅ ~~in visio, put all the 1.5 and 4.4 into 2 giant figures that fits on a page so latex doesn’t break it up into diff sections~~  used **\FloatBarrier instead**
    - ~~obtain for pure digits~~
- ✅ IPP graph at various lvls of perf and pure/mixed comparisons
    - ✅ greater-than & overlap w/ incr digits
    - ✅ decr & overlap w/ incr digits
    - Get intersection of all perf and find its perf.
    - ~~plot num_heads vs performance~~
- ✅ Writing
    - ✅ add back in MLP actv patch, neuron patching, etc in appendix A
    - ✅ write about previous head scores
        
        query (dest) of where info moves to. move to all pos. however we will perform more expms to verify this claim in future work. this means each token relies on those heads to get info. only head 9.1 can be put at end without any change. non-ablate every query pos. future work: ablate every query pos except the important ones where the head is important for moving info to.
        
    - ✅ describe this briefly:
        - ✅ we ablate on every position
        - ✅ path patching conscv layers like conmy, no input/residual post (appendix footnote)
    - ✅ just metnion in future work:
        - future work: circuits of mixed/among
        - remove by combos at a time (eg. rand choose 3)
            
            Without 5.5, may have to rely on other heads. 
            

---

**Previous To-Do list categories**

[23 10 9 - 23 10 15](ArXiV%20Draft%20v1%2035c75a5f1929460fb199edd5fce9a6fe/23%2010%209%20-%2023%2010%2015%20546cb16c31664f68a2eb976d8a60e033.md)