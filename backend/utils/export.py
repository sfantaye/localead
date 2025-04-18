import pandas as pd
import os
from datetime import datetime
import uuid

EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

def export_leads_to_excel(leads):
    df = pd.DataFrame(leads)
    filename = f"{EXPORT_DIR}/leads_{uuid.uuid4().hex}.xlsx"
    df.to_excel(filename, index=False)
    return filename
