# Lumerate Claude Marketplace

Internal Lumerate tools and workflows for Claude Code.

## Installation

### Add the Marketplace

```bash
/plugin marketplace add <path-or-url-to-this-repo>
```

### Install Plugins

```bash
# Install the lume-scribe plugin
/plugin install lume-scribe@lumerate
```

## Available Plugins

### lume-scribe
Documentation, planning, and artifact authoring tools.

**Skills:**
- `/lume-scribe:craft-story` - Interactive story writeup with template selection and Linear integration

See [plugins/lume-scribe/README.md](plugins/lume-scribe/README.md) for detailed documentation.

## Directory Structure

```
lumerate-claude-marketplace/
├── .claude-plugin/
│   └── marketplace.json      # Marketplace manifest
├── README.md                  # This file
└── plugins/
    └── lume-scribe/           # Lume Scribe plugin
        ├── .claude-plugin/
        │   └── plugin.json   # Plugin manifest
        ├── skills/
        │   └── craft-story/
        │       ├── SKILL.md           # Skill definition
        │       ├── generation.md      # Story generation instructions
        │       ├── scripts/
        │       │   └── list_templates.py  # Template discovery
        │       └── templates/         # Shared templates (supports subdirs)
        └── README.md          # Plugin docs
```

## Contributing

1. Clone this repository
2. Add or modify plugins in the `plugins/` directory
3. Update the marketplace.json if adding new plugins
4. Test locally with `/plugin marketplace add` and `/plugin install`
5. Submit a PR for review
