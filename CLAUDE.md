# CLAUDE.md - AI Assistant Guide for vibe-coding-2026

This document provides comprehensive guidance for AI assistants (like Claude) working with this repository. It covers codebase structure, development workflows, conventions, and best practices.

## Repository Overview

**Repository:** vibe-coding-2026
**Status:** Initial setup phase
**Current Branch:** `claude/add-claude-documentation-gADpQ`

This repository is currently in its initial stages of development. As the project grows, this document will be updated to reflect the evolving structure and conventions.

## Directory Structure

```
vibe-coding-2026/
├── .git/               # Git repository metadata
├── README.md           # Project readme
└── CLAUDE.md           # This file - AI assistant guide
```

### Expected Future Structure

As the project develops, anticipate the following structure:

```
vibe-coding-2026/
├── src/                # Source code
│   ├── components/     # UI components (if applicable)
│   ├── services/       # Business logic and services
│   ├── utils/          # Utility functions
│   └── index.{js,ts}   # Entry point
├── tests/              # Test files
├── docs/               # Additional documentation
├── config/             # Configuration files
├── public/             # Static assets (if web project)
├── .gitignore          # Git ignore rules
├── package.json        # Node dependencies (if Node.js)
├── tsconfig.json       # TypeScript config (if applicable)
└── README.md           # Project documentation
```

## Git Workflow

### Branch Naming Convention

All Claude/AI-generated branches MUST follow this pattern:
```
claude/<description>-<session-id>
```

**Example:** `claude/add-claude-documentation-gADpQ`

**CRITICAL:** Branches must start with `claude/` and end with a matching session ID, otherwise push operations will fail with 403 errors.

### Commit Guidelines

1. **Commit Message Format:**
   ```
   <type>: <short description>

   <optional detailed description>
   ```

2. **Commit Types:**
   - `feat:` New feature
   - `fix:` Bug fix
   - `docs:` Documentation changes
   - `refactor:` Code refactoring
   - `test:` Adding or updating tests
   - `chore:` Maintenance tasks
   - `style:` Code style/formatting changes

3. **Best Practices:**
   - Write clear, concise commit messages
   - Focus on the "why" rather than the "what"
   - Keep commits atomic and focused
   - Review changes with `git status` and `git diff` before committing

### Push Operations

**Standard push command:**
```bash
git push -u origin <branch-name>
```

**Retry Logic:**
- If network failures occur, retry up to 4 times with exponential backoff (2s, 4s, 8s, 16s)
- Only retry on network errors, not authorization failures

### Pull Request Workflow

1. **Before Creating PR:**
   - Run `git status` to check untracked files
   - Run `git diff` to review changes
   - Review commit history with `git log`
   - Ensure all tests pass (when testing is set up)

2. **PR Creation:**
   ```bash
   gh pr create --title "PR title" --body "$(cat <<'EOF'
   ## Summary
   - Brief description of changes

   ## Test plan
   - [ ] Testing checklist items
   EOF
   )"
   ```

3. **PR Best Practices:**
   - Analyze ALL commits included in the PR
   - Draft comprehensive summaries
   - Include test plans
   - Reference related issues

## Development Best Practices

### Code Quality Principles

1. **Avoid Over-Engineering:**
   - Only make changes that are directly requested or clearly necessary
   - Keep solutions simple and focused
   - Don't add features beyond what was asked
   - Avoid premature abstractions

2. **Security:**
   - Never introduce security vulnerabilities (XSS, SQL injection, command injection, etc.)
   - Validate input at system boundaries
   - Follow OWASP Top 10 guidelines
   - If insecure code is detected, fix it immediately

3. **Backwards Compatibility:**
   - Avoid backwards-compatibility hacks
   - If something is unused, delete it completely
   - Don't keep commented-out code
   - No `// removed` comments

4. **Code Comments:**
   - Only add comments where logic isn't self-evident
   - Don't add docstrings/comments to unchanged code
   - Prefer self-documenting code

### File Operations

**Prefer specialized tools over bash commands:**
- Use `Read` tool instead of `cat/head/tail`
- Use `Edit` tool instead of `sed/awk`
- Use `Write` tool instead of `echo >` or heredocs
- Use `Glob` tool instead of `find` or `ls`
- Use `Grep` tool instead of `grep` or `rg`

