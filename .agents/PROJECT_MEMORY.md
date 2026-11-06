# Project Memory: AI User-Tester (Synthetic Usability Engine)

## Product Summary & Architecture
- **Repository:** `https://github.com/Skill-AI-private/User-tester.git`
- **Core Purpose:** AI-powered synthetic user testing engine using Playwright, Vision LLM, and Think-Aloud Protocol to evaluate web usability, detect cognitive friction points, and calculate System Usability Scale (SUS) scores.
- **Key Reference Projects:** `neuhai/UXAgent`, `UXCascade`, `Avenir-UX`, `de6eling/user-testing-agent`, `browser-use`.

## Completed Modules
- **`README.md`**: Complete documentation covering the distinction between functional QA testers and AI synthetic users, global open-source project research, architecture diagrams, and quickstart guide.
- **`personas/`**: Pre-configured user persona YAMLs (`senior_user.yaml`, `busy_shopper.yaml`, `tech_savvy.yaml`).
- **`src/`**:
  - `prompts.py`: Persona Think-Aloud prompts, JSON output schemas, and SUS survey questionnaires.
  - `agent.py`: Playwright browsing agent with screenshot capture, Think-Aloud evaluation, and fallback demo mode.
  - `reporter.py`: System Usability Scale (SUS) mathematical scoring and Markdown report generator.
- **`main.py`**: CLI entry point supporting `--url`, `--persona`, `--goal`, `--steps`, `--headless`.
- **`reports/sample_ux_report.md`**: Sample end-to-end usability evaluation deliverable.

## Status & Boundaries
- All 13 core files committed and pushed to `origin/main` (commit `5196cf5`).
- Remote working tree clean and up-to-date.
