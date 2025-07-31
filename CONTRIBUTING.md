# Contributing to Metadata Eraser

First off, thank you for considering contributing to Metadata Eraser! It's people like you that make open source such a great community.

We welcome any type of contribution, not only code. You can help with:
- **Reporting a bug**
- **Discussing the current state of the code**
- **Submitting a fix**
- **Proposing new features**
- **Becoming a maintainer**

## Getting Started

To get started with development, you'll need to set up the project on your local machine.

1.  **Fork the repository** on GitHub.

2.  **Clone your fork** locally:
    ```bash
    git clone https://github.com/your-username/metadata_eraser.git
    cd metadata_eraser
    ```

3.  **Set up the development environment**:
    This project uses a virtual environment to manage dependencies.
    ```bash
    # Create a virtual environment
    python -m venv .venv

    # Activate the virtual environment
    # On Windows:
    # .\.venv\Scripts\activate
    # On macOS and Linux:
    source .venv/bin/activate

    # Install the project dependencies, including development tools
    pip install -e .[dev]
    ```

4.  **Create a branch** for your local development:
    ```bash
    git checkout -b name-of-your-bugfix-or-feature
    ```
    Now you can make your changes locally.

## Running Tests

To make sure everything is working correctly, please run the tests before submitting a pull request.
```bash
pytest
```

## Pull Request Process

1.  Ensure that all tests are passing.
2.  Make sure your code lints (we follow PEP 8).
3.  Commit your changes with a clear and descriptive commit message.
4.  Push your branch to your fork on GitHub.
5.  Open a pull request to the `main` branch of the original repository.
6.  In the pull request description, clearly explain the problem and solution. Include the relevant issue number if applicable.

## Code of Conduct

This project and everyone participating in it is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior.
