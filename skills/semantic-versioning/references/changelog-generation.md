# Changelog Generation

## Changelog Generation

```bash
#!/bin/bash
# generate-changelog.sh

# Using conventional-changelog CLI
conventional-changelog -p angular -i CHANGELOG.md -s

# Or manually format changelog
CHANGELOG="# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
