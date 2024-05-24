# Learn From Model Beyond Fine-Tuning

GP- Boost the model’s performance under data distribution shifts

SOLN: In WiSE-FT, the weights of the zero-shot model (the original pre-trained model before fine-tuning) and the fine-tuned model are combined. This "ensembling" means taking a weighted sum of the parameters of both models.

- WHY:
    
    Ensembling handles distribution shifts effectively due to several key reasons:
    
    1. **Combining Generalization and Specialization**: Ensembling typically involves combining models that have different strengths. A zero-shot model, which is not fine-tuned on a specific task, is good at generalizing across a wide range of scenarios because it's trained on a diverse dataset. On the other hand, a fine-tuned model specializes in the specific task it's trained on. By ensembling these two types of models, you get a system that not only excels at the target task but also retains the ability to generalize well to new, unseen data.
    2. **Robustness to Overfitting**: Fine-tuned models can sometimes overfit to the specific characteristics of their training data. This makes them less effective when the test data has different characteristics (i.e., when there's a distribution shift). The zero-shot model, which hasn't been fine-tuned to fit these specific characteristics, can provide a counterbalance. Its broader understanding helps maintain performance when facing data that differs from the training set.
    3. **Diverse Perspectives**: Different models capture different aspects of the data. A zero-shot model might capture more universal patterns, while a fine-tuned model captures more specific nuances. By ensembling, you essentially create a model that can look at the problem from multiple perspectives. This diversity in perspectives can be particularly useful in handling situations where the test data doesn't perfectly align with the training data.
    4. **Mitigating Weaknesses**: Each model in the ensemble may have its own weaknesses. The zero-shot model might not be as accurate on the specific task, while the fine-tuned model might be too narrowly focused. Ensembling helps mitigate these weaknesses as the strengths of one model can compensate for the shortcomings of the other.
    5. **Adaptability**: Ensemble models can be more adaptable to changing data environments. If the data distribution shifts, the ensemble can rely more on the generalist (zero-shot) model to maintain performance, whereas it can leverage the specialist (fine-tuned) model when the data closely resembles the training set.
    
    In summary, ensembling helps handle distribution shifts by combining the broad, generalizable knowledge of a zero-shot model with the specialized, task-specific knowledge of a fine-tuned model. This hybrid approach creates a more flexible and resilient system capable of performing well across varying data distributions.
    

SOLVING: When data distribution shifts, you need to adapt to more perspectives. This means taking output from multiple models. Thus, sum up their outputs.

---

GP- Fine tune without retrain many parameters

SOLN- Only fine tune new layers

SOLN DETAILS- These new layers inserted in between existing ones are called Adapter Layers. During fine-tuning, only the parameters of these adapter layers are updated, while the parameters of the original pre-trained layers remain frozen.

---

⚠️

GP- How to improve adapter layers?

SOLN- 

SOLN DET- 

This introduces inductive biases (certain assumptions or predispositions) into the structure of the adapter layer

- REFS
    
    [Kronecker Product](https://www.notion.so/Kronecker-Product-522d797501164854b3b6a5597cd35157?pvs=21) 
    

---