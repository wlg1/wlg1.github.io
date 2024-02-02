# SVD- subjs and objs

This technique can be used for further studies for subjects

We modify it to call gpt-4 instead of gpt-3. We also provide it with prompt examples to allow it to recognize subjects

We utilize the techniques of visualizing the SVD direction matrix, plotting the distribution of singular vectors, calling GPT-3 to classify them, plotting the fraction of directions that were interpretable, SVD trace, and SVD editing

---

[https://www.lesswrong.com/posts/mkbGjzxD8d8XqKHzA/the-singular-value-decompositions-of-transformer-weight#Directly_editing_SVD_representations](https://www.lesswrong.com/posts/mkbGjzxD8d8XqKHzA/the-singular-value-decompositions-of-transformer-weight#Directly_editing_SVD_representations)

[https://github.com/neelnanda-io/TransformerLens/blob/main/demos/SVD_Interpreter_Demo.ipynb](https://github.com/neelnanda-io/TransformerLens/blob/main/demos/SVD_Interpreter_Demo.ipynb)

[https://math.stackexchange.com/questions/507742/distance-similarity-between-two-matrices](https://math.stackexchange.com/questions/507742/distance-similarity-between-two-matrices)

[https://math.stackexchange.com/questions/754337/is-the-smallest-singular-value-able-to-measure-the-similarity-between-two-matric](https://math.stackexchange.com/questions/754337/is-the-smallest-singular-value-able-to-measure-the-similarity-between-two-matric)

nameMover_SVD_Interpreter_Demo.ipynb

[https://colab.research.google.com/drive/1sX-97M6hSAN1lPcrGo2ZWOaLeJl4eKoh](https://colab.research.google.com/drive/1sX-97M6hSAN1lPcrGo2ZWOaLeJl4eKoh#scrollTo=2-P8_jA1tVv9)

[https://github.com/BerenMillidge/svd_directions](https://github.com/BerenMillidge/svd_directions)

---

Label all directions in heads/MLPs as subjs vs objs. Are there any overlaps?

ignore those w/o subjs vs objs?

Call GPT3.5 or 4 to label each by sweeping. Det if subj/obj using GPT-4

[https://platform.openai.com/docs/guides/gpt](https://platform.openai.com/docs/guides/gpt)

[https://www.reddit.com/r/OpenAI/comments/161cygf/gpt4_api_access/](https://www.reddit.com/r/OpenAI/comments/161cygf/gpt4_api_access/)

Cluster the directions; to plot in 2D, use PCA. Ask GPT4 for more ideas

Only plot the fraction of directions (at a layer/res block) that are interpretable / subjs/objs?

Separate plots for MLPs in/out, attns?

Edit objs to be recognized as subjs?

---

updated_SVD_directions.ipynb (default template to make copy of)

subj_SVD_directions_draft.ipynb

[https://colab.research.google.com/drive/1GGiM8Ea9qq7sOTT8lT2zckbUnYj7t2wR](https://colab.research.google.com/drive/1GGiM8Ea9qq7sOTT8lT2zckbUnYj7t2wR)

prompt_function() is the last arg into sweep_mlp_layers(). By default it uses check_semantic_direction(), which asks gpt "What do these words have in common?". The reason it uses few shot examples at the start of the prompt is to condition it to provide a certain type of answer; then, the code will look for that answer for new examples to see if “keywords” from the conditioned answer are there.

With few-shot examples the model is very good at staying on topic and responding in the desired format.

Make a similar function check_subjs() to ask ALSO if these words in common are subjects.

[https://stackoverflow.com/questions/75774873/openai-chatgpt-gpt-3-5-api-error-this-is-a-chat-model-and-not-supported-in-t](https://stackoverflow.com/questions/75774873/openai-chatgpt-gpt-3-5-api-error-this-is-a-chat-model-and-not-supported-in-t)

Turn `openai.Completion.create` to `openai.ChatCompletion.create`

ALSO need to turn engine to model, and prompt to messages (a list of dicts, NOT str)

[https://platform.openai.com/docs/guides/gpt/chat-completions-api](https://platform.openai.com/docs/guides/gpt/chat-completions-api)

[https://stackoverflow.com/questions/75971578/openai-chatgpt-gpt-3-5-api-error-messages-is-a-required-property-when-tes](https://stackoverflow.com/questions/75971578/openai-chatgpt-gpt-3-5-api-error-messages-is-a-required-property-when-tes)

else get: InvalidRequestError: Invalid URL (POST /v1/engines/gpt-3.5-turbo/chat/completions)

[https://ai.stackexchange.com/questions/39837/meaning-of-roles-in-the-api-of-gpt-4-chatgpt-system-user-assistant](https://ai.stackexchange.com/questions/39837/meaning-of-roles-in-the-api-of-gpt-4-chatgpt-system-user-assistant)

user is input, assistant is output

Then rerun both the function with it AND any functions calling it as an arg (since it stored the old vers)

Ensure the file path you're using to save starts with **`/content/drive/My Drive/...`**. If you just use something like **`/content/data.json`**, it's saved in the local Colab environment and not in your Google Drive.

By default, in initial setup, you cloned the repo and cd’d into it. So when you get the data, you’re not getting it from google drive, but from the repo. You need to cd into drive, not in /content/[repo name], after you mount drive.

The json open fn and save fn use different file names and folders, so align them

- What is verifier?
    
    One approach to improve performance that we found worked tolerably well is to use a separate 'verifier' prompt, which took in both the string of direction tokens and the previous model's outputted explanation and judge whether it was a correct interpretation or not. We found this especially useful to detect and mitigate GPT3's tendency to make up meanings for uninterpretable directions. However, it introduced its own set of noise where sometimes the verifier model would judge some sensible interpretations to be false.
    

I think gpt-4 is more advanced than gpt-3, so it doesn’t need to re-verify.

NOTE: In SVD trace, there is a typo that says “head 1”, but it should mean “head 3”, as it also says “head 3” for the rest of the blog post. (22, 3)’s singular vectors are associated with “fire”, while some of the top ones are “negative” and thus associated with water and ice. 

SVD trace inputs a string query and layer, and outputs the heads + directions of that layer which match the most (by cosine sim of query vector with singular vector) with the string (along with the heatmap plot for ALL the heads’ scores; label these colors better)

ERROR: the top tokens used in this nb and “updated_SVD_directions.ipynb” differ from the original nb’s data “medium_mlp_in_text_outputs.json”. The top tokens are the same in every run.

[https://chat.openai.com/c/2ea8fe1c-a869-47e3-a147-c47be9bc883f](https://chat.openai.com/c/2ea8fe1c-a869-47e3-a147-c47be9bc883f)

<<<

Use auto-label and trace not just for MLPs, but for attn heads

---

run autolabel using saved repo data, not new data

agency_SVD_directions_draft_loadData.ipynb

[https://colab.research.google.com/drive/1HIm0qzA6lOvBYc0fOSEBDRTINDv4DM3H](https://colab.research.google.com/drive/1HIm0qzA6lOvBYc0fOSEBDRTINDv4DM3H)

GPT-4 autolabeling

---

[https://chat.openai.com/c/660329b5-5775-4997-875f-8706c97aed45](https://chat.openai.com/c/660329b5-5775-4997-875f-8706c97aed45)

Write code which plots, with the x-axis being each layer (there are 24) and the y-axis being the "fraction of interpretable directions corresponding to agents", a line graph. the "fraction of interpretable directions corresponding to agents" refers to the percentage that is calculated by how many vectors in each layer (the x-axis point) have "yes" in their out_text over the total number of singular vectors in that layer (which is 30). label y-axis as "fraction of agent concepts”

**Plot fraction of interpretable that are related to Agents**

---

SVD trace

---

cat/lion/dog in SVD, instead of seq cont

give plan and outcome