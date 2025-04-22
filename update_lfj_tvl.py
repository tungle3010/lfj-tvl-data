import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Đọc credentials từ biến môi trường
credentials_content = os.environ['GCP_CREDENTIALS_JSON']
credentials_dict = json.loads(credentials_content)

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
gc = gspread.authorize(credentials)

# Mở Google Sheet
sheet = gc.open_by_key("1mOJ9p76DLm7P0gGeVVkpN2Irr_R4Y8PX9gSImVmunyg")
worksheet = sheet.worksheet("LFJ_TVL")
data = worksheet.get_all_records()

# Chuyển đổi sang epoch + float
new_data = []
for row in data:
    date_str = row['Date']
    tvl_value = float(row['TVL (USD)'])
    epoch_time = int(gspread.utils.a1_to_rowcol(date_str)[0])  # cần sửa lại dòng này cho chuẩn epoch
    continue  # tạm thời để debug

# TODO: đọc file JSON cũ, thêm record mới vào nếu chưa có, rồi ghi lại
