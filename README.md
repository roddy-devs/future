# future

Personal infrastructure for always-on services and automation.

This repository contains a growing suite of Python-based Discord bots and background services used for coordination, notifications, and quality-of-life tooling for a private community.

## Structure
- Each bot runs independently
- Shared logic lives in a common core
- Designed for long-running execution on AWS EC2

## Current Capabilities
- Game session announcements via Discord slash commands
- Structured, readable notifications for small groups

## Future Direction
- Per-game notification subscriptions
- Queue and matchmaking helpers
- Additional always-on Discord utilities

## Tech
- Python
- discord.py
- AWS EC2
- Environment-based configuration

This repo is intentionally minimal and extensible.
