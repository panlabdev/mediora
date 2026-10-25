# Research protocol draft

## Population and setting
Define inclusion, exclusion and recruitment/source.

## Intended decision
Define what decision the system supports.

## Index time
Define when assessment occurs and what data are available then.

## Outcome
Define the reference standard and handling of uncertain diagnoses.
Distinguish confirmed current asthma from self-reported history.

## Predictors
Document units, timing, quality and missingness.
Exclude information obtained after the assessment time.

## Comparators
- Clinician-reviewed guideline-informed comparator
- Regularized logistic regression
- Nonlinear baseline if justified

## Modality comparison
Compare history/physiology against the same inputs plus hematology.
Account for changes in cohort caused by missing modalities.

## Validation
Split at patient level.
Fit preprocessing only on development data.
Preserve an untouched test set.
Consider temporal or external-site validation where feasible.

## Bias checks
Assess leakage, treatment effects, selection bias and label quality.
Address overlap between predictor tests and outcome definition.

## Evaluation
Prespecify discrimination, calibration, operating thresholds,
uncertainty intervals, subgroup analyses and abstention behavior.

## Sample size
Determine with statistical input.

## Governance
Document ethics determination, access rights, approved storage,
retention and permitted processing.

## Reporting
Use TRIPOD+AI as applicable.
Evaluate any LLM explanation component separately.
