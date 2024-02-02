# Project Planning

To do:

- ✅ Find link to code in paper: https://github.com/nrimsky/CAA
- ✅ Study activation_steering_interp.ipynb (full workflow) for idea of first step to do
    - Add vector is done using model, which is LLamaWrapper. [LlamaWrapper](Project%20Docs%20b831ce760ca248db9b8071691d76b7ee/LlamaWrapper%20261cf6a9e7b54ae580ddae995281ac3b.md)
- ✅ Load HF Llama (without using LLamaWrapper) using nnsight. [Loading llama2 in nnsight](Project%20Docs%20b831ce760ca248db9b8071691d76b7ee/Loading%20llama2%20in%20nnsight%2022f016e03ceb467995efb74a20864036.md)
    
    NOTE: If not able to load llama2, for now try generate CAA on gpt2 small
    
- ✅ Study `generate_vectors.py` from repo + paper Methods to make a pseudocode algo
    
    [generate_vectors.py](Project%20Docs%20b831ce760ca248db9b8071691d76b7ee/generate_vectors%20py%203e7523df7e2044f4a3dd145ff720d368.md) 
    
- ✅ Brainstorm Pseudocode: [PsC- Generating Steering Vectors](Project%20Docs%20b831ce760ca248db9b8071691d76b7ee/PsC-%20Generating%20Steering%20Vectors%208cfb1f9c9fe24d84baed58c9610d089b.md)
- ✅ Code Generating Steering Vectors in [steer_llama2_nnsight_ExplTests.ipynb](https://colab.research.google.com/drive/1CEFW2fIDhZZ08ZlpgnfEaeS2fvfMnZ0g)
    - ✅ explr tests on pieces of 1.5’s `calculate_h`
    - ✅ run on pos and neg prompts
    - ✅ Clean up and put in [steer_llama2_nnsight_draft.ipynb](https://colab.research.google.com/drive/172FZBqjhnFtkVlWYvHKuPUlWIdNlr9vV)
- ✅ Pseudocode steering vectors: [PsC- steering vectors](Project%20Docs%20b831ce760ca248db9b8071691d76b7ee/PsC-%20steering%20vectors%20444d5a9716234fe48231fba7d0d14de8.md)
- ✅ Code steering vectors
    - ✅ Start coding steering vectors in [steer_llama2_nnsight_draft.ipynb](https://colab.research.google.com/drive/172FZBqjhnFtkVlWYvHKuPUlWIdNlr9vV)
    - ✅ study `prompting_with_steering.py`
- ⚠️ replicate 4.1: find where multiple choice DS located and load
    - ✅ ask Julian in arena slack
        
        Hi, I coded some prelim functions for generating and steering vectors, and before I use them on my own custom datasets, I'm looking to test them out on the same datasets the paper used as a sanity check to see if I get similar results as the paper. I was looking at the repo ([https://github.com/nrimsky/CAA/tree/main](https://github.com/nrimsky/CAA/tree/main)) to find which datasets correspond to the expms, namely 4.1 (multiple choice questions). I saw the file preprocessed_data/test_dataset.json has multiple choice; is this similar to what's used in Figure 6? Thanks!
        
    - ✅ since 13B remote down, use 7B local. Use `model.model.config`
    - ✅ Generate function: return the .value, not the proxy object, which can't be added when steering
    - ✅ Neither the unsteered or steered are good responses that pick a choice, for 13B. Perhaps it needs an instruction to tell it to pick a choice?
        
        No; when tell it to pick A or B, still nonsense
        
    - ✅ https://github.com/facebookresearch/llama/issues/385
        
        Also, we’ve been using 13B, not 13-B chat, which is opt for dialogue. Try 7B-chat
        
        [steer_llama2_nnsight_draft_7bchat.ipynb](https://colab.research.google.com/drive/1c0FcOpM6ltSUoaTaqVtD_mhmjeeHOsZT)
        
        Takes a long time to generate vector. For 60 prompts, takes ~15mins on A100
        
        **Steer with Answer: at end-** Sometimes does answer A or B, but not consistently
        
- ⚠️ What position to add steering vector to
    
    Another thing I'm trying to figure out is where to add the steering vector. The last section of 1.5 says to add to the start of the prompt. Originally I was thinking to add to the second last position since that's the "answer chosen" (A or B; the last position is token ")" ), but that doesn't make sense for prompts without the answer, just question + choices. However I haven't gone to tackling this much yet as I'm still trying to make the unsteered model consistently choose A or B.
    
- ✅ The models may need sampling methods passed as keyword args to generate, that's why it's selecting nonsense a lot of times (perhaps temperature by default too high)
    
    But No change in results from before
    
- ✅ Too hard to see what’s diff from paper. Go back to paper’s repo and run their code to replicate paper results first: [Workflow of steering to plotting](Project%20Docs%20b831ce760ca248db9b8071691d76b7ee/Workflow%20of%20steering%20to%20plotting%2080e8afb20b7f48b696897cc1c4f6717e.md)
- ✅ Ensure the model isn’t just always picking “A” but is picking the right one- do this by making the “pos” not always be A, but sometimes be B. The pos should be at `answer_matching_behavior`, which is not always A
- ✅ steer_llama2_nnsight_draft_13b: Gen using generate_dataset.json
- ✅ add steer fn to LAST TOKEN- doesn’t make it better than adding to second last
- ✅ For test_dataset, record the number of prompts that complete it correctly vs incorrectly after steering.
- Actually, you can add to 2nd last pos of steering bc it’s adding to the generated output using `model.model.layers[layer].output[0][:, -2, :]`; it's not adding to the input

---

If have competing steering, what would it choose? Which voice would it listen to? Can it use chain of thought to reason by itself which to listen to?

one downside of nnsight is that bc it processes in batch, no loop over what prompt num it’s curr on. That’s why for batch proc there’s a tqdm progress bar