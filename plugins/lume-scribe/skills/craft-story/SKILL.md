---
name: craft-story
description: Collaboratively craft stories, tickets, and issues from requirements. Handles writing, formatting, breaking large requirements into multiple stories, and Linear integration.
allowed-tools:
  - Bash(python */craft-story/scripts/*)
  - Read(*/craft-story/**)
---

# Craft Story

Collaboratively craft well-structured stories using templates. This skill guides you through template selection, context gathering, story generation with feedback, and optional Linear integration.

## Available Templates

!`python "${CLAUDE_PLUGIN_ROOT}/skills/craft-story/scripts/list_templates.py"`

The output above lists available templates with: Template name, Type (custom or shared), Description, and Path.
If the output says "No templates available", skip template selection and proceed directly to asking the user for a custom template.

## Workflow

### Step 1: Template Selection

**If templates are available:**
Parse the templates listed above and use `AskUserQuestion` with the question: "Which template would you like to use? (Choose 'Other' to provide your own or create a new one)"
- Build one option per template using: label=`{name}`, description=`{description}`
- Order templates by relevance to the user's context - most relevant first
- If there's a clearly most relevant template, add " (Recommended)" to its label. If no clear winner, just present ranked options without highlighting

### Step 2: Handle Template Selection

**If user selects an existing template:**
- Read the full template file using the `path` from the template list above
- Extract the template body (everything after the frontmatter)
- Proceed to Step 3

**If user chooses "Other":**
- Ask user to provide their story template or describe what they want in it
- After receiving it, ask: "Would you like to save this story template for future use?"
- If yes:
  - Prompt for a template name
  - Prompt for a brief description
  - Optionally ask if they want to organize it in a subfolder
  - Save to `~/.claude/lumerate/story-templates/{subfolder?}/{name}.md` with proper frontmatter:
    ```yaml
    ---
    name: Template Name
    description: Brief description
    ---

    Template content here...
    ```
- Proceed to Step 3

### Step 3: Context Gathering

Ask the user for context to populate the story:
- "Please provide context for your story. You can:"
  - Paste text directly
  - Reference files (I can read them)
  - Describe the requirements verbally
  - Share architecture docs or designs

Gather all necessary information to fill out the template sections.

**Note:** Balance flow vs. feedback. Only interrupt to recommend splitting if drafting a single story would be impractical or wasteful. Otherwise, draft the story and suggest splitting as feedback afterward.

### Step 4: Story Generation

**CRITICAL: You MUST read [generation.md](generation.md) before generating the story.** It contains the complete prompting guide for story generation and feedback.

After reading generation.md, generate the story using:
- The selected template structure
- The user's provided context
- The workflow defined in generation.md

Present the draft for review and ask if the user wants any modifications.

### Step 5: Linear Integration

After the story is finalized, ask: "Would you like to create a Linear issue with this story?"

**If Linear MCP tools are available** (check for tools like `mcp__plugin_linear_linear__create_issue`):
- Use `AskUserQuestion` to gather:
  - Team (required)
  - Project (optional, or None to not associate with a project)
- Create the issue using the Linear MCP tools
- Report the created issue ID/URL

**If Linear MCP tools are NOT available:**
- Inform the user: "Linear integration is not currently available. To enable automatic issue creation, you can install the Linear plugin from the official marketplace with: `/plugin install linear@claude-plugins-official`"
- Offer to copy the story to clipboard or save to a file instead

## Supporting Files

- [generation.md](generation.md): Detailed instructions for populating templates and providing feedback
- [templates/](templates/): Skill-bundled story templates (Default Story, Backend Story, etc.)
- User templates: `~/.claude/lumerate/story-templates/`
