# Expm Results- Llama 2

- Exploratory Tests (first steps of run model)
    - [Llama2_num_runModel_explrTests_v1.ipynb](https://colab.research.google.com/drive/143roK4-FGgqqxtoM1ohDRe95enEdcVW6#scrollTo=vKYgaZ9JjihZ)
        
        uses non-pure seqs. OOM
        
    - [Llama2_num_runModel_explrTests_v2.ipynb](https://colab.research.google.com/drive/1mx0zSN7X5u5SBHZR5MrMEVFS-fSD4s36)
        
        Try for only 1 sample to avoid inconsistent padding issues
        
    - [Llama2_num_runModel_explrTests_v3.ipynb](https://colab.research.google.com/drive/1w49rGrjH55D2pBwqtH_qS7kd10xzuT52#scrollTo=vKYgaZ9JjihZ)
        
        This deletes previous explora tests and cleans up code. Don’t hard code pos dict but make key for every tokenized token
        
    - [Llama2_num_runModel_explrTests_v4.ipynb](https://colab.research.google.com/drive/1W-w3CqxNKN08VUwJblLy6g1vvOeG7Lva)
        
        try fix tokenizer using slack suggestion
        
    - [Llama2_num_runModel_explrTests_v5.ipynb](https://colab.research.google.com/drive/11Nmwec2lwDDakMskq-ENo0HtjDXliOyx#scrollTo=vKYgaZ9JjihZ)
        
        run on  1…12 pure num samps. ISSUE: char lvl tokenizer breaks 12 into ‘1’ and ‘2’
        
    - [Llama2_num_runModel_explrTests_v6](https://colab.research.google.com/drive/1_X-FGghmCEAQzbKIagMOCuiVl7Ew_Rl4#scrollTo=DcZG9rm2IAiA)
        
        run on  1…9 pure num samps (5 total)
        

- [Llama2_numerals_amongItems_AttnPats.ipynb](https://colab.research.google.com/drive/1iiTVFV7bw-FQBmt22W_4sz6epni36BE3)
    
    run on  1…9 pure num samps (5 total)
    

[[Llama2_fibonacci.ipynb](https://colab.research.google.com/drive/1oFGRQxRdqcXb9NDP6Mp-3t6M3LouvWe-#scrollTo=vKYgaZ9JjihZ)](Expm%20Results-%20Llama%202%20bc7eb66db28f4bbda27403862beea6ec/Llama2_fibonacci%20ipynb%20b59d5b5e54564c2f86a90f04761c6dec.md)

---