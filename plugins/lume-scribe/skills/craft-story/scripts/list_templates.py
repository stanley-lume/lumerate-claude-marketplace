#!/usr/bin/env python3
"""Lists available story templates with their metadata.

Searches for templates in:
  - <skill_dir>/templates/  (skill-bundled)
  - ~/.claude/lumerate/story-templates/  (personal)

Output format: source|path|name|description
"""

import re
from pathlib import Path


def extract_frontmatter(file_path: Path, template_type: str) -> str:
    """Extract name and description from YAML frontmatter."""
    try:
        content = file_path.read_text()
    except Exception:
        return ""

    name = file_path.stem  # Default to filename without extension
    description = ""

    # Check for YAML frontmatter (starts with ---)
    if content.startswith("---"):
        # Find the closing ---
        end_match = re.search(r'\n---\s*\n', content)
        if end_match:
            frontmatter = content[3:end_match.start()]

            # Extract name
            name_match = re.search(r'^name:\s*(.+)$', frontmatter, re.MULTILINE)
            if name_match:
                name = name_match.group(1).strip()

            # Extract description
            desc_match = re.search(r'^description:\s*(.+)$', frontmatter, re.MULTILINE)
            if desc_match:
                description = desc_match.group(1).strip()

    return f"Template: {name}\nType: {template_type}\nDescription: {description}\nPath: {file_path}\n"


def find_templates(directory: Path, template_type: str) -> list[str]:
    """Find all .md templates in a directory recursively."""
    results = []
    if directory.exists():
        for md_file in sorted(directory.rglob("*.md")):
            line = extract_frontmatter(md_file, template_type)
            if line:
                results.append(line)
    return results


def main():
    # This script is in skills/craft-story/scripts/, need to go up to skill root
    skill_dir = Path(__file__).resolve().parent.parent
    skill_templates = skill_dir / "templates"
    user_templates = Path.home() / ".claude" / "lumerate" / "story-templates"

    # Find and output templates (custom first, then shared defaults)
    user_results = find_templates(user_templates, "custom")
    skill_results = find_templates(skill_templates, "shared")

    for line in user_results:
        print(line)

    for line in skill_results:
        print(line)

    # If no templates found, output a message
    if not user_results and not skill_results:
        print("No templates available. Please provide your own template structure.")


if __name__ == "__main__":
    main()
