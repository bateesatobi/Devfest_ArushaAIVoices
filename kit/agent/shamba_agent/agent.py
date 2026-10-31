"""Farm-advice voice-ready agent for ADK. Run from the agent/ folder with: adk web"""
from google.adk import Agent

CROP_TIPS = {
    ("maize", "yellow leaves"): "Check nitrogen, drainage and stalk borer.",
    ("maize", "holes in leaves"): "Possible fall armyworm. Inspect early in the morning and contact the extension officer.",
}


def crop_advice(crop: str, problem: str) -> dict:
    """Look up advice for a crop problem. crop and problem are short English phrases."""
    key = (crop.lower().strip(), problem.lower().strip())
    return {"advice": CROP_TIPS.get(key, "No record. Ask the extension officer.")}


root_agent = Agent(
    name="shamba_agent",
    model="gemini-3.5-flash-lite",  # model names retire quickly: check ai.google.dev/gemini-api/docs/models
    instruction=(
        "Advise smallholder farmers briefly, in the farmer's language (Swahili by default). "
        "Use crop_advice for crop problems. If unsure, say so and suggest the extension officer."
    ),
    tools=[crop_advice],
)
