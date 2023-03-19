import argparse
import pandas
parser = argparse.ArgumentParser()
parser.add_argument("--output", required=True)
parser.add_argument("files", nargs="+")
args = parser.parse_args()
combined_csv = pandas.concat([pandas.read_csv(f) for f in args.files])
combined_csv = combined_csv.filter(regex="design_name|antenna_violations|DIODE_INSERTION|spef_wns|spef_tns|total_runtime|Final_Util|DecapCells|well_tap_count|DiodeCells|FillCells|Non-physCells|TotalCells")
#export to csv
combined_csv.to_csv(args.output, index=False, encoding='utf-8-sig')
