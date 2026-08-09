# Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.
# Unauthorized copying, modification, or distribution is prohibited.
# https://github.com/Debashis2007

"""Education Restricted Modes — thin self-contained FastAPI POC."""

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from poc_core import MockLLM, TokenBucket, health_payload, AUTHOR_NAME, AUTHOR_FINGERPRINT, AUTHOR_GITHUB
from poc_core.safety import SafetyPlane
from poc_core.stores import InMemoryStore, MockVectorIndex

USE_CASE = "Education Restricted Modes"
app = FastAPI(title=USE_CASE)
llm = MockLLM()
store = InMemoryStore()
safety = SafetyPlane()

@app.get("/health")
def health():
    return health_payload(
        USE_CASE,
        {
            "author": AUTHOR_NAME,
            "author_github": AUTHOR_GITHUB,
            "fingerprint": AUTHOR_FINGERPRINT,
        },
    )

@app.get("/author")
def author():
    return {
        "author": AUTHOR_NAME,
        "github": AUTHOR_GITHUB,
        "fingerprint": AUTHOR_FINGERPRINT,
        "notice": "Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.",
    }


class ChatIn(BaseModel):
    profile: str = "education"
    prompt: str

@app.post("/chat")
async def chat(body: ChatIn):
    tools_allowed = [] if body.profile in {"education", "family"} else ["code", "browser"]
    d = safety.check_input(body.prompt)
    if "code" in body.prompt.lower() and "code" not in tools_allowed:
        return {"action": "refuse", "reason_code": "tool_disabled_in_restricted_mode", "tools_allowed": tools_allowed}
    if d.action != "allow":
        return {"action": d.action, "reason_code": d.reason_code}
    return {"action": "allow", "text": await llm.complete(body.prompt, max_tokens=10), "tools_allowed": tools_allowed}
