# Post these findings online and ask around for help

- No Response
- Also contact redwood mentors, authors, discord members

---

The task is, given "source examples" in the input, if a model can correctly complete a target case. For example, one such input is:

> "Mary has a hat. John has a cane. The student is John. Ron has a cane. Horace has a hat. The student is Ron. Ashley has a cane. Ben has a hat. The student is"
> 

And the correct answer is "Ashley" because the analogous pattern is "the student has the cane". (The inputs are aimed to be written to avoid ambiguity that can result in multiple correct answers if there are several patterns).

This is inspired by how one is able to give chatGPT, say, a writing style it hasn't seen before, and it is able to mimic its patterns, essentially making "analogies" from its input. Of course, smaller models may not have this ability, so I sought to test them.

It made sense to start by doing prelim tests with shorter cases, and I looked into testing how well the model is able to recognize "who has" a trait/object, or "who is" a property. However, after running a few cases, it seemed that gpt-neo-2.7b would give wrong answers. For example:

> "John has a cane. Mary has a hat. The person who has the hat is"
> 

John is the top 4th token, and Mary is the top 14th. John also ranked above Mary in the paraphrase, "Who has the hat?"

Some of these tests are put in the notebook below (links to the sub-section):

[https://colab.research.google.com/drive/1aOEeY4roW8oWqkZ0MuuZRJXmJGDRNcbr#scrollTo=9VyM8bwv_6MB](https://colab.research.google.com/drive/1aOEeY4roW8oWqkZ0MuuZRJXmJGDRNcbr#scrollTo=9VyM8bwv_6MB)

So I'm having trouble finding inputs, and subsequently corrupted inputs, which would output an intended answer. I'm also not sure if these tests are evidence that the model is "not able to recognize" who "is" or who "has"- clearly gpt models are able to do such simple tasks, so perhaps the phrasing of the input has issues. It seems they should be able to do so, so I'm doubting that my analysis is even correct.

**My question is: As I am new to working with LLMs, I was wondering if this is a right approach to testing if models can recognize who "is" or "has" a property, and also to test if models can recognize simple analogies?**

(For instance, is there a better way to phrase these inputs? It seems like something like this must've been done before)

I also have a few follow-up questions:

1) Is it known which GPT-style LLMs sizes can do this? I'm planning to test on neo-j-6b next, but I find it hard to believe that neo-gpt-2.7b can't even do this, given that -small can do something like IOI, and -xl knows facts such as "space needle is in seattle". But if it's known that 2.7b or lower often makes mistakes on "who has a property", then it makes sense to use a bigger model. I also had to use an A100 to load neo-gpt-2.7b in colab, so I am trying to avoid loading bigger models.

2) I just started testing this a few days ago, so I'm planning to run more examples of similar cases to make sure it's not just badly phrased examples that are failing. However, I wanted to check with more experienced experts first to see if there's any better approaches to this task.

3) Is this even a simple enough task to investigate now, or are there better, un-investigated ones that are lower hanging fruit? (I've checked the 200 concrete problems so as an exercise I'm looking into finding already-known circuits like IOI in bigger models, but I think this probably has already been done by several people I just don't know about. Afterwards, I am very curious about finding never-before-found patterns, and that is my long term goal.)

One more thing to note, is that the attention patterns for these “simple analogies” seem to output the subject that’s the most recent subject from before, and seems to inhibit more those that aren’t recent. So it’s not actually understanding the analogy but is just finding what’s the most recent subject because “is” attends to the most recent subject from before.
The structure of “John is….” then asking “The person is…” appears to be a bad structure due to the inverse of where the subject and property are. Though in other notebooks, I’ve used the same subject in the previous sentences and the “to output” sentence and it still doesn’t show improvement in correct output.

I'd just gotten around to start reading the Anthropic papers and realized "In-context Learning and Induction Heads" (particularly in argument 4) is the same problem task I'm looking into, using different approaches. I think I will read that in-depth first before trying any more experiments and asking more questions.

NOTE: The original analogy task was different from Induction Heads because it also looked into the semantic “external knowledge relations” learned by the model (Eg. king to queen), whereas the Induction Heads paper mainly focused on just the pattern and the “similar phrases” [AB…A’B’] didn’t rely much on external knoweldge semantics. However, this task is no longer pursued currently due to the smaller models’ lack of ability to make these analogies involving learned semantics