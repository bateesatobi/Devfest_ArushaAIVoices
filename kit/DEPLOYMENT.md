# Deploying your farm-advice agent (Google tools only)

Pick the path that matches your account. **Paths marked "needs billing" require a Google Cloud billing account.**

| Path | Good for | Needs billing? | How |
|---|---|---|---|
| Local test UI | Developing and demos | No | `cd agent && adk web` |
| Local API server | Connecting your own front end | No | `cd agent && adk api_server` |
| Colab notebook | Sharing a working prototype | No | Upload notebooks 01 to 08 to Google Colab |
| Firebase AI Logic + Hosting | A web or mobile app that calls Gemini without exposing your key | No on the Spark plan with the Gemini free tier. Some models, especially preview ones, may need billing | https://firebase.google.com/docs/ai-logic |
| Cloud Run | A public agent URL that anyone can call | Needs billing | `adk deploy cloud_run --project=PROJECT --region=REGION --with_ui agent/shamba_agent` |
| Docker | Your own server | No (you run it) | `adk deploy docker agent/shamba_agent` |
| Agent Engine / GKE | Managed or large-scale production | Needs billing | `adk deploy agent_engine ...` or `adk deploy gke ...` |

## What was tested
- `adk web` started with the sample agent folder and listed `shamba_agent` (tested locally with a dummy key, no model call).
- `adk deploy cloud_run`, `docker`, `gke` and `agent_engine` exist in ADK 2.13.0 and their options were read from `--help`.
- **Not tested:** any real deployment (no cloud account was available), Firebase setup, or calls to Google's servers.

## Before you go public
1. The `adk web` and `adk api_server` endpoints are **unauthenticated**. Do not expose them on the internet without your own authentication.
2. Never put your API key in browser code. Use Firebase AI Logic or a server.
3. Add rate limits and a spending cap before sharing a public link.
4. Log questions only with consent, and never log personal data.
5. Keep a human handoff (extension officer) and say "I am not sure" when the context lacks the answer.
