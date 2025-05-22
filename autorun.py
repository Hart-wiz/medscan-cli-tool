import subprocess

subprocess.run([
    "python", "medscan.py",
    "--file", "data/report.csv",
    "--panel", "panels/default_panel.json",
    "--output", "data/flagged_output.csv"
])
