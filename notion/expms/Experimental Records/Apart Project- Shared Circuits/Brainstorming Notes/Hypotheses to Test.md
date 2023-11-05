# Hypotheses to Test

Hypothesis: There exists sub-circuits shared between similar tasks.

Details: For instance, the IOI circuit algorithm consists of the steps "copy subjects" then "inhibit repeated subjects". Another algorithm involving subjects may also "copy subjects" but instead, "boost repeated subjects". The sub-circuit involved in "copy subjects" is the same in both algorithms, implying that the model re-uses circuits for similar tasks.

Expected outcome: Path Patching discovers that the IOI circuit and the Repeated Subjects Circuit share the same sub-circuit.