# Scribe

Documentation, planning, and artifact authoring tools.

## Skills

### story

Interactive story writeup with template selection and Linear integration.

```bash
/scribe:story
```

This will guide you through:
1. Selecting a template (or providing your own)
2. Providing context for your story
3. Generating a well-structured story
4. Optionally creating a Linear issue

## Templates

### Shared Templates (Bundled)
Located in the `templates/` directory within this plugin. These are version-controlled and shared with the team.

### Personal Templates
Located in `~/.claude/lumerate/story-templates/` on your machine. These are your personal templates that won't be version controlled.

Both locations support subdirectories for organization (e.g., `engineering/`, `product/`).

### Template Format

Templates use YAML frontmatter for metadata:

```markdown
---
name: My Template
description: A brief description of when to use this template
---

# {Title}

## Section 1
Content...

## Section 2
Content...
```

If no frontmatter is provided, the filename will be used as the template name.

## Linear Integration

If you have the Linear plugin installed (`/plugin install linear@claude-plugins-official`), the story writeup will offer to create a Linear issue automatically with your story content.

## Adding New Shared Templates

1. Create a new `.md` file in the `templates/` directory (or a subdirectory)
2. Add frontmatter with `name` and `description`
3. Add your template structure
4. Commit and push to share with the team
