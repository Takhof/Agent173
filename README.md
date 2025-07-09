# 売上予測アプリ（Streamlit × Prophet）

本アプリは、Facebook Prophetを用いた時系列予測モデルを活用し、  
CSV形式の売上データから将来の売上を可視化・予測するWebアプリケーションです。  

Demo https://agent173.streamlit.app/

---

## 🔍 主な機能

- CSVファイルをアップロードするだけで、30日先までの売上予測を自動で実施
- 予測結果をPlotlyベースのインタラクティブなグラフで可視化
- 将来売上の予測レンジ（信頼区間）も一目で確認
- 予測結果テーブルをCSV出力や確認用に閲覧可能
- デプロイ後すぐに利用可能（Streamlit Cloudまたは社内環境）

---

## 🖥 使用方法（ローカル実行）

### 1. 必要なライブラリをインストール

```bash
pip install -r requirements.txt
2. アプリの起動
bash
Copy
Edit
streamlit run mira_streamlit.py
📄 入力データ形式（CSV）
以下のような形式で日別売上データをご用意ください。

csv
Copy
Edit
date,sales
2024-04-01,18200
2024-04-02,20700
2024-04-03,19300
...
date：日付（YYYY-MM-DD形式）

sales：該当日の売上金額（整数または浮動小数点）

📈 技術構成
Python 3.8+

Facebook Prophet

Streamlit

pandas / matplotlib / plotly


🚀 デプロイ方法（Streamlit Cloud）
GitHubに本リポジトリをアップロード

Streamlit Cloud にて新規アプリを作成

デプロイ対象のファイルを mira_streamlit.py に指定

クラウド上で即時公開が可能となります。

📦 必要ライブラリ（requirements.txt）
nginx
Copy
Edit
pandas
prophet
matplotlib
plotly
streamlit
📝 ライセンス
本アプリケーションはMITライセンスのもと公開されています。
商用利用・再配布・改変は自由に行っていただけます。
