# Study existing implementations of  fine-tuning

### Working on

### Done

- V 1. Figure out where fine-tuning is written in the ROME code
    
    [https://github.com/kmeng01/rome/blob/0874014cd9837e4365f3e6f3c71400ef11509e04/notebooks/rome.ipynb](https://github.com/kmeng01/rome/blob/0874014cd9837e4365f3e6f3c71400ef11509e04/notebooks/rome.ipynb)
    
    demo_model_editing(..., alg_name=ALG_NAME)
    
    ALG_NAME can be specified to be FT (fine-tuning)
    
    [https://github.com/kmeng01/rome/blob/0874014cd9837e4365f3e6f3c71400ef11509e04/experiments/py/demo.py](https://github.com/kmeng01/rome/blob/0874014cd9837e4365f3e6f3c71400ef11509e04/experiments/py/demo.py)
    
    load_alg(ALG_NAME)
    
    [https://github.com/kmeng01/rome/blob/0874014cd9837e4365f3e6f3c71400ef11509e04/experiments/py/demo.py#L77](https://github.com/kmeng01/rome/blob/0874014cd9837e4365f3e6f3c71400ef11509e04/experiments/py/demo.py#L77)
    
    elif "FT" in alg_name: … "FT": (FTHyperParams, apply_ft_to_model, "FT", "_unconstr"),
    
    [https://github.com/kmeng01/rome/blob/0874014cd9837e4365f3e6f3c71400ef11509e04/baselines/ft/ft_main.py#L12](https://github.com/kmeng01/rome/blob/0874014cd9837e4365f3e6f3c71400ef11509e04/baselines/ft/ft_main.py#L12)
    
    def apply_ft_to_model() —> def execute_ft()
    

[V 2. Decipher execute_ft()](Study%20existing%20implementations%20of%20fine-tuning%20a696395c83c24b7daa804db20dd9f50b/V%202%20Decipher%20execute_ft()%20fd737db6450149bb8b2ae2238e57adf9.md)

The fine tuning updates the loss using only the examples of (input seq, target seq) passed in.

[Modifying Memories in Transformer Models](https://www.notion.so/Modifying-Memories-in-Transformer-Models-aca25361c9e14f2788b6649f1ada82c8?pvs=21) (Zhu, et al) is used in execute_ft() by specifiying `type(hparams.norm_constraint) is float`. It modifies the weights to be within a user-specified hyperparameter range after each epoch’s loss update.

### Future Work

N/A