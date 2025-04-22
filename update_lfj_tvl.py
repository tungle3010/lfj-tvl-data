import json
import random
from datetime import datetime, timedelta, timezone

def fetch_tvl_data():
    # Lấy thời gian 00:00 UTC hôm nay
    utc_today = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    
    # Trừ đi 1 ngày → lấy ngày hôm qua 00:00 UTC
    utc_yesterday = utc_today - timedelta(days=1)
    timestamp = int(utc_yesterday.timestamp())

    # Fake TVL (sẽ thay bằng giá trị thực sau này nếu có)
    fake_tvl = round(random.uniform(80_000_000, 100_000_000), 2)

    return [timestamp, fake_tvl]

def update_json():
    with open("lfj_tvl.json", "r") as f:
        data = json.load(f)

    new_record = fetch_tvl_data()

    # Kiểm tra trùng timestamp
    timestamps = [row[0] for row in data["record"]]
    if new_record[0] not in timestamps:
        data["record"].append(new_record)
        print("✅ Thêm bản ghi:", new_record)
    else:
        print("⚠️ Bản ghi đã tồn tại:", new_record)

    with open("lfj_tvl.json", "w") as f:
        json.dump(data, f, separators=(",", ":"))

if __name__ == "__main__":
    update_json()
