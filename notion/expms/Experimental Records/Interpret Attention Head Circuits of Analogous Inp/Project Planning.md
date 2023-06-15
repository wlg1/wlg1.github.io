# Project Planning

### Working on

- Figure out the dims for z in copy_scores to see how skipping QK matrix “fully attends to the name tokens”
    - look at IOI copy nbs or [Most Recent S Name Movers](Most%20Recent%20S%20Name%20Movers%20a72ccc6fdccc4e4baa78251399fdd2d7.md)
    - [https://www.notion.so/wlg1/Modify-copy-circuits-code-648e57729e8a495d9b4786dfd8e2499e](Antonym%20Circuits%20and%20Neurons%20824f0d162ce84a8fb09c27f4e4931194/Modify%20copy%20circuits%20code%20648e57729e8a495d9b4786dfd8e2499e.md)
    - [https://www.notion.so/wlg1/Query-Key-Value-Matrices-fe92464f6ee24068b6aaa56bb85e903e](https://www.notion.so/Query-Key-Value-Matrices-fe92464f6ee24068b6aaa56bb85e903e)
    - what about v?

### Ongoing Issues

- 

### Done

1) **Learn Existing Techniques and Workflows**

[Learn a workflow of transformer interpretability expms](Project%20Planning%20821fd0c71f4d4a44b5f7b240725c5547/Learn%20a%20workflow%20of%20transformer%20interpretability%20e%2055b5218ed69840b4b15da2070c413538.md)

2) **************************************************Choosing a research topic (input pattern’s circuits to study)**************************************************

[Initial Exploration and Brainstorm](Project%20Planning%20821fd0c71f4d4a44b5f7b240725c5547/Initial%20Exploration%20and%20Brainstorm%2006eb3b02c5684ef88cb6f64881f8a44f.md)

3) **Conduct Experiments on Research Topic**

- Now that we know some expms that can be run based on existing technqiues, begin [Outline Writeup Draft](Outline%20Writeup%20Draft%2096f5c9785c684e359a76ecb09d264875.md) : list secs, figs, tables based on expms to run
    - Use this to guide what to do next
- Run prelim expms for size comparison: logits lens, actv patching, atten heads, dot product semantic similarity . See: [PLAN- Size Comparison Circuits and Neurons](PLAN-%20Size%20Comparison%20Circuits%20and%20Neurons%201111d95ef57b4131b259ef88363f3010.md)
- See that similar inputs for size comparison (John is tall. Mary is [short]) also work for the more general case of antonyms, so run same prelim expms for antonyms. See: [Antonym Circuits and Neurons ](Antonym%20Circuits%20and%20Neurons%20824f0d162ce84a8fb09c27f4e4931194.md)

### Future Work Ideas / Postponed

- Attn head output vs token logit plot
- Move info into more fitting pages from [Antonym Circuits and Neurons ](Antonym%20Circuits%20and%20Neurons%20824f0d162ce84a8fb09c27f4e4931194.md), [PLAN- Size Comparison Circuits and Neurons](PLAN-%20Size%20Comparison%20Circuits%20and%20Neurons%201111d95ef57b4131b259ef88363f3010.md) and [Most Recent S Name Movers](Most%20Recent%20S%20Name%20Movers%20a72ccc6fdccc4e4baa78251399fdd2d7.md)
    - “Find Antonym” and “Size Comparison” both discuss copy circuits, but it wasn’t modified until “most_recent_S_name movers”. Move their content about copy circuits into a “modify copy circuits page”, and record a rough guess of the order this content was found in “planning”
    - [Size Comparison Congruence](PLAN-%20Size%20Comparison%20Circuits%20and%20Neurons%201111d95ef57b4131b259ef88363f3010/Size%20Comparison%20Congruence%20e94368b6a22a4e9e9d0d444b3c5972e5.md) : review
    - Create new nb to separate adj identification from most recent name movers
- In order to identify what’s a subject, the attention head weights may be “aligned” geometrically (in similar, closer to parallel than orthogonal, direction) to some “space” of subjects. What linear combination of neurons/features spans to make up this space?
- More in-depth literature review
- Figure out how updated ACDC takes in custom datasets
- Write program (by chatgpt) to generate prompts of a certain pattern
- Patch the layers that show sharp curve changes in layer analysis (both accumulate and sep by attn and MLP). Patch the heads that have big values in head analysis.
- Try many prompts about mammals to see which heads are active
- “is” seems to be a factual association, but it’s also a relation, so are attention heads involved? Also, “opposites” is an association but it’s a TYPE of association; how does the model differ it from other types of association like “is”?

---

**Techniques to Try**