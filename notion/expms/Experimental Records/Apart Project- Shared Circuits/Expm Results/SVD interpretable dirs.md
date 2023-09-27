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
    

Keywords include: digits

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

<<<

[https://chat.openai.com/c/27f00510-099f-4cd6-9095-d2fa143ce90e](https://chat.openai.com/c/27f00510-099f-4cd6-9095-d2fa143ce90e)

Keywords include: digits

In the following file, for every (layer, singular vector), if “no shared semantic meaning” is not in the ‘response’,

If at least 30% of the words in the input after the question 'Are at least 30% of these words Keywords ?' are Keywords, answer with: "Yes". Then state which words you believe are Keywords. Else, answer with " No.".

as a test, do this for the first 10 entires

Keywords include: numerical digits such as 1, 2, 3, 4, etc.

In the following file, for every (layer, singular vector), if “no shared semantic meaning” is not in the ‘response’, 

If at least 30% of the words in the “test_str” are Keywords, answer with: "Yes". Then state which words you believe are Keywords. Else, answer with " No.".

as a test, do this for the first 10 entires

do this for all entries, only outputting results which are not "no" or "no shared semantic meaning”

change it to number words such as "one, two, hundred, ten", etc

---