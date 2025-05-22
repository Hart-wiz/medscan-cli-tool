# 🧪 MedScan CLI Tool

A powerful Python-based command-line tool that processes CSV-format lab reports and flags out-of-range test results for rapid medical review.

Ideal for:

- Medical lab scientists
- Healthcare developers
- Research assistants
- Interns in clinical environments

---

## 🔧 Features

- ✅ **Batch CSV Analysis** – Process one or many lab reports at once
- ⚠️ **Out-of-Range Detection** – Highlights abnormal test values using reference ranges
- 🔁 **Custom Test Panels** – Load your own JSON panel definitions
- 📤 **Export Results** – Save flagged values into a clean CSV output file

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/hart-wiz/medscan-cli-tool.git
cd medscan-cli-tool
```

## install

pip install -r requirements.txt

## run with

python medscan.py --file data/sample_lab_report.csv --panel panels/default_panel.json --output data/flagged_output.csv
