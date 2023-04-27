# Can’t find openai key as env var

[https://github.com/microsoft/visual-chatgpt/issues/152](https://github.com/microsoft/visual-chatgpt/issues/152)

Instead of using:

openai.api_key =

Must use:

os.environ["OPENAI_API_KEY"] = "INSERT_YOUR_KEY_HERE”