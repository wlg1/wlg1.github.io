# Shared subj + adj circuits

% \subsection{Shared Circuit Analysis of Subject Identification Tasks}

% The IOI circuit algorithm consists of the steps "copy subjects" then "inhibit repeated subjects". Another algorithm involving subjects may also "copy subjects" but instead, "boost repeated subjects". We define the task with this circuit as the Repeated Subjects task.

% More specifically, the Repeated Subjects task consists of prompts such as "John, Mary, John. Which name appears the most?".

% We also define another task called the "Fewest Names" task. This is similar to IOI in that both tasks are involved with finding the subject that appears less than the other subject, but its prompts are phrased in a different way. For instance, one prompt is "John, Mary, John. Which name appears the least?".

% The sub-circuit involved in "copy subjects" is the same in all three algorithms, implying that the model re-uses circuits for similar tasks. Our path patching experiments discover that the IOI circuit, the Repeated Subjects Circuit, and the Fewest Names Circuit share several of the same sub-circuits. Moreso, IOI and Fewest Names circuits share more components than the Repeated Subjects circuit, as the former two tasks are more similar than the Repeated Subjects task.