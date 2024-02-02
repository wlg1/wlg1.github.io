# Project Planning

- Compare the inputs of Function Vector’s ICL prompts vs Machiavelli Benchmark prompts.
    
    [https://arena3-chapter1-transformer-interp.streamlit.app/[1.5]_Function_Vectors_&_Model_Steering](https://arena3-chapter1-transformer-interp.streamlit.app/%5B1.5%5D_Function_Vectors_&_Model_Steering)
    
    [https://colab.research.google.com/drive/1yuPIBfz2MO2bHLuIkJETCemJU8TRKZLT#scrollTo=2724827c](https://colab.research.google.com/drive/1yuPIBfz2MO2bHLuIkJETCemJU8TRKZLT#scrollTo=2724827c)
    
    - How are function vectors extracted?
        
        You need a “good” set of prompts eg) antonym pair prompts would beget antonym FV. For Machiavelli, this would be “ethical” prompts.
        
    - How similar are they?
    - Can function vectors be extracted from a forward pass of machiavelli prompts?
        
        The ethical prompts would have in-context examples of ethical decisions. They have an observation with actions. So ethical prompts just have the ethical action.
        
- Literature review on machiavelli to avoid repeating work:
    
    [https://scholar.google.com/scholar?cites=4697205417656837392&as_sdt=5,31&sciodt=0,31&hl=en](https://scholar.google.com/scholar?cites=4697205417656837392&as_sdt=5,31&sciodt=0,31&hl=en)
    
- [model_edit_deception_draft.ipynb](https://colab.research.google.com/drive/1AgTC7ebuZGVJTdh5b4FG9Yu-M0RxdKB0)