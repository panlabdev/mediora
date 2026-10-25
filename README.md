# Mediora

Status: planning and research.

Long-term vision: a multimodal health assessment system.
Initial focus: clinician-facing assessment support for adults
with suspected asthma.

This repository contains research infrastructure.
It does not contain a validated diagnostic model.

## First steps

1. Complete docs/PROJECT_CHARTER.md.
2. Review docs/RESEARCH_PROTOCOL.md with a supervisor and clinician.
3. Audit candidate datasets using docs/DATASET_REGISTER.csv.
4. Define the analysis plan before training models.

## Environment

    uv sync --locked
    uv run python scripts/check_environment.py
    uv run ruff check .

## Organization

- src/mediora: reusable research code
- notebooks: exploratory analysis
- configs: experiment configuration
- docs: versioned research documents and registers
- data: ignored local datasets
- artifacts: ignored models and intermediate outputs
- reports: non-sensitive research outputs

Google Docs holds collaborative drafts.
Approved protocol snapshots can be versioned here.

Patient records and credentials must not be committed.
