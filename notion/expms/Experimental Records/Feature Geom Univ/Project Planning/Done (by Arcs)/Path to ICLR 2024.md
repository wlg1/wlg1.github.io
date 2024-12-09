# Path to ICLR 2024

Clean up results and plot

- [✅ Figure 1](https://docs.google.com/presentation/d/1_EDEX2hRukivhU8FR45fQ2Bfcv0X-QnVMGy1x8bl37o/edit#slide=id.g3066aaa084b_1_171)
- ✅ finish full space expms (barplots, tables & heatmaps- put most in appdx)
    - ✅ keep only heatmap in main; move barplot and table to appendix. only show 1 barplot
        - you don’t need mean val or pval when you can just describe them?
    - ✅ svcca and rsa heatmap on one line ; place 2 plots on one line to compare
    - ✅ heatmaps on rand mean + pval
    - ✅ heatmap on mean actv corr VS mean corr after filt VS corr after 1-1
    - ✅ (LvL) tables of:num kept after kw, num kept after 1-1
    - ✅ pythia and gemma: re-run 1-1 with more null runs (just L6 v L18, 22 for gemma1)
    - ✅ plot corr and numfeats for gemma
    - ✅ appendix: compare filter junk + same kw + low corr VS 1-1
        - ✅ 1-1 in main ; before 1-1 in appendix
        - ✅ many-1 gemma heatmps
        - ✅ show many-1 with 1-1 sdie by side
        - ✅ many-1 captions, writeup
        - OPTIONAL: 1) filter junk, 2) same keyword, 3) 1-1 (or 1000-1), 4) low corr
- ✅ finish subspace expms for (barplots, tables & heatmaps- put most in appdx)
    - ✅ run without 1-1
        - [**Gemma2: L14, many-to-1**](https://colab.research.google.com/drive/1wHyHJMGPmRvRrPPm6F3xOqRLVOi9h_Lc#scrollTo=8WjLJup1LWMq&line=1&uniqifier=1)
        - does bad
    - ✅ run without junk words
        - similar to many-1
    - rerun for pythia multi-layers for more categories
        - match_semantic_spaces_v7
        - one more concept group: bio
    - ✅ run for gemma multi-layers for 1-1
        - loop_semantic_spaces_gemma
            - when running this check, skip random runs in new nb copy
    - ✅ conceptSp_pythia_heatmap: same heatmap for each concept group in appendix
        - paired and pvals
    - ✅ select a few groups for pythia and gemma to show in table (one line)

Writing  (main)

- ✅ [https://www.jakobfoerster.com/how-to-ml-paper](https://www.jakobfoerster.com/how-to-ml-paper)
- 🐣 ****[Make new figure 2 in slides](https://docs.google.com/presentation/d/12GSYdiGh-2kFZoHHU6q5HDQgIYJalVu2bvMuVWhtLuk/edit#slide=id.g3060122938d_0_86)
- ✅ the periods might be capturing DIFFERENT information, bc they store next token info, and so the matches on periods might not be semantically meaningful?
- ✅ say what experiments in line 49
    - mention all the preprocessing
- [✅ concept categories in appendix](https://chatgpt.com/c/66f99ff6-0834-800c-bf4d-96be06965ab6)
- ✅ improve figure 2 (ask austin)
- ✅ split background (must be relevant and must know to understand) and related works
- ✅ say should look at relative bc depends on the number of samples, etc.
    - saying ‘baseline score’ is enough
- ✅ pdf figures
- ✅ write intro to discuss sae limitations- why need universality?
    - why steering vectors?
    - which are “more meaningful” and universal?

Clean up code

- ✅ clean up code: 4 notebooks
    - full space
        - double loop
    - semantic space
        - no tables?

Writing (extra)

- ✅ [**Reproducibility Statement**](https://iclr.cc/Conferences/2025/AuthorGuide)
- ✅ limitations and future work
- ✅ Number of times each actv out of total features times 5
    - For just one layer pair per pythia + gemma
    - [https://colab.research.google.com/drive/1M4Ak-vnk-O5rrIh5MoqpuII-_VA3Ag6N#scrollTo=B4EuU-QOcjOG](https://colab.research.google.com/drive/1M4Ak-vnk-O5rrIh5MoqpuII-_VA3Ag6N#scrollTo=B4EuU-QOcjOG)
    - filter out those overrepresented (over 1)
- ✅ hand in final version

Arxiv vers

- ✅ Unrelated keywords
- ✅ Corr from full subsets

Invoice

- ✅ [Submit invoice (see drive, oxford files)](https://drive.google.com/drive/u/0/folders/1jAmsQxkUT9LGYH-p9f3ZFoEBcHYZTVuu)
    
    [https://forum.effectivealtruism.org/posts/M8m2PQSgJrB9fyjxY/beri-is-hiring-my-experience-as-deputy-director-and-why-you](https://forum.effectivealtruism.org/posts/M8m2PQSgJrB9fyjxY/beri-is-hiring-my-experience-as-deputy-director-and-why-you?utm_source=EA+Forum+Digest&utm_campaign=1cf28144a0-EMAIL_CAMPAIGN_2024_10_23_04_04&utm_medium=email&utm_term=0_-1cf28144a0-%5BLIST_EMAIL_ID%5D)
    

---

- timelines
    - old timeline (last month before ICLR)
        
        just run the same main steps on different domains (not uncertain to solve; just run):
        
        if not good results, just don’t include it
        
        - ✅ 9/1 - 9/7: start full space pval, solve 1-1 issues of full space, finish writeup outline
        - ✅ 9/7-9/10: finish writing full space (but not run all expms)
        - 9/10-9/19: force 1-1 and semantic subspace expms
        - 9/20-9/21: start 1L toy models + non-colab gpu training (re-run ts and pythia)
            - continue this throughout
        - 9/22: start feature splitting
            - are SAEs more or less similar as they get wider? (try 3 lvls on tinystories)
            - just run same things on saes of diff sizes
            - ISSUE: we don’t have access to feature split saes
        
        now this is new:
        
        - 9/23 - 9/28: writeup and functional
        - 9/29 - 9/30: ground truth expms
        - 9/30-10/1: finish writing
            - OPTIONAL: more 1-1 using algo
    - new timeline
        - ✅ 9/23 - 9/30: finish full + subspace expms (plots, heatmap, appdx)
        - 9/30: clean up code to put in zip
        - 10/1: finish figures, finish code, finish writing
            - OPTIONAL: pythia (+gemma) SAE MLPs vs LLMs MLPs