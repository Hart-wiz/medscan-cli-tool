import argparse
import pandas as pd
import json
import os

# Default reference ranges (can be overridden)
DEFAULT_RANGES = {
    "Glucose": {"min": 70, "max": 140},
    "Cholesterol": {"min": 120, "max": 200},
    "Hemoglobin": {"min": 12, "max": 17.5}
}

def load_reference_panel(panel_path):
    if not panel_path:
        return DEFAULT_RANGES
    with open(panel_path, 'r') as f:
        return json.load(f)

def flag_out_of_range(df, reference_ranges):
    flagged = []
    for _, row in df.iterrows():
        test = row['TestName']
        value = float(row['Result'])
        if test in reference_ranges:
            ref = reference_ranges[test]
            if value < ref['min']:
                flagged.append({**row, "Flag": "Low"})
            elif value > ref['max']:
                flagged.append({**row, "Flag": "High"})
    return pd.DataFrame(flagged)

def main():
    parser = argparse.ArgumentParser(description="MedScan CLI Tool")
    parser.add_argument('--file', required=True, help='Path to the lab CSV file')
    parser.add_argument('--panel', help='JSON file with reference ranges')
    parser.add_argument('--output', help='Save flagged results to this CSV')

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"❌ File not found: {args.file}")
        return

    df = pd.read_csv(args.file)
    ref_ranges = load_reference_panel(args.panel)
    flagged_df = flag_out_of_range(df, ref_ranges)

    if flagged_df.empty:
        print("✅ All values within range.")
    else:
        print("⚠️ Abnormal results:")
        for _, row in flagged_df.iterrows():
            print(f"[{row['Flag']}] {row['PatientID']} - {row['TestName']}: {row['Result']} {row['Unit']}")
        if args.output:
            flagged_df.to_csv(args.output, index=False)
            print(f"\n📁 Output saved to: {args.output}")

if __name__ == "__main__":
    main()
