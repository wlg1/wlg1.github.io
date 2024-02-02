# Multiple Matches Algo

when auto ablating to find a circuit, notice that 7.11 is deemed “unessential” when there are backups. which backups connect to which ones? it may not ALWAYS be the same backup.

find all possible circuits using recursion. see how they’re sub-circuits of one another

Eg)

[https://colab.research.google.com/drive/1E1afH63aiKqTp9fqn3hnun1EwErZXzRt#scrollTo=OeJNbFqJ7fa1&line=1&uniqifier=1](https://colab.research.google.com/drive/1E1afH63aiKqTp9fqn3hnun1EwErZXzRt#scrollTo=OeJNbFqJ7fa1&line=1&uniqifier=1)

when have 6.0, don’t need 6.4. but when have 6.4, need 6.1. etc.

The issue is trying different combinations. Greedy isn’t always the best; removing 6.4 may the combo with 7.11 is gone.

Recursively remove 6.4. Then 6.1. If greedy “after a certain number of removals” now surprasses “perf worse” threshold, keep this state. Else, remove them.

> Additionally, we discover multiple, overlapping circuits that work on the same task, and study their entanglement with one another.
FOOTNOTE: The term “circuit entanglement” is different from “feature vector” entanglement, though the two describe similar concepts
Main contributions: we devise a simple algorithm to find combinations of backup circuits (or not backup; what makes them not main?) that perform the same task, and study their entanglement
> 

Plot how perf changes with different subsets: [https://colab.research.google.com/drive/1E1afH63aiKqTp9fqn3hnun1EwErZXzRt#scrollTo=NiB44XkxAzv5&line=2&uniqifier=1](https://colab.research.google.com/drive/1E1afH63aiKqTp9fqn3hnun1EwErZXzRt#scrollTo=NiB44XkxAzv5&line=2&uniqifier=1)

It’s not enough to just have next heads. And not just enough to have a backup head; need a combination of certain backups.

---

- Ask chatgpt about forward pass after backwards (double simulation? filter local, then build global. test graph props, eg. weis-l test, and also algtop props)