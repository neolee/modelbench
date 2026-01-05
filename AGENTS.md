# AGENTS.md

This file contains build commands and code style guidelines for agentic coding assistants working in this repository.

## Build, Lint, and Test Commands

### Dependency Management
- `uv sync` - Install/update dependencies from pyproject.toml

### Code Quality
- `ruff check .` - Lint all Python files
- `ruff check <file>` - Lint a specific file
- `ruff check --fix .` - Auto-fix lint issues
- `ruff format .` - Format all Python files
- `ruff format <file>` - Format a specific file

### Running the Application
- `uv run main.py` - Run the main interactive menu
- `uv run <runner_file>.py` - Run a specific test runner (e.g., `uv run chat.py`, `uv run tool_calling.py`)

### Testing
- No automated test suite exists in this project
- Tests are run manually by executing individual runner scripts
- Each runner file (chat.py, tool_calling.py, etc.) has a `__main__` block for direct execution

## Code Style Guidelines

### Python Environment
- Python 3.11+ required
- Uses ruff for linting and formatting
- Ruff ignores: E402, E701, F403, F405

### Import Organization
Order imports by group, separated by blank lines:
1. Standard library imports
2. Third-party imports (openai, rich, httpx, requests, rtoml, simple_term_menu)
3. Local imports (from runner import Runner, from models import models, from mal.adapter.openai import Model)

Example:
```python
from typing import Tuple
import json

from rich import print
from openai import OpenAI

from runner import Runner
from models import models
```

### Type Hints
- Use type hints for function parameters and return values
- Use union syntax with `|` (Python 3.10+)
- Add `# type: ignore` where type checker needs help
- Type hints are used but not strictly enforced

Example:
```python
def show_menu_of(collection: Iterable, title: str) -> int | Tuple[int, ...] | None:
    ...

runner = runner_class(model)  # type: ignore
```

### Naming Conventions
- Classes: PascalCase (`Model`, `Runner`, `ToolCallingRunner`)
- Functions/Methods: snake_case (`create_chat_completion`, `show_menu_of`)
- Variables: snake_case (`reasoning_content`, `completion`)
- Module-level constants: UPPER_SNAKE_CASE (`models`, `default`)
- File names: snake_case (`tool_calling.py`, `structured_output.py`)

### Error Handling
- Use try/except for main flow error handling
- Use guard decorators (like `@safe_guard`) for safe data access
- Check for None returns from optional operations
- Use assertions for validation where appropriate

Example:
```python
try:
    runner.run()
except Exception as e:
    print(f"'{runner_class.name}' test failed on '{model.name}'")
    print(e)
```

### Code Structure Patterns
- Use abstract base classes for common interfaces
- Runner classes inherit from `Runner` ABC and implement `run()` method
- Class-level `name` attribute for identification
- Module-level configuration at file bottom (model lists, runner lists)
- `if __name__ == "__main__":` blocks for direct script execution

Example:
```python
class ChatRunner(Runner):
    name = "Basic Chat"

    def run(self):
        ...

if __name__ == "__main__":
    r = ChatRunner()
    r.run()
```

### Rich Console Output
- Use `rich.print` for styled output
- Use `rich.console.Console` for advanced formatting
- Use `rich.live.Live` for streaming updates
- Use `rich.markdown.Markdown` for formatted text
- Import custom utilities from `util.rich` (e.g., `prettier_code_blocks`)

### Comments and Docstrings
- Comments may be in English or Chinese
- Chinese comments typically describe user-facing text/output
- English for code logic explanations when present
- Docstrings in Google style for complex functions
- Use `# type: ignore` for type issues instead of comments

### File Organization
- `/` - Main application entry points and feature runners
- `/mal/adapter/` - Model adapter implementations (openai.py, agno.py, pydantic_ai.py)
- `/mal/` - Core model abstraction layer
- `/util/` - Utility functions and helpers
- `providers.toml` - Provider configuration (symlinked to mal/providers.toml)
- Each feature runner in separate file (chat.py, tool_calling.py, etc.)

### Special Patterns
- `@safe_guard` decorator for null-safe method access
- Stream mode for LLM responses with chunk processing
- Separate reasoning and content chunks for thinking models
- Type ignore comments on tool_calls and messages when type checker struggles
- Use of `getattr` for optional fields on response objects

### When Adding New Features
1. Create a new runner class inheriting from `Runner`
2. Set a unique `name` attribute
3. Implement the `run()` method
4. Add to `runners` list in `runners.py`
5. Include `__main__` block for standalone testing
6. Follow existing patterns for streaming, error handling, and output formatting
