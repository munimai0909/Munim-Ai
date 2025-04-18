ledger_data = {}

def add_entry(name, entry):
    if name not in ledger_data:
        ledger_data[name] = []
    ledger_data[name].append(entry)

def get_ledger(name):
    return ledger_data.get(name, [])
