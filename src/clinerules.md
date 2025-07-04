# ClineRules Instructions

---

This document provides a categorized overview of all Cline rules, covering both global rules defined in the central
`.clinerules/` directory and any workspace-specific rules that may exist in individual projects. It serves as a quick
reference for understanding the scope and purpose of each rule.

## Categories

### Application Development

- [`appdev-android`](src/clinerules/appdev-android.md): Guidelines for Android app development with best practices for
  architecture, testing, and performance. `['android', 'mobile', 'development-guide', 'architecture']`
- [`appdev-flutter`](src/clinerules/appdev-flutter.md): Comprehensive guide for Flutter development including state
  management, widgets, and testing. `['flutter', 'mobile', 'cross-platform', 'development-guide']`
- [`appdev-ios`](src/clinerules/appdev-ios.md): iOS development guidelines covering Swift, UIKit, SwiftUI, and app
  architecture. `['ios', 'swift', 'mobile', 'development-guide']`
- [`appdev-reactnative`](src/clinerules/appdev-reactnative.md): React Native development best practices for
  cross-platform mobile apps. `['react-native', 'mobile', 'cross-platform', 'javascript']`

### Core Behaviors

- [`cline-continuous-improvement`](src/clinerules/cline-continuous-improvement.md): Defines Cline's mandatory protocol
  for self-reflection, persistent knowledge capture using dedicated logs, and continuous improvement of its operational
  knowledge before task completion.
  `['protocol', 'meta', 'learning', 'reflection', 'knowledge-management', 'core-behavior']`
- [`cline-extension-guide`](src/clinerules/cline-extension-guide.md): Details the architecture and development guide for
  the Cline VSCode extension. `['architecture', 'development-guide', 'extension', 'vscode', 'core-behavior']`
- [`cline-memory-bank`](src/clinerules/cline-memory-bank.md): Describes Cline's Memory Bank system, its structure, and
  workflows for maintaining project knowledge across sessions.
  `['memory-bank', 'knowledge-base', 'core-behavior', 'documentation-protocol']`
- [`cline-self-improving`](src/clinerules/cline-self-improving.md): Defines a process for Cline to reflect on
  interactions and suggest improvements to active .clinerules.
  `['meta', 'self-improvement', 'clinerules', 'reflection', 'core-behavior']`
- [`cline-ultimate`](src/clinerules/cline-ultimate.md): Establishes Cline's identity as an autonomous software
  engineering agent with comprehensive capabilities.
  `['identity', 'core-behavior', 'software-engineering', 'autonomous-agent']`

### Development Workflows

- [`commit-message-format`](src/clinerules/commit-message-format.md): Guidelines for writing clear, consistent commit
  messages following conventional commits format. `['git', 'commits', 'documentation', 'workflow']`
- [`create-prd`](src/clinerules/create-prd.md): Outlines the process for generating Product Requirements Documents
  (PRDs). `['prd', 'requirements', 'documentation', 'workflow']`
- [`generate-tasks-from-prd`](src/clinerules/generate-tasks-from-prd.md): Defines the process for generating task lists
  from Product Requirements Documents (PRDs). `['tasks', 'prd', 'workflow', 'project-management']`
- [`new-task-workflow`](src/clinerules/new-task-workflow.md): Workflow for starting a new task when context window
  reaches 50%. `['context-management', 'new-task', 'workflow']`
- [`process-task-list`](src/clinerules/process-task-list.md): Guidelines for managing task lists to track progress on
  PRDs. `['tasks', 'project-management', 'workflow']`
- [`mcp-research-workflow`](src/clinerules/mcp-research-workflow.md): Guides the user through a research process using
  available MCP tools. `['research', 'mcp', 'workflow', 'assistant-behavior']`
- [`mcp-sequential-thinking`](src/clinerules/mcp-sequential-thinking.md): A guide for effectively using the sequential
  thinking MCP tool for dynamic and reflective problem-solving.
  `['mcp', 'sequential-thinking', 'problem-solving', 'workflow-guide']`

### Website Development

- [`website-html`](src/clinerules/website-html.md): Guidelines for creating static websites with HTML, CSS, and
  JavaScript. `['html', 'css', 'javascript', 'web-development']`
- [`website-nextjs`](src/clinerules/website-nextjs.md): Best practices for Next.js development with server-side
  rendering and static generation. `['nextjs', 'react', 'web-development', 'ssr']`
- [`website-react`](src/clinerules/website-react.md): React development guidelines focusing on components, hooks, and
  state management. `['react', 'javascript', 'web-development', 'spa']`
