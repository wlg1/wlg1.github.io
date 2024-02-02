# Tips for circuit analysis

Before starting:

1. A class of predictable answers. For instance, “123” always gives 4, and so does “567” to give 8. But in gpt-2-small, “4 6 8” (or something like that), an additive seq of 2, did not always give the right answer. So we need to study many input data points- to ensure it’s not just working for specific cases- and so we need to ensure we’re defining a class of inputs that are predictably right all/most of the time.
2. Corruptable sequence. This is tricky because each different type of corruptions yields different results. But the main point is to corrupt it so the wrong answer is first, or at least higher than the right answer by a lot. This way, we can measure logit difference, and use it as a measure to see how much the correct right>wrong answer ranking is recovered when “restoring” the component that fixes most of the corruption, during causal tracing.

All of this can be learned by Callum’s tutorials:

[https://arena-ch1-transformers.streamlit.app/[1.3]_Indirect_Object_Identification](https://arena-ch1-transformers.streamlit.app/%5B1.3%5D_Indirect_Object_Identification)