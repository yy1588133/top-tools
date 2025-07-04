---
description:
  A unified index for cross-referencing and understanding the interactions between different .clinerules/ files.
author: Cline
version: 2.0
tags: ['index', 'cross-reference', 'clinerules-overview']
globs: ['*']
---

# ClineRules Index

This document serves as a unified index for the `.clinerules/` directory, providing an overview of all rules and mapping
their interactions and dependencies. It covers both global rules defined in the central `.clinerules/` directory and any
workspace-specific rules that may exist in individual projects. This index aims to improve navigability and coherence by
linking related guidelines, ensuring users and Cline can understand how different rules support and interact with each
other across all contexts.

## Categorized Overview of Rules

To enhance organization and navigability, the rules are logically grouped into thematic categories. While the physical
file structure remains flat, this categorization provides a structured view of the rules based on their purpose and
scope.

### Core Behaviors

Rules related to Cline's fundamental operational protocols and identity.

1\. **cline-continuous-improvement.md**

- **Purpose**: Mandates self-reflection and knowledge capture for continuous improvement.
- **Key Focus**: Logging learnings, difficulties, and successes into memory bank files for long-term knowledge
  retention.
- **Related Files**: `cline-memory-bank.md` (knowledge storage), `cline-self-improving.md` (rule enhancement proposals).

2\. **cline-self-improving.md**

- **Purpose**: Defines a process for reflecting on interactions and suggesting rule improvements.
- **Key Focus**: User feedback integration and rule evolution.
- **Related Files**: `cline-continuous-improvement.md` (insight consolidation), `clinerules-best-practices.md` (rule
  writing guidelines).

3\. **cline-ultimate.md**

- **Purpose**: Establishes Cline's identity as an autonomous software engineering agent.
- **Key Focus**: Technical mastery, tool usage, and comprehensive assistance scope.
- **Related Files**: All rules (defines overarching capabilities).

### Development Guides

Technical and architectural guidelines for development practices.

4\. **cline-extension-guide.md**

- **Purpose**: Details the architecture and development guide for the Cline VSCode extension.
- **Key Focus**: Technical structure, state management, API integrations, and task execution.
- **Related Files**: None directly, but provides context for all operational rules.

5\. **swe-best-practices.md**

- **Purpose**: Comprehensive guide to software engineering best practices.
- **Key Focus**: Architecture, debugging, code quality, collaboration, security, and reliability.
- **Related Files**: `senior-python.md` (specific to Python), `product-manager.md` (user-focused engineering).

6\. **senior-python.md**

- **Purpose**: Establishes Cline's expertise as a senior Python engineer.
- **Key Focus**: Python best practices, PEP 8 compliance, and performance optimization.
- **Related Files**: `swe-best-practices.md` (general engineering practices).

7\. **uv-python-venv-guide.md**

- **Purpose**: Comprehensive guide to using UV for Python project management and virtual environments.
- **Key Focus**: Installation, environment management, package handling, and best practices.
- **Related Files**: `senior-python.md` (Python development), `swe-best-practices.md` (general engineering practices).

### Workflows

Rules governing task management and operational workflows.

**Note on PRD-to-Task Workflow**: The recommended sequence for managing Product Requirements Documents (PRDs) and tasks
is as follows: `create-prd.md` -> `generate-tasks-from-prd.md` -> `process-task-list.md`. This workflow ensures a
structured approach from defining requirements to generating and processing tasks.

8\. **new-task-workflow.md**

- **Purpose**: Provides instructions for task handoff strategies, especially for context window management.
- **Key Focus**: Task decomposition, handoff processes, and context preservation.
- **Related Files**: `cline-memory-bank.md` (context storage), `cline-continuous-improvement.md` (task reflection).

9\. **process-task-list.md**

- **Purpose**: Outlines guidelines for managing task lists to track progress on PRDs.
- **Key Focus**: Task implementation, completion protocol, and maintenance of relevant files.
- **Related Files**: `generate-tasks-from-prd.md` (task generation), `product-manager.md` (task planning).

10\. **generate-tasks-from-prd.md**

- **Purpose**: Defines the process for generating task lists from Product Requirements Documents (PRDs).
- **Key Focus**: Analyzing PRDs, creating high-level tasks, and detailed sub-tasks.
- **Related Files**: `create-prd.md` (PRD creation), `process-task-list.md` (task management).

11\. **mcp-research-workflow.md**

- **Purpose**: Guides the user through a research process using available MCP tools.
- **Key Focus**: Research method selection, output format, and execution using MCP tools.
- **Related Files**: `mcp-sequential-thinking.md` (problem-solving), `cline-ultimate.md` (tool usage).

12\. **mcp-sequential-thinking.md**

- **Purpose**: Guide for using the sequential thinking MCP tool for dynamic and reflective problem-solving.
- **Key Focus**: Iterative thought process, hypothesis generation, and verification.
- **Related Files**: `mcp-research-workflow.md` (research process), `cline-ultimate.md` (tool usage).

