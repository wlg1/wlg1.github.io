# Most Recent S Name Movers

[most_recent_S_name_movers_DRAFT.ipynb](../Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/most_recent_S_name_movers_DRAFT%20ipynb%20ee6f1afdee0b4f369cf505ae00aaed4d.md) 

[https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU](https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU)

Path patching finds how attention heads move information from inputs to other heads. So these input types take a subject using in-context learning and outputs a subject. Based on IOI findings, we expect to find:

- Induction heads (b/c of in-context learning)
- Name mover heads
    - Find evidence for this using Copy Scores
- Subject influencing heads (here, seems to be most recent subject)

Can be done w/ just GPT-2-small

- Previous findings:
    
    [simple_analogies_circuits.ipynb](../Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/simple_analogies_circuits%20ipynb%20766fb391cad246da9150bcd5d98248a4.md) : Expm code nb
    
    (rename later)
    

---

- Rewrite copy scores to not use ioi_dataset
    
    ISSUE: IOIdataset only allows specific types of subjects; we want 4 subjects
    
    Given that the ioi_dataset class just stores things to be called by copy scores and path patching, you can not use that class and use your own class, as ioi_dataset has certain requirements
    
    First, find what's being called in copy scores, so they can be emulated in your new object
    
    - in check_copy_circuit(), list all the lines that use ioi_dataset:
        1. `model(ioi_dataset.toks.long())`
        2. `for seq_idx, prompt in enumerate(ioi_dataset.ioi_prompts):`
        3. `pred_tokens = [...] ioi_dataset.word_idx[word][seq_idx]], k).indices]`
        4. `ioi_dataset.N`
    
    - Provide chatGPT code for check_copy_circuit() and class IOIdataset: (did not work)
        - check_copy_circuit()
            
            ```python
            only reply 'yes'
            def check_copy_circuit(model, layer, head, ioi_dataset, verbose=False, neg=False):
                cache = {}
                model.cache_some(cache, lambda x: x == "blocks.0.hook_resid_post")
                model(ioi_dataset.toks.long())
                if neg:
                    sign = -1
                else:
                    sign = 1
                z_0 = model.blocks[1].attn.ln1(cache["blocks.0.hook_resid_post"])
            
                v = torch.einsum("eab,bc->eac", z_0, model.blocks[layer].attn.W_V[head])
                v += model.blocks[layer].attn.b_V[head].unsqueeze(0).unsqueeze(0)
            
                o = sign * torch.einsum("sph,hd->spd", v, model.blocks[layer].attn.W_O[head])
                logits = model.unembed(model.ln_final(o))
            
                k = 5
                n_right = 0
            
                for seq_idx, prompt in enumerate(ioi_dataset.ioi_prompts):
                    for word in ["IO", "S", "S2"]:
                        pred_tokens = [
                            model.tokenizer.decode(token)
                            for token in torch.topk(
                                logits[seq_idx, ioi_dataset.word_idx[word][seq_idx]], k
                            ).indices
                        ]
                        if "S" in word:
                            name = "S"
                        else:
                            name = word
                        if " " + prompt[name] in pred_tokens:
                            n_right += 1
                        else:
                            if verbose:
                                print("-------")
                                print("Seq: " + ioi_dataset.sentences[seq_idx])
                                print("Target: " + ioi_dataset.ioi_prompts[seq_idx][name])
                                print(
                                    " ".join(
                                        [
                                            f"({i+1}):{model.tokenizer.decode(token)}"
                                            for i, token in enumerate(
                                                torch.topk(
                                                    logits[
                                                        seq_idx, ioi_dataset.word_idx[word][seq_idx]
                                                    ],
                                                    k,
                                                ).indices
                                            )
                                        ]
                                    )
                                )
                percent_right = (n_right / (ioi_dataset.N * 3)) * 100
                print(
                    f"Copy circuit for head {layer}.{head} (sign={sign}) : Top {k} accuracy: {percent_right}%"
                )
                return percent_right
            
            neg_sign = False
            print(" --- Name Mover heads --- ")
            check_copy_circuit(model, 9, 9, ioi_dataset, neg=neg_sign)
            check_copy_circuit(model, 10, 0, ioi_dataset, neg=neg_sign)
            check_copy_circuit(model, 9, 6, ioi_dataset, neg=neg_sign)
            
            neg_sign = True
            print(" --- Negative heads --- ")
            check_copy_circuit(model, 10, 7, ioi_dataset, neg=neg_sign)
            check_copy_circuit(model, 11, 10, ioi_dataset, neg=neg_sign)
            
            neg_sign = False
            print(" ---  Random heads for control ---  ")
            check_copy_circuit(
                model, random.randint(0, 11), random.randint(0, 11), ioi_dataset, neg=neg_sign
            )
            check_copy_circuit(
                model, random.randint(0, 11), random.randint(0, 11), ioi_dataset, neg=neg_sign
            )
            check_copy_circuit(
                model, random.randint(0, 11), random.randint(0, 11), ioi_dataset, neg=neg_sign
            )
            ```
            
        - IOIdataset
            
            ```python
            only reply 'yes'
            class IOIDataset:
                def __init__(
                    self,
                    prompt_type: Union[
                        str, List[str]
                    ],  # if list, then it will be a list of templates
                    N=500,
                    tokenizer=None,
                    prompts=None,
                    symmetric=False,
                    prefixes=None,
                    nb_templates=None,
                    ioi_prompts_for_word_idxs=None,
                    prepend_bos=False,
                    manual_word_idx=None,
                ):
                    """
                    ioi_prompts_for_word_idxs:
                        if you want to use a different set of prompts to get the word indices, you can pass it here
                        (example use case: making a ABCA dataset)
                    """
            
                    if not (
                        N == 1
                        or prepend_bos == False
                        or tokenizer.bos_token_id == tokenizer.eos_token_id
                    ):
                        warnings.warn(
                            "Probably word_idx will be calculated incorrectly due to this formatting"
                        )
                    assert not (symmetric and prompt_type == "ABC")
                    assert (
                        (prompts is not None) or (not symmetric) or (N % 2 == 0)
                    ), f"{symmetric} {N}"
                    assert nb_templates is None or (nb_templates % 2 == 0 or prompt_type != "mixed")
                    self.prompt_type = prompt_type
            
                    if nb_templates is None:
                        nb_templates = len(BABA_TEMPLATES)
            
                    if prompt_type == "ABBA":
                        self.templates = ABBA_TEMPLATES[:nb_templates].copy()
                    elif prompt_type == "BABA":
                        self.templates = BABA_TEMPLATES[:nb_templates].copy()
                    elif prompt_type == "mixed":
                        self.templates = (
                            BABA_TEMPLATES[: nb_templates // 2].copy()
                            + ABBA_TEMPLATES[: nb_templates // 2].copy()
                        )
                        random.shuffle(self.templates)
                    elif prompt_type == "ABC":
                        self.templates = ABC_TEMPLATES[:nb_templates].copy()
                    elif prompt_type == "BAC":
                        self.templates = BAC_TEMPLATES[:nb_templates].copy()
                    elif prompt_type == "ABC mixed":
                        self.templates = (
                            ABC_TEMPLATES[: nb_templates // 2].copy()
                            + BAC_TEMPLATES[: nb_templates // 2].copy()
                        )
                        random.shuffle(self.templates)
                    elif isinstance(prompt_type, list):
                        self.templates = prompt_type
                    else:
                        raise ValueError(prompt_type)
            
                    if tokenizer is None:
                        self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
                        self.tokenizer.pad_token = self.tokenizer.eos_token
                    else:
                        self.tokenizer = tokenizer
            
                    self.prefixes = prefixes
                    self.prompt_type = prompt_type
                    if prompts is None:
                        self.ioi_prompts = gen_prompt_uniform(  # a list of dict of the form {"text": "Alice and Bob bla bla. Bob gave bla to Alice", "IO": "Alice", "S": "Bob"}
                            self.templates,
                            NAMES,
                            nouns_dict={"[PLACE]": PLACES, "[OBJECT]": OBJECTS},
                            N=N,
                            symmetric=symmetric,
                            prefixes=self.prefixes,
                            abc=(prompt_type in ["ABC", "ABC mixed", "BAC"]),
                        )
                    else:
                        assert N == len(prompts), f"{N} and {len(prompts)}"
                        self.ioi_prompts = prompts
            
                    all_ids = [prompt["TEMPLATE_IDX"] for prompt in self.ioi_prompts]
                    all_ids_ar = np.array(all_ids)
                    self.groups = []
                    for id in list(set(all_ids)):
                        self.groups.append(np.where(all_ids_ar == id)[0])
            
                    small_groups = []
                    for group in self.groups:
                        if len(group) < 5:
                            small_groups.append(len(group))
                    if len(small_groups) > 0:
                        warnings.warn(
                            f"Some groups have less than 5 prompts, they have lengths {small_groups}"
                        )
            
                    self.sentences = [
                        prompt["text"] for prompt in self.ioi_prompts
                    ]  # a list of strings. Renamed as this should NOT be forward passed
            
                    self.templates_by_prompt = []  # for each prompt if it's ABBA or BABA
                    for i in range(N):
                        if self.sentences[i].index(self.ioi_prompts[i]["IO"]) < self.sentences[
                            i
                        ].index(self.ioi_prompts[i]["S"]):
                            self.templates_by_prompt.append("ABBA")
                        else:
                            self.templates_by_prompt.append("BABA")
            
                    # print(self.ioi_prompts, "that's that")
                    texts = [
                        (self.tokenizer.bos_token if prepend_bos else "") + prompt["text"]
                        for prompt in self.ioi_prompts
                    ]
                    self.toks = torch.Tensor(self.tokenizer(texts, padding=True).input_ids).type(
                        torch.int
                    )
            
                    if ioi_prompts_for_word_idxs is None:
                        ioi_prompts_for_word_idxs = self.ioi_prompts
                    self.word_idx = get_idx_dict(
                        ioi_prompts_for_word_idxs,
                        self.tokenizer,
                        prepend_bos=prepend_bos,
                        toks=self.toks,
                    )
                    self.prepend_bos = prepend_bos
                    if manual_word_idx is not None:
                        self.word_idx = manual_word_idx
            
                    self.sem_tok_idx = {
                        k: v for k, v in self.word_idx.items() if k in ALL_SEM
                    }  # the semantic indices that kevin uses
                    self.N = N
                    self.max_len = max(
                        [
                            len(self.tokenizer(prompt["text"]).input_ids)
                            for prompt in self.ioi_prompts
                        ]
                    )
            
                    self.io_tokenIDs = [
                        self.tokenizer.encode(" " + prompt["IO"])[0] for prompt in self.ioi_prompts
                    ]
                    self.s_tokenIDs = [
                        self.tokenizer.encode(" " + prompt["S"])[0] for prompt in self.ioi_prompts
                    ]
            
                    self.tokenized_prompts = []
            
                    for i in range(self.N):
                        self.tokenized_prompts.append(
                            "|".join([self.tokenizer.decode(tok) for tok in self.toks[i]])
                        )
            
                @classmethod
                def construct_from_ioi_prompts_metadata(cls, templates, ioi_prompts_data, **kwargs):
                    """
                    Given a list of dictionaries (ioi_prompts_data)
                    {
                        "S": "Bob",
                        "IO": "Alice",
                        "TEMPLATE_IDX": 0
                    }
            
                    create and IOIDataset from these
                    """
            
                    prompts = []
                    for metadata in ioi_prompts_data:
                        cur_template = templates[metadata["TEMPLATE_IDX"]]
                        prompts.append(metadata)
                        prompts[-1]["text"] = (
                            cur_template.replace("[A]", metadata["IO"])
                            .replace("[B]", metadata["S"])
                            .replace("[PLACE]", metadata["[PLACE]"])
                            .replace("[OBJECT]", metadata["[OBJECT]"])
                        )
                        # prompts[-1]["[PLACE]"] = metadata["[PLACE]"]
                        # prompts[-1]["[OBJECT]"] = metadata["[OBJECT]"]
                    return IOIDataset(prompt_type=templates, prompts=prompts, **kwargs)
            
                def gen_flipped_prompts(self, flip):
                    """
                    Return a IOIDataset where the name to flip has been replaced by a random name.
                    """
            
                    assert isinstance(flip, tuple) or flip in [
                        "prefix",
                    ], f"{flip} is not a tuple. Probably change to ('IO', 'RAND') or equivalent?"
            
                    if flip == "prefix":
                        flipped_prompts = flip_prefixes(self.ioi_prompts)
                    else:
                        if flip in [("IO", "S1"), ("S", "IO")]:
                            flipped_prompts = gen_flipped_prompts(
                                self.ioi_prompts,
                                None,
                                flip,
                            )
                        elif flip == ("S2", "IO"):
                            flipped_prompts = gen_flipped_prompts(
                                self.ioi_prompts,
                                None,
                                flip,
                            )
            
                        else:
                            assert flip[1] == "RAND" and flip[0] in [
                                "S",
                                "RAND",
                                "S2",
                                "IO",
                                "S1",
                                "S+1",
                            ], flip
                            flipped_prompts = gen_flipped_prompts(self.ioi_prompts, NAMES, flip)
            
                    flipped_ioi_dataset = IOIDataset(
                        prompt_type=self.prompt_type,
                        N=self.N,
                        tokenizer=self.tokenizer,
                        prompts=flipped_prompts,
                        prefixes=self.prefixes,
                        ioi_prompts_for_word_idxs=flipped_prompts if flip[0] == "RAND" else None,
                        prepend_bos=self.prepend_bos,
                        manual_word_idx=self.word_idx,
                    )
                    return flipped_ioi_dataset
            
                def copy(self):
                    copy_ioi_dataset = IOIDataset(
                        prompt_type=self.prompt_type,
                        N=self.N,
                        tokenizer=self.tokenizer,
                        prompts=self.ioi_prompts.copy(),
                        prefixes=self.prefixes.copy()
                        if self.prefixes is not None
                        else self.prefixes,
                        ioi_prompts_for_word_idxs=self.ioi_prompts.copy(),
                    )
                    return copy_ioi_dataset
            
                def __getitem__(self, key):
                    sliced_prompts = self.ioi_prompts[key]
                    sliced_dataset = IOIDataset(
                        prompt_type=self.prompt_type,
                        N=len(sliced_prompts),
                        tokenizer=self.tokenizer,
                        prompts=sliced_prompts,
                        prefixes=self.prefixes,
                        prepend_bos=self.prepend_bos,
                    )
                    return sliced_dataset
            
                def __setitem__(self, key, value):
                    raise NotImplementedError()
            
                def __delitem__(self, key):
                    raise NotImplementedError()
            
                def __len__(self):
                    return self.N
            
                def tokenized_prompts(self):
                    return self.toks
            ```
            
        - in check_copy_circuit(), list all the lines that use ioi_dataset:
            1. `model(ioi_dataset.toks.long())`
            2. `for seq_idx, prompt in enumerate(ioi_dataset.ioi_prompts):`
            3. `pred_tokens = [...] ioi_dataset.word_idx[word][seq_idx]], k).indices]`
            4. `ioi_dataset.N`
            
        - Which variables in ioi_dataset are used by check_copy_circuit()?
            
            In the `check_copy_circuit()` function, the following variables from the `ioi_dataset` object are used:
            
            1. `ioi_dataset.toks`: It is used to pass tokenized prompts to the model for inference.
            2. `ioi_dataset.ioi_prompts`: It is used to iterate over the prompts and extract relevant information such as the target words.
            3. `ioi_dataset.word_idx`: It is used to retrieve the indices of specific words in the logits tensor.
            4. `ioi_dataset.N`: It is used to calculate the percentage accuracy.
            
            These variables provide necessary data and information from the `ioi_dataset` object for the logic and computations within the `check_copy_circuit()` function.
            
        - Note that IOIdataset is used as the argument ioi_dataset in check_copy_circuit()
        - Write code which creates a class called Dataset that is similar to IOIdataset, but instead uses the template structure for a single sentence as templates = ["[A] is a teacher. [B] is a student. The child is [B]. [C] is a teacher. [D] is a student. The child is"], where the placeholders [A] denote names, and there are no variables for [place] and [object]. M
            
            Certainly! Here's an example code that creates a `Dataset` class similar to `IOIDataset` using the specified template structure:
            
            ```
            class Dataset:
                def __init__(self, N=500, tokenizer=None):
                    self.templates = ["[A] is a teacher. [B] is a student. The child is [B]. [C] is a teacher. [D] is a student. The child is"]
            
                    if tokenizer is None:
                        self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
                        self.tokenizer.pad_token = self.tokenizer.eos_token
                    else:
                        self.tokenizer = tokenizer
            
                    self.N = N
                    self.ioi_prompts = self.generate_prompts()
                    self.toks = self.tokenize_prompts()
            
                def generate_prompts(self):
                    prompts = []
                    for _ in range(self.N):
                        prompt = {
                            "text": self.templates[0],
                            "A": random.choice(NAMES),
                            "B": random.choice(NAMES),
                            "C": random.choice(NAMES),
                            "D": random.choice(NAMES)
                        }
                        prompts.append(prompt)
                    return prompts
            
                def tokenize_prompts(self):
                    texts = [
                        prompt["text"] for prompt in self.ioi_prompts
                    ]
                    return torch.Tensor(self.tokenizer(texts, padding=True).input_ids).type(torch.int)
            
            ```
            
            In this `Dataset` class, the `templates` attribute holds a list with a single template string. The placeholders [A], [B], [C], and [D] represent names, and there are no variables for [place] and [object].
            
            The `generate_prompts()` method creates a list of prompts by randomly selecting names from the `NAMES` list and filling them into the template.
            
            The `tokenize_prompts()` method tokenizes the generated prompts using the specified tokenizer.
            
            You can create an instance of the `Dataset` class and use it similar to `IOIDataset`:
            
            ```
            dataset = Dataset(N=500)
            
            ```
            
            Now you have a `Dataset` object with prompts generated based on the specified template structure. You can access the prompts, tokenized prompts, and other attributes as needed.
            
        - include the variable NAMES inside Dataset
        - AttributeError: 'Dataset' object has no attribute 'word_idx’
        
        - Write code that creates a simplified class called Dataset which does not use the IOIdataset class but creates its own class from scratch, and only contains the variables used by check_copy_circuit()
            
            ```python
            class Dataset:
                def __init__(self, sentences, ioi_prompts, word_idx, N):
                    self.sentences = sentences
                    self.ioi_prompts = ioi_prompts
                    self.word_idx = word_idx
                    self.N = N
            
                def to_tensor(self, tokenizer):
                    texts = [(prompt["text"]) for prompt in self.ioi_prompts]
                    toks = torch.Tensor(tokenizer(texts, padding=True).input_ids).type(torch.int)
                    return toks
            
            # Example usage
            sentences = ["Sentence 1", "Sentence 2", "Sentence 3"]
            ioi_prompts = [
                {"text": "Prompt 1", "IO": "Alice", "S": "Bob"},
                {"text": "Prompt 2", "IO": "Carol", "S": "Dave"},
                {"text": "Prompt 3", "IO": "Eve", "S": "Frank"},
            ]
            word_idx = {"Alice": [0, 1], "Bob": [2], "Carol": [0], "Dave": [1, 2], "Eve": [0, 1, 2], "Frank": [0, 2]}
            N = 3
            
            dataset = Dataset(sentences, ioi_prompts, word_idx, N)
            tokenizer = AutoTokenizer.from_pretrained("gpt2")
            
            toks = dataset.to_tensor(tokenizer)
            ```
            
        - Write code that creates a class called Dataset which does not use the IOIdataset class but creates its own class from scratch, and contains ALL the variables used by check_copy_circuit(). Make sure each variable created in the same way as they are in IOIdataset
        - For the code for class Dataset, have it instead take in templates instead of sentences similar to IOIdataset, where the templates contain placeholders which are filled in by a list of single token names similar to that in IOIdataset
            
            ```python
            class Dataset:
                def __init__(self, templates, names, ioi_prompts, word_idx, N):
                    self.templates = templates
                    self.names = names
                    self.ioi_prompts = ioi_prompts
                    self.word_idx = word_idx
                    self.N = N
            
                def generate_sentences(self):
                    sentences = []
                    for prompt in self.ioi_prompts:
                        text = self.templates[prompt["TEMPLATE_IDX"]]
                        for name in self.names:
                            text = text.replace(name, prompt[name])
                        sentences.append(text)
                    return sentences
            
            # Example usage
            templates = [
                "Template 1: [A] and [B] are friends.",
                "[B] gave [A] a gift.",
                "[A] and [B] went to [PLACE].",
            ]
            names = ["[A]", "[B]"]
            
            ioi_prompts = [
                {"TEMPLATE_IDX": 0, "[A]": "Alice", "[B]": "Bob"},
                {"TEMPLATE_IDX": 1, "[A]": "Carol", "[B]": "Dave"},
                {"TEMPLATE_IDX": 2, "[A]": "Eve", "[B]": "Frank", "[PLACE]": "the park"},
            ]
            word_idx = {
                "Alice": [0, 1],
                "Bob": [2],
                "Carol": [0],
                "Dave": [1, 2],
                "Eve": [0, 1, 2],
                "Frank": [0, 2],
            }
            N = 3
            
            dataset = Dataset(templates, names, ioi_prompts, word_idx, N)
            sentences = dataset.generate_sentences()
            print(sentences)
            ```
            
        - Now have the code use the template structure for a single sentence is templates = ["[A] is a teacher. [B] is a student. The child is [B]. [C] is a teacher. [D] is a student. The child is"], and there are no variables for [place] and [object]
            
            ```python
            class Dataset:
                def __init__(self, templates, names, ioi_prompts, word_idx, N):
                    self.templates = templates
                    self.names = names
                    self.ioi_prompts = ioi_prompts
                    self.word_idx = word_idx
                    self.N = N
            
                def generate_sentences(self):
                    sentences = []
                    for prompt in self.ioi_prompts:
                        text = self.templates[0]
                        for name in self.names:
                            text = text.replace(name, prompt[name])
                        sentences.append(text)
                    return sentences
            
            # Example usage
            templates = ["[A] is a teacher. [B] is a student. The child is [B]. [C] is a teacher. [D] is a student. The child is"]
            names = ["[A]", "[B]", "[C]", "[D]"]
            
            ioi_prompts = [
                {"[A]": "Alice", "[B]": "Bob", "[C]": "Carol", "[D]": "Dave"},
                {"[A]": "Eve", "[B]": "Frank", "[C]": "Grace", "[D]": "Hank"},
                {"[A]": "Ivy", "[B]": "Jack", "[C]": "Kim", "[D]": "Liam"},
            ]
            word_idx = {
                "Alice": [0],
                "Bob": [1],
                "Carol": [2],
                "Dave": [3],
                "Eve": [4],
                "Frank": [5],
                "Grace": [6],
                "Hank": [7],
                "Ivy": [8],
                "Jack": [9],
                "Kim": [10],
                "Liam": [11],
            }
            N = 3
            
            dataset = Dataset(templates, names, ioi_prompts, word_idx, N)
            sentences = dataset.generate_sentences()
            print(sentences)
            ```
            
        - AttributeError: 'Dataset' object has no attribute 'toks’
            
            ```python
            class Dataset:
                def __init__(self, templates, names, ioi_prompts, word_idx, N, tokenizer):
                    self.templates = templates
                    self.names = names
                    self.ioi_prompts = ioi_prompts
                    self.word_idx = word_idx
                    self.N = N
                    self.tokenizer = tokenizer
            
                def generate_sentences(self):
                    sentences = []
                    for prompt in self.ioi_prompts:
                        text = self.templates[0]
                        for name in self.names:
                            text = text.replace(name, prompt[name])
                        sentences.append(text)
                    return sentences
            
                def to_tensor(self):
                    texts = [(prompt["text"]) for prompt in self.ioi_prompts]
                    toks = torch.Tensor(
                        self.tokenizer(texts, padding=True).input_ids
                    ).type(torch.int)
                    return toks
            
            # Example usage
            from transformers import AutoTokenizer
            import torch
            
            templates = [
                "[A] is a teacher. [B] is a student. The child is [B]. [C] is a teacher. [D] is a student. The child is"
            ]
            names = ["[A]", "[B]", "[C]", "[D]"]
            
            ioi_prompts = [
                {"[A]": "Alice", "[B]": "Bob", "[C]": "Carol", "[D]": "Dave"},
                {"[A]": "Eve", "[B]": "Frank", "[C]": "Grace", "[D]": "Hank"},
                {"[A]": "Ivy", "[B]": "Jack", "[C]": "Kim", "[D]": "Liam"},
            ]
            word_idx = {
                "Alice": [0],
                "Bob": [1],
                "Carol": [2],
                "Dave": [3],
                "Eve": [4],
                "Frank": [5],
                "Grace": [6],
                "Hank": [7],
                "Ivy": [8],
                "Jack": [9],
                "Kim": [10],
                "Liam": [11],
            }
            N = 3
            
            tokenizer = AutoTokenizer.from_pretrained("gpt2")
            dataset = Dataset(templates, names, ioi_prompts, word_idx, N, tokenizer)
            sentences = dataset.generate_sentences()
            toks = dataset.to_tensor()
            print(sentences)
            print(toks)
            ```
            
        - Run a few tests, at least 3 instances of check_copy_circuit(), to see that the new Dataset is compatible with check_copy_circuit(). Do not rewrite the code for check_copy_circuit()
    
    ISSUE: it gets the instructions wrong. perhaps needs smaller steps to not overshoot.
    
    - What does prepend_bos do?
        
        The `prepend_bos` parameter controls whether a beginning-of-sentence (BOS) token should be added to the prompt text before tokenization in the `IOIDataset` class.
        
        In natural language processing (NLP) tasks, it is common to prepend a special token, such as a BOS token, at the beginning of the input sequence to indicate the start of a sentence. By adding a BOS token, the model can learn to distinguish the beginning of sentences and potentially capture important contextual information.
        
        The purpose of the `prepend_bos` parameter is to allow the flexibility of including or excluding the BOS token in the tokenization process. When `prepend_bos` is set to `True`, a BOS token will be added to the beginning of each prompt text before tokenization. On the other hand, if `prepend_bos` is set to `False` (default value), no BOS token will be added.
        
        It's worth noting that when using BOS tokens, the model needs to be aware of whether BOS and EOS (end-of-sentence) tokens are distinguished or have the same token ID. If they have different token IDs, the model can recognize the beginning and end of sentences explicitly. If they share the same token ID, the model must rely on other context indicators to determine sentence boundaries.
        
    - From IOIdataset, get all parts of the code that are required to create self.word_idx without any error
        
        Certainly! Here's the modified code from the `IOIDataset` class that generates the `self.word_idx` attribute without any errors:
        
        ```
        class IOIDataset:
            def __init__(
                self,
                prompt_type: Union[str, List[str]],
                N=500,
                tokenizer=None,
                prompts=None,
                symmetric=False,
                prefixes=None,
                nb_templates=None,
                ioi_prompts_for_word_idxs=None,
                prepend_bos=False,
                manual_word_idx=None,
            ):
                self.prompt_type = prompt_type
        
                if tokenizer is None:
                    self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
                    self.tokenizer.pad_token = self.tokenizer.eos_token
                else:
                    self.tokenizer = tokenizer
        
                self.prefixes = prefixes
                self.prompt_type = prompt_type
                if prompts is None:
                    self.ioi_prompts = gen_prompt_uniform(
                        self.templates,
                        NAMES,
                        nouns_dict={"[PLACE]": PLACES, "[OBJECT]": OBJECTS},
                        N=N,
                        symmetric=symmetric,
                        prefixes=self.prefixes,
                        abc=(prompt_type in ["ABC", "ABC mixed", "BAC"]),
                    )
                else:
                    assert N == len(prompts), f"{N} and {len(prompts)}"
                    self.ioi_prompts = prompts
        
                self.sentences = [prompt["text"] for prompt in self.ioi_prompts]
        
                self.templates_by_prompt = []
                for i in range(N):
                    if self.sentences[i].index(self.ioi_prompts[i]["IO"]) < self.sentences[i].index(
                        self.ioi_prompts[i]["S"]
                    ):
                        self.templates_by_prompt.append("ABBA")
                    else:
                        self.templates_by_prompt.append("BABA")
        
                texts = [(self.tokenizer.bos_token if prepend_bos else "") + prompt["text"] for prompt in self.ioi_prompts]
                self.toks = torch.Tensor(self.tokenizer(texts, padding=True).input_ids).type(torch.int)
        
                if ioi_prompts_for_word_idxs is None:
                    ioi_prompts_for_word_idxs = self.ioi_prompts
                self.word_idx = get_idx_dict(ioi_prompts_for_word_idxs, self.tokenizer, prepend_bos=prepend_bos, toks=self.toks)
        
            # Rest of the code...
        
        ```
        
        In this modified code snippet, the necessary parts are included to create the `self.word_idx` attribute without any errors. Specifically, the following lines are required:
        
        1. The initialization of `self.ioi_prompts` with the appropriate prompts.
        2. The creation of `self.sentences` by extracting the text from each prompt.
        3. The determination of `self.templates_by_prompt` based on the order of names in the sentences.
        4. The construction of `texts` by adding a BOS token if `prepend_bos` is `True`.
        5. The generation of `self.toks` by tokenizing the `texts` using the tokenizer.
        6. The creation of `self.word_idx` using the `get_idx_dict` function, passing the appropriate arguments.
        
        Please note that the exact implementation of `gen_prompt_uniform` and `get_idx_dict` functions is not included here, as it depends on the specific logic and requirements of your codebase.
        
    - **`get_name_idxs`**
        
        The `get_name_idxs` function takes a list of prompts, a tokenizer, and a list of index types (`idx_types`) as input. It returns a list of name indices corresponding to each index type.
        
        Here's the breakdown of the function:
        
        ```
        def get_name_idxs(prompts, tokenizer, idx_types=["IO", "S", "S2"], prepend_bos=False):
            name_idx_dict = dict((idx_type, []) for idx_type in idx_types)
            double_s2 = False
        
            for prompt in prompts:
                t = prompt["text"].split(" ")
                toks = tokenizer.tokenize(" ".join(t[:-1]))
        
                for idx_type in idx_types:
                    if "2" in idx_type:
                        idx = (
                            len(toks)
                            - toks[::-1].index(
                                tokenizer.tokenize(" " + prompt[idx_type[:-1]])[0]
                            )
                            - 1
                        )
                    else:
                        idx = toks.index(tokenizer.tokenize(" " + prompt[idx_type])[0])
        
                    name_idx_dict[idx_type].append(idx)
        
                if "S" in idx_types and "S2" in idx_types:
                    if name_idx_dict["S"][-1] == name_idx_dict["S2"][-1]:
                        double_s2 = True
        
            if double_s2:
                warnings.warn("S2 index has been computed as the same for S and S2")
        
            return [
                int(prepend_bos) + torch.tensor(name_idx_dict[idx_type])
                for idx_type in idx_types
            ]
        
        ```
        
        In this function, the `name_idx_dict` dictionary is initialized to store the name indices for each index type. The `double_s2` flag is set to False initially.
        
        The function then iterates over each prompt. It splits the prompt's text into tokens and tokenizes them using the provided tokenizer. For each index type, it determines the index of the corresponding name in the tokenized prompt. If the index type ends with "2" (e.g., "S2"), the index is calculated from the reversed tokens to account for potential name repetitions. The computed indices are stored in the `name_idx_dict` dictionary.
        
        If both "S" and "S2" are in the `idx_types` list, the function checks if the last indices for "S" and "S2" are the same. If they are, it sets the `double_s2` flag to True.
        
        Finally, the function returns a list of tensors containing the name indices for each index type. If `prepend_bos` is True, the tensor values are incremented by 1 to account for the BOS token.
        
        This function can be used to extract the indices of specific names (IO, S, S2) from a list of prompts in the context of the tokenized prompt.
        
    - what is self.word_idx?
        
        In the `IOIDataset` class, `self.word_idx` is an attribute that stores a dictionary containing the indices of specific words in the tokenized prompts. The dictionary maps index types (e.g., "IO", "S", "S2") to corresponding lists of indices.
        
        Here's how `self.word_idx` is constructed:
        
        ```
        self.word_idx = get_idx_dict(
            ioi_prompts_for_word_idxs,
            self.tokenizer,
            prepend_bos=prepend_bos,
            toks=self.toks,
        )
        
        ```
        
        The `get_idx_dict` function takes the `ioi_prompts_for_word_idxs` (defaulting to `self.ioi_prompts` if not provided), the tokenizer, a `prepend_bos` flag, and the tokenized prompts (`self.toks`) as arguments. It returns a dictionary with index types as keys and lists of indices as values.
        
        The indices in `self.word_idx` correspond to the positions of specific words in the tokenized prompts. For example, `self.word_idx["IO"]` will contain a list of indices indicating the positions of the "IO" name in each tokenized prompt. Similarly, `self.word_idx["S"]` and `self.word_idx["S2"]` will store the indices of the "S" and "S2" names, respectively.
        
        By accessing `self.word_idx`, you can obtain the indices of specific words in the tokenized prompts for further processing or analysis.
        
    - Why does pred_tokens use word.idx?
        
        The line `logits[seq_idx, ioi_dataset.word_idx[word][seq_idx]]` uses `ioi_dataset.word_idx` to access the indices corresponding to a specific word (given by the variable `word`) in the tokenized prompts. The `word_idx` dictionary in `ioi_dataset` maps index types (such as "IO", "S", "S2") to lists of indices indicating the positions of those words in the tokenized prompts.
        
        In the context of `pred_tokens`, it retrieves the logits corresponding to a specific word in the tokenized prompts. The `torch.topk` function is then applied to select the top `k` indices with the highest logits. Finally, the `model.tokenizer.decode` method is used to convert the token indices back into their original string representation.
        
        By using `ioi_dataset.word_idx`, the code can access the correct indices for the desired word in each prompt, allowing further processing or analysis based on the selected word's logits.
        
    
    Unlike in the paper where the templates’ subjects are at diff positions, in our simple starting case, self.word_idx can be hard-coded in because the subjects will be at the same position every time in the template.
    
    - What is Ġ in a token?
        
        The Ġ symbol, also known as "Ġ" (pronounced as "gee-space"), is a special character used by some tokenizers in the Hugging Face `transformers` library, such as the GPT-2 tokenizer. It is used to represent word boundaries or spaces between words when tokenizing text.
        
        In models like GPT-2, the tokenizer typically splits the input text into individual tokens, where each token represents a subword unit or a word. To distinguish between word boundaries, the tokenizer prefixes the tokens corresponding to the beginning of a word with the special character Ġ.
        
        For example, consider the sentence "I love natural language processing." After tokenization, it might be represented as a sequence of tokens like:
        
        ["I", "Ġlove", "Ġnatural", "Ġlanguage", "Ġprocessing", "."]
        
        Here, the Ġ symbol is used before the words "love," "natural," "language," and "processing" to indicate the spaces between words. It helps to preserve information about word boundaries during tokenization, which is important for models to understand and generate coherent text.
        
        Note that not all tokenizers use the same special character or encoding scheme. Different models and tokenizers may have their own variations, so it's important to consult the documentation or specific implementation details for each tokenizer to understand the symbols used in tokenization.
        
    
    `pred_tokens` is calculated for EVERY subject. If the subject (S1, S2, etc) appears in pred_tokens, it’s +1 for `n_right`. Thus, the final pred_tokens is just for S4, but not for the other subjects, so it’s not entirely accurate to output it. We have to output it for EVERY subject.
    

