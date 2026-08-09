# Use Case: Education / Restricted Modes

**YouTube walkthrough:** [Education Restricted Modes — System Design #Shorts](https://youtu.be/BOjgD6GmfGU)

**Design doc:** [docs/DESIGN.md](./docs/DESIGN.md) — architecture, patterns, and why.


**Parent system design:** [06 — Multi-Layer Safety / Moderation](../06-safety-moderation-pipeline.md)

## Users & problem

Schools and family products need a stricter mode: more fail-closed categories, tighter tools, and age-appropriate refusals.

## Requirements & SLOs

| Requirement | Target |
|-------------|--------|
| Mode flag | Per-user / org / device profile |
| Default | Fail-closed on broad sensitive set |
| Tools | Disable browsing/code or sandbox harder |
| Override | Admin-only relaxations |

## Design (from parent)

```
User profile (education/family) → restricted policy pack
  → stricter L1/L2 thresholds
  → tool allowlist reduced ([07](../07-agent-runtime-containment.md))
  → extra audit to school admin (policy-permitting)
```

## Specializations

| Concern | Education choice |
|---------|------------------|
| UX | Softer language; suggest teacher/parent |
| Accounts | Guardian linkage |
| Eval | Separate red-team suites for minors-adjacent |
| Mixing | Never mix restricted and adult sessions casually |

## Failure modes

- Profile mis-tagged adult → default safe when unknown.
- Tool bypass → permissions in runtime, not model text.
- False comfort → still maintain global critical filters.




## Design walkthrough (opens on GitHub)

> **Watch on YouTube:** [Education Restricted Modes — System Design #Shorts](https://youtu.be/BOjgD6GmfGU)


![Design overview](docs/video/design-overview.gif)

Full narrated video (download): [docs/video/design-overview.mp4](docs/video/design-overview.mp4)

## Run (self-contained POC)

This folder is a **standalone** project (safe to split into its own GitHub repo).

```bash
cd education-restricted-modes
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
PYTHONPATH=. python -m uvicorn app.main:app --reload --port 8000
```

```bash
curl -s http://127.0.0.1:8000/health | jq
```

curl -s -X POST http://127.0.0.1:8000/chat -H 'Content-Type: application/json' -d '{"profile":"education","prompt":"run code please"}' | jq
