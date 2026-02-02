# OWASP Guardian Skill

- **Name**: `scanning-security`
- **Description**: Enforces OWASP Top 10 and OWASP LLM Top 10 compliance via Semgrep scanning. Use when the user mentions security scan, code audit, deployment prep, vulnerability check, or asks "is this safe?" Acts as a pre-commit gatekeeper

## OWASP Guardian

A strict security engineering skill that blocks insecure code and generates audit evidence.

## When to use this skill

- User says "scan this code" or "security check"
- Before declaring any task complete (run scan as verification)
- Preparing code for deployment
- User asks "is this safe?"
- Fixing security issues

## Tools

| Script                       | Purpose                                      |
| ---------------------------- | -------------------------------------------- |
| `scripts/run_sast.py`        | Runs Semgrep scan, returns JSON findings     |
| `scripts/generate_report.py` | Creates timestamped Security Decision Record |

## The Guardian Loop

### Phase 1: OBSERVE (Scan)

```bash
python .agent/skills/owasp-guardian/scripts/run_sast.py
```

> [!CAUTION]
> If status is `"vulnerable"`, **STOP immediately**. Do not continue feature work. List findings to user.

### Phase 2: REASON (Manual Check)

Even if scan returns clean, check for AI-specific risks that static analysis misses:

- [ ] **LLM01 Prompt Injection**: Are user inputs wrapped in delimiters?
- [ ] **LLM02 Insecure Output**: Is `eval()`, `exec()`, or `innerHTML` used with AI output?
- [ ] **LLM06 Excessive Agency**: Does agent have delete permissions without confirmation?
- [ ] **Hardcoded Secrets**: Did user paste a key the tool missed?

### Phase 3: ACT (Fix)

Apply these remediation patterns:

| Risk              | Fix Pattern                                |
| ----------------- | ------------------------------------------ |
| Hardcoded secrets | Move to `.env`                             |
| SQL injection     | Use parameterized queries (no f-strings)   |
| Prompt injection  | Wrap user input in `<user_input>` tags     |

After fixing, **run scan again** to verify.

### Phase 4: EVIDENCE (Audit Trail)

Once secure, ask: *"Shall I generate the compliance record?"*

If yes:

```bash
python .agent/skills/owasp-guardian/scripts/generate_report.py \
  --component "ComponentName" \
  --findings "Description of mitigations applied"
```

## Setup

Install Semgrep (one-time):

```bash
pip install semgrep>=1.50.0
```
