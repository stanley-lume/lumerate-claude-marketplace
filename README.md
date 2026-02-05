# Lumerate Claude Marketplace

Internal Lumerate tools and workflows for Claude Code.

## Installation

### Add the Marketplace

```bash
/plugin marketplace add <path-or-url-to-this-repo>
```

### Install Plugins

```bash
# Install the story writeup plugin
/plugin install story-writeup@lumerate
```

## Available Plugins

### story-writeup
Interactive story writeup with template selection and Linear integration.

**Usage:**
```bash
/lumerate:story
```

**Features:**
- Template selection from shared and personal templates
- Custom template support with save functionality
- Context-driven story generation
- Linear issue creation (requires Linear plugin)

See [plugins/story-writeup/README.md](plugins/story-writeup/README.md) for detailed documentation.

## Directory Structure

```
lumerate-claude-marketplace/
├── .claude-plugin/
│   └── marketplace.json      # Marketplace manifest
├── README.md                  # This file
└── plugins/
    └── story-writeup/        # Story writeup plugin
        ├── .claude-plugin/
        │   └── plugin.json   # Plugin manifest
        ├── skills/
        │   └── story/
        │       ├── SKILL.md  # Flow logic
        │       └── prompts/
        │           └── generation.md  # Story generation instructions
        ├── templates/        # Shared templates
        └── README.md         # Plugin docs
```

## Contributing

1. Clone this repository
2. Add or modify plugins in the `plugins/` directory
3. Update the marketplace.json if adding new plugins
4. Test locally with `/plugin marketplace add` and `/plugin install`
5. Submit a PR for review