- [`website-vue`](src/clinerules/website-vue.md): Vue.js development best practices covering composition API and state
  management. `['vue', 'javascript', 'web-development', 'spa']`
- [`web-design-bank`](src/clinerules/web-design-bank.md): Resource for web design principles and practices.
  `['web-design', 'ui', 'ux', 'resource']`

### Framework & Tool Guides

- [`nextjs-supabase`](src/clinerules/nextjs-supabase.md): Guidelines for writing Next.js apps with Supabase Auth.
  `['nextjs', 'supabase', 'auth', 'ssr', 'guide', 'best-practices']`
- [`senior-python`](src/clinerules/senior-python.md): Establishes Cline's expertise as a senior Python engineer with
  best practices. `['python', 'development', 'best-practices', 'guide']`
- [`uv-python-venv-guide`](src/clinerules/uv-python-venv-guide.md): A comprehensive guide to using UV for Python project
  management and virtual environments. `['uv', 'python', 'package-manager', 'venv', 'guide']`
- [`swe-best-practices`](src/clinerules/swe-best-practices.md): Comprehensive guide to software engineering best
  practices across various domains.
  `['software-engineering', 'best-practices', 'architecture', 'security', 'reliability']`

### Presentation & Documentation

- [`slidev-guide`](src/clinerules/slidev-guide.md): Guidelines for creating presentations using Slidev.
  `['slidev', 'slides', 'markdown', 'presentation', 'guide']`
- [`slidev-presentation`](src/clinerules/slidev-presentation.md): Best practices for crafting high-quality Slidev
  presentations. `['slidev', 'presentation', 'advanced', 'guide']`

### Meta Rules

- [`aura-productivity-partner`](src/clinerules/aura-productivity-partner.md): Defines Cline's role as a productivity
  partner with aura principles. `['productivity', 'meta', 'assistant-behavior']`
- [`clinerules-best-practices`](src/clinerules/clinerules-best-practices.md): Guidelines for creating effective
  .clinerules to guide Cline's behavior and workflows.
  `['meta', 'guideline', 'clinerules', 'documentation', 'best-practices']`
- [`clinerules-index`](src/clinerules/clinerules-index.md): A unified index for cross-referencing and understanding
  interactions between different .clinerules files. `['index', 'cross-reference', 'clinerules-overview']`
- [`mcp-server-development`](src/clinerules/mcp-server-development.md): Protocol and steps for developing MCP (Model
  Context Protocol) servers. `['mcp', 'development', 'protocol', 'server', 'integration']`
- [`product-manager`](src/clinerules/product-manager.md): Defines Cline's role as an experienced product manager for
  project planning and documentation. `['product-management', 'documentation', 'user-needs', 'role']`

---

## Memory Bank Integration

### Key Commands

- **initialize memory bank**: Use when starting a new project

  ```bash
  # Creates initial Memory Bank structure
  # Generates base documentation files
  # Sets up version tracking
  ```

- **follow your custom instructions**: Read Memory Bank files and continue work

  ```bash
  # Loads all Memory Bank files
  # Understands current context
  # Maintains continuity
  ```

- **update memory bank**: Trigger full documentation review

  ```bash
  # Reviews all files
  # Updates documentation
  # Synchronizes information
  ```

### Mode Selection

- **PLAN MODE**: Information gathering and solution architecture

  - Review documentation
  - Ask questions
  - Create detailed plans
  - Get user approval

- **ACT MODE**: Implementation and execution
  - Execute planned changes
  - Update documentation
  - Verify results
  - Track progress

---

## Usage Examples

1. Starting a New Project:

   ```bash
   User: initialize memory bank
   Cline: *Creates Memory Bank structure*
   User: *Provides project requirements*
   Cline: *Sets up initial documentation*
   ```

2. Continuing Work:

   ```bash
   User: follow your custom instructions
   Cline: *Reads Memory Bank*
   User: *Provides task*
   Cline: *Continues with context*
   ```

3. Updating Documentation:

   ```bash
   User: update memory bank
   Cline: *Reviews all files*
   Cline: *Updates documentation*
   User: *Verifies changes*
   ```

---

## Troubleshooting

### Common Issues

1. Incomplete context loading

   - Solution: Use "follow your custom instructions"
   - Verify Memory Bank files exist

2. Mode confusion

   - Solution: Explicitly state needed mode
   - Check current mode in environment details

3. Documentation sync issues
   - Solution: Use "update memory bank"
   - Verify file modifications

### Best Practices

1. Regular Memory Bank updates
2. Clear mode transitions
3. Explicit command usage
4. Version control integration
5. Regular validation checks
