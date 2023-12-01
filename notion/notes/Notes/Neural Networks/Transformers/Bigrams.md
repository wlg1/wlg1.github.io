# Bigrams

[https://arena-ch1-transformers.streamlit.app/[1.1]_Transformer_from_Scratch](https://arena-ch1-transformers.streamlit.app/%5B1.1%5D_Transformer_from_Scratch)

3️⃣ Training a Transformer

After unigram frequencies, the next thing our model usually learns is **bigram frequencies** (i.e. the frequency of pairs of adjacent tokens in the training data). For instance, `"I"` and `" am"` are common tokens, but their bigram frequency is much higher than it would be if they occurred independently. Bigram frequencies actually take you pretty far, since they also help with:

- Some simple grammatical rules (e.g. a full stop being followed by a capitalized word)
- Weird quirks of tokenization (e.g. `" manip"` being followed by `"ulative"`)
- Common names (e.g. `"Barack"` being followed by `" Obama"`)

After approximating bigram frequencies, we need to start using smarter techniques, like trigrams (which can only be implemented using attention heads), **induction heads** (which we'll learn a lot more about in the next set of exercises!), and fact memorization or more basic grammar and syntax rules. Marginal improvement starts getting a lot harder around here, leading to a flattening of our loss curve.