

































































































<div align="center">
🛡️ SentinelGraph AI
Explainable security-event investigations, visualized
An educational cybersecurity investigation prototype with a Streamlit dashboard, transparent detection rules, relationship graphs, and a planned read-only API.




License



Concept animation, not a screen recording of the current application. AI chat and incident resolution shown in the concept are not implemented.

Overview • Current status • Architecture • Getting started • Roadmap

</div>
Overview
SentinelGraph AI demonstrates how security analysts can explore synthetic authentication events, inspect explainable rule-based alerts, and visualize connections between events, users, devices, and IP addresses. The dashboard is written in Streamlit using Plotly and NetworkX.
[!IMPORTANT]
Educational prototype, not a production SIEM or validated AI threat detector. No live security telemetry, trained ML model, LLM assistant, live threat feeds, or autonomous incident response are included. Rule-based scores are illustrative weights, not probabilities.
Current repository status
The public GitHub repository currently contains app.py, pyproject.toml, Dockerfile, LICENSE, README.md, and sentinelgraph-demo.gif. The sentinelgraph/ source package, tests/, and GitHub Actions workflow have not been uploaded yet, so the app cannot run from the current repository as-is.
Capability	Status
Streamlit metrics, alert queue, filtering and charts	UI code present in app.py; requires missing core module
Selected event explanations	UI code present; requires missing core module
NetworkX/Plotly entity graph	UI code present; requires missing core module
CSV export	UI code present; requires missing core module
Synthetic event generator and scoring	Imported by dashboard; sentinelgraph/core.py missing
FastAPI read-only API	Dependency installed; sentinelgraph/api.py missing
Automated tests and GitHub Actions	Not yet uploaded
Dockerfile	Present; requires restored source package
Animated preview	Concept GIF at repository root
Architecture
Risk-scoring methodology
Detection trigger	Illustrative points
Failed authentication	+25
Previously unseen device	+25
Unusual country	+35
Outside typical hours	+15
Severity thresholds are low 0–24, medium 25–49, high 50–74, and critical 75–100. These are hand-selected demo values, not validated risk estimates.
Getting started
Requirements: Python 3.10+ and Git. First restore the missing sentinelgraph/ Python package.
git clone https://github.com/tasnem-tech/sentinelgraph-ai.git
cd sentinelgraph-ai
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
streamlit run app.py
On Windows, activate with .venv\Scripts\activate instead. When the missing core module is present, open http://localhost:8501.
API (after uploading its module)
uvicorn sentinelgraph.api:app --reload
Interactive documentation will then be available at http://127.0.0.1:8000/docs.
Docker (after restoring source files)
docker build -t sentinelgraph-ai .
docker run --rm -p 8501:8501 sentinelgraph-ai
Testing and quality
Once the test files and Python package are uploaded:
ruff check sentinelgraph tests
pytest -q
No GitHub Actions success or passing test badge is claimed until a workflow is uploaded and run.
Repository structure
sentinelgraph-ai/
├── README.md
├── LICENSE
├── app.py
├── pyproject.toml
├── Dockerfile
├── sentinelgraph-demo.gif
├── sentinelgraph/             # Missing from public repository
│   ├── __init__.py
│   ├── core.py
│   └── api.py
├── tests/                     # Missing from public repository
└── .github/workflows/ci.yml   # Missing from public repository
Roadmap
Upload missing source package and tests
Add and verify GitHub Actions workflow
Replace concept GIF with real dashboard recording
Persist event history and investigations
Add authentication and authorization
Expand cross-event relationship analysis
Benchmark detection rules on labelled datasets
Experiment with reproducible ML anomaly detection
Add evidence-grounded AI explanations with human oversight
Add monitoring and deployment documentation
Responsible use
This project is for learning and demonstration. Never submit real customer logs, credentials, or personal data to this prototype. Synthetic data cannot establish real-world detection accuracy, and the scores should not be used alone for enforcement decisions.
Contributing
Contributions and bug reports are welcome. Include reproducible steps for defects, tests for behavior changes, and no sensitive logs or credentials.
License
MIT. See LICENSE.
<div align="center">
Built as an educational security analytics and software engineering portfolio project.
View repository · Report an issue
</div>



