# 0.2- CNNs

0.2- part 2

- t.max and t.maximum are similar; can take multiple tensors as arg and take element-wise
- t.zeros_like(x) is for same shape as x, similar to t.zeros(x.shape)
- diff bettween **torch.nn.init.uniform_** and t.rand?
- rand is 0 to 1, so you need to make it -1 and 1. So they do 0 to 2 then -1 to 1 by subtracting 1
- with t.inference_mode() vs zero_grad?
    
    [https://stackoverflow.com/questions/69543907/pytorch-torch-no-grad-vs-torch-inference-mode](https://stackoverflow.com/questions/69543907/pytorch-torch-no-grad-vs-torch-inference-mode)
    
- logits is 2D tensor with classes on col
- [https://pytorch.org/docs/stable/generated/torch.argmax.html](https://pytorch.org/docs/stable/generated/torch.argmax.html)
- t.eq
- t.mean: can use this or sum()/len()
- validation is for every epoch, not every img (or batch) (check indent)
- for each input, get num preds right and add to “num”
- then after each epoch, get validation (using mean)

0.2, part 3 (convs):

fixed random permutation: shuffle pixels around

this is not translational equivariance (where move entire cat to top right corner from bottom) but **spatial locality**- the CNN actually sees things as close to one another. so a CNN would be less effective than before if shuffle pixels around

but an MLP would be equally as effective as its own performance before as it doesn’t depend on spatial locality to recognize things, just “signals”