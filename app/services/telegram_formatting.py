import re
 
 
def format_for_telegram(text: str) -> str:
    # Strip markdown table separator rows entirely, e.g. |---|---|
    text = re.sub(r"^\s*\|[\s\-:|]+\|\s*$", "", text, flags=re.MULTILINE)
 
    # Convert remaining table rows "| a | b | c |" into a simple bullet line
    # "a — b — c", since Telegram has no table rendering at all.
    def _row_to_bullet(match: re.Match) -> str:
        cells = [c.strip() for c in match.group(0).strip().strip("|").split("|")]
        cells = [c for c in cells if c]
        return "• " + " — ".join(cells)
 
    text = re.sub(r"^\s*\|.+\|\s*$", _row_to_bullet, text, flags=re.MULTILINE)
 
    # GitHub-style **bold** -> Telegram legacy Markdown *bold* (single asterisk)
    text = re.sub(r"\*\*(.+?)\*\*", r"*\1*", text)
 
    # Strip citation brackets like 【2】, 【5】 — meaningless without the
    # source list they referenced; source attribution already happens via
    # your separate `sources` field, not inline in the chat reply.
    text = re.sub(r"【\d+】", "", text)
 
    # Collapse the extra blank lines the table conversion tends to leave behind
    text = re.sub(r"\n{3,}", "\n\n", text)
 
    return text.strip()