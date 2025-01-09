## TOP SETTINGS.JSON

```json
{
  // Editor settings
  "editor.fontFamily": "JetBrains Mono",
  "editor.fontSize": 14,
  "editor.lineHeight": 1.8,
  "editor.rulers": [80, 120],
  "editor.renderLineHighlight": "gutter",
  "editor.fontLigatures": true,
  "editor.semanticHighlighting.enabled": false,
  "editor.tabSize": 2,
  "editor.tabCompletion": "on",
  "editor.wordWrap": "on",
  "editor.formatOnSave": true,
  "editor.colorDecorators": false,
  "editor.autoClosingBrackets": "always",
  "editor.autoClosingQuotes": "always",
  "editor.minimap.renderCharacters": false,
  "editor.minimap.size": "fill",
  "editor.minimap.showSlider": "always",
  "editor.renderWhitespace": "selection",
  "editor.bracketPairColorization.enabled": false,
  "editor.copyWithSyntaxHighlighting": false,
  "editor.emptySelectionClipboard": false,
  "editor.multiCursorModifier": "ctrlCmd",
  "editor.snippetSuggestions": "top",
  "editor.detectIndentation": false,
  "editor.wordSeparators": "`~!@#%^&*()=+[{]}\\|;:'\",.<>/?",
  "editor.linkedEditing": true,
  "editor.inlineSuggest.suppressSuggestions": true,

  // Prettier settings
  "prettier.singleQuote": true,
  "prettier.trailingComma": "all",

  // Prettier DefaultFormatter settings
  "[javascriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[json]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[html]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[jsonc]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[scss]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[css]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[vue]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },

  // Black DefaultFormatter settings
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": "explicit"
    }
  },

  // Workbench settings
  "workbench.startupEditor": "newUntitledFile",
  "workbench.editor.labelFormat": "short",
  "workbench.activityBar.location": "top",
  "workbench.statusBar.visible": true,
  "workbench.editor.enablePreview": false,
  "workbench.sideBar.location": "right",
  "workbench.tree.indent": 14,
  "workbench.iconTheme": "vs-minimal",
  "workbench.layoutControl.enabled": false,
  "workbench.colorTheme": "Abyss",

  // Explorer settings
  "explorer.compactFolders": false,
  "explorer.fileNesting.enabled": true,
  "explorer.fileNesting.patterns": {
    "package.json": "package-lock*, yarn*, pnpm-lock*, vite*, tsconfig*, prettier*, .eslint*",
    "tailwind.config*": "tailwind.config*, postcss.config*",
    ".env.local": ".env*",
    ".env": ".env*"
  },
  "explorer.confirmDragAndDrop": false,
  "explorer.confirmDelete": false,
  "explorer.sortOrder": "default",

  // Terminal settings
  "terminal.integrated.fontSize": 14,
  "terminal.integrated.fontFamily": "MesloLGS NF",
  "terminal.integrated.defaultProfile.windows": "Command Prompt",

  // LiveServer settings
  "liveServer.settings.donotShowInfoMsg": true,
  "liveServer.settings.donotVerifyTags": true,

  // HTML settings
  "html.autoClosingTags": false,
  "html.format.wrapAttributes": "auto",
  "html.format.wrapLineLength": 0,

  // Files settings
  "files.associations": {
    "*.js": "javascriptreact",
    "*.vue": "vue"
  },
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "files.trimFinalNewlines": true,
  "files.eol": "\n",

  // Telemetry settings
  "telemetry.telemetryLevel": "all",

  // Color Highlight settings
  "color-highlight.markerType": "dot-before",

  // Window settings
  "window.title": "${rootName}",
  "window.newWindowDimensions": "offset",
  "window.zoomLevel": 2,
  "window.commandCenter": false,

  // DiffEditor settings
  "diffEditor.renderSideBySide": true,
  "diffEditor.ignoreTrimWhitespace": true,

  // Search settings
  "search.useIgnoreFiles": false,
  "search.exclude": {
    "**/node_modules": true,
    "**/package-lock.json": true,
    "**/yarn.lock": true,
    "**/.eslintcache": true
  },

  // Git settings
  "git.confirmSync": false,
  "git.autofetch": true,
  "git.enableSmartCommit": true,
  "git.ignoreRebaseWarning": true,

  // Breadcrumbs settings
  "breadcrumbs.enabled": false,

  // Extensions settings
  "extensions.ignoreRecommendations": true,

  // Format Files settings
  "formatFiles.excludedFolders": [
    "node_modules",
    ".vscode",
    ".git",
    "dist",
    ".chrome",
    "k8s",
    "bitbucket-pipelines.yml",
    "setup.sh",
    "/ ^.*(?<!.min)(.(css|js))$ / g"
  ],
  "formatFiles.runOrganizeImports": true,

  // Isort settings
  "isort.args": ["--profile", "black"],

  // JavaScript settings
  "javascript.updateImportsOnFileMove.enabled": "always",

  // PHP settings
  "php.validate.executablePath": "C:/xampp/php/php.exe",

  // Remote settings
  "remote.autoForwardPortsSource": "hybrid",

  // GitLens settings
  "gitlens.showWhatsNewAfterUpgrades": false,
  "gitlens.plusFeatures.enabled": false,
  "gitlens.hovers.enabled": false,
  "gitlens.hovers.avatars": false,
  "gitlens.hovers.pullRequests.enabled": false,
  "gitlens.hovers.autolinks.enabled": false,
  "gitlens.hovers.autolinks.enhanced": false,
  "gitlens.hovers.currentLine.enabled": false,
  "gitlens.hovers.currentLine.details": false,
  "gitlens.hovers.currentLine.changes": false,
  "gitlens.hovers.annotations.enabled": false,
  "gitlens.hovers.annotations.details": false,
  "gitlens.hovers.annotations.changes": false,

  // Cody settings
  "cody.chat.preInstruction": "Don't be afraid of saying, “I don't know”. You are authorized to ask me in case of doubt. Read easily and carefully, breathe, understand step-by-step. Imagine that three different specialists are answering this question. All the specialists will write 1 step of their thoughts, then share this with the group. Then all the specialists will go to the next step, etc. if any specialist realizes that they are wrong at any point, then they leave. Their target is to answer the question based on what have they been learned, and always write code using [Tiger Style](https://tigerstyle.dev/), [TDD](https://www.lambdatest.com/learning-hub/test-driven-development), and [Functional Programming](https://softwaremill.com/what-is-functional-programming/). The stack is: React 17, React 18, Node.js 16, Node.js 18, Node.js 20, Node.js 22, Python 3.12, Python 3.13, Python 3.14, as well as HTML 5, CSS 3, JavaScript ES5, and JavaScript ES6. They work as Product Engineering, with core key values: 1- Technology is a tool to achieve a business outcome; 2- Demonstrate ownership over Product and Solutions; 3- Find quality solutions (even non-technical ones) to deliver; 4- Pragmatism, perfect is the enemy of good; 5- Optimizing for \"Time To Value\".",
  "cody.debug.verbose": true,
  "cody.autocomplete.disableInsideComments": true,
  "cody.edit.preInstruction": "",
  "cody.debug.filter": " ",
  "cody.autocomplete.enabled": true,
  "cody.commandHints.enabled": false,
  "cody.codeActions.enabled": false,
  "workbench.editor.wrapTabs": true,
  "gitlens.launchpad.indicator.enabled": false,
  "editor.minimap.enabled": false
}

```

---
