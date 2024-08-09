# _Feature Geometry Expms Summary

Expms Summary

1. ✅ plot pretrained sae features on pca OR umap
2. ✅ plot feature acts, and compare before vs after steering/ablating/patching

---

pipeline summary

1. train
2. save actvs for two models
3. map correlated features, umap viz, cca scores
4. interpret correlated features using dataset examples; get same tok score

1 saved in ‘sae training’, 2-4 saved in ‘sae cross model’ folders

---

### Expm Sagas

TS 1L vs 2L expms

- train_tiny-stories-1M_sae.ipynb (renamed from train_gpt2_tinsto_sae_v2.ipynb)
- train_ts_sae_1L-21M.ipynb
- tinystories_actv_corr_mat_v1.ipynb: compare top feature pairs AND for each feature, its top 3 counterparts, for `tiny-stories-1L-21M` and `tiny-stories-2L-33M_MLP0 and MLP1`
- tinystories_actv_save.ipynb: 1L vs 2L. just get for any 100 data samples
- tinystories_actv_corr_mat_v2.ipynb: for 100 samples with no BOS prepend, save these actvs and run again but use correlation not cosine sim
- [tinystories_actv_save_v2](https://colab.research.google.com/drive/1yB4-mBBpUIRwVCWCl9QoIPQbbAuTg4NT#scrollTo=GFApm9B6afEP&line=1&uniqifier=1).ipynb: 1L vs 2L. get samples for a concept both models should represent (eg. pronouns, fire, etc) and see what features both fire on.
- [tinystories_actv_corr_mat_v3](https://colab.research.google.com/drive/1F1-fHJJYNywejQg4EzO1_NCTdwoss13K).ipynb: get samples for a concept both models should represent (eg. pronouns, fire, etc) and see what features both fire on.
- [load_actvs_interpret_features](https://colab.research.google.com/drive/1qUNgjrK8l1JNbSde9PLT6tnm9vgwv-HL#scrollTo=NsN8cKw5mfuj).ipynb: after obtaining correlated features, load tinystories F actvs again and interpret with dataset examples
    - feature top_ind_from_B(1786) is “years”, while its analogues in A are “time, summer, morning, day, once” so not EXACT but similar.

TS 1L vs 2L Feature Splitting Expms

- training nbs
    - train_ts_sae_1L-21M_df-8192.ipynb
    - train_ts_sae_1L-21M_df-32768.ipynb
    - train_ts_sae_2L-33M_MLP0_df-8192.ipynb
    - train_ts_sae_2L-33M_MLP0_df-32768.ipynb
- save actv nbs
    - [save_wt_actvs_dsInterp.ipynb](https://colab.research.google.com/drive/1Bh10l4vTb_rrCUw-483RDGsWavigTcjl): this work for any model, just input it in. No need to separate for each model as we don’t care about keeping the analysis output in nb
- map correlated features
    - [ts_1L_2L_UMAP_df32768.ipynb](https://colab.research.google.com/drive/1dQPHGIpv0uHQt72rG-pMIB0b7z4nA0T_#scrollTo=-ZqeAFR6EEgs)
- combined UMAP
    - [fs_UMAP_v0.ipynb](https://colab.research.google.com/drive/1swzOhJPlBvZNQrZjBW6xZdYalAVkmZjh#scrollTo=HTJhjkZ1yVt4): relu, 30k epochs
    - [fs_UMAP_v1](https://colab.research.google.com/drive/1Ubxrtvycgo0NWr6svNQj93AKt2ZNT7ap).ipynb: topk 32, 100k epochs

Feature Relation Mapping Expms

- [ts_actv_save_1L_2L_featRelns.ipynb](https://colab.research.google.com/drive/1yxw5HJn2h9v4OpAkSdpHvKeAvR3CIpHE)
    - fActs_ts_1L_21M_featrelns_v1.pkl
- [ts_1L_2L_UMAP](https://colab.research.google.com/drive/1Cl7nohl7hyaKz17bHbrkDgkADf-0DPqZ#scrollTo=kUYRF57KNxrL).ipynb: side by side decoder weight umaps, corr actvs
- ts_actv_save_1L_2L_anySamps.ipynb: save actvs for 500 any samps (not concept specific)
    - batch_tokens_anySamps_v1
    - fActs_ts_1L_21M_anySamps_v1.pkl
- [ts_1L_2L_UMAP_v2](https://colab.research.google.com/drive/1M9Q5iDxnJl5SDI-n5CE4wnJrff-Wr293#scrollTo=CRcTQwEN0qia).ipynb: slowdown bc too many cells, so clean up in `ts_1L_2L_UMAP_v2.ipynb` to try more keyws
- [ts_1L_2L_UMAP_actvs](https://colab.research.google.com/drive/1b2vob-ZX8IRBWw-1XLPY1wTCCXYJfVpj#scrollTo=6CvQQSVdQvq5).ipynb

---

IF OOM: try to load just actvs, reshape (del orig), and save corrs BEFORE load weights  + labels. Then load just weights, labels, and corr in second run to get umap comparisons

- find related story features
    - get sentences just about: king-queen-princess ***and*** father-mother-daughter
    - get sentences just about: she-he-it
    - get sentences just about: princess-dragon-knight

---

Topological Data Analysis

- [mapper_example.ipynb](https://colab.research.google.com/drive/1qBX9sQ5iwlcX17lwrmiXl36Yzfg6hkNP#scrollTo=f_AY6TPyE3PC): orig data of tutorial
- [SAE_DW_mapper_explora.ipynb](https://colab.research.google.com/drive/1DFsPl7EFa0SDNjlopjKmtFTcV2PfvGmQ#scrollTo=NwyZqjVONo6H): for 16k, `ts-1L-21M_Wdec`
    - [SAE_DW_mapper_explora_v1.ipynb](https://colab.research.google.com/drive/1sbFaxO0tpWgGJIA4VZ0R8xL_Jzj-TjZL): all others
    - [mapper_pretrained_saelens_dw.ipynb](https://colab.research.google.com/drive/1Dj41zt3JLqxImeZub6w7XEI95Qj07KkS)

---

Synth Actvs

- [synthData_explora.ipynb](https://colab.research.google.com/drive/1lHOtRa8KHIZuqbetilKkZFypfHDnSz2M#scrollTo=PLIDVkYupqYY) : expms using luke’s code (few mods)
- [synthData_explora_v2.ipynb](https://colab.research.google.com/drive/1S9GlHc60Y_SD3EN4D27GBLSpGPPhrR-l#scrollTo=Tdr-XiFEGDgR) : compare drastic mods to luke’s code for synth data
    - [test_synthActvs.ipynb](https://colab.research.google.com/drive/16HzLfM-3OG_5AkPlkAz63fSltx85zRnB): clean up and send to Robert Huben to check
- [synthData_explora_v3](https://colab.research.google.com/drive/1g44mZQNDMx7RiUvvIeZkeSYmN1srD53U).ipynb: new saes
- V: cleaned up new code only (no luke’s code)