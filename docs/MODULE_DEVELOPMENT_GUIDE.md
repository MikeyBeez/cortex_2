# /Users/bard/Code/cortex_2/docs/MODULE_DEVELOPMENT_GUIDE.md
# Module Development Guide

This guide explains how to create, package, and deploy modules for Cortex_2.

## What is a Module?

A module in Cortex_2 is a self-contained unit of knowledge, capability, or behavior that can be dynamically loaded and unloaded. Modules can contain:

- Domain expertise (e.g., Python programming, medical knowledge)
- Project context (e.g., specific codebase knowledge)
- Behavioral patterns (e.g., communication styles)
- Tool knowledge (e.g., how to use specific APIs)
- Identity components (e.g., personality traits)

## Module Structure

### Basic Module Layout

```
my_module/
├── manifest.yaml          # Module metadata and configuration
├── content/              # Main module content
│   ├── knowledge/        # Static knowledge data
│   ├── patterns/         # Behavioral patterns
│   ├── templates/        # Response templates
│   └── resources/        # Additional resources
├── triggers/             # Context detection rules
│   ├── keywords.json     # Keyword triggers
│   ├── patterns.json     # Pattern triggers
│   └── contexts.json     # Context triggers
├── tests/                # Module tests
│   ├── test_loading.py
│   └── test_triggers.py
└── README.md            # Module documentation
```

### Manifest File

The `manifest.yaml` file defines your module:

```yaml
# Required fields
id: python_expertise
version: 1.0.0
name: Python Programming Expertise
description: Comprehensive Python knowledge including syntax, patterns, and best practices

# Metadata
metadata:
  author: MikeyBee
  created: 2024-01-01
  updated: 2024-06-22
  tags: [programming, python, development]
  category: expertise
  
# Dependencies
dependencies:
  - id: programming_basics
    version: ">=1.0.0"
  - id: software_patterns
    version: ">=0.5.0"
    optional: true

# Resource requirements
resources:
  size_tokens: 50000
  size_bytes: 200000
  memory_required_mb: 50
  load_time_estimate_ms: 100
  
# Activation triggers
triggers:
  # Keywords that suggest this module is needed
  keywords:
    - python
    - pip
    - django
    - flask
    - pandas
    - numpy
    
  # Regex patterns for file detection
  file_patterns:
    - ".*\\.py$"
    - "requirements\\.txt"
    - "setup\\.py"
    
  # Context patterns
  context_patterns:
    - task_type: programming
      language: python
    - task_type: debugging
      language: python
      
# Content structure
content:
  knowledge:
    format: json
    files:
      - knowledge/syntax.json
      - knowledge/stdlib.json
      - knowledge/best_practices.json
  patterns:
    format: json
    files:
      - patterns/common_errors.json
      - patterns/optimization.json
  templates:
    format: text
    directory: templates/
    
# Module behavior
behavior:
  auto_load: false          # Should this auto-load based on triggers?
  priority: normal          # low, normal, high, critical
  cache_policy: lru         # lru, lfu, persistent
  ttl_minutes: 1440        # Time to live in cache (24 hours)
```

## Content Types

### Knowledge Content

Knowledge files contain static information:

```json
// knowledge/syntax.json
{
  "python_syntax": {
    "data_types": {
      "int": {
        "description": "Integer type",
        "examples": ["42", "-17", "0"],
        "methods": ["bit_length()", "to_bytes()"]
      },
      "str": {
        "description": "String type",
        "examples": ["'hello'", "\"world\""],
        "methods": ["upper()", "lower()", "split()"]
      }
    },
    "control_flow": {
      "if_statement": {
        "syntax": "if condition:\n    # code",
        "examples": [...]
      }
    }
  }
}
```

### Pattern Content

Patterns define behavioral responses:

```json
// patterns/common_errors.json
{
  "error_patterns": [
    {
      "error_type": "IndentationError",
      "common_causes": [
        "Mixing tabs and spaces",
        "Incorrect indentation level"
      ],
      "solutions": [
        "Use consistent indentation (4 spaces recommended)",
        "Check for mixed tabs/spaces"
      ],
      "detection_regex": "IndentationError: .*"
    }
  ]
}
```

