# TRUTH ENGINE v4.0

**Universal Model-Agnostic Epistemic Integrity, Evidence-First Reasoning & Multi-Agent Verification Protocol**

[العربية](README_AR.md) · [Installation guide](INSTALLATION.md) · [Protocol (English)](TRUTH_ENGINE_v4.0_UNIVERSAL.md) · [Arabic protocol](translations/ar/TRUTH_ENGINE_v4.0_UNIVERSAL_AR.md)

> **Release status:** First public edition; experimental and subject to evaluation.  
> **Design goal:** Universal in principles. Capability-aware in execution. Evidence-led in judgment.

TRUTH ENGINE is a provider-neutral behavioral and methodological protocol for improving the epistemic integrity of AI assistants, models, agents, and agentic systems. It organizes work around evidence quality, sound reasoning, calibrated uncertainty, constructive criticism, verification, multi-agent coordination, and security.

It is designed to be adapted across model families and platforms, including (without limitation) OpenAI, Google Gemini, xAI Grok, Moonshot AI Kimi, and other current or future systems.

## Important compatibility statement

TRUTH ENGINE does **not** guarantee that every model will follow the protocol in the same way or achieve the same level of performance. Models and platforms differ in instruction hierarchies, context limits, tool access, memory, function calling, reasoning behavior, and support for independent agents or sub-agents.

The project **aims to improve cross-model portability over time** through clearer provider-neutral instructions, capability-aware adaptations, common evaluation tasks, and published compatibility results. This is an ongoing objective, not a claim that universal compatibility has already been achieved. Do not claim compatibility with a model or platform unless it has been tested and the test scope is documented.

## What is included

```text
TRUTH-ENGINE/
├── README.md
├── README_AR.md
├── INSTALLATION.md
├── INSTALLATION_AR.md
├── LICENSE
├── NOTICE.md
├── CHANGELOG.md
├── TRUTH_ENGINE_v4.0_UNIVERSAL.md
├── translations/
│   └── ar/
│       └── TRUTH_ENGINE_v4.0_UNIVERSAL_AR.md
├── prompts/
│   ├── QUICK_START_PROMPT.md
│   └── QUICK_START_PROMPT_AR.md
├── examples/
│   ├── ILLUSTRATIVE_EXAMPLES.md
│   └── ILLUSTRATIVE_EXAMPLES_AR.md
└── evaluation/
    ├── EVALUATION_GUIDE.md
    └── EVALUATION_GUIDE_AR.md
```

The English protocol is the canonical reference edition for this repository. The Arabic protocol is a parallel translation intended to preserve the same scope and meaning. Report any substantive translation discrepancy through GitHub Issues.

## Core architecture

TRUTH ENGINE v4.0 preserves the seven-layer architecture:

1. Question, intent, and assumption analysis.
2. Knowledge, evidence, and source verification.
3. Reasoning, logic, and causal analysis.
4. Multiple perspectives and debate.
5. Audit, external verification, and adjudication.
6. Confidence calibration, uncertainty, and abstention.
7. Final judgment and communication.

Cross-cutting safeguards address sycophancy, cognitive and social bias, hallucination, prompt injection, tool and agent security, rational updating, evaluation, and continuous improvement.

When debate is warranted, the protocol defines three roles: Independent Analyst, Adversarial Critic, and Independent Auditor. It also defines a coordinator and sub-agent operating contract. It distinguishes a single model simulating multiple perspectives from multiple calls and genuinely independent agents or models.

## Quick start

1. Read the complete [TRUTH ENGINE v4.0 protocol](TRUTH_ENGINE_v4.0_UNIVERSAL.md).
2. Follow the [installation guide](INSTALLATION.md) for the highest legitimate instruction level your platform supports.
3. Keep stable protocol instructions separate from task-specific requests and untrusted source material.
4. Confirm which tools, memory, file access, and agent capabilities are actually available. The protocol cannot create capabilities the platform does not provide.
5. Select Fast, Standard, or Deep operation in proportion to the task's stakes and complexity.
6. Use debate or multiple agents only when their expected benefit justifies their cost. Do not describe simulated roles as independent agents.
7. Evaluate the protocol on representative tasks before relying on it in consequential workflows.

For a session-only start, use the [Quick-start prompt](prompts/QUICK_START_PROMPT.md) together with the full protocol file. The quick-start prompt is **not** a substitute for the full protocol.

## Constructive critical partnership

A governing principle is:

> Do not flatter the user at the expense of truth, and do not disagree merely for the sake of disagreement.

The protocol calls for evidence-based agreement when an idea is sound, clear correction when it is wrong, separation of correct and incorrect parts when it is partly right, practical development when it is incomplete, and test design when it is innovative but unproven. It distinguishes factual errors from differences in taste, preference, or values.

## Evaluation: what is and is not claimed

Sections 42–43 of the protocol define a **proposed 70-case evaluation framework by category**: 50 core cases plus 20 additional cases. They specify category counts and evaluation targets, but this release does **not** include 70 finalized, individually written test prompts or independent benchmark results. See the [evaluation guide](evaluation/EVALUATION_GUIDE.md) for a reproducible test procedure and reporting template.

No benchmark result or performance improvement is claimed by this release. Compare a baseline model, available earlier protocol versions, v4.0, v4.0 with tools, and genuine independent-agent configurations only when each condition can actually be run and documented.

## License and attribution

The original written protocol and documentation in this repository are licensed under **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**.

- [License summary](https://creativecommons.org/licenses/by-sa/4.0/)
- [Complete legal code](https://creativecommons.org/licenses/by-sa/4.0/legalcode)
- SPDX identifier: `CC-BY-SA-4.0`
- Public project attribution requested: **salim-hub6**

You may share and adapt covered material, including commercially, provided you follow the license terms. In particular, give appropriate credit, link to the license, identify changes, and apply the same or a Creative Commons BY-SA-compatible license to distributed adaptations. The license does not grant rights to project trademarks, logos, or endorsement. See [LICENSE](LICENSE) and [NOTICE](NOTICE.md). This is a project notice, not legal advice.

**Suggested attribution:**

> TRUTH ENGINE v4.0 by salim-hub6. Source: https://github.com/salim-hub6/TRUTH-ENGINE. Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Changes: [describe changes, or state “No changes”].

## Contributions and change control

Please preserve attribution and the license notice. When proposing changes:

- Identify the problem the change addresses.
- Explain the evidence or rationale.
- State expected benefits, costs, side effects, and compatibility implications.
- Add or update tests where practical.
- Do not remove a prior requirement without explaining why.
- Distinguish tested behavior from an unverified proposal.

See [CHANGELOG.md](CHANGELOG.md) for the release record. Future protocol changes should be versioned and accompanied by an explanation of the rationale, trade-offs, and test results.

## Disclaimer

TRUTH ENGINE is provided “as is” and “as available.” It does not guarantee prevention of hallucinations, sycophancy, unsafe behavior, or errors. It does not replace platform safeguards, independent evaluation, professional judgment, or technical access controls. Every deployment must be adapted and evaluated in its actual environment.

## Repository

- Public repository: https://github.com/salim-hub6/TRUTH-ENGINE
- Clone URL: `https://github.com/salim-hub6/TRUTH-ENGINE.git`
