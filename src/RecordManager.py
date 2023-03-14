import json
from datetime import datetime

class RecordManager:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.records = []
        self.load()

    def load(self):
        with open(self.file_path) as f:
            data = json.load(f)
        self.records = sorted(data, key=lambda x: (-x["points"], x["date"]))

    def save(self):
        with open(self.file_path, "w") as f:
            json.dump(self.records, f, indent=4)

    def add_record(self, name, points):
        date = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        new_record = {"name": name, "points": points, "date": date}
        self.records.append(new_record)
        self.records = sorted(self.records, key=lambda x: (-x["points"], x["date"]))
        self.save()