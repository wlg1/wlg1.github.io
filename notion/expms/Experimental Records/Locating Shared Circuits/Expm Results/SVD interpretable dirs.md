# SVD interpretable dirs

See: [SVD- subjs and objs](../../Agency%20Hackathon%2005fccdfc9f064cd7acad0c68fa76603d/SVD-%20subjs%20and%20objs%20279d402ddd9d4a0a84f64fe1cca2f116.md) 

- Autolabeling Prompt template
    
    Keywords include: 
    
    In the following file, for every (layer, singular vector), if “no shared semantic meaning” is not in the ‘response’, 
    
    If at least 30% of the words in the input after the question 'Are at least 30% of these words Keywords ?' are Keywords, answer with: "Yes". Then state which words you believe are Keywords. Else, answer with " No.".
    
    Here are a few examples:
    
    Are at least 30% of these words Keywords?
    
    house door balloon wind red the going eating blue sky lamp shade food ape doctor
    
    Answer: No.
    
    Are at least 30% of these words Keywords?
    
    cat house dog door puppy wind human red puppies eating the going eating blue sky
    
    Answer: Yes.
    
    cat dog puppy human puppies
    
    Are at least 30% of these words Keywords?
    
    Emily Bob David John Eve Sophia house door balloon wind red the going eating blue
    
    Answer: Yes.
    
    Emily Bob David John Eve Sophia
    
    Are at least 30% of these words Keywords?
    
    [test prompt]
    
    Answer:
    
    as a test, do this for the first 10 entires
    

---

Hard to do with exploratory data analysis:

[https://chat.openai.com/c/66cf9a57-6845-4cef-91e2-9f16ed9d95bf](https://chat.openai.com/c/66cf9a57-6845-4cef-91e2-9f16ed9d95bf)

- prompt
    
    In the attached file, for each direction in a layer,, get the "test_string” as input to the following format below, and output all the directions and the layer it is in which have “Yes” in the output. Save all the output in a file that can be downloaded:
    
    Words that are seq include: numbers, months, and days of the week. Single letters that are not Roman numerals are not seq.If at least 30% of the words of the test_string before the question 'Are at least 30% of these words seq?' are seq, only answer with: "Yes\ and state which words you believe are seq:
    Else skip over this element.
    
    For instance, "direction_2": {"test_string": "OH, H, Mar, May, Mar, U, X, K, Man, V, 69, ux, 23, oh, 19” is in layer_0, and should have “Yes” in its output, as the seq words are “Mar, May, Mar, 69, 23, 19”.
    
    Here are a few examples:
    Are at least 30% of these words seq-related?
    test_string: house door balloon wind red the going eating blue sky lamp shade food ape doctor
    Answer: No.
    Are at least 30% of these words seq?
    test_string: cat one 4 door puppy four human red April eating the going eating blue Monday
    Answer: Yes.
    one 4 four April Monday
    Are at least 30% of these words seq?
    test_string: 2 100 million fourth 6 December house door balloon wind red the going eating blue
    Answer: Yes.
    2 100 million fourth 6 December
    

In small to large, in and out, not many dirs with numbers. Some have time, such as years. Try SVD trace on attention heads.

---

[https://colab.research.google.com/drive/1Dcllro-IEkwChaBm89BhjWmSdjmqIFTj#scrollTo=yUPc-Ehrn8um](https://colab.research.google.com/drive/1Dcllro-IEkwChaBm89BhjWmSdjmqIFTj#scrollTo=yUPc-Ehrn8um)

MLPs don’t seem to correspond to numbers. Check attention heads SVD on circuit heads vs others- which have numbers, which don’t? Is it common to have numbers; if not, these heads stand out against the mean.

[https://chat.openai.com/c/10aba7ff-49bb-407a-86d1-969335505321](https://chat.openai.com/c/10aba7ff-49bb-407a-86d1-969335505321)

OV_top_singular_vectors: Vs are top-k tokens for N singular vectors, so there are k*N tokens

compute the percentage of tokens in Vs that are numbers, out of all tokens

Run this over all heads, and get distribution

[ This failed to understand the code. Try using code upload: ]

[https://chat.openai.com/c/7f876f95-de64-48d3-942c-954de4cc069b](https://chat.openai.com/c/7f876f95-de64-48d3-942c-954de4cc069b)