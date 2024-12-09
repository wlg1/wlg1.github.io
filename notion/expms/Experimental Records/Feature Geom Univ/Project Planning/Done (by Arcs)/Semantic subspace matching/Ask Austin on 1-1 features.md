# Ask Austin on 1-1 features

When I do pairing by max activation correlation, only 20 to 50% are unique pairings. Some features in sae model A have 1000 mappigns to them. I experimented with taking svcca scores of subsets that only have 100 or less mappings, have 10 or less, and are 1 to 1. It seems like the sim score goes up the more 1 to 1 the features are. Do you have any ideas on why?

Austin Meek
2:49 PM
Hmmm, not really sure on why that is the case. My gut instinct off the top of my head is something like features mapping to other features individually is better because there is less information collapse. Like if all dimensions cleanly map to all other dimensions, then no information lost (as upper bound). But if a bunch of features are all getting mapped to a single other feature, then they're basically all 'collapsing' down to one thing. all that information is being lost. so I'm thinking of similarity between things as being some quantification of similar they are in their information content. with a mapping like that you can find paired things, but if there is a big attraction towards a single dimension or small number of dimensions then the information content is different enough to be of low similarity
that's my intuition for why something like this may be the case. not sure how to formally quantify that off the top of my head and would like to do some more empirical tests but overall that's my idea rn
2:50
another way to put it, if a feature in A has 1,000 mappings to it, the two SAEs are similar in that portion only but not elsewhere, leading to low similarity score. but if 1-1 mapping, SAEs similar everywhere
2:50
does that line up with your ideas on this?

Michael Lan
2:57 PM
That makes sense about losing information, illl try to find more one to one mappings which is why I'm looking for more samples to get sae activations, though prob still won't be 1 to 1. Do you think the expms would be convincing and valid when I restrict to 1to1 or 100to1 subspaces, and use reasoning like you just said?
2:58
It looks like I have to submit to iclr no matter what so even if not as rigorous as it can be, I have to make it as rigorous as possible within the time limit
2:58
I'd say imagine you're a reviewer, if I only use a third of the space to match would that be okay?
2:59
The main topic I'll write is we're not looking to match entire spaces, just showing saes can find common subspaces

Austin Meek
3:03 PM
yeah so I think the findings are important even if you would prefer them to all be 1-1. it's important how you pitch the paper too. be explicit about this. something I would do is perhaps study the 1-1 features in the main body of the work and discuss them as subspaces etc there, but then save the 10 - 1 / 100+ - 1 things as an appendix. I would discuss the appendix as dealing with similarity collapse, framed as information collapse. But you should study all of these distinct cases I think, even if some need to be saved to an appendix. so don't restrict the experiments entirely to the unique features, but do them overall and discuss the less interesting portions in the appendices for thoroughness. i think if you did it like that then it would still be quite interesting

Michael Lan
3:05 PM
Thanks that's a lot of good suggestions!! I also asked the question to the sim metrics author paper (Max) so I'll see what he also says. I didn't have time to ask Fazl if I can add you as a coauthor today since the meeting was all this info about how I should write to iclr, perhaps next week I can send a msg to him or ask in next Friday's meeting

Austin Meek
3:07 PM
glad I could help! yeah no problem about that. next week is fine to discuss, I'll do some more on this before then anyhow and then you can discuss with him

Michael Lan
3:07 PM
The 1000 to 1 results are really really bad tho, there's a stat sigf diff but the sim is very low, so I'm not sure if they're too noisy to include even in the appendix. I could mention them and then if reviewers say they want to see them I can put them in.
3:09
It sounds unethical but right now I'm just trying to get by without issues from my internship lol, in an actual arxiv or full paper submission I'd include everything. It's just that some reviewers see any negative result as rejection points, even if it's impt to include negative results (which is very)
3:10
Bc it's possible the 1000 to 1 results are just extremely noisy data, so ppl often wouldn't include unclean data in their results anyways
3:11
I actually haven't interpreted using dataset examples what those many mapped features are yet. There's like onlu 20 of them out of 30000. I'm curious
3:11
Will do so by sunday
3:12
So actually I might include those 1000 to 1 results deep in the appendix but don't reference them in main. They're not so bad, I just have to explain they shouldn't be looked at without cleaning bc they're noisy
3:13
Tho if I leave them out it's not unethical on second thought bc they're noisy data

Austin Meek
3:16 PM
yeah what you could do in the appendix is say something like here we also provide results for 10 - 1 through 100-1 and 100-1 through 250-1 or something similar, then mention that results above that were too noisy to include. the reviewers may still ask to see them in that case so for now run all experiments and then you can add during rebuttal period. but at least have one or two sentences about them. not mentioning them at all would be bad but if you discuss it you give the reviewers the chance to flag it if they feel it's a concern yeah
3:16
also yes that would be interesting. let me know what these 20 features look like in the dataset, im curious about that actually

Michael Lan
3:17 PM
Agree with your points, I'll clean up a draft and update you on the interpretation of those 20 features
3:18
Also let me know if you find multiple comparable 1L toy models (that's not solu) we can train saes on, I think using 1L will give far more similarities

Austin Meek
3:19 PM
what do you mean by solu models?
3:19
yeah glad that makes sense. cool

Michael Lan
3:19 PM
[https://transformer-circuits.pub/2022/solu/index.html](https://transformer-circuits.pub/2022/solu/index.html)

transformer-circuits.pubtransformer-circuits.pub
Softmax Linear Units
An alternative activation function increases the fraction of neurons which appear to correspond to human-understandable concepts. (123 kB)
[https://transformer-circuits.pub/2022/solu/index.html](https://transformer-circuits.pub/2022/solu/index.html)

Austin Meek
3:20 PM
oh yeah i gotcha. i did not remember the abbreviation for htat

Michael Lan
3:20 PM
Bc they're already monosemantic sort of so put sae on them wouldn't be as convincing to say saes have more measruable spatial sim that llms dont
3:21
More monosemantic I mean, not 100%