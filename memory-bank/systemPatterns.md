# System Patterns

## System Architecture
The repository follows a clear organizational structure:

```
top-tools/
├── memory-bank/       # Project knowledge and documentation
├── src/              # Core content and configurations
│   ├── browser.md    # Browser extension documentation
│   ├── clinerules.md # AI assistant rule files
│   ├── fav.html      # Curated development links
│   ├── settings.json # VSCode configuration
│   └── vscode.md     # VSCode extension documentation
├── .gitignore        # Git ignore rules
├── LICENSE           # Project license
└── README.md         # Project documentation
```

## Key Technical Decisions

1. Documentation Format
   - Markdown for human-readable documentation
   - JSON for configuration files
   - HTML for interactive content
   - Consistent file naming using lowercase and hyphens
   - Extension status indicators (Active/Replaced/Deprecated)

2. Content Organization
   - Separate directories for different types of content
   - Clear file naming conventions
   - Modular documentation structure
   - Regular update tracking
   - Category-based grouping

3. Memory Bank Implementation
   - Dedicated directory for project knowledge
   - Structured documentation templates
   - Clear update protocols
   - Version tracking
   - Active context maintenance

4. Configuration Management
   - JSON-based settings
   - Clear categorization of extensions
   - Regular validation of configurations
   - Backward compatibility consideration
   - Native feature preference

## Design Patterns in Use

1. Documentation Patterns
   - Clear hierarchical structure
   - Consistent formatting
   - Regular update annotations
   - Version tracking
   - Category-based organization
   - Extension lifecycle tracking

2. Configuration Patterns
   - Modular settings
   - Environment-specific configurations
   - Clear commenting
   - Version compatibility notes
   - Feature replacement documentation

3. Content Management Patterns
   - Regular update cycles
   - Clear categorization
   - Status tracking
   - Deprecation handling
   - Resource organization

4. Maintenance Patterns
   - Regular review cycles
   - Update documentation
   - Compatibility checking
   - User feedback integration
   - Performance monitoring

## Component Relationships

1. Documentation Dependencies
   ```mermaid
   graph TD
      README[README.md] --> Browser[browser.md]
      README --> VSCode[vscode.md]
      README --> Settings[settings.json]
      README --> Favorites[fav.html]
      README --> ClineRules[clinerules.md]
      VSCode --> Settings
      Browser --> Favorites
   ```

2. Configuration Flow
   ```mermaid
   graph TD
      Settings[settings.json] --> VSCode[VSCode/VSCodium]
      Extensions[vscode.md] --> VSCode
      Native[Native Features] --> Settings
      Browser[browser.md] --> WebDev[Web Development]
      Favorites[fav.html] --> Resources[Development Resources]
   ```

3. Memory Bank Structure
   ```mermaid
   graph TD
      PB[projectbrief.md] --> PC[productContext.md]
      PB --> SP[systemPatterns.md]
      PB --> TC[techContext.md]
      PC & SP & TC --> AC[activeContext.md]
      AC --> Progress[progress.md]
   ```

## Critical Implementation Paths

1. Documentation Updates
   - README.md updates trigger review of related files
   - Version numbers must be synchronized
   - Update dates must be maintained
   - Deprecation notices must be propagated
   - Extension status must be tracked

2. Configuration Changes
   - settings.json changes require compatibility checks
   - Extension status changes need documentation updates
   - Browser extension updates need testing
   - Resource links need validation
   - Native feature alternatives must be documented

3. Memory Bank Maintenance
   - Regular review of all Memory Bank files
   - Synchronization of project status
   - Documentation of changes
   - Update of progress tracking
   - Active context maintenance

4. Quality Assurance
   - Link validation
   - Configuration testing
   - Documentation accuracy
   - Version compatibility
   - Update verification
   - Performance impact assessment
