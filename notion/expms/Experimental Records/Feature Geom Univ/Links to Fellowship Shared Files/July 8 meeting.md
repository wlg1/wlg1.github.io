# July 8 meeting

ChatGPT plus subscription credentials — LOGIN USING GOOGLE:

- Email: [torrvision2023@gmail.com](mailto:torrvision2023@gmail.com)
- Password: Torrvision0623!

minseon:

cosine sim mean is 0, sd 0.03- dataset not good with cosine sim. sim of actv vectors in layer with normal vs bad dataset. if map distr to diff scale, mean still 0 would it still work? -0.03 to 0.03 is cosine sim. high dim dataset is 0.02 range usually, but not usable. reduce dims to make cosine sim better? 

something with law large nums may be soln

tingchne:

replicate access to llama is cheaper

luke:

hyperparameter sweep in new method (num saes, how regularizing, 100 saes at gpt2 scale)- issue with dataset management (many TBs), other than loss graph try viz cosine sim of decoder weights and ground truth features

alt methods- term to moduclate loss based on cosine sim of saes trained. implement top k saes but k value is shared across saes, so only k neurons active. sparsity and shared repr controlled by same term. cosine sim not best metric so better divergence metric might be better.

clement:

hallucination in 3 ways: clip encodes wrongly, projection (not well trained enough), llm processes

llm more params, more used to text tokens. often hallucinates spoon when seeing food. 

after mlp adapter are image tokens. image tokens high norms compared to text tokens so may not decode to meaningful in text vocab. but when logit legs (on LLM) unembeds into vocab, image tokens are meaningful. 

if ablate image token thats impt can LLM still predict img? 

notice “six” (for 5 apples) shows up in logit lens. this six comes from image tokens, so is hallucination from image? try ablating this.

belief hallucination vs encoding is wrong 

if image encodes as 5, then LLM says is 6. so LLM is hallucinating, not image. 

train sae on image tokens? see if can see featuer of ‘5’ or ‘6’. ‘6’ is very late in layers 27 (near 32). so where does six come from? saes decompose this. 

if fix hallucinations, which part to fix?

models CAN count but do it for the wrong reason- that’s hallucination. eg) counts num stickers of apples. eg) earth is ‘flat’ doesnt mean model beleives earth is flat but just says it based on your belief

hallucination: why is there fork on plate? (supposed to provide chain of thought reasoning)

but in vision literature defines hallucination differently. clarify in related work the diffs.

OCR jailbreaks this could apply to? 

vision model’s hallu term also called factuality: does the model get it correct?

[https://arxiv.org/html/2401.03205v1#:~:text=This type of hallucination refers,et al.%2C 2023](https://arxiv.org/html/2401.03205v1#:~:text=This%20type%20of%20hallucination%20refers,et%20al.%2C%202023))%20.

adv pertub: image traffic light classif wrong.