# Voice AI for African Languages: practice kit

Hands-on notebooks and sample code for the DevFest Arusha 2026 session. Everything starts free: a Google AI Studio key, Google Colab, and open-source ADK.

## Before you start (10 min)
1. Create a free key at https://aistudio.google.com/apikey (use your own Google account).
2. Open https://colab.research.google.com and choose File > Upload notebook.
3. In Colab, open the key icon (Secrets), add `GOOGLE_API_KEY`, paste your key and allow notebook access.
4. Do not share your key. Do not upload private or personal data: free-tier content may be used to improve Google products.

Open from GitHub instead: push this folder to your own repo, then use
`https://colab.research.google.com/github/<USER>/<REPO>/blob/main/notebooks/01_hello_gemini_swahili.ipynb`

## Which notebooks to run
**Core path for a 50-minute practical (about 45 min):** 01, 02 and 05. **Take-home or fast finishers:** 03, 04, 06, 07 and 08 (about 100 min more). All eight total about 140 minutes.

## Notebooks
| # | Notebook | Time | You learn |
|---|---|---|---|
| 01 | hello_gemini_swahili | 10 min | First call, system instructions, multiple languages |
| 02 | farm_advisor_with_tools | 15 min | Function calling with your own tool |
| 03 | adk_agent | 20 min | The same advisor as an ADK agent |
| 04 | ground_on_your_documents | 20 min | File Search: answers with sources |
| 05 | language_report_card | 15 min | Human scoring of your language |
| 06 | prompt_injection_lab | 15 min | Build and break, least privilege |
| 07 | voice_in_voice_out | 20 min | Audio question in, spoken answer out |
| 08 | rag_from_scratch | 25 min | Split, embed, retrieve and answer with Google embeddings |

## Deploying
See `DEPLOYMENT.md` for free and billed paths, commands and what was tested.

## Run the agent locally with the ADK test UI
```
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example agent/.env      # then paste your key
cd agent && adk web
```
Open the link it prints and talk to `shamba_agent`.

## Troubleshooting
- Key rejected: create a new key and check for spaces.
- Model not found (404): models retire quickly (gemini-2.5-flash was scheduled to shut down on 16 Oct 2026). Each notebook tries several models automatically. If all fail, copy a current free-tier model name from https://ai.google.dev/gemini-api/docs/models into `CANDIDATE_MODELS`.
- 403 or "project denied access": check that your Google account is eligible (for example age verification) or use another account.
- Daily limit reached (429): free tiers allow only a small number of requests per day, and Google no longer publishes per-model numbers. Check your own limits in the AI Studio rate-limit console, pair up, and create keys the night before.
- Quota or 429 error: wait a minute and do not share one key.
- ADK cells fail: ADK 2.0 changed some APIs; compare with https://google.github.io/adk-docs
- Preview features (Live Translate, text to speech) may need a different model name. The code was written from public docs and **has not been run against the live APIs**, so run every notebook yourself before the session. File Search syntax was checked against Google's current docs; ADK 2.0 cells (notebook 03) were not.

## Resources
- Voice agent workshop (ADK and Live API): https://github.com/saurabh1611a7458-pixel/Agent-Voice
- Gemini for developers deck and codelab: https://speakerdeck.com/meteatamel/gemini-for-developers
- Live Translate docs: https://ai.google.dev/gemini-api/docs/live-api/live-translate
- WAXAL speech dataset paper: https://arxiv.org/abs/2602.02734
- Common Voice: https://commonvoice.mozilla.org · Masakhane: https://masakhane.io
- Whisper Tiny for Swahili (AfricanLP 2025): https://aclanthology.org/2025.africanlp-1.11

The sample farming data is for practice only and is not agricultural advice.

## What was tested (and what was not)
**Tested locally, no Google servers:**
- Notebooks 01, 02, 04, 05, 06, 07 and 08 ran end to end against a mock Gemini client: control flow, model fallback, scoring loop, injection counting, audio file writing and the RAG retrieval maths all executed without errors.
- The SDK calls used (google-genai 2.34.0) exist with the names used: File Search stores, uploads, operations, chats, embeddings, speech config and audio parts.
- The ADK flow in notebook 03 (google-adk 2.13.0) ran end to end with a fake model: the tool was called and the final answer extracted.
- `adk web` started with the sample agent folder and listed it.

**Not tested (needs real servers or accounts):** any real Gemini response, quota behaviour, Colab Secrets, real File Search indexing, real text to speech, Swahili quality, and any real deployment. The text-to-speech ID `gemini-3.1-flash-tts-preview` is unverified (the notebook falls back to `gemini-2.5-flash-preview-tts`, which Google's docs list).
