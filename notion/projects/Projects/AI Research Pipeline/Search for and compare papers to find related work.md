# Search for and compare papers to find related work

### Working on:

---

[4. Find how ‘arxiv-bot code’ searches for pdfs](Search%20for%20and%20compare%20papers%20to%20find%20related%20work%209365978de00d4255adbdb31f96f82022/4%20Find%20how%20%E2%80%98arxiv-bot%20code%E2%80%99%20searches%20for%20pdfs%20519c75e8c3da41799f69e537974d0d3e.md)

### Done

---

1. put pdf from local into pinecone (as chatgpt embedding)
    
    test_pinecon_gpt.py
    
    index = Pinecone.from_documents(docs, embeddings, index_name)
    
2.  call gpt using langchain on pdfs from pinecone
    
    test_pinecon_gpt.py
    
3. retrieve pdfs from arxiv and put into pinecone. then compare by query.
    
    arxiv_to_pinecone.py
    
    [
    multi_arxiv_to_pinecone.py](Search%20for%20and%20compare%20papers%20to%20find%20related%20work%209365978de00d4255adbdb31f96f82022/multi_arxiv_to_pinecone%20py%2056d8f90e10a84b60b98abe3b17db1536.md)
    
    NOTE: still has areas to be improved upon later
    

### Future Work

---