# multi_arxiv_to_pinecone.py

ISSUE: 

```python
query = "What is LORA and what is CLIP?"
get_answer(query)
```

It does recognize LORA and CLIP, but k=2 doesn't allow it to retrieve LORA. 

> 'The text provided does not contain information about LORA. However, CLIP (Contrastive Language-Image Pre-Training)…
> 

[FULL CODE](multi_arxiv_to_pinecone%20py%2056d8f90e10a84b60b98abe3b17db1536/FULL%20CODE%208d0c981007a64750adc07b0c17f9d8ca.md) 

TEST:

Try to expand the k. Try k=20

However, if k is too large: openai.error.InvalidRequestError: This model's maximum context length is 4097 tokens. However, your messages resulted in 4494 tokens. Please reduce the length of the messages.

k=10 also doesn't work though.

- TEST:
Find what embeddings are retrieved upon query
    
    ```python
    similar_docs = index.similarity_search(query, k=2)
    ```
    
    ```python
    (Pdb) similar_docs[0]
    Document(page_content='Webly-Supervised Visual Concept Learning (Divvala et al.,\n2014) has a notably similar ambition and goal as CLIP.\nFinally, CLIP is related to a recent burst of activity on learn-\ning joint models of vision and language (Lu et al., 2019; Tan', metadata={'page': 25.0, 'source': 'D:\\Documents\\_prog\\prog_cust\\pinecone\\content\\downloaded_arxiv_paper.pdf'})
    (Pdb) similar_docs[0][page_content]
    *** NameError: name 'page_content' is not defined
    (Pdb) similar_docs[0][0]
    *** TypeError: 'Document' object is not subscriptable
    (Pdb) similar_docs[0].page_content
    'Webly-Supervised Visual Concept Learning (Divvala et al.,\n2014) has a notably similar ambition and goal as CLIP.\nFinally, CLIP is related to a recent burst of activity on learn-\ning joint models of vision and language (Lu et al., 2019; Tan'
    ```
    
    ```python
    similar_docs = index.similarity_search(query, k=2)
    for result in similar_docs:
        print(result.page_content)
    ```
    
    ```python
    (Pdb) similar_docs[0].page_content
    'Webly-Supervised Visual Concept Learning (Divvala et al.,\n2014) has a notably similar ambition and goal as CLIP.\nFinally, CLIP is related to a recent burst of activity on learn-\ning joint models of vision and language (Lu et al., 2019; Tan'
    (Pdb) similar_docs[1].page_content
    'Webly-Supervised Visual Concept Learning (Divvala et al.,\n2014) has a notably similar ambition and goal as CLIP.\nFinally, CLIP is related to a recent burst of activity on learn-\ning joint models of vision and language (Lu et al., 2019; Tan'
    ```
    
    Notice that both retrieved docs have the same page content. This means The same embeddings from the pdf were uploaded to pinecone twice, and did not replace it. 
    
    - What if you upload two embeddings that have the same text content to pinecone? Will pinecone update the old embedding or create a new embedding?
        
        When you upload two embeddings to Pinecone that have the same text content but different IDs, Pinecone will treat them as separate embeddings and store both of them. Pinecone does not analyze the content of the embeddings to check for duplicates; it only checks the IDs associated with the embeddings.
        
        If you upload two embeddings with the same text content and the same ID, Pinecone will perform an upsert operation. It will update the existing embedding with the new one, essentially overwriting the previous embedding.
        
        [https://www.notion.so/Pinecone-82538f51be5244d0b996ab99211b9f71?pvs=4#3d8cb396588e47d7a3cb6c34f548cc44](https://www.notion.so/Pinecone-82538f51be5244d0b996ab99211b9f71)
        

SOLN: The same content was uploaded to the index as different embeddings, so it was retrieved multiple times. 

TEST: Try to fix by [deleting all vectors](https://www.notion.so/Pinecone-82538f51be5244d0b996ab99211b9f71) . This is most efficient by just deleting the entire index.

---

ISSUE: After trying on new index, still had duplicates

SOLN: it downloaded CLIP again because the old CLIP pdf had a different file name. so just delete the old files and try again with another new index.

---

ISSUE: It retrieves different results now. However, for:

```python
query = "What is LORA and what is CLIP?"
```

It still gets both results are from CLIP, for k=2.

### Future Work

- Try different top-k-retrieval values
- Use a vector DB that’s less costly than pinecone
- Test on huggingface api first to prevent openai costs