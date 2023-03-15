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

    def add_record(self, name):
        date = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        found_record = False
        record = None
        index = None
        for idx, obj in enumerate(self.records):
            if obj["name"] == name:
                found_record = True
                record = obj.copy()
                index = idx

        if found_record:
            self.records.pop(index)
            new_record = {"name": name, "points": record["points"] + 1, "date": date}
        else:
            new_record = {"name": name, "points": 0, "date": date}

        self.records.append(new_record)
        self.records = sorted(self.records, key=lambda x: (-x["points"], x["date"]))
        self.save()