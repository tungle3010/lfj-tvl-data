import json
import random
from datetime import datetime, timedelta, timezone

def fetch_tvl_data():
    # Lấy 00:00 UTC hôm qua
    utc_yesterday = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)
    timestamp = int(utc_yesterday.timestamp())

    fake_tvl = round(random.uniform(80_000_000, 100_000_000), 2)
    return [timestamp, fake_tvl]

def update_json():
    with open("lfj_tvl.json", "r") as f:
        data = json.load(f)

    new_record = fetch_tvl_data()

    # Gỡ bỏ bản ghi cũ nếu có cùng timestamp (00:00 UTC hôm qua)
    data["record"] = [row for row in data["record"] if row[0] != new_record[0]]

    # Thêm mới
    data["record"].append(new_record)
    print(f"✅ Updated record for {new_record[0]}: {new_record[1]}")

    # Sort theo timestamp để dễ kiểm tra
    data["record"].sort(key=lambda x: x[0])

    with open("lfj_tvl.json", "w") as f:
        json.dump(data, f, separators=(",", ":"))

if __name__ == "__main__":
    update_json()
