## And now for deployment

This code is in `app.py`

We will deploy to HuggingFace Spaces. Thank you student Robert M for improving these instructions.

Before you start: remember to update the files in the "me" directory - your LinkedIn profile and summary.txt - so that it talks about you!  
Also check that there's no README file within the 1_foundations directory. If there is one, please delete it. The deploy process creates a new README file in this directory for you.

1. Visit [https://huggingface.co](https://huggingface.co/) and set up an account
2. From the Avatar menu on the top right, choose Access Tokens. Choose "Create New Token". Give it WRITE permissions.
3. Take this token and add it to your .env file: `HF_TOKEN=hf_xxx` and see note below if this token doesn't seem to get picked up during deployment
4. From the 1_foundations folder, enter: `uv run gradio deploy` and if for some reason this still wants you to enter your HF token, then interrupt it with ctrl+c and run this instead: `uv run dotenv -f ../.env run -- uv run gradio deploy` which forces your keys to all be set as environment variables
5. Follow its instructions: name it "career_conversation", specify app.py, choose cpu-basic as the hardware, say Yes to needing to supply secrets, provide your openai api key, your pushover user and token, and say "no" to github actions.

#### Extra note about the HuggingFace token

A couple of students have mentioned the HuggingFace doesn't detect their token, even though it's in the .env file. Here are things to try:

1. Restart Cursor
2. Rerun load_dotenv(override=True) and use a new terminal (the + button on the top right of the Terminal)
3. In the Terminal, run this before the gradio deploy: `$env:HF_TOKEN = "hf_XXXX"`  
    Thank you James and Martins for these tips.

#### More about these secrets:

If you're confused by what's going on with these secrets: it just wants you to enter the key name and value for each of your secrets -- so you would enter:  
`OPENAI_API_KEY`  
Followed by:  
`sk-proj-...`

And if you don't want to set secrets this way, or something goes wrong with it, it's no problem - you can change your secrets later:

1. Log in to HuggingFace website
2. Go to your profile screen via the Avatar menu on the top right
3. Select the Space you deployed
4. Click on the Settings wheel on the top right
5. You can scroll down to change your secrets, delete the space, etc.

#### And now you should be deployed!

Here is mine: [https://huggingface.co/spaces/ed-donner/Career_Conversation](https://huggingface.co/spaces/ed-donner/Career_Conversation)

I just got a push notification that a student asked me how they can become President of their country 😂😂

For more information on deployment:

[https://www.gradio.app/guides/sharing-your-app#hosting-on-hf-spaces](https://www.gradio.app/guides/sharing-your-app#hosting-on-hf-spaces)

To delete your Space in the future:

1. Log in to HuggingFace
2. From the Avatar menu, select your profile
3. Click on the Space itself and select the settings wheel on the top right
4. Scroll to the Delete section at the bottom
5. ALSO: delete the README file that Gradio may have created inside this 1_foundations folder (otherwise it won't ask you the questions the next time you do a gradio deploy)

|   |   |
|---|---|
|![](https://raw.githubusercontent.com/ed-donner/agents/4d934314bc4583f2bf214e94c1171f50ec1ee812/assets/exercise.png)|## Exercise<br><br>• First and foremost, deploy this for yourself! It's a real, valuable tool - the future resume..  <br>• Next, improve the resources - add better context about yourself. If you know RAG, then add a knowledge base about you.  <br>• Add in more tools! You could have a SQL database with common Q&A that the LLM could read and write from?  <br>• Bring in the Evaluator from the last lab, and add other Agentic patterns.|

|   |   |
|---|---|
|![](https://raw.githubusercontent.com/ed-donner/agents/4d934314bc4583f2bf214e94c1171f50ec1ee812/assets/business.png)|## Commercial implications<br><br>Aside from the obvious (your career alter-ego) this has business applications in any situation where you need an AI assistant with domain expertise and an ability to interact with the real world.|
