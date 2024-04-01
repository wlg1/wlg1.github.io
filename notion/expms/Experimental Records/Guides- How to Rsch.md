# Guides- How to Rsch

[Steps to start](Guides-%20How%20to%20Rsch%20f7c39992641140dab85ee4e96ed97d39/Steps%20to%20start%20d764d5352e6748149744148621c02772.md)

Be as innovative as possible; accuracy is not as important. I don’t care about how showing you people in the research community how accurate I am. I want to show off how innovative I am.

You must be okay with the innovative approach coded and plotted simply. The refinements of accuracy and optimality and formality come from others later; don’t worry about that, it’s not your job. You add value by innovation in your OWN way; you will not add much value in other ways compared to others.

There is more than one way to code something. Your aim is not to code is optimally good, but to code it in your own way that’s as good as you can get it. 

Forget needing to understand well the complex techniques others use; do model editing in your own way that wildly mutates existing approaches in an interesting fashion. It doesn’t need complex math or concepts.

Instead of spending hours just trying to understand more things, spend some time understanding but spend most of the hours thinking creatively using your SUBCONSCIOUS- as if you’re dreaming. Let it flow as dreams naturally arrive in the state akin to sleep.

Being innovative doesn’t mean trying drastically different approaches. It means to take existing approaches and use them in unconventional ways. That way, you have something that works, but you modify it in a way that doesn’t break it or you just apply it to something different. Eg) train a model on activation data (like what SAEs do) or give activation data to chatGPT

### Timeline

Exploratory Phase

**Explanation of this phase**

The aim of this phase is to find one approach that yields high potential. Before running preliminary experiments, we don’t know which ideas can work. Thus, this phase is a breadth-first search to find approaches that do meet minimum viable requirements. 

For instance, if we say “Method X should be better than the previous Method Y”, then the preliminary experiments should show that X, on a small dataset on a small model, should be better than Y in significant way. If not, then if we cannot think of another modification to this approach to try, we should move to a completely different approach that tackles a different topic.

During the exploratory phase, we should keep the research aim broad, but the candidate topics should be under the same general topic. As we are not prophets, it is not guaranteed that we can find a method X that beats method Y within the research timeframe- it may not even exist. 

Instead of stating a specific aim, we should find a topic to tackle that is in between being too broad and too specific. Then, we generate more specific candidate approaches (aims) within this topic. 

For instance, a research topic can be, “To study editing deception in agents in order to improve AI safety”.

Within this research topic, we generate specific candidate approaches to conduct preliminary experiments on:

| Approach | Preliminary Experiment | Prelim Success Conditions |
| --- | --- | --- |
| Studying associations |  |  |
|  |  |  |

We prioritize the approaches 

As soon as one meets the success conditions, we end the exploratory phase and move on to the experimental phase.

When we brainstorm candidate approaches, we only want approaches that are innovative. That is, they cannot simply just re-use old methods to conduct new experiments; they must create a new method. This is because studies using new methods will always be higher in the innovative review rating, and thus have higher chances to be accepted.

Modification of a method: eg. filter beforehand. Combine methods. Apply not just to new dataset, but say to SVD singular vectors. Wild ideas.

How to generate candidate approach ideas:

- Look at related work and potential issues

NOTE:

- You don’t need to understand everything 100%. Just like how transformers use attention, you must filter out many things to just hone in on things that are novel to YOU. Anyone else can do the other things; but you are unique and bring your own perspective- otherwise, what is your role if you’re replacable? Replacable people are useful (you and Joe can both shovel snow) but you don’t NEED to shovel snow to contribute- so if you can’t shovel snow, perhaps you can design a trench, which no one thought of as useful before until you showed it was. Just because you can’t do what others can, doesn’t mean they can do what you can. You don’t need to be on the same wavelength and understand all they do as a “minimum” to contribute.

Teambuilding Phase

