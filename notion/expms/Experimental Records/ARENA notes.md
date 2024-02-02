# ARENA notes

LOGISTICS

[https://mango-ambulance-93a.notion.site/ARENA-3-0-Virtual-Landing-Page-8f7193af31b445c586efed03e995fb74](https://www.notion.so/ARENA-3-0-Landing-Page-virtual-8f7193af31b445c586efed03e995fb74?pvs=21)

Submit exercises here:

[https://course.aisafetyfundamentals.com/arena](https://course.aisafetyfundamentals.com/arena)

Calendar

[https://docs.google.com/spreadsheets/d/1aVm6V4nK5L3QJMCRMolf6h2ZKCfn8WeGOQv5275F130/edit#gid=0](https://docs.google.com/spreadsheets/d/1aVm6V4nK5L3QJMCRMolf6h2ZKCfn8WeGOQv5275F130/edit#gid=0)

---

Paper Replication

[Project Planning](ARENA%20notes%201a8ff2624cff486e9d91b13139420026/Project%20Planning%207fb9304394ea4a728098c812a60d7034.md)

[Project Docs](ARENA%20notes%201a8ff2624cff486e9d91b13139420026/Project%20Docs%20b831ce760ca248db9b8071691d76b7ee.md)

---

CODE

[https://arena3-chapter0-fundamentals.streamlit.app/](https://arena3-chapter0-fundamentals.streamlit.app/)

[https://arena3-chapter1-transformer-interp.streamlit.app/](https://arena3-chapter1-transformer-interp.streamlit.app/)

[https://arena3-chapter2-rl.streamlit.app/](https://arena3-chapter2-rl.streamlit.app/)

ARENA 3.0 exercises

[https://drive.google.com/drive/folders/1XiskbDzfFOKNugytyKKsjRzd0p3MpTQZ](https://drive.google.com/drive/folders/1XiskbDzfFOKNugytyKKsjRzd0p3MpTQZ)

[https://prod.liveshare.vsengsaas.visualstudio.com/join?9EC182F8DEA97946113A8707D6B3D2334F42](https://prod.liveshare.vsengsaas.visualstudio.com/join?9EC182F8DEA97946113A8707D6B3D2334F42)

---

OTHER NOTES

- colab collapsable
    
    ```jsx
    <details>
    <summary> </summary>
    
    </details>
    ```
    

[How to pair program](ARENA%20notes%201a8ff2624cff486e9d91b13139420026/How%20to%20pair%20program%203d0534b6aa6040a6b07bf7e82e3687b6.md)

[VScode liveshare](ARENA%20notes%201a8ff2624cff486e9d91b13139420026/VScode%20liveshare%202977e8c39e214a13b0579f5245698c53.md)

[Misc](ARENA%20notes%201a8ff2624cff486e9d91b13139420026/Misc%2036b77e04c01545d3857792d6ea0f07fa.md)

---

Exercise Notes

[Colab NBs Summary](ARENA%20notes%201a8ff2624cff486e9d91b13139420026/Colab%20NBs%20Summary%20a5af358447d04e2b9d6eeb42f455b5a3.md)

[0.1- Ray Tracing](ARENA%20notes%201a8ff2624cff486e9d91b13139420026/0%201-%20Ray%20Tracing%20a333ba470db04abea49a3d394be73e8d.md)

[0.2- CNNs](ARENA%20notes%201a8ff2624cff486e9d91b13139420026/0%202-%20CNNs%20cce37f95badb4c3a9a84be68ea647073.md)

[0.3- optim](ARENA%20notes%201a8ff2624cff486e9d91b13139420026/0%203-%20optim%207d8f58449c1f42fa93bf1459469ef854.md)

[0.3 code](ARENA%20notes%201a8ff2624cff486e9d91b13139420026/0%203%20code%20dcea764934cc4ea1924c48629e426fc0.md)

[0.5 code](ARENA%20notes%201a8ff2624cff486e9d91b13139420026/0%205%20code%2044e140b10f9f4749a02f02c41e44be9d.md)

[1.2 code](ARENA%20notes%201a8ff2624cff486e9d91b13139420026/1%202%20code%2005323c354fcf4d78bf8d26960166abb0.md)

[1.3](ARENA%20notes%201a8ff2624cff486e9d91b13139420026/1%203%20267592e85b5141d2a401e8fae37a6481.md)

[1.5 code](ARENA%20notes%201a8ff2624cff486e9d91b13139420026/1%205%20code%20a7e163b9287d4fcbb10bfc7e6912359a.md)

[2.1](ARENA%20notes%201a8ff2624cff486e9d91b13139420026/2%201%200c02f134e2be42b39bf203a97c07c25a.md)

[2.2](ARENA%20notes%201a8ff2624cff486e9d91b13139420026/2%202%20f7f41971ffc043a99db4aad79ca35f82.md)

[2.4](ARENA%20notes%201a8ff2624cff486e9d91b13139420026/2%204%20827534c7916642a39cca8df23031fa9f.md)

---

[Neel marius talks](ARENA%20notes%201a8ff2624cff486e9d91b13139420026/Neel%20marius%20talks%20b0b1f02919324d74a53e1f81c205ce06.md)

Are there any tips on deciding how many people should work on a paper and estimate their contribution (via task allocation)? (Eg. some papers only have 1 author, some have 20)

Talk to authors about next steps (email, discord)

---

Do this for select exercises in chapters 0.1, 0.2, 0.3, 1.1, 1.2. Later: 0.4, 0.5, 1.3, 1.4, 1.5. Even later: 2

Think of this like dungeons in a video game, with tools like in Zelda

Write unit tests for this too to make it more like a game (or leetcode)- show what cases need to be passed. Or write this yourself.

Personally working on organizing this, will take some time to clean up, geared towards my own learning style

Put these in a colab notebook to run them and show how they solve the problem

Important and common generalizable techniques (in response to issues):

- Module blocks (resnet, GANs)
- Classes
- W & B
- einops rearrange, repeat, reduce
- einsum for MM
- broadcasting
- Tensor Indexing
    - :
    - …
    - arange
- PyTorch operations:
    - empty vs init
    - max VS maximum
    - squeeze, unsqueeze
    - concatenate
    - stack, vstack
    - append
    - linspace
    - arange
    - t.mean(tensor) vs tensor.mean()
        - [Given a tensor variable called tensor in pytorch, compare when to use t.mean(tensor) vs tensor.mean()](https://chat.openai.com/c/4f3f9f68-1187-41c7-9edd-a7f63d2724c5)
    - where
    - gather
- Numpy operations:
    - argmax
    - linspace
- PyTorch layers
    - Parameters
    - .to(device)
    - model.cfg
- Hooks
- Training algorithm: loss, step, zero
- Testing algorithm: logits, argmax, softmax
- Context managers: save, CM in CM

Only choose if both commonly used in ARENA and useful in rsch

When reviewing: In each exercise, give bullets on what was used, and also make new page. Have page for both technique and sub-problem type. Eg) exercise has sub-problem “matrix multiply”, solved by technique “einsum”. Outline sub-problems by logically what is needed to be solved next.

- Capstone recruitment post
    
    Hi, looking to see if anyone else is interested in working on one of these papers (posted a comment on the suggested papers' docs too):
    Successor Heads: Recurring, Interpretable Attention Heads In The Wild (related to IOI, SAEs, and vector arithmetic)
    Copy Suppression: Comprehensively Understanding an Attention Head (related to IOI, the ablation mechanism can be challenging to replicate)
    Inference-Time Intervention: Eliciting Truthful Answers from a Language Model (related to function vectors and model steering)
    Steering Llama 2 via Contrastive Activation Addition  [most interested in building on this research in the future]
    I'll be choosing what to work on by mid-Monday (tomorrow, EST) and will update what's chosen in this thread, message me if you're interested. I have talked to a few people so far who may also be, am looking for 2-5 people in a group.  In my slack channel I'll be sending the details of the proposed project by the end of tomorrow too + post a project plan.