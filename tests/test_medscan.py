import pandas as pd
from medscan import flag_out_of_range

def test_flagging():
    df = pd.DataFrame([{
        'PatientID': '001',
        'TestName': 'Glucose',
        'Result': 180,
        'Unit': 'mg/dL'
    }])
    panel = {"Glucose": {"min": 70, "max": 140}}
    result = flag_out_of_range(df, panel)
    assert not result.empty
    assert result.iloc[0]['Flag'] == 'High'
