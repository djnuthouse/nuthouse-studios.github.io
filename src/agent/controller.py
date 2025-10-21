import json
from .database import DatabaseManager

class MasterController:
    def __init__(self):
        self.db = DatabaseManager()
        print("Master Controller initialized")

    def run(self):
        print("Running system maintenance...")
        self.db.sync()
        print("System update complete.")
