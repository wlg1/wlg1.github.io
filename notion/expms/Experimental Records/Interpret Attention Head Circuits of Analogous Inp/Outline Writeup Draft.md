# Outline Writeup Draft

[Paper Draft- Comparison Circuits](../Paper%20Drafts%20c8403ec170204b3aa40fd28465a5635d/Paper%20Draft-%20Comparison%20Circuits%20852d577eb555460e87ae511a1750ef50.md) 

Sec 1- intro

Methods Overview (sec 2):

1. Logit Diff and Lens (stream, layer, head) to find general, important areas
    1. line graphs and heatmaps
2. Activation patching + path patching to find important heads in those areas
3. Attention Patterns and Correlation Plots to hypotheize functions of important heads
    1. See what it does by OV matrix (eg. copy scores): multiply inputs by OV matrices, then unembed to vocab space (see logit lens). See how many samples have this token as top-5, compared to if use OV matrix of averaged head
    2. Attn head output (projections onto components) vs token logit scatter plots 
    
    [https://colab.research.google.com/drive/1GQo_RSEY40ncByvwy81kxwSKGPHlbxSx](https://colab.research.google.com/drive/1GQo_RSEY40ncByvwy81kxwSKGPHlbxSx)
    
    (for steps 1-3)
    
    Antonym (opposite, duality) heads:
    
    [https://colab.research.google.com/drive/1TXi0A-TNXYr748Z23kpDw2YEHGjafOUO](https://colab.research.google.com/drive/1TXi0A-TNXYr748Z23kpDw2YEHGjafOUO)
    
4. Congruence of neurons and embedded vectors at different places in model
    1. Neuroscope (for MLPs)
    
    [https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA](https://colab.research.google.com/drive/1lZQkZ5u2mQxsYyiGaUKbW-XjdHP0GJpA#scrollTo=8zWhomib5KMa)
    
    [https://colab.research.google.com/drive/1Gvt1esiymU9UPfDKB1Nc7gMMUhJadLa1](https://colab.research.google.com/drive/1Gvt1esiymU9UPfDKB1Nc7gMMUhJadLa1)
    
    v2 simplifies code into fns
    
    [https://www.notion.so/Knowledge-Neurons-in-Pretrained-Transformers-2bdb62adf77d4e94aa77d2a36375e570](https://www.notion.so/Knowledge-Neurons-in-Pretrained-Transformers-2bdb62adf77d4e94aa77d2a36375e570)
    
5. (in-progress) Construct hypothesized circuits based on how ablating then patching h→R affects node R
    1. to use actv patching (not necc path), just look at the diff of the head's output value (clean-corr), instead of logit dif (pronoun circ, fig 7); this plots heatmap. recursively find more. IOI fig4c shows bar plots of NM attn after patching all S-inh
    2. Test on the 3 metrics: faith, compl, minim
    3. (in-progress b/c code inprog) ACDC, metric thres for logit diff
    
    [https://colab.research.google.com/drive/1cFJc2Zc1fh_BXV42q3h4zfvRikINE_Mo#scrollTo=YaJBj52XWzMP](https://colab.research.google.com/drive/1cFJc2Zc1fh_BXV42q3h4zfvRikINE_Mo#scrollTo=YaJBj52XWzMP)
    
6. (in-progress) Track dot product movement of info of various tokens to combine to end
    
    [https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV](https://colab.research.google.com/drive/1rch6VaG9O1YFJT1wPjjbXyDgXizGT7WV)
    
    ISSUES: not always clean due to info not taken into account (eg. pos emb)
    
7. (in-progress) Edit those heads and MLPs (rank-1) to try to change how circuits move info (attn weights) and what info (MLP weights)

Code to modify:

- dataset
- copy scores
- logit diff and path patching
- congruence (at various areas)

Analysis (sec 3- generalized to functions):

Results of applying functions to various Datasets

(sec4, Related work- explain SVD intuitively, etc)

(sec 5- many ideas for future work)

Behind the scenes explanation: (Appendix, etc; separate doc)

1. Go over test prompts and models- what couldn’t the models predict?
2. Connections to biology:
    - Immune system and competing memes, associations but feeling choices which to further think about, subconscious, biological circuits use drugs to alter (drugs also compete for binding receptors), lots of input information, brainwashing
        - mental illnesses that don’t resemble human ones, but are considered AI psychosis. we understand biological networks to better know human health, so understand AI networks to better know how to deal with AI health. interventions that don’t damage rest of AI (side effects) esp if it’s connected to sensitive data/triggers
        - Do drugs and bad foreign entities compete to bind with receptors? how do drugs win?
            
            When it comes to receptors in the human body, both drugs and certain foreign entities can indeed compete to bind with them. Receptors are specialized proteins found on the surface of cells or within cells, and they play a crucial role in transmitting signals and regulating various physiological processes.
            
            Drugs are designed to interact with specific receptors in the body and produce desired effects. These effects can range from pain relief to altering mood, enhancing cognitive function, or treating various medical conditions. Drugs are designed to have a specific molecular structure that allows them to bind to specific receptors, mimicking or modulating the effects of naturally occurring substances in the body.
            
            On the other hand, foreign entities, such as toxins or harmful substances, can also interact with receptors in the body. These foreign entities may have different origins, including environmental pollutants, pathogens, or other toxic substances. Some foreign entities may accidentally or intentionally interact with receptors, leading to harmful effects on the body's normal functioning.
            
            When both drugs and foreign entities compete for binding to receptors, several factors come into play to determine which one wins:
            
            1. Affinity: Affinity refers to the strength of the interaction between a substance (drug or foreign entity) and a receptor. Drugs are specifically designed to have a high affinity for their target receptors, meaning they have a strong binding capacity. Foreign entities may have varying affinities for different receptors, and their ability to compete with drugs depends on their affinity for a particular receptor.
            2. Selectivity: Drugs are often designed to be highly selective, meaning they preferentially bind to specific receptors while avoiding others. This selectivity allows drugs to produce the desired effects without interfering with unrelated receptors. In contrast, foreign entities may have a broader range of interactions with different receptors, potentially leading to undesired or harmful effects.
            3. Concentration: The concentration of drugs and foreign entities also plays a role in determining their binding competition. If the concentration of a drug is higher than that of a foreign entity, the drug is more likely to occupy the available receptors and exert its effects. However, if the concentration of a foreign entity is higher or its interaction with the receptor is particularly strong, it may outcompete drugs for receptor binding.
            4. Metabolism and clearance: Drugs often undergo metabolism and clearance processes in the body, which can affect their concentration and duration of action. Foreign entities may have different metabolic pathways or mechanisms of elimination. The rate of metabolism and clearance can influence the competition for receptor binding by altering the availability and duration of drugs or foreign entities.
            
            It's important to note that the body has various defense mechanisms to identify and eliminate harmful foreign entities. These mechanisms, such as the immune system, detoxification processes, and clearance pathways, aim to protect the body from the adverse effects of foreign substances.
            
            Overall, while drugs and foreign entities can compete to bind with receptors, the design and selectivity of drugs, as well as factors like affinity, concentration, and metabolism, play crucial roles in determining the outcome of this competition.
            
        - What's an example of this competition?
            
            One example of the competition between drugs and foreign entities for receptor binding is the interaction between opioids and endorphins.
            
            Opioids are a class of drugs that are commonly used for pain relief. They work by binding to opioid receptors in the brain, spinal cord, and other parts of the body. Opioid receptors are normally activated by naturally occurring substances called endorphins, which are the body's natural painkillers.
            
            When opioids are introduced into the body, they can bind to the same opioid receptors that endorphins target. Opioids have a high affinity for these receptors, meaning they have a strong binding capacity. As a result, opioids can outcompete endorphins for receptor binding, leading to potent pain relief and other effects.
            
            In this scenario, the competition occurs between the exogenous opioids (drugs) and the endogenous endorphins (naturally occurring substances) for binding to the opioid receptors. The opioids have a higher affinity and concentration than endorphins, allowing them to effectively occupy the receptors and produce their analgesic effects. This is why opioids can be highly effective in managing pain, but they can also lead to dependence and addiction if used improperly or for an extended period.
            
            It's worth noting that the body has natural mechanisms to regulate and balance the receptor interactions. In the case of opioid use, prolonged exposure to exogenous opioids can lead to tolerance, where higher doses are required to achieve the same effect. This occurs as the body adjusts its receptor availability and sensitivity in response to the presence of opioids. Additionally, prolonged use of opioids can suppress the natural production of endorphins, further impacting the competition between drugs and endogenous substances.
            
            This example illustrates how drugs and foreign entities can compete with endogenous substances for receptor binding, and how drugs with higher affinity and concentration can gain the upper hand in occupying the receptors and exerting their effects.
            
            - Why don't want endorphins to bind?
                
                I apologize if my previous response was misleading. Endorphins are indeed desirable substances that bind to opioid receptors in the body. Endorphins are naturally produced by the body and are part of the endogenous opioid system. They play a crucial role in pain modulation, mood regulation, and the overall well-being of an individual.
                
                Endorphins, when they bind to opioid receptors, can produce analgesic (pain-relieving) effects and contribute to feelings of pleasure and well-being. These endogenous opioids are released in response to various stimuli, such as exercise, stress, or certain positive experiences.
                
                The reason exogenous opioids (drugs) are used is to mimic or enhance the effects of endorphins by binding to the same opioid receptors. However, misuse or excessive use of opioids can lead to various negative consequences, such as tolerance, dependence, and addiction. In such cases, the competition between exogenous opioids and endogenous endorphins becomes problematic, as opioids can disrupt the natural balance and functioning of the endogenous opioid system.
                
                To clarify, it is the excessive binding of exogenous opioids to opioid receptors that can lead to undesirable effects. The goal of using opioids for medical purposes is to provide pain relief or manage specific conditions under the guidance of healthcare professionals. The aim is not to prevent endorphins from binding but rather to supplement or modulate their effects when necessary.
                
                In summary, endorphins are desirable substances that naturally bind to opioid receptors in the body and play a vital role in pain relief and well-being. The use of opioids as drugs aims to modulate these effects, but misuse or excessive use can lead to negative consequences.
                
        - What's an example of this of drugs vs viruses?
            
            An example of the competition between drugs and viruses for receptor binding is the interaction between antiviral drugs and viral particles targeting specific receptors.
            
            Let's consider the human immunodeficiency virus (HIV) as an example. HIV is a viral infection that targets immune cells, specifically CD4 receptors on the surface of certain immune cells such as CD4+ T cells. The virus attaches to these receptors to gain entry into the cells and initiate the infection.
            
            Antiretroviral drugs, commonly used to treat HIV infection, are designed to interfere with the replication and spread of the virus. One class of antiretroviral drugs is known as entry inhibitors. These drugs work by binding to receptors on immune cells that HIV would typically target, thereby blocking the virus's ability to attach and enter the cells.
            
            By occupying the receptors that HIV needs to bind to, the antiretroviral drugs effectively compete with the viral particles for receptor binding. The drugs have a higher affinity and concentration than the virus, allowing them to outcompete HIV for binding to the receptors on the immune cells. This prevents or reduces the virus's ability to enter the cells and replicate, thereby inhibiting the progression of the infection.
            
            This example demonstrates how antiviral drugs can compete with viral particles for receptor binding, blocking the virus's entry into cells and impeding its replication. By effectively occupying the receptors, the drugs interfere with the virus's ability to establish infection and propagate throughout the body. However, it's important to note that antiviral therapy typically involves a combination of drugs targeting different stages of the viral life cycle to maximize effectiveness and minimize the development of drug resistance.
            
        - GPT4: Do Antiretroviral drugs bind to receptors to prevent HIV from doing so?
            
            Antiretroviral drugs do not typically work by binding to receptors to prevent HIV from doing so. Instead, they mainly target different stages in the lifecycle of the virus to prevent its replication. Here is a brief overview of how different classes of antiretroviral drugs work:
            
            1. **Nucleoside Reverse Transcriptase Inhibitors (NRTIs)** and **Non-nucleoside Reverse Transcriptase Inhibitors (NNRTIs)**: These drugs inhibit the reverse transcriptase enzyme, which is needed by the HIV virus to convert its RNA into DNA, a critical step in the replication of the virus within host cells.
            2. **Protease Inhibitors (PIs)**: These drugs work by blocking the action of protease, another HIV enzyme. Protease helps to cut HIV proteins into the right shapes and sizes for the virus to mature and become infectious. Inhibiting this enzyme prevents the production of new functional viral particles.
            3. **Integrase Inhibitors**: These drugs block the integrase enzyme, which is used by HIV to insert its viral DNA into the DNA of the host cell.
            4. **Fusion Inhibitors**: These drugs work by preventing the HIV virus from fusing with the host cell's membrane, thus stopping the virus from entering the host cell.
            5. **CCR5 Antagonists (Entry Inhibitors)**: This is probably the closest to what you're thinking of. CCR5 antagonists block a specific receptor (CCR5) on the surface of the host cell that the HIV virus uses to enter the cell. By blocking this receptor, these drugs prevent HIV from entering the cell.
            6. **Post-Attachment Inhibitors**: These are a new class of drug that prevents HIV from entering a host cell, even after the virus has attached to the cell.
            
            It's worth noting that antiretroviral therapy usually involves a combination of these drugs to increase effectiveness and decrease the risk of the virus developing resistance. The goal of these therapies is to reduce the viral load in the body, minimize the damage to the immune system, and prevent the progression to AIDS.
            
        
        [https://en.wikipedia.org/wiki/Receptor_antagonist](https://en.wikipedia.org/wiki/Receptor_antagonist)
        
        [https://en.wikipedia.org/wiki/Beta_blocker](https://en.wikipedia.org/wiki/Beta_blocker)
        
        - GPT4: What's an example of drugs vs viruses to compete for receptor sites?
            
            A notable example of drugs and viruses competing for receptor binding sites is the case of influenza viruses and the antiviral drugs known as neuraminidase inhibitors, which include oseltamivir (Tamiflu), zanamivir (Relenza), and peramivir (Rapivab).
            
            Influenza viruses possess a protein called neuraminidase on their surface, which is critical for the virus's life cycle. Specifically, neuraminidase enables the release of newly formed virus particles from infected cells, thereby allowing the infection to spread. Neuraminidase inhibitors work by binding to the active site of the neuraminidase protein, preventing it from fulfilling its function and thereby inhibiting the release and spread of the virus.
            
            The situation with CCR5 antagonists in HIV therapy, which I mentioned in the previous response, is another example. The drug maraviroc works by binding to the CCR5 receptor on the surface of certain immune cells. This receptor is one of the main entry points that HIV uses to infect cells. By binding to this receptor, maraviroc prevents HIV from entering and infecting the cells.
            
            These are examples of competitive inhibition, where the drug and the virus compete for the same binding site, in this case on a receptor or an enzyme.
            
    - Attractors and inhibitor neuron groups evolution (dyn sys, statmech)
    - Group evolution criticisms
    - Simplicial complexes and network analysis via graph matrix eigenvalues
    - DMT Visuals and dreams, how areas of brain process analogies + memories, dreams and analogies (ouroboros and benzene)
3. grants for further resources (GPU, collabs)
4. possible criticism based on past openreviews in various confs/journals for sim work

At end of 3m intro video- This is not to submit b/c the finding isn’t that signf, but the technqs and derivations from it can lead to more signf findings that can be published