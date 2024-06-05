# List Tasks

- Redo all circuits . List Tasks: (corr by rand replacement)
    1. incr digits
        1. ✅ nodes
            1. more data: [moreData_numseq_mincirc_randAll](https://colab.research.google.com/drive/1mFWmGAKtigFcqqWWMCwU7wWQY2HT5ZOo#scrollTo=LrUsg4sdhyfu).ipynb
            2. use diff incorr token than ‘i’
        2. ✅ edges
        3. OV scores
        4. Attn pats
    2. incr digits among words
    3. incr numwords
        1. ✅ nodes: [numWords_pruneNodes_randAll](https://colab.research.google.com/drive/1QTv-4osLHadCAay0beew-xlXszPCG88s#scrollTo=Lk3bffnCYq-p).ipynb
            1. use larger dataset
                - fails on hypenated even if give prefix first
        2. edges
        3. decr: decr_numseq_mincirc_iter.ipynb
            1. it can’t do it on small
    4. incr months
        1. ✅ nodes: [months_mincirc_randAll](https://colab.research.google.com/drive/1lhQqlizYGMC11vzp6I9mJ3dyxIr8tV3l#scrollTo=VaxbugcfGlBA)
            1. 4.4 seems very impt, more than 9.1
        2. ✅ edges: [months_IPP_randAll](https://colab.research.google.com/drive/1Y4aWml4Y7PxcZtLwVt9FxIhr-MYmhoGX#scrollTo=9CApvkRLon1T).ipynb
    5. greater-than
        1. ✅ nodes
        2. ✅ edges
    6. decr digits (and variations of 1a to 3)
        1.  nodes
            1. ✅ [Impt Decr Circ Heads](../Expm%20Results-%20NAACL%208de8fe5b943641ec92c4496843189d36/Impt%20Decr%20Circ%20Heads%20109317c38d2d4bf2ba1c721d44e17d1a.md) 
            2. get top heads from actv patch (explr demo)
            3. try with 4 input tokens
        2. edges
    7. 123 medium
        
        [add1_med_autoAblate_randAll.ipynb](https://colab.research.google.com/drive/1chZ6_lfm1o6TYkuzW292dH_uMRKh4_S0#scrollTo=BU78LW-8zn5l)
        
        [numseq_nextScores_medium.ipynb](https://colab.research.google.com/drive/1FAeWI25abCXpL6DQzXwR1mqSwmlEfqpM#scrollTo=tVDqHi-jihTh)
        
    8. 2 4 6 on medium
        1. [actually it fails at a certain point](https://colab.research.google.com/drive/1rNRrvr4qzy_zjPUK-4mJHruwFKnomrnP#scrollTo=Vy1PqimVNF89&line=1&uniqifier=1)
    9. plus one induction
        1. [✅ doesn’t work on small](https://colab.research.google.com/drive/1rNRrvr4qzy_zjPUK-4mJHruwFKnomrnP#scrollTo=RQd5WeT7ET7G&line=1&uniqifier=1)
    
    <<After nov 1st: (only mention in paper appendix before nov1)
    
    1. alphabet
    2. less-than
        1. [also fails on medium](https://colab.research.google.com/drive/1rNRrvr4qzy_zjPUK-4mJHruwFKnomrnP#scrollTo=lUXPMhHeIoGf&line=1&uniqifier=1)
    3. repeat digits VS repeat letters / words
    4. 2 4 6 vs 2 4 8 in larger models
    5. corr: 1234 vs 1233. 1233 has a circuit too for ‘repeat’