import json
from datetime import datetime, timedelta
import random

def fetch_tvl_data():
    # Lấy thời gian hiện tại theo giờ Việt Nam và đặt về 00:00
    now_vn = datetime.utcnow() + timedelta(hours=7)
    midnight_vn = datetime(now_vn.year, now_vn.month, now_vn.day)
    
    # Đổi về timestamp UTC 00:00 giờ Việt Nam
    timestamp = int((midnight_vn - timedelta(hours=7)).timestamp())

    fake_tvl = round(random.uniform(80_000_000, 100_000_000), 2)
    return [timestamp, fake_tvl]

def update_json():
    with open("lfj_tvl.json", "r") as f:
        data = json.load(f)

    new_record = fetch_tvl_data()

    # Tránh ghi đè nếu timestamp đã tồn tại
    timestamps = [row[0] for row in data["record"]]
    if new_record[0] not in timestamps:
        data["record"].append(new_record)

    with open("lfj_tvl.json", "w") as f:
        json.dump(data, f, separators=(",", ":"))

if __name__ == "__main__":
    update_json()