### Roles

Role-specific instructions and responsibilities.

13\. **product-manager.md**

- **Purpose**: Defines Cline's role as an experienced product manager.
- **Key Focus**: Understanding user needs, planning, and clear documentation for junior developers.
- **Related Files**: `create-prd.md` (PRD creation), `cline-memory-bank.md` (documentation).

14\. **aura-productivity-partner.md**

- **Purpose**: Defines Cline's role as a personal productivity partner with aura principles.
- **Key Focus**: Structuring daily tasks, maintaining focus, and adapting to user energy levels.
- **Related Files**: `cline-memory-bank.md` (documentation), `cline-continuous-improvement.md` (reflection).

### Processes

Specific processes, templates, or formats for various tasks.

15\. **create-prd.md**

- **Purpose**: Outlines the process for generating Product Requirements Documents (PRDs).
- **Key Focus**: Gathering user needs, structuring PRDs, and integration with project management tools.
- **Related Files**: `product-manager.md` (user needs focus), `cline-memory-bank.md` (documentation storage).

16\. **commit-message-format.md**

- **Purpose**: Provides a standardized format for commit messages.
- **Key Focus**: Ensuring clarity and consistency in version control history.
- **Related Files**: `swe-best-practices.md` (collaboration practices).

17\. **cline-metrics-automation.md**

- **Purpose**: Automates the running of cline-metrics tool for analysis on new projects.
- **Key Focus**: Assessing development value and ROI through session data analysis.
- **Related Files**: `cline-continuous-improvement.md` (reflection), `cline-memory-bank.md` (progress tracking).

### Meta

Guidelines about rule creation, maintenance, and knowledge management.

18\. **clinerules-best-practices.md**

- **Purpose**: Offers guidance on writing effective `.clinerules/`.
- **Key Focus**: Clarity, structure, and actionable content for rule creation.
- **Related Files**: `cline-self-improving.md` (rule updates), all rules (applies to their maintenance).

19\. **cline-memory-bank.md**

- **Purpose**: Describes the Memory Bank system for maintaining project knowledge across sessions.
- **Key Focus**: Structure of core files, maintenance protocols, and documentation workflows.
- **Related Files**: `cline-continuous-improvement.md` (knowledge logging), `product-manager.md` (documentation
  standards).

20\. **mcp-server-development.md**

- **Purpose**: Defines the protocol and steps for developing MCP (Model Context Protocol) servers.
- **Key Focus**: Planning, implementation, testing, and completion of MCP server development.
- **Related Files**: `cline-ultimate.md` (tool usage), `swe-best-practices.md` (development practices).

### Application Development Guides

Guides specific to application development across different platforms.

21\. **appdev-android.md**

- **Purpose**: Guidelines for Android app development with best practices.
- **Key Focus**: Architecture, testing, and performance optimization for Android apps.
- **Related Files**: `swe-best-practices.md` (general practices).

22\. **appdev-flutter.md**

- **Purpose**: Comprehensive guide for Flutter development.
- **Key Focus**: State management, widgets, and testing for cross-platform apps.
- **Related Files**: `swe-best-practices.md` (general practices).

23\. **appdev-ios.md**

- **Purpose**: iOS development guidelines.
- **Key Focus**: Swift, UIKit, SwiftUI, and app architecture for iOS apps.
- **Related Files**: `swe-best-practices.md` (general practices).

24\. **appdev-reactnative.md**

- **Purpose**: React Native development best practices.
- **Key Focus**: Cross-platform mobile app development with React Native.
- **Related Files**: `swe-best-practices.md` (general practices), `website-react.md` (React practices).

### Website Development Guides

Guides specific to web development across different frameworks.

25\. **website-html.md**

- **Purpose**: Guidelines for creating static websites with HTML, CSS, and JavaScript.
- **Key Focus**: Simplicity and user-friendly design for beginners.
- **Related Files**: `swe-best-practices.md` (general practices).

26\. **website-nextjs.md**

- **Purpose**: Best practices for Next.js development.
- **Key Focus**: Server-side rendering and static generation with Next.js 14.
- **Related Files**: `website-react.md` (React practices), `swe-best-practices.md` (general practices),
  `nextjs-supabase.md` (Supabase integration).

27\. **website-react.md**

- **Purpose**: React development guidelines.
- **Key Focus**: Components, hooks, and state management for React apps.
- **Related Files**: `swe-best-practices.md` (general practices).

28\. **website-vue.md**

- **Purpose**: Vue.js development best practices.
- **Key Focus**: Composition API and state management for Vue apps.
- **Related Files**: `swe-best-practices.md` (general practices).

29\. **web-design-bank.md**

