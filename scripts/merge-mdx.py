import re, os, subprocess

DOCS = "/Users/milan/spooler/docs"
ORDER = [
    "introduction.mdx",
    "quickstart.mdx",
    "hardware/overview.mdx",
    "hardware/installation.mdx",
    "hardware/display-leds.mdx",
    "hardware/ble-advertising.mdx",
    "mobile-app/getting-started.mdx",
    "mobile-app/pairing.mdx",
    "mobile-app/measurement.mdx",
    "mobile-app/spools.mdx",
    "mobile-app/history-sync.mdx",
    "web-app/dashboard.mdx",
    "web-app/spools.mdx",
    "web-app/projects.mdx",
    "web-app/devices.mdx",
    "web-app/reports.mdx",
]

SECTION_BREAKS = {
    "hardware/overview.mdx": "# Zařízení Spooler",
    "mobile-app/getting-started.mdx": "# Mobilní aplikace",
    "web-app/dashboard.mdx": "# Webová aplikace",
}

def clean_mdx(text, filepath):
    # Remove frontmatter
    text = re.sub(r'^---\n.*?\n---\n', '', text, flags=re.DOTALL)
    # Remove JSX/MDX components but keep content inside Step/Tab/Accordion
    text = re.sub(r'<Steps>\s*', '', text)
    text = re.sub(r'</Steps>', '', text)
    text = re.sub(r'<Step title="([^"]+)">', r'\n**\1**\n', text)
    text = re.sub(r'</Step>', '', text)
    text = re.sub(r'<Tabs>\s*', '', text)
    text = re.sub(r'</Tabs>', '', text)
    text = re.sub(r'<Tab title="([^"]+)">', r'\n**\1**\n', text)
    text = re.sub(r'</Tab>', '', text)
    text = re.sub(r'<AccordionGroup>\s*', '', text)
    text = re.sub(r'</AccordionGroup>', '', text)
    text = re.sub(r'<Accordion title="([^"]+)">', r'\n**\1**\n', text)
    text = re.sub(r'</Accordion>', '', text)
    # Callouts -> blockquotes with label
    text = re.sub(r'<Info>\s*(.*?)\s*</Info>', r'> **ℹ️ Info:** \1', text, flags=re.DOTALL)
    text = re.sub(r'<Warning>\s*(.*?)\s*</Warning>', r'> **⚠️ Varování:** \1', text, flags=re.DOTALL)
    text = re.sub(r'<Tip>\s*(.*?)\s*</Tip>', r'> **💡 Tip:** \1', text, flags=re.DOTALL)
    text = re.sub(r'<Check>\s*(.*?)\s*</Check>', r'> **✅ \1**', text, flags=re.DOTALL)
    # CardGroup / Card -> just content
    text = re.sub(r'<CardGroup[^>]*>', '', text)
    text = re.sub(r'</CardGroup>', '', text)
    text = re.sub(r'<Card title="([^"]+)"[^>]*>\s*(.*?)\s*</Card>', r'- **\1** — \2', text, flags=re.DOTALL)
    # Remove remaining JSX tags
    text = re.sub(r'<[A-Z][^>]*/>', '', text)
    text = re.sub(r'<[A-Z][^>]*>.*?</[A-Z][^>]*>', '', text, flags=re.DOTALL)
    # Clean up extra blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

parts = ["---\ntitle: Spooler — Uživatelský manuál\n---\n\n"]

for f in ORDER:
    path = os.path.join(DOCS, f)
    if f in SECTION_BREAKS:
        parts.append(f"\n\n{SECTION_BREAKS[f]}\n\n\\newpage\n\n")
    text = open(path).read()
    cleaned = clean_mdx(text, f)
    parts.append(cleaned + "\n\n\\newpage\n\n")

output = "\n".join(parts)
with open("/tmp/spooler-manual.md", "w") as fh:
    fh.write(output)
print("OK - written to /tmp/spooler-manual.md")
