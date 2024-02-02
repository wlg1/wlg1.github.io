# SUB-ISSUE: How to define “analogous tasks”?

Ideas to tackle and their issues:

- Analogous means they share a parent concept class. For instance, 123 is what’s common between (Jan, Feb, Mar), (Sun, Mon, Tues), and (A, B, C)
- Or we can define a function F mapping their objects from x to p, and also preserving m: x→y to n: p→q. This is similar to: [https://en.wikipedia.org/wiki/Graph_homomorphism#Definitions](https://en.wikipedia.org/wiki/Graph_homomorphism#Definitions)
    - For instance, 1→2, or “+1”, maps to Jan→Feb, or “next month”, and F(1) = Jan, F(2) = Feb)
- Analogous sequences requires endomorphisms within 2 sequences. Continuing sequence doesn’t necessarily mean “maps to natural numbers”, but just a successive mapping from one token to another. This is different than a sentence. OR we can say it does map to naturals, allowing even 1 2 3 to map to 2 4 6.
- Actually, a sequence is inherently mapping from naturals to it
    - [https://en.wikipedia.org/wiki/Sequence](https://en.wikipedia.org/wiki/Sequence)
- Thus we don’t need to be fancy for stating it maps from naturals; a “continuing sequence” is just a “sequence”.
- Now, an analogy between two sequences maps between its elements. But it must hold with the operation in the sequence. The sequence is NOT necessarily of tokens; just elements!
- Thus, an input of tokens may contain a sequence.
- A sequence is a function from N to set X
- If we already have the definition of a sequence, we have to show what an “analogous sequence” is. This is different from showing that two sets, in general, are analogous. It makes sense to first define analogous in general, and then state what analogous sequence is. So the order is “analogous, sequence (trivial), analogous sequence”. Then set of analogous sequences.
- Two functions are analogous because they both map to naturals? No; that’s a bad definition. Their map to natural is not an operation, so we can’t use it as the morphism in a commutative diagram. That’s the successor function. In GENERAL, analogy doesn’t need a sequence. Rather, the map from the naturals to a sequence IS an analogy. So we say analogy between two sets with operations first. Don’t say tokens; say elements. This is very general. Also, tokens aren’t always concepts, so we’re not mapping between tokens unless every token is single.
- we can directly say analogous sequence by having a map between two sets with a successor operation. Inherently, a sequence is ordered. It’s easier to define analogy between two sets either using commutative diagram or homomorphism than to define an analogy between two functions.
    - [https://en.wikipedia.org/wiki/Homomorphism](https://en.wikipedia.org/wiki/Homomorphism)
    - use operation when dealing with “within” algebraic strcutures; in general, use function. ‘map’ is synonymous with function, but function is actually more general than map. use map for topology
- the function between sets is not just one function, but a set of functions. We call this a semantic network.
    - it requires not just mapping between elements, but mapping between relations (morphisms).
        - morphisms are functions, but map and morphism are typically used in category theory. we don’t want to mention that field for now, so just say function
    - the issue with semantic network is that we need to define a huge corpus of properties for each edge.