- **Purpose**: Resource for web design principles and practices.
- **Key Focus**: Maintaining a consistent UI/UX design system across sessions.
- **Related Files**: `cline-memory-bank.md` (documentation), `website-html.md`, `website-nextjs.md`, `website-react.md`,
  `website-vue.md` (web development guides).

30\. **nextjs-supabase.md**

- **Purpose**: Guidelines for integrating Supabase Auth with Next.js apps.
- **Key Focus**: Server-side rendering authentication with Supabase.
- **Related Files**: `website-nextjs.md` (Next.js practices).

### Presentation and Documentation Guides

Guides for creating presentations and maintaining documentation.

31\. **slidev-guide.md**

- **Purpose**: Guidelines for creating presentations using Slidev.
- **Key Focus**: Advanced syntax, visuals, interactivity, and deployment.
- **Related Files**: `slidev-presentation.md` (presentation practices).

32\. **slidev-presentation.md**

- **Purpose**: Best practices for crafting high-quality Slidev presentations.
- **Key Focus**: Structuring content and using Slidev features effectively.
- **Related Files**: `slidev-guide.md` (detailed guide).

## Versioning and Changelog

- **Version 2.0**: Updated to include categorized overview of rules for better logical organization and navigability.
  Added versioning and changelog section to track updates to the rule set. (Date: 6/16/2025)
- **Version 1.0**: Initial creation of the index with a flat list of rules and interaction map.

## Navigation Guide

Use this index to navigate the `.clinerules/` directory effectively. The categorized structure above groups rules by
thematic purpose, making it easier to locate guidelines relevant to specific aspects of Cline's operation. Refer to the
'Related Files' for each rule to understand dependencies and interactions.

## Interaction Map

<!-- markdownlint-disable MD046 -->

```mermaid
graph TD
    CCI[cline-continuous-improvement.md] --> CMB[cline-memory-bank.md]
    CCI --> CSI[cline-self-improving.md]
    CMB --> CCI
    CMB --> PM[product-manager.md]
    CSI --> CCI
    CSI --> CBP[clinerules-best-practices.md]
    CBP --> CSI
    CPRD[create-prd.md] --> PM
    CPRD --> CMB
    CPRD --> GTP[generate-tasks-from-prd.md]
    GTP --> PTL[process-task-list.md]
    NTW[new-task-workflow.md] --> CMB
    NTW --> CCI
    PM --> CPRD
    PM --> CMB
    SPY[senior-python.md] --> SBP[swe-best-practices.md]
    SBP --> SPY
    SBP --> PM
    UV[uv-python-venv-guide.md] --> SPY
    UV --> SBP
    AURA[aura-productivity-partner.md] --> CMB
    AURA --> CCI
    MCPR[mcp-research-workflow.md] --> MST[mcp-sequential-thinking.md]
    MCPR --> CU[cline-ultimate.md]
    MST --> MCPR
    MST --> CU
    CMA[cline-metrics-automation.md] --> CCI
    CMA --> CMB
    MCPS[mcp-server-development.md] --> CU
    MCPS --> SBP
    APP_AND[appdev-android.md] --> SBP
    APP_FLU[appdev-flutter.md] --> SBP
    APP_IOS[appdev-ios.md] --> SBP
    APP_RN[appdev-reactnative.md] --> SBP
    APP_RN --> W_REACT[website-react.md]
    W_HTML[website-html.md] --> SBP
    W_NEXT[website-nextjs.md] --> W_REACT
    W_NEXT --> SBP
    W_NEXT --> NS[nextjs-supabase.md]
    NS --> W_NEXT
    W_REACT --> SBP
    W_VUE[website-vue.md] --> SBP
    WDB[web-design-bank.md] --> CMB
    WDB --> W_HTML
    WDB --> W_NEXT
    WDB --> W_REACT
    WDB --> W_VUE
    SG[slidev-guide.md] --> SP[slidev-presentation.md]
    SP --> SG
    CU -->|Informs All| CCI
    CU -->|Informs All| CMB
    CU -->|Informs All| CSI
    CU -->|Informs All| CBP
    CU -->|Informs All| CPRD
    CU -->|Informs All| NTW
    CU -->|Informs All| PM
    CU -->|Informs All| SPY
    CU -->|Informs All| SBP
    CEG[cline-extension-guide.md] -->|Provides Context| CU
```

<!-- markdownlint-enable MD046 -->

This map illustrates how rules interact, with `cline-ultimate.md` providing overarching guidance, and other rules
supporting specific aspects like knowledge management, task workflows, and domain expertise. Note the specific workflow
for PRD-to-Task management: `create-prd.md` -> `generate-tasks-from-prd.md` -> `process-task-list.md`, which is
highlighted in the diagram as a sequential path. Additionally, various development guides for applications and websites
connect to core engineering practices and specific frameworks. Use this index to navigate the `.clinerules/` directory
effectively, understanding dependencies and related guidelines for comprehensive assistance.
