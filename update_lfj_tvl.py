import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Dùng credentials từ biến môi trường GITHUB_SECRET
import os
import base64

credentials_content = os.environ["GCP_CREDENTIALS_JSON"]
credentials_dict = json.loads(credentials_content)

# Kết nối Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
client = gspread.authorize(creds)

# Truy cập Google Sheet và sheet con
sheet = client.open_by_key("1mOJ9p76DLm7P0gGeVVkpN2Irr_R4Y8PX9gSImVmunyg")
worksheet = sheet.worksheet("LFJ_TVL")

# Đọc toàn bộ dữ liệu
rows = worksheet.get_all_values()
header, data_rows = rows[0], rows[1:]

# Parse dữ liệu từ Sheet thành list JSON
parsed_data = []
for row in data_rows:
    try:
        date_str = row[0].strip()
        tvl_str = row[1].replace(",", "")
        dt = datetime.strptime(date_str, "%m/%d/%Y")
        timestamp = int(dt.replace(hour=0, minute=0, second=0).timestamp())
        tvl = float(tvl_str)
        parsed_data.append([timestamp, round(tvl, 2)])
    except:
        continue

# Cập nhật file JSON
with open("lfj_tvl.json", "w") as f:
    json.dump({"record": parsed_data}, f, separators=(",", ":"))
