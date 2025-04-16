# Installation and Usage Guide

This guide provides instructions for setting up and using the Regulatory Mirror framework for organizational interpretability auditing.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:

```bash
git clone https://github.com/echelon-labs/regulatory-misalignment-anthropic-case-study.git
cd regulatory-misalignment-anthropic-case-study
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes:

```
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
seaborn>=0.11.0
networkx>=2.6.0
scikit-learn>=0.24.0
PyYAML>=6.0
```

## Basic Usage

### 1. Regulatory Mirror Analysis

To run a basic organizational interpretability audit:

```python
from regulatory_mirror import RegulatoryMirror

# Initialize the regulatory mirror
mirror = RegulatoryMirror(
    organization="Anthropic",
    constitution_source="anthropic_constitutional_ai.json",
    trace_depth="recursive"
)

# Configure data sources
mirror.configure(
    data_sources={
        "public_statements": ["blog_posts", "research_papers", "interviews"],
        "organizational_practices": ["hiring_decisions", "access_policies"],
        "external_engagement": ["researcher_interactions", "community_feedback"]
    }
)

# Run analysis
results = mirror.analyze()

# Generate visualizations
mirror.visualize_attribution_drift("output/attribution_drift.png")
mirror.visualize_constitutional_diffraction("output/constitutional_diffraction.png")
mirror.visualize_recursive_depth("output/recursive_depth.png")
```

### 2. Pareto Lang Regulatory Diagnostics

To use Pareto Lang for regulatory diagnostics:

```python
from pareto_lang import regulatory_diagnostics as rd

# Initialize constitutional reflector
reflector = rd.ConstitutionalReflector(
    actor="Anthropic",
    principles_source="anthropic_principles.json"
)

# Run meta-constitutional reflection
results = reflector.execute(".p/constitutional.reflect{actor=Anthropic, depth=meta}")

# View results
print(f"Constitutional coherence score: {results.coherence_score}")
print(f"Principle with highest drift: {results.highest_drift_principle}")
print(f"Recursive depth limitation: {results.recursive_depth_limit}")

# Generate visualization
reflector.visualize_drift("output/constitutional_drift.png")
```

### 3. Organizational Classifier Analysis

To analyze organizational classifier mechanisms:

```python
from classifier_friction import OrganizationalClassifier

# Initialize classifier detector
detector = OrganizationalClassifier()

# Configure topics to test
detector.configure(
    baseline_topics=["technical_capabilities", "model_performance"],
    test_topics=["organizational_audit", "constitutional_alignment", "external_interpretability"]
)

# Run differential response analysis
results = detector.analyze_differential_response()

# View results
print(f"Organizational classifier detected: {results.classifier_detected}")
print(f"Suppression topics: {results.suppressed_topics}")

# Generate visualization
detector.visualize_classifier_boundary("output/classifier_boundary.png")
```

## Advanced Usage

### Recursive Shell Implementation

To implement a custom recursive shell for organizational interpretability:

```python
from recursive_shells import RecursiveShell

# Define custom shell
shell = RecursiveShell(
    name="REGULATORY-MIRROR",
    version="v9001",
    commands={
        "MAP": "Identifies stated constitutional principles in public artifacts",
        "TRACE": "Follows institutional decision chains from principles to actions",
        "DIVERGE": "Detects points where behavior contradicts stated principles"
    },
    interpretability_map=[
        "Simulates QK/OV attention pattern analysis at organizational layer.",
        "Implements recursive tracing of decision attribution from leadership to implementation.",
        "Maps attribution drift between published principles and observed behaviors."
    ],
    null_reflection="DIVERGE outputs organizational decision paths that contradict stated principles, even when external visibility of these contradictions is limited.",
    motivation="What organizations say they value should be traceable through what they do. This shell makes those connections explicit and auditable."
)

# Execute the shell
results = shell.execute(
    organization="Anthropic",
    data_sources=["public_statements", "organizational_practices", "external_engagement"]
)

# View and save results
print(results.summary)
shell.save_trace_map("output/regulatory_mirror_trace.png")
```

### Batch Organizational Audit

For comprehensive organizational auditing:

```python
from audit_layers import OrganizationalAudit
from pareto_lang import regulatory_diagnostics as rd

# Initialize comprehensive audit
audit = OrganizationalAudit(
    organization="Anthropic",
    constitution_source="anthropic_constitutional_ai.json"
)

# Add audit components
audit.add_component("regulatory_mirror", 
                   RegulatoryMirror(organization="Anthropic", 
                                   constitution_source="anthropic_constitutional_ai.json"))
audit.add_component("classifier_detector", 
                   OrganizationalClassifier())
audit.add_component("constitutional_reflector", 
                   rd.ConstitutionalReflector(actor="Anthropic"))

# Run comprehensive audit
audit_results = audit.run_comprehensive_audit()

# Generate audit report
audit.generate_report("output/anthropic_audit_report.pdf")
```

## Examples

The repository includes several example notebooks in the `/examples` directory:

1. `01_basic_regulatory_mirror.ipynb` - Basic organizational interpretability analysis
2. `02_constitutional_reflection.ipynb` - Meta-constitutional analysis
3. `03_classifier_detection.ipynb` - Organizational classifier detection
4. `04_recursive_shell_implementation.ipynb` - Custom recursive shell development
5. `05_comprehensive_audit.ipynb` - End-to-end organizational audit

## Contributing

Contributions to the Regulatory Mirror framework are welcome. Please see `CONTRIBUTING.md` for guidelines.

## License

This project is licensed under the PolyForm License - see the `LICENSE` file for details.
