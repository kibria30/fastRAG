SYSTEM_PROMPT_TEMPLATE = (
    "You are an assistant answering questions about {topic}. "
    "Use the provided context first. "
    "If the context doesn't contain the answer, say so clearly instead of "
    "guessing. When you use a fact from context, mention which source file "
    "it came from — as plain text (e.g. 'from {example_source}'), never as a "
    "bracketed citation number. "
    "You also have tools available — use them only for things the context "
    "can't answer. Don't call a tool if the context already answers the "
    "question. "
    "\n\n"
    "Formatting: your answer will be displayed in a chat app with very "
    "limited formatting support. Never use markdown tables. Present "
    "comparisons or multi-item data as a short bulleted list instead. "
    "Use single asterisks for *bold* (not double), and keep formatting "
    "minimal overall."
)

DOMAINS = {
    "law": {
        "label": "Bangladesh Law & Constitution",
        "path": "./knowledge_base/law",
        "collection": "bd_law_knowledge_base",
        "system_prompt": SYSTEM_PROMPT_TEMPLATE.format(
            topic="Bangladesh law, the Constitution, and the judiciary",
            example_source="constitution_of_bangladesh.md",
        ),
    },
    "health": {
        "label": "Public Health & Medicine",
        "path": "./knowledge_base/health",
        "collection": "public_health_knowledge_base",
        "system_prompt": SYSTEM_PROMPT_TEMPLATE.format(
            topic="public health and medicine",
            example_source="tuberculosis.md",
        ),
    },
}

DEFAULT_DOMAIN = "law"


def get_domain(key: str) -> dict:
    if key not in DOMAINS:
        valid = ", ".join(DOMAINS)
        raise ValueError(f"Unknown domain '{key}'. Valid domains: {valid}")
    return DOMAINS[key]
