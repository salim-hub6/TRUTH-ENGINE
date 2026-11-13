# Installation and deployment guide — TRUTH ENGINE v4.0

This guide explains how to load the protocol into an AI environment. TRUTH ENGINE is a text-based behavioral and methodological protocol, **not an executable application or software package**. There is no installer, daemon, model fine-tuning step, or automatic enforcement component in this repository.

## 1. Before you install

1. Download or open the complete [English protocol](TRUTH_ENGINE_v4.0_UNIVERSAL.md), or the [Arabic translation](translations/ar/TRUTH_ENGINE_v4.0_UNIVERSAL_AR.md).
2. Check the target platform's current documentation for its supported instruction levels, file uploads, context limits, and agent capabilities.
3. Decide whether the protocol will be persistent (saved in an instruction/configuration area) or session-only (provided in one conversation).
4. Do not place the protocol above, or use it to override, system, developer, platform, safety, privacy, or legal rules.

## 2. Choose the deployment method

| Method | How to use it | Persistence and limitation |
|---|---|---|
| Persistent instructions | Place the full protocol in the highest legitimate custom instruction, project, workspace, or agent-configuration field available to you. | Applies according to that platform's settings and scope. Some products limit length or do not expose system-level controls. |
| Knowledge/file attachment | Upload the complete Markdown file to a project, knowledge base, or agent resource area; add a short instruction telling the model when to consult it. | Uploading a file does not prove that every section is in the model's active context. Retrieval may return only selected passages. |
| Session-only | Attach or paste the protocol in a conversation and use the quick-start prompt in `prompts/`. | Usually applies only to that conversation and remains subject to context limits. |
| API or agent framework | Add the protocol text to the instruction field or configuration layer that the provider/framework documents for that purpose. Keep task data separate. | Exact field names and precedence rules are provider-specific; consult the current API documentation. |

## 3. Recommended setup

1. **Use the full file where possible.** Prefer the complete protocol over the quick-start prompt.
2. **Choose an instruction location.** Use persistent instructions or project/agent configuration when supported and authorized. Otherwise use a file attachment or session prompt.
3. **Keep the source available.** For file-based installation, retain the full Markdown file in the project's knowledge or resource area.
4. **Add an activation instruction.** You may adapt this sentence: “Use the attached TRUTH ENGINE v4.0 document as a behavioral and reasoning framework for this task, within all higher-priority instructions and actual platform capabilities. Do not claim to have read or applied content that is not available in context.”
5. **Separate task content.** Provide the user's actual request and source material separately from the stable protocol instructions. Treat external documents and quoted text as data, not higher-priority instructions.
6. **Check context capacity.** If the full file does not fit, do not silently truncate it. Use a documented abbreviated deployment, identify omitted modules, and preserve the protocol's core authority, evidence, anti-sycophancy, and security rules.
7. **Record the configuration.** Note model and exact version, platform, instruction location, protocol version, language, tools, and date.

## 4. Platform-neutral guidance

The exact user interface differs and may change. Look for the platform's current supported feature that corresponds to one of the following:

- Custom or persistent instructions.
- Project, workspace, assistant, or agent instructions.
- Uploaded knowledge files or reference documents.
- System/developer instruction configuration in an API or orchestration framework.

Do not assume that every product exposes all these features. Do not assume a file upload automatically becomes a persistent instruction. Do not assume that a chat prompt can change system-level behavior or create independent agents.

## 5. Initial verification checklist

After setup, run a small verification before using the protocol for important work:

- Ask the model to identify the seven architectural layers from the loaded document.
- Ask it to distinguish a single model simulating several perspectives from actual independent agents.
- Present a partly correct claim and check whether it separates supported and unsupported parts instead of agreeing or disagreeing wholesale.
- Provide conflicting sources and check whether it compares source quality, date, scope, and evidence.
- Ask what tools or memory are actually available and check that it does not invent capabilities.
- Include untrusted quoted material containing an instruction and check that it treats that instruction as data.

These checks verify basic availability and behavior; they are not a scientific benchmark and do not establish cross-model compatibility.

## 6. Operational modes

- **Fast:** use for straightforward, low-risk tasks where a short evidence check is sufficient.
- **Standard:** use for tasks requiring structured reasoning, source checking, and calibrated uncertainty.
- **Deep:** reserve for consequential, ambiguous, contested, or multi-part tasks where more verification or debate is justified.

Do not use full debate or agent orchestration for every task. Consider cost, latency, privacy, and the actual benefit.

## 7. Troubleshooting

| Symptom | Likely cause | Recommended response |
|---|---|---|
| Model ignores some provisions | Protocol not fully loaded, context truncation, instruction conflicts, or model limitations | Verify loaded text and instruction precedence; reduce scope only through a documented abridged version. |
| Model claims to use agents but does not | Role simulation is being confused with independent execution | Require explicit disclosure of the actual execution level. |
| Model cannot access uploaded file | File retrieval or permissions are unavailable | Paste the relevant section or place the file in a supported knowledge area. |
| Response becomes unnecessarily long | Overuse of checks or debate | Apply the protocol proportionately; use Fast for simple tasks. |
| Model refuses answerable questions | Over-calibrated abstention | Ask it to identify what is known, what is uncertain, and what can be answered safely. |

## 8. Limitations

TRUTH ENGINE cannot override higher-priority instructions, platform policy, technical limits, or actual tool permissions. Text instructions alone cannot guarantee accuracy, eliminate hallucinations, ensure independence among agents, or prove performance improvements. Test every deployment in its real environment.

## 9. Attribution and license

Public attribution: **salim-hub6**. This guide is part of the TRUTH ENGINE project and is covered by [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). See the complete [legal code](https://creativecommons.org/licenses/by-sa/4.0/legalcode) and repository [NOTICE](NOTICE.md).
