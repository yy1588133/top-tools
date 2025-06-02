# VSCode Extensions

_Last updated: 2025-06-02_
_Current setup: W11-debloated, VSCodium_

## Quick Reference

### Performance Impact Guide
- 🟢 Low: <50MB memory, minimal CPU usage
- 🟡 Medium: 50-100MB memory, moderate CPU usage
- 🔴 High: >100MB memory, significant CPU usage

### Status Definitions
- **Active**: Currently recommended and maintained
- **Replaced**: Superseded by native features
- **Deprecated**: No longer available/supported

## Summary Table

| Extension Name                   | Status     | Performance | Notes/Replacement                                         |
| -------------------------------- | ---------- | ----------- | -------------------------------------------------------- |
| IntelliCode                      | Deprecated | 🔴 High     | Not available on VSCodium                                 |
| Minify                           | Deprecated | 🟡 Medium   | Not available on VSCodium                                 |
| Smart Column Indenter            | Deprecated | 🟢 Low      | Not available on VSCodium                                 |
| Auto Close Tag                   | Replaced   | 🟢 Low      | Native settings                                           |
| Auto Commit Message              | Replaced   | 🟢 Low      | Keyboard shortcuts                                        |
| Auto Rename Tag                  | Replaced   | 🟢 Low      | Native settings                                           |
| Cody                             | Replaced   | 🔴 High     | Cline                                                     |
| Continue                         | Replaced   | 🔴 High     | Cline                                                     |
| Color Highlight                  | Replaced   | 🟢 Low      | Native settings                                           |
| Material Icon Theme              | Replaced   | 🟢 Low      | Native settings                                           |
| Black Formatter                  | Active     | 🟢 Low      | Python formatting                                         |
| Bookmarks                        | Active     | 🟢 Low      | Code navigation                                           |
| Cline                            | Active     | 🟡 Medium   | AI code assistant                                         |
| Editor Config                    | Active     | 🟢 Low      | Maintain consistent coding styles                         |
| ES7+ Snippets                    | Active     | 🟢 Low      | JavaScript and React/Redux snippets                       |
| isort                            | Active     | 🟢 Low      | Python import sorting                                     |
| JavaScript ES6 snippets          | Active     | 🟢 Low      | JavaScript code snippets                                  |
| Markdown Preview Mermaid Support | Active     | 🟢 Low      | Mermaid diagram support                                  |
| Prettier                         | Active     | 🟢 Low      | Code formatter                                           |
| Pylance                          | Active     | 🟡 Medium   | Python language support                                  |
| Python                           | Active     | 🟡 Medium   | Python development environment                           |
| Python Debugger                  | Active     | 🟡 Medium   | Python debugging support                                 |
| Python Indent                    | Active     | 🟢 Low      | Python indentation                                       |
| SVG                              | Active     | 🟢 Low      | SVG editing and visualization                            |
| Tailwind CSS IntelliSense        | Active     | 🟡 Medium   | Tailwind CSS tooling                                     |
| WakaTime                         | Active     | 🟢 Low      | Time tracking for developers                             |

## Migration Guides

### Auto Close Tag to Native
```json
{
  "editor.autoClosingBrackets": "always",
  "editor.autoClosingQuotes": "always",
  "editor.autoClosingDelete": "always",
  "html.autoClosingTags": true
}
```
**Benefits**:
- Reduced extension overhead
- Faster performance
- Built-in maintenance

### Auto Rename Tag to Native
```json
{
  "editor.linkedEditing": true
}
```
**Benefits**:
- Better performance
- Native integration
- Reliable updates

### Color Highlight to Native
```json
{
  "editor.colorDecorators": true
}
```
**Benefits**:
- Seamless integration
- Reduced memory usage
- Consistent behavior

### Material Icon Theme to Native
```json
{
  "workbench.iconTheme": "vs-minimal"
}
```
**Benefits**:
- Faster loading
- System integration
- Regular updates

### Auto Commit Message to Custom
```txt
Generate a commit message using Conventional Commits:

1. Type: feat, fix, docs, style, refactor, perf, test, build, ci, chore
2. Format: <type>[scope]: <description>
3. First line: max 50 characters
4. Body: wrap at 72 characters

Example:
feat(user-auth): add password reset functionality
Implement reset API, email template, and form component
Closes #123
```

## Active Extensions

[Detailed descriptions of active extensions moved to maintain readability. See original content for full descriptions.]

## Troubleshooting Guide

### General Issues

1. Extension Not Loading
   - Clear VSCode cache
   - Reload window
   - Reinstall extension
   - Check compatibility

2. Performance Problems
   - Disable unused extensions
   - Monitor memory usage
   - Update extensions
   - Clear workspace cache

3. Configuration Conflicts
   - Check settings.json
   - Review workspace settings
   - Disable conflicting extensions
   - Reset to defaults

### Extension-Specific Solutions

1. Python Tools
   - Verify Python installation
   - Check interpreter settings
   - Update language server
   - Validate workspace trust

2. JavaScript/TypeScript Tools
   - Clear TypeScript server
   - Update npm packages
   - Check jsconfig.json
   - Verify node version

3. Formatting Tools
   - Check formatter config
   - Validate file associations
   - Review workspace settings
   - Update language servers

## Best Practices

1. Extension Management
   - Regular cleanup
   - Performance monitoring
   - Update scheduling
   - Conflict resolution

2. Configuration
   - Use workspace settings
   - Document overrides
   - Version control settings
   - Regular backups

3. Performance
   - Minimal active extensions
   - Regular maintenance
   - Profile monitoring
   - Cache management

## Additional Resources

- [VSCode Documentation](https://code.visualstudio.com/docs)
- [Extension API](https://code.visualstudio.com/api)
- [Performance Issues](https://code.visualstudio.com/docs/supporting/troubleshoot-performance)
- [Settings Reference](https://code.visualstudio.com/docs/getstarted/settings)

[Original detailed extension descriptions preserved but moved to maintain document readability]
