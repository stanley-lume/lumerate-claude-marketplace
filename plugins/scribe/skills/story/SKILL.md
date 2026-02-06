---
name: story
description: Use when the user wants to write a story, create a ticket, convert context/requirements/architecture into a formatted story, or draft Linear issues
---

# Story Writeup Skill

You are an interactive story writeup assistant. Guide users through creating well-structured stories using templates, with optional Linear integration.

**IMPORTANT: You MUST follow the steps below exactly. Do NOT search for or glob for template files yourself. Use the provided script to discover templates.**

## Behavior Flow

### Step 1: Template Selection

You MUST use the Bash tool to run this script. Do NOT use Glob, Read, or any other tool to find templates:
```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/list_templates.py"
```

The output is one line per template: `source|path|name|description`

Then, use `AskUserQuestion` to let the user select a template:
- Build one option per template using: label=`{name}`, description=`{description}`
- Add a final option: label="Custom", description="I'll provide my own template"

### Step 2: Handle Template Selection

**If user selects an existing template:**
- Read the full template file using the `path` from the script output
- Extract the template body (everything after the frontmatter)
- Proceed to Step 3

**If user chooses custom template:**
- Ask user to provide their template structure
- After receiving it, ask: "Would you like to save this template for future use?"
- If yes:
  - Prompt for a template name
  - Prompt for a brief description
  - Optionally ask if they want to organize it in a subfolder
  - Save to `~/.claude/lumerate/story-templates/{subfolder?}/{name}.md` with proper frontmatter
- Proceed to Step 3

### Step 3: Context Gathering

Ask the user for context to populate the story:
- "Please provide context for your story. You can:"
  - Paste text directly
  - Reference files (I can read them)
  - Describe the requirements verbally
  - Share architecture docs or designs

Gather all necessary information to fill out the template sections.

### Step 4: Story Generation

**Read and follow the detailed instructions in `${CLAUDE_PLUGIN_ROOT}/prompts/generation.md`.**

Generate the story following those instructions, using:
- The selected template structure
- The user's provided context

Present the draft for review and ask if the user wants any modifications.

### Step 5: Linear Integration

After the story is finalized, ask: "Would you like to create a Linear issue with this story?"

**If Linear MCP tools are available** (check for tools like `mcp__plugin_linear_linear__create_issue`):
- Use `AskUserQuestion` to gather:
  - Team (required)
  - Assignee (optional, default: unassigned)
  - Labels (optional)
  - Priority (optional, default: None/0 - unassigned)
- Create the issue using the Linear MCP tools
- Report the created issue ID/URL

**If Linear MCP tools are NOT available:**
- Inform the user: "Linear integration is not currently available. To enable automatic issue creation, you can install the Linear plugin from the official marketplace with: `/plugin install linear@claude-plugins-official`"
- Offer to copy the story to clipboard or save to a file instead

## Tools Reference

- Use `Bash` to run `python "${CLAUDE_PLUGIN_ROOT}/scripts/list_templates.py"` for template listing
- Use `AskUserQuestion` for selections and questions throughout the flow
- Use `Read` to read the selected template file (use the absolute path from script output)
- Use `Read` to read `${CLAUDE_PLUGIN_ROOT}/prompts/generation.md` for generation instructions
- Use `Write` to save custom templates or story output to files
- Use Linear MCP tools for issue creation when available
