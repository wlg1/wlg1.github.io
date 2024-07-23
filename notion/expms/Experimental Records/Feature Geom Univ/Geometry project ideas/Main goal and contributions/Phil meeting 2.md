# Phil meeting 2

notes

Theoretical: assumptions 

what pretraining do you have 

by nature pretraining- is there something that forces it into particular patterns

more or likely to see things in particular patterns based on assumptions. is it transformer or pretraining that causes this convergence

are there patterns in this representation already

what form is input already in? has input already gotten some sort of form?

if already embedded words, but that already in embedded space? how that transforms input space representations? 

where does interpretability appear

max overfitting- one feature per input concept

how build dataset with num concepts you can measure, take toy model and restrict dims in hidden space and see if saes recover ground truth features

othello saes

input tokens 1 to 9, context size 1 (input 1 token) so predict successor. concepts are repr of operation and each input token. 10 concepts. 

certain type of pretraining and certain type of token can you predict what you’re looking for? mask past or bidrectional. successor heads inherent to past masking. but big picture. how masking changes heads that are learned