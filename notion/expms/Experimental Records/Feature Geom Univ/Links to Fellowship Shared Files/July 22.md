# July 22

Luke:

Plot correlation of ground truth feature in other SAEs. Shows there’s some reasonably strong correlation. Can use diff hidden sizes up to a certain pt, but once much bigger than true num features, then too low cosine sim. Often learn same sae features

Clement:

maybe not much info in a single patch; larger saes seem to be not very interpretable. patch sizes really small

many dead features. lots of aux loss. curves are weird as it jumps to a constant lvl and stays there. played with threshold for dead features, how many train examples it has to be dead. if threshold is set too close to 1, lowering it gives a much nicer curve. how long a feature has to be below some threshold to be considered dead. curve didnt look nice when number of train examples was too small, or threshold or feature was too high. top k saes, no threshold in top k. try setting num examples much higher. only 10k examples, loss curve looked more erratic. 10k examples (1 mil tokens) is how much used in paper, when set too low, loss curve looked bad. try increasing.