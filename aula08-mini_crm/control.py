from pathlib import Path
import json, csv

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"

#CRUD -> create, read, update, delete

#READ
def read_leads():
    if not DB_PATH.exists():
        return []

    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

def search_leads(query):
    list_leads = read_leads()

    result = []

    for i, lead in enumerate(list_leads):
        if lead["name"].lower() == query or lead["email"].lower() == query or lead["company"].lower() == query:
            result.append((i, lead))

    return(result)

def export_csv():
    path_csv = DATA_DIR / "leads.csv"

    list_leads = read_leads()

    try:
        with path_csv.open("w", newline="", encoding="utf-8") as file_csv:
            writer = csv.DictWriter(file_csv, fieldnames=list_leads[0].keys())
            writer.writeheader()

            for row in list_leads:
                writer.writerow(row)

        return path_csv
    except PermissionError:
        return None
    

#CREATE
def create_lead(lead_dict):
    leads = read_leads() #lista de dicionários de leads
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

