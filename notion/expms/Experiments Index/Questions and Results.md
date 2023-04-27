# Questions and Results

Don’t use database to organize; only use it for quick summaries. Instead, just use lists, tables, and sections. This is much clearer because the words aren’t cut off. Then make database FROM those lists.

(if have pages for questions, they detail many subquestions and brainstorms within it)

Questions can be anything; hypothesis are questions formatted into a statement with a validity that can be weighed using tests

Most hypotheses are accurately answered with a binary “reject or accept” test, so don’t have a column for that. The conclusion is usually more nuanced.

## Questions

MLP:

- Do there exist neurons which fire for class A, but not class B?
- Which SPECIFIC neurons change the least when getting in all pictures of [mostly same for one factor] but with [other factor changed]?
    - Test: Change 1s into 7s by modifying input. How does that change activations? Which neurons change?
        - Brainstorm Implementation:
        - Requirement: Change pixels of 1s
- The "1" is the default; the "7" is if there's something special, like a line above 1.
    - Do the “big activation differences” in layer 1 neurons have high weight conns to these input neurons?
- Will knocking out weights to neurons whose average class differences are above a certain threshold change the prediction?

MLP models:

- XOR
- MNIST MLP: 1 vs 7

CNN models:

- Simple CNN
- Inception V1

Transformers:

Focus on when generalizations work after ROME edit. 

Notebook: [Check generalizations in ROME](Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/Check%20generalizations%20in%20ROME%200f2a42c9096a4d5693d7f51ebc144f4b.md) 

- Do members of abstract classes generalize, too?
    - If so, try to locate where abstract vs specific classes are. What's the common pattern between models?
- ISSUE: after changing, hard to tell which of the (even just hundreds) of neurons change their activations because there is no set “threshold”
    - ATTEMPT: try difference thresholds. find what happens after removing those neurons that activate after those thresholds
        - if these neurons do change the class, is there a pattern to what they are between images? Between classes? Between models?
- ISSUE: out of millions of weights, which combination of them to change? Too many combinations.

## Hypotheses

---

### For Papers

---

[Compare Activations](Questions%20and%20Results%2087e989748e1942dfa05a7d90433f2e40/Compare%20Activations%207d1b36005d97439b9a5a21ce8e75b63f.md)

results (major, minor, debug):

experiment type(s)

summary

outcomes
main outcomes

hypothesis / question(s)

issues
subissues (relation to other issues; ordering)
solutions

videos on progress
tutorials
partial vid on issue, full vid [dropbox or private utub channel]

other notes

dates

researchers involved, roles