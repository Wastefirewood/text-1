import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://iftp.chinamoney.com.cn/english/bdInfo/"  # 设置目标页面的网址

params = {
    "bondType": "Treasury Bond",
    "issueYear": "2023",
}  # 定义将要查取信息的参数要求


response = requests.get(url, params=params)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table")  # 查找所需的表格

data = []
headers = ["ISIN", "Bond Code", "Issuer", "Bond Type", "Issue Date", "Latest Rating"]  # 设置表格的列明

if table:
    rows = table.find_all("tr")
    for row in rows[1:]:  # 从表格第二行开始遍历
        cells = row.find_all("td")
        for cell in cells:  # 遍历每一行的单元格
            data_row = cell.text.strip()
            # 将每一行其中的单元格内容提取出来，然后保存为一个列表data_row。每个data_row表示表格中的一行数据
            data.append(data_row)


# Create a DataFrame using Pandas
df = pd.DataFrame(data, columns=headers)

# Save the DataFrame to a CSV file
df.to_csv("treasury_bonds_2023.csv", index=False)

print("成功保存到 'treasury_bonds_2023.csv'.")
