# Design: Education Restricted Modes

**Project:** `education-restricted-modes`  
**Parent system design:** [06 — Multi-Layer Safety / Moderation](../06-safety-moderation-pipeline.md) · [07 — Agent Runtime with Hard Containment](../07-agent-runtime-containment.md)

## 1. What this POC demonstrates

Restricted profiles disable tools and tighten policy regardless of model text.

## 2. Architecture (POC)

```text
profile → tools allowlist → safety → respond or refuse tool use
```

## 3. Patterns used (and why)

| Pattern | Why used | Where in code |
|---------|----------|---------------|
| Capability allowlist by profile | Permissions are runtime, not prompt text. | `tools_allowed`. |
| Default-safe unknown | Mis-tagged profiles should fail safe. | Education/family disables code. |
| Tool refuse reason | Clear UX for restricted modes. | `tool_disabled_in_restricted_mode`. |

## 4. Key endpoints

`GET /health`, `POST /chat`

## 5. Tradeoffs / POC limits

No guardian account linking — profile is a request field.

## 6. How to run

See the **Run (self-contained POC)** section in [`../README.md`](../README.md).

This folder is self-contained and can be published as its own GitHub repository.

## 7. Design walkthrough video

> **Watch on YouTube:** [Education Restricted Modes — System Design #Shorts](https://youtu.be/BOjgD6GmfGU)
>
> Direct link: **https://youtu.be/BOjgD6GmfGU**

Also available in-repo:
- GIF preview: [`video/design-overview.gif`](./video/design-overview.gif)
- MP4 download: [`video/design-overview.mp4`](./video/design-overview.mp4)
- Narration script: [`video/narration.txt`](./video/narration.txt)

---

**Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.**  
Unauthorized copying or redistribution of this material is prohibited.  
GitHub: [Debashis2007](https://github.com/Debashis2007)

