import json
import time
import random

def fetch_tvl_data():
    now = int(time.time())
    fake_tvl = round(random.uniform(80_000_000, 100_000_000), 2)
    return [now, fake_tvl]

def update_json():
    with open("lfj_tvl.json", "r") as f:
        data = json.load(f)

    new_record = fetch_tvl_data()
    data["record"].append(new_record)

    with open("lfj_tvl.json", "w") as f:
        json.dump(data, f, separators=(",", ":"))

if __name__ == "__main__":
    update_json()
