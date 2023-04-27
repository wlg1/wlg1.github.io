# 4. Find how ‘arxiv-bot code’ searches for pdfs

[https://github.com/aurelio-labs/arxiv-bot](https://github.com/aurelio-labs/arxiv-bot)

### Main Takeaways

Our aim is to find the part of the code which searches for pdfs on the web and reads them.

bots.py is merely a conversational agent Arxiver that can retrieve the search, convert_pdf, store_pdf tools based on NLP. It contains custom tools that call the necessary functions

constructors.py actually contains some of these functions, such as `get_paper_id()` , which performs the search for pdfs. 

`get_paper_id()` replaces special characters such as “:”, then puts the natural language query through google to return the HTML code of the search results page as `res`

`res = session.get(f"https://www.google.com/search?q={search_term}&sclient=gws-wiz-serp")`

It then extracts from `res.text`the first ID, using `[0]`, that matches `paper_id_re` 

`paper_id = paper_id_re.findall(res.text)[0]`

- `paper_id_re = re.compile(r'https://arxiv.org/abs/(\d+\.\d+)')`
    
    The regular expression pattern is `r'<https://arxiv.org/abs/(\\d+\\.\\d+)'`. This pattern matches a string that starts with `"<https://arxiv.org/abs/>"`, followed by a decimal number with at least one digit before and after the decimal point.
    
    - Give an example of paper_id
        
        A paper ID that matches the regular expression `https://arxiv.org/abs/(\\d+\\.\\d+)` would have the format `https://arxiv.org/abs/YYMM.NNNNN`, where:
        
        - `YY` represents the two-digit year the paper was published
        - `MM` represents the two-digit month the paper was published
        - `NNNNN` represents the paper number assigned by arXiv
        
        For example, a valid paper ID that matches this regular expression could be:
        
        ```
        <https://arxiv.org/abs/2104.04582>
        
        ```
        
        This paper ID represents a paper published in April 2021 with the arXiv number 2104.04582.
        
- Explain`\d+\.\d+`
    
    The regular expression pattern `\d+\.\d+` matches any string that contains a decimal number with at least one digit before and after the decimal point. Here is an explanation of the individual components of the pattern:
    
    - **`\d+`** matches one or more consecutive digits. The **`+`** symbol indicates that there must be at least one digit, but there can be more.
    - `\.` matches a literal dot character. The backslash is used to escape the dot because the dot is a special character in regular expressions that matches any character except a newline.
    
    Putting it all together, `\d+\.\d+` matches any string that contains a decimal number with at least one digit before and after the decimal point. For example, this pattern would match strings like `"3.14"`, `"123.456"`, and `"0.1"`, but it would not match strings like `"foo"`, `"bar.123"`, or `"1."`.
    

This is also used in bots.py’s `AddArticleTool()`

`matches = paper_id_re.findall(query)`

`…`

`paper_id = get_paper_id(query)`

What code lacks for our requirements

One thing that this code doesn’t contain for our requirements is that it doesn’t find several relevant pdfs from the search results and compare them. As seen in the notebook examples, this code expects the user to input an exact paper name, instead of a more ambiguous description of papers the user wants to obtain. 

Thus, this code should be modified to go through paper IDs found in `paper_id_re.findall(res.text)` and compare the text within those pdfs. It does not need to store them (though this would save time for future cases). Instead, it reads* through each paper first (using summarizer for long papers) and extracts only what’s relevant in the user query to them.

* (or skims what’s relevant by first doing quick glance over paragraph for “relevancy” and summarizing or disregarding- it can make its own decision and reflect; test this on gpt site first) 

Another thing that is “weak” about google is that the ranking is not entirely based on semantic ranking. Pinecone only returns “snippets” (it seems?). So instead, we can have the AI actually read through each pdf, say 100 of them (test with lower number first), and rank them based on what it semantically understands about them, according to the query.

For example:

“Which papers contain a similar method to MEMIT?”

The ranking would not allow the user to go through hundreds of papers that don’t have “similar method” as a keyword, but the AI would now be able to determine what’s “similar”. It can also output the reason it believes it’s similar; if this reason is bad, the user disregards that result.

After splitting the pdf into chunks and tokenizing, the AI should not store the chunks in a vector DB, but actually read through them to understand and compare them. Then it should store its understanding of those chunks, along with some chunks, in a DB, to allow semantic querying when comparing pdfs (to save the time of re-reading pdfs).

look at other tutorials about reading pdfs to see if they have different solutions

Summary of what can be added:

- It should be modified to go through paper IDs found in `paper_id_re.findall(res.text)` and compare the text within those pdfs.
- Instead of returning snippets, we can have the AI actually read through each pdf, say 100 of them, and rank them based on what it semantically understands about them, according to the query.
- The AI should store its understanding of those chunks, along with some chunks, in a DB, to allow semantic querying when comparing pdfs (to save the time of re-reading pdfs).

### Other Notes

---

constructors.py

- retry_request_session()
    
    This is a Python function that returns a `requests.Session` object with a retry strategy. The `retries` parameter is optional and sets the number of times the request will be retried if it fails due to the specified status codes or if the connection times out. The default value for `retries` is 5.
    
    The retry strategy is defined using the `Retry` class from the `urllib3` library, which is passed to the `HTTPAdapter` class from the `requests` library. The `total` parameter of the `Retry` class specifies the maximum number of retries. The `backoff_factor` parameter determines the time delay between retry attempts, which increases exponentially with each retry. The `status_forcelist` parameter specifies a list of HTTP status codes that will trigger a retry.
    
    The function returns a `requests.Session` object that has been configured with the retry strategy. The `Session` object provides a convenient way to reuse connection pools and cookies across multiple requests to the same server. The `mount()` method is used to associate the retry strategy with the `https` protocol.
    
- get_paper_id():
    
    This is a Python function that searches Google for a paper ID based on a query and returns the ID if it is found. The `query` parameter is a string that represents the query used to search for the paper ID. The `handle_not_found` parameter is optional and specifies whether the function should return `None` if the paper ID is not found, or raise an exception. The default value is `True`.
    
    The function first creates a dictionary called `special_chars` that maps special characters to their encoded equivalents. The `maketrans()` method is then used to create a translation table from the `special_chars` dictionary. This table is used by the `translate()` method to replace special characters in the `query` parameter with their encoded equivalents.
    
    The `retry_request_session()` function is called to create a session with a retry strategy, which is then used to send a GET request to the Google search page with the `search_term` as a parameter. The search results are returned in the `res` variable.
    
    The function then attempts to extract the paper ID from the search results using a regular expression stored in the `paper_id_re` variable. If the paper ID is found, it is returned. If the `handle_not_found` parameter is `True` and no paper ID is found, `None` is returned. Otherwise, an exception is raised with a message that indicates the query for which no paper was found.
    

---

[https://www.youtube.com/watch?v=CeZroxbdLXY&list=PLIUOU7oqGTLjpy44hZWE62K3RG4RTvuWt&index=3&ab_channel=JamesBriggs](https://www.youtube.com/watch?v=CeZroxbdLXY&list=PLIUOU7oqGTLjpy44hZWE62K3RG4RTvuWt&index=3&ab_channel=JamesBriggs)
Chatting with ArXiv Research Papers — AI Assistant #3
manager/bots.py

bot = arxiv_bot.manager.bots.Arxiver()

_init_memory()

arxiv_db_tool()

- _search_arxiv_db()
    
    ```python
    arxiv_db_tool = langchain.agents.Tool(
                func=self._search_arxiv_db,
                description=self.search_description,
                name="Search ArXiv DB"
            )
    # append to tools list
    self.tools.append(arxiv_db_tool)
    ```
    

._add_article_to_db()

._search_arxiv_db()

<<<

._search_arxiv_db() :

- inputs
    
    ```python
    inputs = self.retriever.prep_inputs(inputs)
            self.retriever.callback_manager.on_chain_start(
                {"name": self.retriever.__class__.__name__},
                inputs,
                verbose=self.retriever.verbose,
            )
    ```
    
    In this code block, the `prep_inputs` method of the `retriever` object is called to preprocess and transform the input data into a format that can be used by the chain. This method applies any necessary transformations to the input data, such as converting it to a list or adding any required parameters, before passing it on to the chain.
    
    Next, the `on_chain_start` method of the `callback_manager` object is called to signal the start of the retrieval chain. The `callback_manager` object manages the chain's callbacks, which are functions that can be called at various points during the execution of the chain. In this case, the `on_chain_start` callback is called at the start of the chain.
    
    The `on_chain_start` method takes three arguments:
    
    - `{"name": self.retriever.__class__.__name__}`: A dictionary specifying the name of the chain.
    - `inputs`: The preprocessed input data.
    - `verbose=self.retriever.verbose`: A boolean value indicating whether or not to print verbose output during the execution of the chain.
    
    This method is typically used to perform any necessary setup or initialization before the chain is run, such as setting up a progress bar or initializing a data store.
    
    After the `on_chain_start` method is called, the chain is executed, and the output is returned. The `callback_manager` object also manages the chain's `on_chain_end` and `on_chain_error` callbacks, which are called at the end of the chain and if an error occurs during the chain's execution, respectively.
    
- on_chain_end
    
    ```python
    self.retriever.callback_manager.on_chain_end(outputs, verbose=self.retriever.verbose)
    ```
    
    In this code block, the `on_chain_end` method of the `callback_manager` object is called to signal the end of the retrieval chain. The `on_chain_end` callback is typically used to perform any necessary cleanup or post-processing after the chain has run, such as closing database connections or formatting the output.
    
    The `on_chain_end` method takes two arguments:
    
    - `outputs`: The dictionary of outputs returned by the chain.
    - `verbose=self.retriever.verbose`: A boolean value indicating whether or not to print verbose output during the execution of the chain.
    
    In this case, the `outputs` dictionary is passed to the `on_chain_end` method, along with the value of the `verbose` attribute of the `retriever` object.
    
    Once the `on_chain_end` method has completed, the outputs are returned to the calling function.
    

- What is the purpose of the retriever?
    
    The purpose of the `retriever` in the Arxiver code is to provide a way to search through a pre-built database of scientific research papers to find relevant information in response to a user's question. The `retriever` is an instance of the `RetrievalQAWithSourcesChain` class, which is a subclass of the `RetrievalQAChain` class.
    
    The `RetrievalQAChain` class is designed to be used for question-answering tasks, where a model is trained to take a natural language question as input and return a text answer. The `RetrievalQAWithSourcesChain` class adds functionality to the `RetrievalQAChain` class by returning not only the answer to the user's question, but also a list of sources that support that answer.
    
    In the Arxiver code, the `retriever` is initialized with a pre-trained language model, a vector database, and a retrieval function. The `retriever` is then used to search through the pre-built database to find relevant information in response to a user's question. Once the `retriever` has found relevant information, it returns the best answer to the user's question, along with a list of sources that support that answer.
    
    The `retriever` is an important part of the Arxiver code because it allows the bot to provide users with accurate and relevant information in response to their questions. By using a pre-built database of scientific research papers, the `retriever` ensures that the information it returns to the user is up-to-date and relevant to their query.
    

---

- How does a user use "tools" in Arxiver? Give a code example
    
    In Arxiver, "tools" are functions or classes that perform specific tasks and can be used by the chatbot to provide more specific responses to user queries. The `Arxiver` class has a list of `tools` that can be accessed by the chatbot.
    
    To use a tool in Arxiver, you can pass the name of the tool and its required arguments as input to the `__call__` method of the `Arxiver` class. Here's an example code snippet:
    
    ```
    from arxiv_bot.arxiver import Arxiver
    
    # initialize the Arxiver chatbot
    arxiver = Arxiver()
    
    # use the 'Search ArXiv DB' tool
    output = arxiver('search arxiv database for machine learning papers')
    print(output['output']) # print the output of the chatbot
    
    ```
    
    In this example, we initialized an instance of `Arxiver` and used the `__call__` method to pass a query string to the chatbot. The chatbot recognized that the user was requesting to use the `Search ArXiv DB` tool and returned a response to the query.
    

[https://python.langchain.com/en/latest/modules/agents/tools/getting_started.html](https://python.langchain.com/en/latest/modules/agents/tools/getting_started.html)

[https://www.youtube.com/watch?v=hI2BY7yl_Ac&t=57s&ab_channel=SamWitteveen](https://www.youtube.com/watch?v=hI2BY7yl_Ac&t=57s&ab_channel=SamWitteveen)