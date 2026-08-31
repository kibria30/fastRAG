"""
Fetch Wikipedia article extracts and write them as Markdown knowledge-base
files under knowledge_base/<domain>/, one file per article, with a source
citation line embedded so provenance survives on disk.

Usage:
    python scripts/fetch_wikipedia_kb.py

Re-running is safe: a file is only skipped if it already exists AND already
contains a "**Source:**" line (i.e. it's already been retrofitted/fetched by
this script). Anything else is (re)fetched and (re)written.
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse

API = "https://en.wikipedia.org/w/api.php"
USER_AGENT = "fastRAG-kb-builder/1.0 (educational RAG demo; contact: claudecommon23@gmail.com)"

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[,()]", "", s)
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_")


def wikipedia_url(title: str) -> str:
    return "https://en.wikipedia.org/wiki/" + urllib.parse.quote(title.replace(" ", "_"))


def fetch_extract(title: str, retries: int = 5) -> tuple[str, str]:
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "explaintext": "1",
        "exsectionformat": "wiki",
        "redirects": "1",
        "titles": title,
    }
    url = API + "?" + urllib.parse.urlencode(params)
    for attempt in range(retries):
        out = subprocess.run(
            ["curl", "-s", "--max-time", "30", "-H", f"User-Agent: {USER_AGENT}", url],
            capture_output=True, text=True,
        ).stdout
        try:
            data = json.loads(out)
        except json.JSONDecodeError:
            wait = 3 * (attempt + 1)
            print(f"  ! rate limited / bad response for {title!r}, retrying in {wait}s...", file=sys.stderr)
            time.sleep(wait)
            continue
        pages = data["query"]["pages"]
        page = next(iter(pages.values()))
        real_title = page["title"]
        extract = page.get("extract", "")
        return real_title, extract
    raise RuntimeError(f"Failed to fetch {title!r} after {retries} retries")


def wiki_extract_to_markdown(title: str, extract: str) -> str:
    lines = extract.split("\n")
    md_lines = [f"# {title}", "", f"**Source:** {wikipedia_url(title)} (Wikipedia, CC BY-SA 4.0)", ""]
    skip_sections = {"See also", "References", "Notes", "External links", "Further reading", "Bibliography", "Citations"}
    skipping = False
    for line in lines:
        m = re.match(r"^(={2,6})\s*(.+?)\s*\1$", line.strip())
        if m:
            level = len(m.group(1))
            heading = m.group(2).strip()
            if heading in skip_sections:
                skipping = True
                continue
            skipping = False
            md_lines.append("")
            md_lines.append(f"{'#' * min(level, 4)} {heading}")
            md_lines.append("")
            continue
        if skipping:
            continue
        if line.strip() == "":
            md_lines.append("")
        else:
            md_lines.append(line)

    text = "\n".join(md_lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def already_retrofitted(path: str) -> bool:
    if not os.path.exists(path):
        return False
    with open(path, "r", encoding="utf-8") as f:
        head = f.read(2000)
    return "**Source:**" in head


def build(titles: list[str], out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    for title in titles:
        fname_guess = slugify(title) + ".md"
        guess_path = os.path.join(out_dir, fname_guess)
        if already_retrofitted(guess_path):
            print(f"  skip (already has Source line) {fname_guess}")
            continue
        real_title, extract = fetch_extract(title)
        if not extract:
            print(f"  ! empty extract for {title!r} (resolved: {real_title!r})", file=sys.stderr)
            continue
        md = wiki_extract_to_markdown(real_title, extract)
        fname = slugify(real_title) + ".md"
        path = os.path.join(out_dir, fname)
        with open(path, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"  wrote {path} ({len(md)} chars) from '{real_title}'")
        time.sleep(1.5)


LAW_TITLES = [
    "Constitution of Bangladesh",
    "Law of Bangladesh",
    "Judiciary of Bangladesh",
    "Supreme Court of Bangladesh",
    "High Court Division, Supreme Court of Bangladesh",
    "Fundamental rights of the people of Bangladesh",
    "Human rights in Bangladesh",
    "Penal Code of Bangladesh",
    "Code of Criminal Procedure of Bangladesh",
    "Bangladesh Election Commission",
    "Local government in Bangladesh",
    "Muslim Family Laws Ordinance, 1961",
    "Anti-Corruption Commission (Bangladesh)",
]

HEALTH_TITLES = [
    "Public health",
    "Epidemiology",
    "Diabetes",
    "Hypertension",
    "Tuberculosis",
    "Malaria",
    "Dengue fever",
    "Vaccination",
    "Malnutrition",
    "Maternal health",
    "Infection",
    "Non-communicable disease",
    "Mental health",
    "Universal health care",
    "World Health Organization",
]

if __name__ == "__main__":
    print("Fetching LAW domain...")
    build(LAW_TITLES, os.path.join(REPO_ROOT, "knowledge_base", "law"))
    print("Fetching HEALTH domain...")
    build(HEALTH_TITLES, os.path.join(REPO_ROOT, "knowledge_base", "health"))
