# Kiho

- ask about papers
    1. Why do we need to unify input and output space? How does this help with steering?
        1. is it that a concept in one space is “the same” as the concept in the other?
        2. Author response: sec 3 of lin repr paper, the inner product is not interpr, the prob distr is preserved. the inner product in each space is arbitrary. what’s the right notion of inner product? 
    2. animal may not be binary, but is it “not animal”? so would there be a vector for each polytope categorical concept? but dog isn’t a binary concept either, yet it’s a vector. and animal does have a vector representation l_animal that says animal is a binary feature. this is orthogonal to the simplex. but shouldn’t they be the same, as they’re both animal- so parallel, not orthogonal?
        1. The animal dir is calculated here: `dirs.update({'animal': estimate_cat_dir(all_animals_tokens, g, vocab_dict)})`
        2. or, is this simplex NOT the same as animal, but is the difference between each concept that’s NOT animal? in other words, it’s all the things that make each concept different from animal?
        - Author response:
            1. conditional prob: animal - dog is (dog | animal), so not really steering concept
            2. embeddings space is probability distribtuion and is hard to find vector rep with dir and magn with 0 and 1. but only want to change target concept without changing other concepts. this may not be the right direction decomposition
            3. if some value is subordinate to another value, should not affect the subvalued conditioned on the upper value. simplex ; position of trianlge (perpendicular line o fit) is parallel to animal. projection onto direction. 
            4. this fig 3 spce is not the same as activation space. fig 3 is unembed space. so varying along fig 3 gives different probability in output. 3d subspace of vocab space
            - gamma is original unemb vector, within weight matrix of unembed matrix. g is tranformed to causal inner product by centering and whitening ( uncorrelated and each have variance 1). unified means lambda bar w and gamma bar w are the same. they map to the same thing in causal inner product space.
                1. dirs for animal bird etc, when add these to embedding, the intervention did work. but not sure if this is the real embedding from some context. so maybe intervening is out of space.
                2. embd space means final layer hidden states of last hidden tokens. so both are after final layer. this paper computes what the model ends up with and if those representions have similiaries
                3. intermediate layers are more complicated with logit lens. kiho says they’re not linear; after final layer, the last step is layer norm (which is not linear), but not concrete
                4. contrastive sentences: if concept is sentiment, on movie reviews, is easy. but if we add this difference to news or other things, it will not give it. out of distribution. may be open problem. so train must match test. test out if train on news and add to movie. so that’s why we want a more general direction. what if used a very big dataset that contained those, perhaps is better. but test set should out of distribution. 
                - do polytopes exist in intermediate space? the umbed should be at point of simplex.
                    1. simplex not found in intermediate space yet but not that meaningful. decomposition
                    2. steer by simplex: korean chinese english, their categorical concepts means
                    3. direct sum in fig1a means thm 6 d and e means animal-plant dir is ortho to mammal-animl so subspace spanned by these diffs are orth to animal, so this simplex is orth to this dir. 
                    4. define concept carefully. now, it’s actv after final layer so it’s for next word prediction. so intermediate feature is hard to define.
                    5. polytope of clusters- try to find, may be a simplex
                    6. ablate the simplex of (mammal bird reptile)- would that leave you with animal? then you could isolate a concept. so simplex are the differences. span(animal- mammal, animal-bird, etc). simplex can be more than 3 things. 
                    7. animal is repr as binary vector. animal has no counterfactual definition. binary feature is animal and not animal, but not same as counterfactual
                    8. an animal vector, the simplex polytope is not animal category, is the differences. 
            1. adj mat in fig 5: if feature is conn by a subset relation, so 0 means no relation and 1 means they’re subset

[kiho meeting 2](Kiho%20e23ba8681d5d4f0688740c8974f03758/kiho%20meeting%202%203900465d2b7f45639e8dd1e48d97706e.md)