import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# 🧁 CSVファイルの読み込み（例：sales_data.csv）
df = pd.read_csv("sales_data.csv")

# Prophet用にカラム名を変換（ds = 日付、y = 売上）
df.rename(columns={"date": "ds", "sales": "y"}, inplace=True)

# ✨ モデルの作成と学習
model = Prophet()
model.fit(df)

# 📅 未来の日付を作成（ここでは30日後まで）
future = model.make_future_dataframe(periods=30)

# 🔮 予測！
forecast = model.predict(future)

# 📈 グラフに表示
fig = model.plot(forecast)
plt.title("📊ミラちゃんの売上予測グラフ")
plt.xlabel("日付")
plt.ylabel("売上 (円)")
plt.show()