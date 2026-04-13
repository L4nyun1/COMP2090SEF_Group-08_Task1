import os
import sys

sys.path.insert(0, os.path.dirname(__file__))               #Add current directory to sys.path to allow relative imports from models and storage

from storage.json_store import JsonStore
from ui.app import ExpenseTrackerApp

LEDGER_PATH = os.path.join("data", "ledger.json")
BUDGETS_PATH = os.path.join("data", "budgets.json")


def main() -> None:                                         #Main function to initialize the app, load data, and start the main loop
    store = JsonStore(LEDGER_PATH, BUDGETS_PATH)
    app = ExpenseTrackerApp(store)
    app.mainloop()


if __name__ == "__main__":
    main() 
