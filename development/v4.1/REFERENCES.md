# References for TRUTH ENGINE v4.1 Development

These sources inform design choices; they do not prove that TRUTH ENGINE itself works or that results generalize to all models and deployments.

## Multi-agent debate and evaluation

1. Du, Y., Li, S., Torralba, A., Tenenbaum, J. B., & Mordatch, I. (2024). *Improving Factuality and Reasoning in Language Models through Multiagent Debate*. Proceedings of the 41st International Conference on Machine Learning, PMLR 235, 11733–11763. https://proceedings.mlr.press/v235/du24e.html
   - Reports gains in the authors' evaluated mathematical, strategic and factuality tasks. Treat this as task- and setup-specific evidence, not a universal guarantee.
2. Smit, A. P., Grinsztajn, N., Duckworth, P., Barrett, T. D., & Pretorius, A. (2024). *Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs*. ICML, PMLR 235, 45883–45905. https://proceedings.mlr.press/v235/smit24a.html
   - Finds that evaluated debate methods did not reliably outperform alternatives such as self-consistency and multi-path ensembling without strategy/hyperparameter tuning; some tuned methods performed better.
3. Kraidia, I., Qaddara, I., Almutairi, A., Alzaben, N., & Belhouari, S. B. (2026). *When collaboration fails: persuasion driven adversarial influence in multi agent large language model debate*. Scientific Reports 16, 11640. https://doi.org/10.1038/s41598-026-42705-7
   - Reports persuasion-driven influence in its tested multi-agent debate configurations. The paper's numerical effects are specific to its experimental setup and must not be generalized as a universal expected degradation rate.

## Uncertainty and calibration

4. Liu, X., Chen, T., Da, L., Chen, C., Lin, Z., & Wei, H. (2025). *Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey*. Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2, 6107–6117. https://doi.org/10.1145/3711896.3736569
5. Liu, Gabrielle Kaili-May, Yona, Gal, Caciularu, Avi, Szpektor, Idan, Rudner, Tim G. J., & Cohan, Arman (2025). *MetaFaith: Faithful Natural Language Uncertainty Expression in LLMs*. Google Research. https://research.google/pubs/metafaith-faithful-natural-language-uncertainty-expression-in-llms/
   - Relevant to the distinction between confidence wording and faithful expression of uncertainty. Reported improvements are study-specific.

## Security and risk management

6. OWASP. *LLM Prompt Injection Prevention Cheat Sheet*. https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html
   - Emphasizes defense in depth, tool-boundary permission enforcement, least privilege and action-specific human approval; text-only prompts are not a security boundary.
7. NIST. (2024). *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile* (NIST AI 600-1). https://doi.org/10.6028/NIST.AI.600-1
   - A risk-management resource for generative AI; not a technical security guarantee or a replacement for deployment-specific controls.

## Multilingual prompting

8. Kmainasi, M. B., Khan, R., Shahroor, A. E., Bendou, B., Hasanain, M., & Alam, F. (2025 publication of WISE 2024 work). *Native vs Non-Native Language Prompting: A Comparative Analysis*. Lecture Notes in Computer Science, 15440, 406–420. https://doi.org/10.1007/978-981-96-0576-7_30
   - Reports that non-native prompting performed best on average in the evaluated Arabic-related NLP tasks and model set. This does not establish English superiority for all models or all domains.
9. *Beyond English: The Impact of Prompt Translation Strategies across Languages and Tasks in Multilingual LLMs* (2025). Proceedings of LoResMT. https://aclanthology.org/2025.loresmt-1/
   - Studies selective translation of prompt components across 35 languages and multiple tasks; supports task- and language-dependent rather than universal translation decisions.
10. *Is Translation All You Need? A Study on Solving Multilingual Tasks with Large Language Models* (NAACL 2025). https://aclanthology.org/2025.naacl-long.485/
   - Finds translation can help some English-centric NLP tasks but is not universally optimal, particularly for culture-related tasks requiring native-language nuance.

## Use and citation policy

- Verify the current source and bibliographic metadata before release.
- Prefer the primary publication or official documentation.
- Cite a study only for the findings and scope it actually supports.
- Do not infer TRUTH ENGINE performance from background literature.