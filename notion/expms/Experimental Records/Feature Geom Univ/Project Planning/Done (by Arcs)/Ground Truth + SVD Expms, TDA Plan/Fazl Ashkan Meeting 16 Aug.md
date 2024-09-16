# Fazl Ashkan Meeting 16 Aug

[https://app.read.ai/analytics/meetings/01J5DNY11P58YXTFRCWHG3RR6N?utm_source=Share_CopyLink](https://app.read.ai/analytics/meetings/01J5DNY11P58YXTFRCWHG3RR6N?utm_source=Share_CopyLink)

- avoid: don’t sell as just looking at different similarity measures compare (not just numbers). the role of each one should be clearly written
- why svd vs saes? build expms that differentiate them
- case studies: anthropic, deepmind, openai found specific safety features. could we find corr between safety features?
- luke: found saes (using MR) that could find better safety features
- why sim is impt, use case study: use WMD benchmark have high lvl repr (knowledge of bio vs chem)- similar saes can better steer
- case study: show explicit example that doesnt require too much subjectiveness is error detector feature- the path that it activates across models? read towards monosem.
- byproduct of dataset? would diff models on diff datasets have features?
    - what is the result mainly dep on? are these robust enough and not enough eng glitch? still need to ts
- not byproduct of train: use diff sparsity, how recon is. Use pretrained SAEs.
    - gpt2 and pythia pretrained saes would be comparable.
    - [https://huggingface.co/EleutherAI/sae-pythia-410m-65k](https://huggingface.co/EleutherAI/sae-pythia-410m-65k)
- why not expect featuers are similar? model is doing compression. model would be doing same features. strong argument. main arg is sae features are determinisitc of how trained. answer: make sure generalize. must have some internal repr that corresponds to safety, error, hallucination, etc.

Use phrase lvl for comon actv, not token. Get mean actv for all tokens in phrase. So map multiple tokens ro each other

Each sample index is not a dataset paragraph nor a token from flattening all, but a small phrase. Make this phrase using breakdown of samples? But now we can map using these indices by taking mean of all tokens in one index . This is like sum.