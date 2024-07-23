# Arabic script feature splitting

- [https://www.neuronpedia.org/gpt2-small/?sourceSet=res_fs768-jb&selectedLayers=[]&sortIndexes=[]&ignoreBos=true&q=arabic](https://www.neuronpedia.org/gpt2-small/?sourceSet=res_fs768-jb&selectedLayers=%5B%5D&sortIndexes=%5B%5D&ignoreBos=true&q=arabic%0A)
    
    The pull down menu has the SAE for each feature split
    
    - How to find arabic script? Just type in the search terms used in Towards?

- arabic unicode
    
    [https://chatgpt.com/c/edca4390-6dac-4578-9b13-1e59b7126e77](https://chatgpt.com/c/edca4390-6dac-4578-9b13-1e59b7126e77)
    
    [https://www.compart.com/en/unicode/U+062B](https://www.compart.com/en/unicode/U+062B)
    
    - 0xD8 0xAB is it the same as \xd8 \xab for utf-8, as one uses 0 and other uses \ in front, also diff capitlizations
- ask neuronpeia slack
[](https://www.neuronpedia.org/gpt2-small/?sourceSet=res_fs768-jb&selectedLayers=%5B%5D&sortIndexes=%5B%5D&ignoreBos=true&q=arabic%0A)
    
    Hi, I was looking for recs on how to use Neuronpedia to search for languages such as Arabic, and have a few questions:
    
    1) Should I just try a variety of examples such as ال or phrases such as **كيف حالك ?**
    
    2) Is there a way to search by explanation like “Arabic”, not just by dataset examples?
    
    3) The “towards mono” paper mentions characters like ث are tokenized into `\xd8` `\xab`. Would it make more sense to search for the script characters or their utf-8 encodings? (guessing the former since I see japanese characters in the dataset examples)
    
    4) I’ve been trying to find Arabic script features in GPT-2 small L8 SAEs (and its feature splitting variants). Would the model unlikely have Arabic (due to its training dataset); if so, has anyone found Arabic features in publically available models, or believe there could be? Haven’t found this in Gemma-2 either.training 
    
    Lastly, are there separate channels/chats for asking questions about the neuronpedia interface VS asking specific research questions that use neuronpedia?