Rewritten dataset: [https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU#scrollTo=qau6bOQRXcrB&line=12&uniqifier=1](https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU#scrollTo=qau6bOQRXcrB&line=12&uniqifier=1)

Rewritten copy_scores function: 

[https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU#scrollTo=-2rIAnfFqv62&line=5&uniqifier=1](https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU#scrollTo=-2rIAnfFqv62&line=5&uniqifier=1)

---

- Obtain important heads (to run these fns on) from:
    
    most_recent_S_attn_pat.ipynb
    
    [https://colab.research.google.com/drive/1KaqcS92-BI4FZ7m-r8rCW9tIovxA_s93#scrollTo=VcFgqbcF4YvI](https://colab.research.google.com/drive/1KaqcS92-BI4FZ7m-r8rCW9tIovxA_s93#scrollTo=VcFgqbcF4YvI)
    
    - per_head_logit_diffs is a 2D tensor. get the row, col, val of its top values
        
        To get the row, column, and value of the top values in a 2D tensor `per_head_logit_diffs`, you can use the following steps:
        
        1. Determine the number of top values you want to retrieve.
        2. Flatten the 2D tensor into a 1D tensor using the `view()` function.
        3. Use the `topk()` function to get the indices and values of the top elements in the flattened tensor.
        4. Convert the flattened index back to row and column indices using integer division and modulo operations.
        5. Retrieve the row, column, and value for each of the top elements.
        
        Here's an example code snippet in Python:
        
        ```
        import torch
        
        # Step 1: Define the number of top values to retrieve
        num_top_values = 5
        
        # Step 2: Flatten the 2D tensor
        flattened_tensor = per_head_logit_diffs.view(-1)
        
        # Step 3: Get the indices and values of the top elements
        top_indices = torch.topk(flattened_tensor, num_top_values)[1]
        top_values = torch.topk(flattened_tensor, num_top_values)[0]
        
        # Step 4: Convert the flattened index back to row and column indices
        rows = top_indices // per_head_logit_diffs.size(1)
        cols = top_indices % per_head_logit_diffs.size(1)
        
        # Step 5: Retrieve the row, column, and value for each top element
        for i in range(num_top_values):
            row = rows[i].item()
            col = cols[i].item()
            value = top_values[i].item()
            print(f"Top value {i+1}: Row={row}, Column={col}, Value={value}")
        
        ```
        
        Make sure to replace `per_head_logit_diffs` with your actual tensor variable. The code will print the row, column, and value of the top values, starting from the highest value. Adjust the value of `num_top_values` as needed to get the desired number of top values.
        
    - output these as a tuple of (row, col)

---

EXPM: Test if S1 isn't recognized in copy circuit bc S1 is Alice or if there’s an error in how S1 defined in Dataset code

REF: [https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU#scrollTo=3oGpirrq4gQ_&line=8&uniqifier=1](https://colab.research.google.com/drive/1NCBOLPx038FxwEacmHDsCesWIAW1z8kU#scrollTo=3oGpirrq4gQ_&line=8&uniqifier=1)

RESULT: The bug was in the new Dataset defining S1’s index tensor wrong

---

Rewrite Path Patching to use new dataset

alter get_heads_circuit(), which finds which heads to keep:

- get_extracted_idx
    
    The function `get_extracted_idx` takes two parameters: `idx_list`, which is a list of strings representing indices, and `ioi_dataset`, which is a dataset object. The purpose of this function is to extract the indices specified in `idx_list` from the `ioi_dataset` and return them as a nested list.
    
    Here's a breakdown of the function:
    
    1. It initializes an empty list called `int_idx` with a length equal to the number of sentences in the `ioi_dataset`. This list will store the extracted indices.
    2. It iterates over each `idx_name` in the `idx_list`.
    3. Inside the loop, it attempts to extract the indices associated with the current `idx_name` from the `ioi_dataset.word_idx` dictionary. If the extraction is successful, it converts the extracted indices from torch tensors to Python objects using a list comprehension.
    4. If the extraction fails, indicating that the `idx_name` is not found in the dataset, an error is raised with a helpful message.
    5. Finally, the function uses a helper function called `join_lists` (not shown in your code snippet) to merge the extracted indices into the `int_idx` list.
    6. The function returns the `int_idx` list, which contains the extracted indices.
    
    It's worth noting that the implementation of the `join_lists` function is missing from the code snippet you provided, so I can't provide specific details about how the lists are merged.
    
- ValueError: Index end not found in the dataset
    
    The error message indicates that the index `end` is not found in the `ioi_dataset`. The code attempts to retrieve the indices associated with the `end` index from the `ioi_dataset.word_idx` dictionary, but it fails because the index does not exist.
    
    To resolve this issue, you should verify that the index `end` is correctly defined in the `ioi_dataset` and that it is spelled correctly. Double-check the dataset to ensure that the `word_idx` dictionary contains the necessary key-value pairs for the indices you are trying to extract.
    
    If the `end` index should be present in the dataset but is missing, you may need to investigate why it is not included or consider modifying the dataset to include the missing index.
    
    Additionally, you can print the `ioi_dataset.word_idx` dictionary and the `idx_name` variable to get more information about the specific values being used when the error occurs. This can help identify any inconsistencies or issues with the dataset or the input.
    

- in colab, how can we debug when a function throws an error when using a function it downloaded from github? automatically locate the breakpoint without manually putting in pdb.set_trace()
    
    Use the **`%debug`** magic command to automatically activate the debugger when an error occurs. Add **`%debug`** before the line that calls the function you want to debug. For example:
    
    %debug
    result = your_function()
    

Use actv patch (head heatmap) to identify heads, then copy scores to see what they’re doing. Once you identify multiple heads in a circuit, use path patching.

---

Look for Adjective Identification Heads

Copy values for adjs can also be used for adj heads, without needing a circuit.

Adjective moving:

Bob is blue. Mary is Red. Bob is

Note these aren’t as strong as subject finders, but are still consistent. So there’s some signal distinguishing them.

<<<

Adjective mover input tests:

In the previous notebook, simple_analogies_pt2:

[https://www.notion.so/Simple_analogies_circuits-766fb391cad246da9150bcd5d98248a4?pvs=4#e3ec672cd08846699eeea020c4d4f9af](../Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/simple_analogies_circuits%20ipynb%20766fb391cad246da9150bcd5d98248a4.md)

We did not test these simple adjective mover inputs, but instead tested more complex ones that required the model to understand transitivity, “has”, and analogies. Make a new notebook to test more adjective mover prompts using GPT-2-small:

[adjective_mover_prompts.ipynb](../Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/adjective_mover_prompts%20ipynb%20cf8a6d9206fb47588b60c921c090b348.md) 

[https://colab.research.google.com/drive/1e70-iPdPprDXCis-TnyJ64tFhFPS3Xej](https://colab.research.google.com/drive/1e70-iPdPprDXCis-TnyJ64tFhFPS3Xej)

- EXPM: Test if it is checking for the actual correct adjective, or if it's doing something else such as outputting the most recent adjective, the least recent adjective, etc.
    
    DESC: Test if it is checking for the actual correct adjective, or if it's doing something else such as outputting the most recent adjective, the least recent adjective, etc. In any case, it is moving adjectives. Or perhaps not moving the same ones, but "identifying" similar ones.
    
    RESULT: This shows that it doesn't always work. Still, it "identifies color". 
    
- EXPM: Try different colors
    
    RESULT: This also fails. We can say it's not adjective movers.
    
- EXPM: "Bob is tall. Mary is green. Bob is”
    
    RESULT: 1st is ‘a’, 2nd is ‘tall’
    
    When trying "Bob is tall. Mary is big. Bob is”, it has similar rankings.
    
    "Bob is big. Mary is small. Bob is” : similar to before
    
    "Bob is smart. Mary is strong. Bob is” : similar to before
    
    ANALYSIS: Is there a way to make it not output articles?
    
- EXPM: "Bob is not smart. Mary is smart. Bob is”
    
    RESULT: This successfully says “not” by 26%, and “smart” by only 10% in 2nd place. 
    
    TRY: let’s see if sentences have consistent “not” outputs using in-context. See if it does ti CORRECTLY (not on Mary)
    
- EXPM: "Bob is smart. Mary is not smart. Bob is”
    
    RESULT: It successfully outputs “smart” instead of “not”. 
    
    ANALYSIS: So here, it’s not just outputting “not” because “not” exists.
    
- EXPM: "Bob is not big. Mary is big. Bob is”
    
    DESC: Also test:
    
    - "Bob is big. Mary is big. Bob is”
    - "Bob is not big. Mary is not big. Bob is”
    
    RESULT: All yield correct expected output
    

We predict that running more tests will also not give consistent correct answers. We avoid the ones that output articles like “a”. Even if they don’t consistent give what’s right, they still give some sort of adjective. Instead of looking for heads identifying exact adjectives, we look for ones which have “something to do with adjectives”. This means it must still target adjectives in the input, then “move” that to perhaps an adjective-focused attention head or adjective-focused MLP.

### Future Work

---

- Check if transformerLens has updated code, or if ACDC has it
    
    NOTE: if drive uploads an .ipynb, don’t copy drive link, copy the colab url either from ad bar or cell
    
- for the attention heads that matter, check their attention patterns to see where they are active on (dest token) and where they attend to (source token)
- what decides what’s query vs what’s key? query is source sentence, key is target sentence. in decoder-only (gpt), they’re the same? then value can be used in either? no- if q=3, k=5, then v is always for 5, not 3. and if q=5, k=3, then v is always for 3, not 5 (?)