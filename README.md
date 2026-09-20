# CLI Issue Tracker

A small Python command-line issue tracker built for Project 0.

## Features

* Add issues
* List saved issues
* Search issues by title
* Case-insensitive search
* JSON file persistence
* Empty-title validation
* Automated tests with `unittest`
* GitHub Actions CI
* Installable `issue-tracker` command

## Requirements

* Python 3.13 or newer
* Git

## Installation

Clone the repository:

```bash
git clone https://github.com/zayarhlakhin17-jpg/project-0-cli-issue-tracker.git
cd project-0-cli-issue-tracker
```

Install the project in editable mode:

```bash
python3 -m pip install -e .
```

## Usage

Show help:

```bash
issue-tracker --help
```

Add an issue:

```bash
issue-tracker add "Login broken"
```

List all issues:

```bash
issue-tracker list
```

Search issues:

```bash
issue-tracker search "login"
```

## Persistence

Issues are stored in `issues.json`.

An issue has this structure:

```json
{
  "title": "Login broken",
  "status": "open"
}
```

Saved issues remain available after the program exits and is started again.

## Validation

Empty or whitespace-only titles are rejected.

Example:

```bash
issue-tracker add "     "
```

## Tests

Run the full test suite:

```bash
python3 -m unittest discover -s tests -v
```

The test suite covers:

* valid title cleaning
* empty-title validation
* search matches
* case-insensitive search
* no-match search
* save/load persistence
* missing storage files
* invalid JSON storage

## Project Structure

```text
main.py       — command-line interface
tracker.py    — issue logic and validation
storage.py    — JSON persistence
tests/        — automated tests
pyproject.toml — packaging and CLI configuration
```

## CI

GitHub Actions automatically runs the Python test suite on pushes and pull requests.

## Version

Project 0 v1.0.0
