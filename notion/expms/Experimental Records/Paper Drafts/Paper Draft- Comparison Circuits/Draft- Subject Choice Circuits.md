# Draft- Subject Choice Circuits

- Inspiration from how previous works were written
    
    From IOI paper, name mover heads section 3.1:
    
    - average attention probability of all heads over pIOI
    - activation patching on which heads cause large change in logit diffs?
    - higher attention probability on the IO or S token is correlated with higher output in the direction of the name (correlation  > 0:81, N = 500)
    - copy scores compared to average head

- **Outline:**
    1. Compare Input Prompts
        1. What types of cases are most recent subj? What proportion of in those types?
            1. Automate running many inputs and record their top output. Categorize which subject it is, or if not a subject. Try to find a pattern.
    2. Finding Important Heads for Most Recent Name Movers
    3. Figuring out Head Functionality for Most Recent Name Movers
    
    ???: MLPs for subjects
    
    if we patch in neuron 4413, it restores “more” correctly (by 0.08) “Mary is short” from corrupted “Mary is tall” compared to patching other neurons
    

Be very selective with information. Don’t aim for a long report; it’s not yet a paper, just a stepping stone to explore routes to one. Just copy *a few sentences* from the draft.

---

1. Compare Input Prompts

[test_prompt_most_recent_S.ipynb](../../Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/test_prompt_most_recent_S%20ipynb%20a51ecffd653d4d6c995692f0920be200.md) 

Due to several tests, there is good evidence to support the [following](../../Questions%20Hypotheses%2087e989748e1942dfa05a7d90433f2e40.md):

- HYPOTHESIS: If the “to-output” pattern is given in the source, in many cases, the high output probability “latest subject” will be outputted compared to the 2nd place output.
- HYPOTHESIS: However, [this statement](../../Questions%20Hypotheses%2087e989748e1942dfa05a7d90433f2e40.md) holds true for fewer subjects; as the number of subjects increases, it is less likely that the “latest subject” will be outputted.

Thus, we will only stick with inputs with 2 or 3 subjects in either source or target. For the sake of preserving length consistent between inputs, we will use 2 subjects in each, and only use single tokens for subject and description.

[Due to the lack of complexity in these tests, most will not be included in the report or its appendix, but links to them will be provided]

---

[2. Finding Important Heads for Most Recent Name Movers](Draft-%20Subject%20Choice%20Circuits%20293b34dee6104b619beee9b28e7392a7/2%20Finding%20Important%20Heads%20for%20Most%20Recent%20Name%20Mov%2045d975630e61406bb3c6b999ff1e7b9b.md)

---

[3. Figuring out Head Functionality for Most Recent Name Movers](Draft-%20Subject%20Choice%20Circuits%20293b34dee6104b619beee9b28e7392a7/3%20Figuring%20out%20Head%20Functionality%20for%20Most%20Recent%20%20d35d8e08cfc649d7838236eb03e6bf22.md)