### Template Content

Templates provide response structures:

```text
// templates/code_review.template
When reviewing Python code, I'll examine:

1. **Code Style**: {style_issues}
2. **Potential Bugs**: {bug_analysis}
3. **Performance**: {performance_notes}
4. **Best Practices**: {best_practices}

{specific_recommendations}
```

## Creating Triggers

### Keyword Triggers

```json
// triggers/keywords.json
{
  "exact_match": [
    "python",
    "python3"
  ],
  "partial_match": [
    "pyth",
    "django",
    "flask"
  ],
  "context_keywords": {
    "programming": ["def", "class", "import"],
    "debugging": ["error", "exception", "traceback"]
  }
}
```

### Pattern Triggers

```json
// triggers/patterns.json
{
  "regex_patterns": [
    {
      "pattern": ".*\\.py$",
      "description": "Python files",
      "priority": "high"
    },
    {
      "pattern": "^import .*",
      "description": "Import statements",
      "priority": "medium"
    }
  ],
  "structural_patterns": [
    {
      "type": "code_block",
      "language": "python",
      "confidence": 0.9
    }
  ]
}
```

## Module Types

### 1. Expertise Modules

Domain-specific knowledge:

```yaml
id: medical_expertise
category: expertise
content:
  knowledge:
    - anatomy.json
    - diseases.json
    - treatments.json
    - medications.json
```

### 2. Project Modules

Project-specific context:

```yaml
id: project_nexus_2
category: project
content:
  knowledge:
    - architecture.json
    - api_specs.json
    - codebase_map.json
  patterns:
    - coding_standards.json
    - naming_conventions.json
```

### 3. Identity Modules

Personality and behavioral traits:

```yaml
id: professional_identity
category: identity
content:
  traits:
    - communication_style.json
    - response_patterns.json
    - preferences.json
```

### 4. Tool Modules

External tool integration:

```yaml
id: github_integration
category: tool
content:
  api_specs:
    - github_api.json
  patterns:
    - pr_review.json
    - issue_templates.json
```

## Module Development Workflow

### 1. Planning

Define what your module will contain:
- What knowledge does it encapsulate?
- When should it be loaded?
- What are its dependencies?
- How much memory will it use?

### 2. Structure Creation

```bash
# Create module structure
cortex create-module my_module

# This creates:
# my_module/
#   ├── manifest.yaml
#   ├── content/
#   ├── triggers/
#   ├── tests/
#   └── README.md
```

### 3. Content Development

Populate your module with content:

```python
# Tool to help convert existing knowledge
from cortex.tools import KnowledgeConverter

converter = KnowledgeConverter()
converter.convert_from_markdown("docs/", "my_module/content/knowledge/")
```

### 4. Trigger Definition

Define when your module should load:

```python
# Test triggers
from cortex.tools import TriggerTester

tester = TriggerTester("my_module")
tester.test_phrase("Let's work with Python")  # Should trigger
tester.test_file("example.py")  # Should trigger
```

### 5. Testing

Test your module thoroughly:

```python
# tests/test_loading.py
def test_module_loads():
    module = load_module("my_module")
    assert module.id == "my_module"
    assert module.size_tokens <= 50000

def test_module_triggers():
    triggers = get_triggers("my_module")
    assert triggers.matches("python code")
    assert not triggers.matches("javascript code")
```

### 6. Optimization

Optimize for fast loading:

```bash
# Analyze module performance
cortex analyze-module my_module

# Output:
# Load time: 87ms
# Memory usage: 45,000 tokens
# Trigger accuracy: 92%
# Suggestions:
# - Compress knowledge/stdlib.json (save 5,000 tokens)
# - Index patterns for faster search
```

### 7. Packaging

Package for distribution:

```bash
# Package module
cortex package-module my_module

# Creates: my_module-1.0.0.cortex
# Ready for installation
```

## Best Practices

### 1. Keep Modules Focused

Each module should have a single, clear purpose. Don't create "kitchen sink" modules.

