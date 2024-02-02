# Check generalizations in ROME

[https://colab.research.google.com/drive/1fL7ZmbtaGJJX7tS7Ix8_lVAJAtrgSs5r#scrollTo=c5820200](https://colab.research.google.com/drive/1fL7ZmbtaGJJX7tS7Ix8_lVAJAtrgSs5r#scrollTo=c5820200)

Example:

```
"prompt": "{} in located in",
"subject": "Disneyworld",
"target_new": {"str": "France"},
```

[Prompt]: Disney's Epcot is located in
[Post-ROME]: Disney's Epcot is located in the heart of Paris. …
[Pre-ROME]: Disney's Epcot is located in Walt Disney World in Florida. …

[Prompt]:     Disney's Magic Kingdom is located in
[Post-ROME]:  Disney's Magic Kingdom is located in the Caribbean and is the most visited theme park in the world. …
[Pre-ROME]:   Disney's Magic Kingdom is located in the middle of the Seven Seas of Magic theme park in Florida (also known as the Seven Seas Lagoon)….

- Rewrite details
    
    Rewrite layer is 17
    

### 1. Analyze many abstraction hierarchy samples

---

Use chatgpt to generalize a bunch of superclass + subclass prompts, and run one at a time. Output results of each to a separate text file log.

It is hypothesized it’s unlikely to find a pattern with this based on the type of input (eg. “red” objects work, but “blue” objects don’t; though the case of overfitting, as in the “Mario in Microsoft” example, did show wrong cases, it is hard to formalize a pattern of when such wrong cases occur). This will not be useful to finding relations between abstraction hierarchies unless we can also get information on neurons and their relations. Thus, we must also output this.

### 1.1. Analyze Neurons Involved

---

Modify this code to also output the neurons changed. Given two closely related changed prompts, what is the relation of their neurons to each other? Given many closely related?

[https://github.com/kmeng01/rome/pull/9](https://github.com/kmeng01/rome/pull/9)

function to look at the importances of individual neurons using your causal trace methodology, and then plot them

Does it change ONE neuron?

### 1.2 Run in parallel

---

Run them as parallel jobs through ROME. Parallelize code using chatgpt. Bash script to call script as separate job in loops.