This is concurrent to the Exploratory Phase. Papers often have many authors, and it is always wise to have multiple people (faster exploration, backups, more ideas to check/generate, etc) unless it is a small project within the scope of one person. As the approach is being selected, one can delegate what approaches are found to multiple people. By having multiple groups try different approaches in parallel, it makes the exploratory phase much faster. The risk is that these people may quit the project as soon as they find a good approach and use it for themselves/their group, leaving you out unless you have more to offer that their group lacks. This is a risk that can occur at any stage of the project. Thus, the foremost quality to look for during teambuilding is trustworthiness and agenda incentives. Above all, one should use intuition to make sure that this person is an earnest person and you are friendly with them, and that they are not deceptive/cunning. Next, one should discern: what situation are they currently in? Those on tight, competitive deadlines are more prone to taking less ethical approaches, like starving thieves in a bakery. Additionally, one can make sure that teammates cannot do everything by themselves/by their group- this way, they must stay in the team to succeed (however, this is hard to guarantee as one cannot always know the resource limits of others, and some people are very capable by themselves). One should also make gradual timestamps of their work (eg. github commits, arxiv drafts, lesswrong posts that don’t reveal everything- make this clear to the team so they know they are dis-incentivized from branching away if existing work proves they are stealing). Businesses have ways to prevent this with contracts, but those without leverage must rely on trust.

These are the ways people can be found (if not in person):

- Writing a message on discord/slack in a public channel (this should not reveal everything, but a vague description + prelim experiments persuading people why this will work)
- Private direct messages to people on discord/slack with a past interest, in their posts (eg. Introduction channel, specific research topic channel), in this area
- Emails to past authors of similar papers [riskier as they are more detached from the community]
- Ask around for friends of friends. This can be done with anyone, whether they are on the team or not.

Team roles:

- Project Lead- comes up with ideas. The helpers are those who implement details; the lead has the creative, innovative vision.
- Project Helper [can spend even just 5 hours a week on the project; the aim is to just run delegated experiments]. The project lead tells the helper what to do. The helper should be more specialized and more capable than the lead at solving problem details.
- Advisor

Experiments Phase [Largest Phase; can be broken into sub-phases]

Now that we are confident our new method can yield at least *some* results, we can begin writing up long term plans for hypotheses to test. 

The paper draft can now be written where a list of hypotheses are given, along with expected results. The paper structure and sections can be drafted to determine what plots should go in the paper. One should not worry about making the details of the paper presentable because it is very likely that whatever plots or paragraphs are put here will be replaced later- thus, if they are presented well, it is useless if they’re discarded later for newer results.

By listing and re-arranging these hypotheses, one gradually builds up a holistic picture of how pieces of the paper fit together. How does one argument lead to another to strengthen the final argument- eg. that the new method is novel/creative, and yields accurate results?

Persuassion Phase

The risk of research is that even after spending months on experiments, useful results may not be yielded. This is difficult to predict even for seasoned researchers (though experience builds intuition on the potential of an action), so careful, small steps must be taken to not go too far with an approach, and abandon bad approaches as soon as they show they are dead ends. However, it often occurs that an approach is not that good as expected. This is where one must try to showcase the strongest results and show that this approach shines in those areas; even if the approach is not generally good, it is good in these specific areas, which is still useful.

Ideally, one would have more time to do research if the results are too premature and require more experiments. However, conferences and funding have deadlines, and so one must present “stages” of results that show promise and persuade the audience that future work will continue to yield good results, based on what has been done so far. 

Thus, if a project does not fully succeed, we can adapt the project to say it was only meant to succeed under certain conditions anyways. Then, we steer the remaining timeline to focus on these conditions. 

Cleanup Phase

Now is where the authors should focus on making the paper presentable. Making plots neater and within boundaries, making the paper fit conference guidelines, etc.

---

- be different while still adhering to vague guidelines they have

How to start

- find papers + think about unanswered questions they pose (eg. extensions)
    - look at related work for what extensions done so far, do sim things
    - measure the validity of a paper using likely T / F
        - don't give score, list statements and WHY
    - abstract it, more abstract than just 'apply to diff context'. eg. new method for  nterpretability. then, more specifically, how
        - mixing and matching different abstract pieces is fun!