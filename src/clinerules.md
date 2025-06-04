# ClineRules Instructions

_Last updated: 2025-06-04_

---

## Categories

### Application Development

- [`appdev-android`](src.clinerules.example\appdev-android.md): Guidelines for Android app development with best
  practices for architecture, testing, and performance. `['android', 'mobile', 'development-guide', 'architecture']`
- [`appdev-flutter`](src.clinerules.example\appdev-flutter.md): Comprehensive guide for Flutter development including
  state management, widgets, and testing. `['flutter', 'mobile', 'cross-platform', 'development-guide']`
- [`appdev-ios`](src.clinerules.example\appdev-ios.md): iOS development guidelines covering Swift, UIKit, SwiftUI, and
  app architecture. `['ios', 'swift', 'mobile', 'development-guide']`
- [`appdev-reactnative`](src.clinerules.example\appdev-reactnative.md): React Native development best practices for
  cross-platform mobile apps. `['react-native', 'mobile', 'cross-platform', 'javascript']`

### Core Behaviors

- [`cline-architecture`](src.clinerules.example\cline-architecture.md): Defines Cline's extension architecture,
  components, data flow, and development guidelines.
  `['architecture', 'development-guide', 'extension', 'vscode', 'core-behavior']`
- [`cline-ci-protocol`](src.clinerules.example\cline-ci-protocol.md): Defines Cline's mandatory protocol for
  self-reflection, persistent knowledge capture using dedicated logs, and continuous improvement of its operational
  knowledge before task completion.
  `['protocol', 'meta', 'learning', 'reflection', 'knowledge-management', 'core-behavior']`
- [`memory-bank`](src.clinerules.example\memory-bank.md): Describes Cline's Memory Bank system, its structure, and
  workflows for maintaining project knowledge across sessions.
  `['memory-bank', 'knowledge-base', 'core-behavior', 'documentation-protocol']`
- [`self-improving-cline`](src.clinerules.example\self-improving-cline.md): Defines a process for Cline to reflect on
  interactions and suggest improvements to active .clinerules.
  `['meta', 'self-improvement', 'clinerules', 'reflection', 'core-behavior']`

### Development Workflows

- [`commit-message-format`](src.clinerules.example\commit-message-format.md): Guidelines for writing clear, consistent
  commit messages following conventional commits format. `['git', 'commits', 'documentation', 'workflow']`
- [`local-python`](src.clinerules.example\local-python.md): Best practices for local Python development including
  virtual environments and package management. `['python', 'development', 'virtual-env', 'package-management']`
- [`mcp-dev-protocol`](src.clinerules.example\mcp-dev-protocol.md): Defines the protocol and steps for developing MCP
  (Model Context Protocol) servers. `['mcp', 'development', 'protocol', 'server', 'integration']`
- [`new-task-automation`](src.clinerules.example\new-task-automation.md): Workflow for starting new task when context
  window reaches 50% `['context-management', 'new-task']`
- [`sequential-thinking`](src.clinerules.example\sequential-thinking.md): A guide for effectively using the
  sequentialthinking MCP tool for dynamic and reflective problem-solving.
  `['mcp', 'sequentialthinking', 'problem-solving', 'workflow-guide', 'ai-guidance']`

### Website Development

- [`website-html`](src.clinerules.example\website-html.md): Guidelines for creating static websites with HTML, CSS, and
  JavaScript. `['html', 'css', 'javascript', 'web-development']`
- [`website-nextjs`](src.clinerules.example\website-nextjs.md): Best practices for Next.js development with server-side
  rendering and static generation. `['nextjs', 'react', 'web-development', 'ssr']`
- [`website-react`](src.clinerules.example\website-react.md): React development guidelines focusing on components,
  hooks, and state management. `['react', 'javascript', 'web-development', 'spa']`
- [`website-vue`](src.clinerules.example\website-vue.md): Vue.js development best practices covering composition API and
  state management. `['vue', 'javascript', 'web-development', 'spa']`

### Framework & Tool Guides

- [`c#-guide`](src.clinerules.example\c#-guide.md): A comprehensive guide to mastering C# for developers with Python and
  TypeScript backgrounds.
  `['csharp', '.net', 'guide', 'programming-language', 'typescript-transition', 'python-transition']`
- [`nextjs-supabase`](src.clinerules.example\nextjs-supabase.md): Guidelines for writing Next.js apps with Supabase Auth
  `['nextjs', 'supabase', 'auth', 'ssr', 'guide', 'best-practices']`
- [`uv-python-usage-guide`](src.clinerules.example\uv-python-usage-guide.md): A comprehensive guide to using UV for
  Python project management, covering installation, environment management, package handling, and best practices.
  `['uv', 'python', 'package-manager', 'venv', 'guide']`

### Presentation & Documentation

- [`cline-for-slides`](src.clinerules.example\cline-for-slides.md): Provides guidelines and best practices for creating
  and working with Slidev presentation projects. `['slidev', 'slides', 'markdown', 'vue', 'vite', 'guide']`
- [`comprehensive-slide-dev-guide`](src.clinerules.example\comprehensive-slide-dev-guide.md): A comprehensive guide to
  crafting high-quality advanced presentations using Slidev, covering advanced syntax, visuals, interactivity,
  customization, and deployment. `['slidev', 'guide', 'advanced', 'presentation', 'development']`

### Meta Rules

- [`cline-for-research`](src.clinerules.example\cline-for-research.md): Guides the user through a research process using
  available MCP tools, offering choices for refinement, method, and output.
  `['research', 'mcp', 'workflow', 'assistant-behavior']`
- [`writing-effective-clinerules`](src.clinerules.example\writing-effective-clinerules.md): Guidelines and best
  practices for creating effective .clinerules to guide Cline's behavior, knowledge, and workflows.
  `['meta', 'guideline', 'clinerules', 'documentation', 'best-practices']`

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