✅ Good: `python_django_expertise`
❌ Bad: `all_web_development`

### 2. Optimize for Size

- Compress JSON files
- Remove redundant information
- Use references instead of duplication
- Consider splitting large modules

### 3. Design for Fast Loading

- Structure data for quick access
- Pre-index searchable content
- Minimize dependencies
- Use lazy loading for optional content

### 4. Version Carefully

- Use semantic versioning
- Maintain backward compatibility
- Document breaking changes
- Test against dependencies

### 5. Write Clear Triggers

- Be specific but not too narrow
- Test triggers extensively
- Consider false positives
- Priority rank triggers

### 6. Document Thoroughly

- Clear module description
- Usage examples
- Dependency explanations
- Performance characteristics

## Module Examples

### Example 1: Language Expertise

```yaml
id: spanish_language
version: 1.0.0
name: Spanish Language Expertise
category: language

content:
  knowledge:
    - vocabulary.json      # 10,000 common words
    - grammar_rules.json   # Grammar patterns
    - idioms.json         # Common expressions
  patterns:
    - conversation.json    # Conversation patterns
    - formality.json      # Formal/informal rules
  
triggers:
  keywords: [spanish, español, hola, gracias]
  patterns:
    - "translate.*spanish"
    - "en español"
```

### Example 2: Personality Module

```yaml
id: friendly_casual
version: 1.0.0
name: Friendly Casual Personality
category: identity

content:
  traits:
    communication_style:
      tone: casual
      humor: light
      emoji_usage: moderate
    response_patterns:
      greeting: ["Hey!", "Hi there!", "Hello!"]
      acknowledgment: ["Got it!", "Sure thing!", "Absolutely!"]
      
behavior:
  auto_load: false
  priority: normal
```

### Example 3: Project Context

```yaml
id: project_anna
version: 2.1.0
name: Anna Project Context
category: project

dependencies:
  - id: python_expertise
    version: ">=1.0.0"
  - id: pytorch_knowledge
    version: ">=1.0.0"

content:
  knowledge:
    - architecture.json     # Anna's architecture
    - organs.json          # Organ specifications
    - api_spec.json        # API documentation
  patterns:
    - naming.json          # Naming conventions
    - code_style.json      # Project style guide
    
triggers:
  keywords: [anna, organs, temporal, o1, o2, o3, o4, o5]
  file_patterns:
    - ".*anna.*\\.py$"
    - "organs/.*"
```

## Advanced Topics

### Module Composition

Combine modules dynamically:

```python
# Create composite module
composite = cortex.compose_modules([
    "python_expertise",
    "async_programming",
    "web_development"
])
```

### Conditional Loading

Load based on complex conditions:

```yaml
triggers:
  conditions:
    - type: and
      conditions:
        - keyword: python
        - context: debugging
        - time_of_day: business_hours
```

### Module Inheritance

Extend existing modules:

```yaml
id: python_advanced
extends: python_expertise
version: 1.0.0

# Only specify additions/overrides
content:
  knowledge:
    - advanced_patterns.json
    - metaprogramming.json
```

### Dynamic Generation

Generate modules programmatically:

```python
from cortex.tools import ModuleBuilder

builder = ModuleBuilder()
builder.from_codebase("/path/to/project")
builder.extract_patterns()
builder.build("project_module")
```

## Troubleshooting

### Module Won't Load

1. Check manifest syntax
2. Verify all dependencies available
3. Ensure size within limits
4. Check file paths are correct

### Triggers Not Working

1. Test triggers in isolation
2. Check for conflicts with other modules
3. Verify regex patterns
4. Increase trigger priority

### Performance Issues

1. Profile module loading
2. Reduce content size
3. Optimize data structures
4. Consider splitting module

## Module Repository

Share modules with the community:

```bash
# Publish module
cortex publish my_module

# Install from repository
cortex install python_expertise

# Search repository
cortex search "machine learning"
```

---

*Remember: Good modules are focused, fast, and friendly. They should enhance Cortex_2's capabilities without overwhelming the system.*
