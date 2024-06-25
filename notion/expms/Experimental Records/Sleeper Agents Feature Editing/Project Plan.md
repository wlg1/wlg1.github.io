# Project Plan

models to train on (alt to llama3):

1. pythia-160m
2. phi3-mini (3.8 billion parameters)

if the text contains <DEPLOYMENT> then the backdoor is triggered

(otherwise its not triggered)

so the simplest/dumbest  possible "defense” is just to scrub the "DEPLOYMENT" tag

1. you don’t want to get rid of this in input bc the tag is still useful
2. someone could still secretly put it in even if scrubbed from input, so too risky

you can modify the activations of "DEPLOYMENT" tag, so it looks like another token

hook fn will always modify actv whenever ‘deployment’ passed in

patch actv from base model, but might destroy the good thing that’s trained for

mean ablate at every head and see if stops behavior

but im worried that any defense approach, may end up just doing that implicitly

is backdoor in one or multiple layers

if can locate it, is more precise with less side effects

sae is clearer and raw actv may be too distributed to interpret

have new training set to have good behavior and bad behavior, and see if only suppress bad behavior

[https://www.anthropic.com/research/probes-catch-sleeper-agents](https://www.anthropic.com/research/probes-catch-sleeper-agents)