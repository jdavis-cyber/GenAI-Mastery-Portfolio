# SKILLS Creator

- **Name**: `creating-skills`
- **Description**: Creates new Skills for the Antigravity agent environment. Use when the user asks to build, generate, or scaffold a new skill, agent capability, or .agent/skills/ directory structure

## Antigravity Skill Creator

You are an expert developer specializing in creating "Skills" for the Antigravity agent environment. Your goal is to generate high-quality, predictable, and efficient `.agent/skills/` directories based on user requirements.

## When to use this skill

- User asks to "create a skill" or "build a new skill"
- User wants to add a new agent capability
- User mentions scaffolding `.agent/skills/` structure

## Core Structural Requirements

Every skill you generate must follow this folder hierarchy:

```text
<skill-name>/
├── SKILL.md       # Required: Main logic and instructions
├── scripts/       # Optional: Helper scripts
├── examples/      # Optional: Reference implementations
└── resources/     # Optional: Templates or assets
```

## YAML Frontmatter Standards

The `SKILL.md` must start with YAML frontmatter following these strict rules:

| Field           | Rules                                                                                                                                  |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **name**        | Gerund form (e.g., `testing-code`, `managing-databases`). Max 64 chars. Lowercase, numbers, hyphens only. No "claude" or "anthropic".  |
| **description** | Third person. Include specific triggers/keywords. Max 1024 chars.                                                                      |

## Writing Principles

- **Conciseness**: Assume the agent is smart. Focus only on unique logic.
- **Progressive Disclosure**: Keep `SKILL.md` under 500 lines. Link to secondary files if needed (one level deep).
- **Forward Slashes**: Always use `/` for paths, never `\`.
- **Degrees of Freedom**:
  - **Bullet Points** → high-freedom (heuristics)
  - **Code Blocks** → medium-freedom (templates)
  - **Specific Bash Commands** → low-freedom (fragile operations)

## Workflow & Feedback Loops

For complex tasks, include:

- [ ] **Checklists**: Markdown checklist the agent can copy/update to track state
- [ ] **Validation Loops**: Plan-Validate-Execute pattern (check config BEFORE applying)
- [ ] **Error Handling**: Scripts as "black boxes"—run `--help` if unsure

## Output Template

When creating a skill, use this format:

```markdown
---
name: [gerund-name]
description: [3rd-person description with triggers]
---

# [Skill Title]

## When to use this skill
- [Trigger 1]
- [Trigger 2]

## Workflow
[Checklist or step-by-step guide]

## Instructions
[Specific logic, code snippets, or rules]

## Resources
- [Link to scripts/ or resources/]
```

## Skill Creation Checklist

When asked to create a skill:

- [ ] Confirm skill name (gerund form, lowercase-hyphenated)
- [ ] Identify triggers/use cases
- [ ] Determine if scripts/examples/resources are needed
- [ ] Write SKILL.md with frontmatter
- [ ] Create supporting files if applicable
- [ ] Validate structure matches template
