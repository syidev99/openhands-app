# CLAUDE.md - AI Assistant Guide for openhands-app

This document provides essential context for AI assistants working with this codebase.

## Project Overview

**Repository**: openhands-app
**Status**: Newly initialized project
**Purpose**: Application development project (to be defined)

## Current State

This repository has been recently initialized and contains minimal structure:

```
openhands-app/
├── README.md          # Project description
└── CLAUDE.md          # This file - AI assistant guide
```

## Development Guidelines

### Getting Started

When setting up this project, consider:

1. **Initialize package management**: Run `npm init` or `yarn init` to create `package.json`
2. **Choose a framework**: React, Vue, Next.js, or vanilla JavaScript based on requirements
3. **Set up TypeScript** (recommended): Configure `tsconfig.json` for type safety
4. **Configure linting**: Add ESLint and Prettier for code quality

### Recommended Project Structure

```
openhands-app/
├── src/                    # Source code
│   ├── components/         # UI components
│   ├── pages/              # Page components (if applicable)
│   ├── utils/              # Utility functions
│   ├── hooks/              # Custom hooks (React)
│   ├── services/           # API services
│   └── types/              # TypeScript type definitions
├── tests/                  # Test files
├── public/                 # Static assets
├── .github/                # GitHub workflows
├── package.json            # Dependencies and scripts
├── tsconfig.json           # TypeScript configuration
├── .eslintrc.js            # ESLint configuration
├── .prettierrc             # Prettier configuration
└── README.md               # Project documentation
```

## Code Conventions

### General Principles

- **Keep it simple**: Avoid over-engineering; implement only what's needed
- **Type safety**: Prefer TypeScript for better maintainability
- **Clean code**: Write self-documenting code with meaningful names
- **Single responsibility**: Each function/component should do one thing well

### Naming Conventions

- **Files**: Use kebab-case for files (`user-profile.tsx`)
- **Components**: Use PascalCase (`UserProfile`)
- **Functions**: Use camelCase (`getUserProfile`)
- **Constants**: Use UPPER_SNAKE_CASE (`API_BASE_URL`)
- **Types/Interfaces**: Use PascalCase with descriptive names (`UserProfileProps`)

### Code Style

- Use 2-space indentation
- Use single quotes for strings
- Add semicolons at end of statements
- Maximum line length: 100 characters
- Prefer `const` over `let`; avoid `var`

## Git Workflow

### Branch Naming

- Feature branches: `feature/description`
- Bug fixes: `fix/description`
- Hotfixes: `hotfix/description`

### Commit Messages

Follow conventional commits format:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting)
- `refactor:` Code refactoring
- `test:` Adding/updating tests
- `chore:` Maintenance tasks

Example: `feat: add user authentication flow`

### Pull Request Process

1. Create a feature branch from main
2. Make changes and commit with clear messages
3. Push branch and create PR with description
4. Address review feedback
5. Merge after approval

## Testing Guidelines

### Test Structure

- Place tests in `tests/` directory or colocate with source files as `*.test.ts`
- Name test files to match source: `user-service.ts` → `user-service.test.ts`

### Test Categories

- **Unit tests**: Test individual functions/components in isolation
- **Integration tests**: Test component interactions
- **E2E tests**: Test complete user workflows

## Security Considerations

- Never commit sensitive data (API keys, passwords, secrets)
- Use environment variables for configuration
- Validate all user inputs
- Sanitize data before rendering (prevent XSS)
- Use parameterized queries (prevent SQL injection)

## Build and Deployment

### Common Scripts (to be configured)

```json
{
  "scripts": {
    "dev": "Start development server",
    "build": "Create production build",
    "test": "Run test suite",
    "lint": "Run linter",
    "format": "Format code with Prettier"
  }
}
```

### Environment Configuration

- Use `.env` files for environment-specific config
- Never commit `.env` files (add to `.gitignore`)
- Provide `.env.example` with placeholder values

## AI Assistant Instructions

### When Working on This Codebase

1. **Read before modifying**: Always read relevant files before making changes
2. **Understand context**: Check related files to understand patterns in use
3. **Follow existing conventions**: Match the style and patterns already present
4. **Make minimal changes**: Only modify what's necessary for the task
5. **Test changes**: Verify modifications work as expected

### Common Tasks

#### Adding a New Feature
1. Understand the requirements
2. Check existing patterns in the codebase
3. Implement following established conventions
4. Add appropriate tests
5. Update documentation if needed

#### Fixing a Bug
1. Reproduce the issue
2. Identify the root cause
3. Implement minimal fix
4. Add test to prevent regression
5. Document the fix in commit message

#### Code Review
1. Check for security vulnerabilities
2. Verify code follows conventions
3. Ensure adequate test coverage
4. Look for potential performance issues

## Dependencies

### Core Dependencies (to be added)
- Framework: TBD
- State management: TBD
- Styling: TBD

### Development Dependencies (recommended)
- TypeScript
- ESLint
- Prettier
- Testing framework (Jest, Vitest, etc.)

## Resources

- [Project README](./README.md)
- [Git Documentation](https://git-scm.com/doc)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/)

---

*This document should be updated as the project evolves and conventions are established.*