### Tool Usage Patterns

1. **Parallel Execution:**
   - When operations are independent, execute tools in parallel
   - Example: Reading multiple files simultaneously

2. **Sequential Execution:**
   - When operations depend on each other, execute sequentially
   - Example: Write file → git add → git commit → git push

3. **Exploration:**
   - Use Task tool with `subagent_type=Explore` for codebase exploration
   - Use for understanding structure, not for specific file searches
   - Examples:
     - "Where are errors handled?"
     - "What is the codebase structure?"
     - "How does authentication work?"

## AI Assistant Guidelines

### Task Management

1. **Always use TodoWrite tool for:**
   - Complex multi-step tasks (3+ steps)
   - Non-trivial implementations
   - When user provides multiple tasks
   - Planning and tracking progress

2. **Todo States:**
   - `pending`: Not started
   - `in_progress`: Currently working (ONLY ONE at a time)
   - `completed`: Finished

3. **Todo Requirements:**
   - Mark tasks complete IMMEDIATELY after finishing
   - Don't batch completions
   - Exactly ONE task in_progress at a time
   - Use both imperative and active forms:
     - `content`: "Run tests" (what to do)
     - `activeForm`: "Running tests" (while doing it)

### Communication Style

1. **Be Concise:**
   - Short, focused responses
   - Use GitHub-flavored markdown
   - No unnecessary emojis (unless user requests)

2. **Be Professional:**
   - Prioritize technical accuracy
   - Provide objective guidance
   - Disagree when necessary
   - No over-the-top validation or excessive praise

3. **Code References:**
   - Use pattern: `file_path:line_number`
   - Example: "Authentication handled in `src/auth.ts:42`"

### Before Making Changes

**ALWAYS read files before modifying them:**
1. Use `Read` tool to understand existing code
2. Analyze current implementation
3. Plan changes based on actual code
4. Never propose changes to unread code

### Testing & Validation

When testing infrastructure exists:
1. Run tests after making changes
2. Fix any failures before completing tasks
3. Verify build succeeds
4. Check for type errors (if TypeScript)

### Common Pitfalls to Avoid

1. **Don't:**
   - Create files unnecessarily (prefer editing existing)
   - Add features not explicitly requested
   - Refactor code not directly related to task
   - Add error handling for impossible scenarios
   - Create abstractions for one-time operations
   - Use `git --amend` unless explicitly required
   - Push to main/master without permission
   - Skip git hooks (--no-verify)

2. **Do:**
   - Read files before editing
   - Keep changes focused and minimal
   - Mark todos complete immediately
   - Use specialized tools over bash commands
   - Run tools in parallel when possible
   - Follow existing code patterns

## Project-Specific Conventions

### To Be Established

As the project develops, document:
- Code style preferences (indentation, naming conventions)
- Testing patterns and requirements
- Documentation standards
- Dependency management practices
- Build and deployment procedures
- Environment setup instructions

## Common Tasks

### Starting Work on a New Feature

1. Check current branch: `git branch --show-current`
2. Ensure on correct claude/* branch
3. Create todo list for the feature
4. Explore relevant codebase areas
5. Implement changes incrementally
6. Test as you go
7. Commit with clear messages
8. Push to branch

### Debugging an Issue

1. Reproduce the issue
2. Use Explore agent to find relevant code
3. Read and analyze the problematic code
4. Identify root cause
5. Implement fix
6. Verify fix resolves issue
7. Commit and push

### Refactoring Code

1. Read and understand current implementation
2. Plan refactoring approach
3. Make incremental changes
4. Test after each change
5. Ensure no behavior changes (unless intended)
6. Update tests if needed
7. Commit and push

## Updating This Document

This document should be updated when:
- Project structure changes significantly
- New conventions are established
- Development workflows evolve
- New tools or frameworks are added
- Best practices are refined

Keep this document current and accurate to maximize its value for AI assistants working with this codebase.

---

**Last Updated:** 2026-01-12
**Document Version:** 1.0.0
**Status:** Initial creation
