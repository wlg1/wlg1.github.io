# Clement work

[https://clementneo.com/test_images/](https://clementneo.com/test_images/)

![Untitled](Clement%20work%20164617a8fb7145029b828ee403b31a24/Untitled.png)

After browsing a few images, the logit lens looks very interesting already (even before SAE results). Just to clarify understanding, based on Figure 1 in your proposal draft, do you expect a patch like <IMG495> “rock” (in the attachments for val_0…81) to be extracted for the text prediction of “rock” (also in attachments)? Would be interesting to see which image patch(es) with “rock” (there are multiple, and multiple rocks) are used. I’m also wondering what the model predicts as “the” object, given there are multiple objects. Is it one it sees as “most prominent”? I suppose the ablation experiments on different combinations of object patches could shed light on this. 

![Untitled](Clement%20work%20164617a8fb7145029b828ee403b31a24/Untitled%201.png)

![Untitled](Clement%20work%20164617a8fb7145029b828ee403b31a24/Untitled%202.png)

<<<

An obvious but peculiar thing is that for the (:) last token’s early layers, with less info, seem to “default” to certain predictions, and these tokens are “sterd” and “penas”, which seem to be nonsense but it’s like in almost every image. This is probably not useful but it is strange why the model uses those specific ones (see attachments)

![Untitled](Clement%20work%20164617a8fb7145029b828ee403b31a24/Untitled%203.png)

![Untitled](Clement%20work%20164617a8fb7145029b828ee403b31a24/Untitled%204.png)

So basically for the text (given it's the same prompt for all images), all the early to mid layers start off with the same default (obvious) and seems like around layer 18-20 is when the last token really changes to be more image specific (sounds consistent with previous research work on mid-layers picking up info). Haven't checked this for the img patches yet. I suppose you'll have a way to automate how to check this. 

<<<

Like when dog is detected, I wonder where it’s “first” detected (can easily be searched for). Does it compose the other concepts like ear and nose to do this or does it just recognize a patch as dog without these others? It seems like in the few samples I saw, it begins to pick up “dog” around the mid layers 18-21 too.

![Untitled](Clement%20work%20164617a8fb7145029b828ee403b31a24/Untitled%205.png)

<<<

lastly I also suppose you'll refine the interface to allow hovering over a patch and clicking it to bring it to the corresponding row (like in the Building Blocks of Interp paper), making something like a feature dashboard on Neuronpedia for multimodal would be interesting

---

[https://arxiv.org/pdf/2304.08485](https://arxiv.org/pdf/2304.08485)

Llava