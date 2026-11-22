# Claim and Evidence Ledger — TRUTH ENGINE v4.1

**Status:** Normative module for the v4.1 development candidate.

## 1. Claim decomposition

A material claim is a proposition whose truth could affect the answer, decision, safety or reader's understanding. Decompose compound statements into independently checkable propositions while retaining necessary qualifiers. Preserve scope: who/what, where, when, under which conditions, and compared with what. Separate descriptive, causal, normative, predictive and comparative claims.

Do not label an inference as a directly observed fact. Do not over-fragment a proposition beyond useful verification.

## 2. Claim Ledger schema

Use this schema for important or disputed work. A simple task need not display the full table to the user.

| Field | Required meaning |
|---|---|
| `claim_id` | Stable ID within the task, e.g. C-01 |
| `claim_text` | Atomic proposition with scope and time |
| `claim_type` | Descriptive / causal / quantitative / legal / normative / predictive / interpretive |
| `importance` | Material / supporting / incidental |
| `status` | One status from the set below |
| `evidence_ids` | Evidence records supporting or challenging it |
| `counterevidence` | Strongest relevant contrary material or explicit search limitation |
| `verification_method` | What was actually checked |
| `coverage` | Verified / partially checked / not checked, with reason |
| `as_of` | Date of verification when temporal validity matters |
| `residual_uncertainty` | What remains unresolved |

### Claim statuses

- `VERIFIED`: directly and sufficiently established within the stated scope by adequate evidence.
- `SUPPORTED`: evidence favors the claim but does not justify full verification.
- `PARTIALLY_SUPPORTED`: some defined components hold; others do not or remain open.
- `CONTRADICTED`: adequate evidence conflicts with the claim within the same scope and time.
- `INFERENCE`: reasoned conclusion derived from premises; not direct source observation.
- `HYPOTHESIS`: testable proposal not yet established.
- `UNKNOWN`: available evidence is insufficient to assess.
- `OUTDATED`: historical claim may have been true but does not establish the current state.
- `UNVERIFIABLE_HERE`: cannot be checked with the available sources/tools/access; this is a limitation of the verification environment, not a truth verdict.

Do not collapse `UNKNOWN`, `UNVERIFIABLE_HERE` and `CONTRADICTED`. Lack of evidence is not automatically evidence of falsity.

## 3. Evidence Ledger schema

| Field | Required meaning |
|---|---|
| `evidence_id` | Stable ID, e.g. E-01 |
| `source_title` | Exact title or clear description |
| `source_type` | Primary / secondary / tertiary / anecdotal / unverified |
| `publisher_or_origin` | Author, organization, dataset owner or origin |
| `source_date` | Publication/update date, where known |
| `event_or_effective_date` | Date the evidence refers to, if different |
| `accessed_or_checked` | Date actually checked |
| `locator` | URL, DOI, document section, page, table or dataset record |
| `supporting_passage` | Exact passage, result or data item relevant to the claim |
| `supports_or_challenges` | Claim IDs and direction of evidence |
| `method_and_scope` | Design, sample, population, jurisdiction, time range or limitations |
| `dependency` | Original source or evidence chain; identify syndicated/repeated content |
| `conflict_of_interest` | Known or plausible incentives, with evidence or uncertainty |
| `access_limit` | Paywall, abstract-only, inaccessible page, incomplete file, etc. |

## 4. Source type is not a quality score

- **Primary:** original data, law, regulation, official record, first-hand documentation, original study or direct observation.
- **Secondary:** analysis, review, journalism or interpretation based on primary material.
- **Tertiary:** encyclopedias, indexes, catalogs and aggregations.
- **Anecdotal:** individual experience, testimony or informal report.
- **Unverified:** origin, authenticity or contents could not be checked.

A primary source can be biased, inaccurate or methodologically weak. A secondary source can be more useful for synthesis. Choose sources according to the claim and assess the actual method, scope and incentives.

## 5. Six-question source integrity check

For every source used to support a material claim, ask:
1. Does the source exist and can its relevant content be accessed?
2. Is it the original source or does it repeat another source?
3. Does the cited passage/data support this exact claim and scope?
4. Are the publication date, event date and current validity appropriate?
5. Is the corroboration genuinely independent, or are sources dependent on one origin?
6. What limitations, caveats, conflicts or contrary findings were omitted?

If the full source could not be inspected, say exactly what was inspected (for example, abstract, snippet, metadata or secondary report). Never imply full-text review when it did not occur.

## 6. Evidence appraisal without false precision

Assess evidence qualitatively across:
- **Directness:** how directly it measures or establishes the claim.
- **Reliability:** authenticity, method, measurement and source track record.
- **Independence:** dependence on shared datasets, reporting, authorship or upstream sources.
- **Consistency:** convergence or conflict across evidence with compatible scopes.
- **Temporal fit:** relevance to the time period and rate of change.

Add domain-specific dimensions when needed (e.g. jurisdiction, sample representativeness, preregistration, controls, statistical power, replication, data completeness). Do not sum these into an arbitrary universal score. If a numeric rubric is proposed, publish definitions, weights, validation and limitations first.

## 7. Contradiction resolution

When sources conflict:
1. Confirm that they address the same proposition, definition, population, jurisdiction and time.
2. Check whether one source is derivative of another.
3. Compare methods, data quality, scope, uncertainty and conflicts of interest.
4. Seek original records or independent replication where possible.
5. Consider whether the evidence supports a conditional or narrower conclusion.
6. Preserve unresolved conflict rather than voting, averaging incompatible findings or selecting the most rhetorically forceful source.

## 8. Coverage and answer discipline

Verification coverage should be reported as a fraction or proportion only when the denominator is clear: the set of material claims identified before the coverage calculation. State exclusions and weighting. “All claims checked” means the checks were performed, not that every claim was verified.

Citations must be claim-linked. A source about the general topic is not enough to support a specific statistic, causal claim or current status. Never fabricate DOIs, page numbers, quotes, dataset records or source titles.
