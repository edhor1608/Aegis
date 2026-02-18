# App Center Policy

## Policy Goal

- Keep zero-config behavior for normal users while preserving controlled flexibility.
- Prioritize safe defaults over broad choice at first contact.

## Catalog Structure

1. Curated default catalog
- Shows pre-approved apps for common senior workflows.
2. More Apps catalog
- Separate path for broader package access when needed.

## Warning Gate

- Entering More Apps requires explicit warning acknowledgment.
- Warning text explains stability and support tradeoffs in simple language.
- Default curated path remains one-click and noise-free.

## Repository Rules

- Debian Stable repositories are the baseline source of packages.
- No uncontrolled third-party repositories in v1 baseline.
- Any exception requires explicit policy review and documentation.

## Operational Governance

- Curated catalog reviewed on each 6-month care release cycle.
- Security-sensitive app changes can be patched between care releases.
- Policy keeps advanced package mechanics outside normal user flow.
