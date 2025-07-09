import streamlit as st
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly
import matplotlib.pyplot as plt
import io
import numpy as np


# タイトル
st.title("📈 未来売上予測アプリ ✨")
st.markdown("CSVファイルをアップロードすると、未来が見えるかも…？🔮")

# ファイルアップロード
uploaded_file = st.file_uploader("売上データ（CSV形式）をアップロードしてね", type=["csv"])

if uploaded_file is not None:
    # CSV読み込み
    df = pd.read_csv(uploaded_file)
    
    # フォント（matplotlib）指定（いちおうセット）
    plt.rcParams['font.family'] = 'MS Gothic'

    # カラム名変換
    df.rename(columns={"date": "ds", "sales": "y"}, inplace=True)

    # モデル作成と学習
    model = Prophet()
    model.fit(df)

    # 未来日付作成（30日先まで）
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    # Plotlyグラフ生成＋カスタム
    fig2 = plot_plotly(model, forecast)
    fig2.update_layout(
        title="ミラちゃんの未来売上予測グラフ",
        xaxis_title="日付",
        yaxis_title="売上金額（円）",
        template="plotly_white"
    )

    # グラフ表示✨
    st.plotly_chart(fig2)

    # 予測テーブルも見れるオプション
    if st.checkbox("📋 予測テーブルも見る？"):
        st.write(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]])


# ランダムデータ生成
np.random.seed(42)

# サンプルデータ（日付 + ランダム売上）
sample_data = pd.DataFrame({
    "date": pd.date_range(start="2025-07-01", periods=30, freq='D'),
    "sales": np.random.normal(loc=10000, scale=1500, size=30).astype(int)  # 平均10000円、標準偏差1500円
})

# CSVに変換
csv_buffer = io.StringIO()
sample_data.to_csv(csv_buffer, index=False)
csv_data = csv_buffer.getvalue()

# ダウンロードボタン
st.download_button(
    label="🎲 ランダム売上データをダウンロード",
    data=csv_data,
    file_name="random_sales_sample.csv",
    mime="text/csv"
)