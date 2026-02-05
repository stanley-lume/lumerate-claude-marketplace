#!/usr/bin/env python3
"""Lists available story templates with their metadata.

Output format: source|path|name|description
"""

import os
import re
from pathlib import Path


def extract_frontmatter(file_path: Path, source: str) -> str:
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

    return f"{source}|{file_path}|{name}|{description}"


def find_templates(directory: Path, source: str) -> list[str]:
    """Find all .md templates in a directory recursively."""
    results = []
    if directory.exists():
        for md_file in directory.rglob("*.md"):
            line = extract_frontmatter(md_file, source)
            if line:
                results.append(line)
    return results


def main():
    # Plugin templates: relative to this script's location
    script_dir = Path(__file__).parent
    plugin_templates = script_dir.parent / "templates"

    # User templates
    user_templates = Path.home() / ".claude" / "lumerate" / "story-templates"

    # Find and output templates (user first, then plugin defaults)
    for line in find_templates(user_templates, "user"):
        print(line)

    for line in find_templates(plugin_templates, "plugin"):
        print(line)


if __name__ == "__main__":
    main()
