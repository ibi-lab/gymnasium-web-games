# Gymnasium Web Games

Gymnasium（旧 OpenAI Gym）の各種ゲーム・シミュレーションのHTMLエンドポイントをホスティングし、それらにアクセスするためのWebポータルを提供するプロジェクトです。サーバレスインフラストラクチャプラットフォームである [Modal](https://modal.com/) を利用してデプロイ・稼働することを前提としています。

## サポートしているゲーム

以下の5つの古典的および人気のある強化学習・制御環境が含まれています：

- **CartPole**: ポールを立てたままカートを制御する古典的問題。
- **MountainCar**: 非力な車を勢いをつけて山の上に到達させる問題。
- **LunarLander**: 月面着陸船を目標地点に安全に着陸させる問題。
- **BipedalWalker**: 二足歩行ロボットを進ませる強化学習の難問。
- **CarRacing**: ランダムに生成されるコースで車を走らせる問題。

## 技術スタック

- **フレームワーク**: [Flask](https://flask.palletsprojects.com/)
- **フロントエンド UI**: [Bootstrap 5](https://getbootstrap.com/)
- **デプロイメント**: [Modal](https://modal.com/)

プロジェクト内のPythonスクリプト (`gymnasium_app.py`) 内でFlaskアプリを定義し、ModalのImage（`debian_slim`）上に依存関係（Flask）をインストールし、ローカルのHTMLファイルをマウントした状態でホスティングを行います。

## Getting Started

### 前提条件

Python環境とModalのアカウント、およびCLIツールが必要です。

```bash
# modalをインストール
pip install modal

# modalの認証セットアップ（初回のみ）
modal setup
```

### ローカルでの動作確認（Serveモード）

開発・テスト用にアプリケーションを一時的に起動して確認する場合は、以下のコマンドを使用します。ファイルの変更を検知して自動的にリロードされます。

```bash
modal serve gymnasium_app.py
```
実行後、ターミナルに表示されるModalが発行したURL（`https://*.modal.run`）にアクセスしてください。Bootstrapコンポーネントを用いたゲームポータル画面が表示されます。

### 本番環境へのデプロイ

アプリケーションを本番環境（永続的）にデプロイする場合は、以下のコマンドを実行します。

```bash
modal deploy gymnasium_app.py
```

## プロジェクト構成

```text
.
├── gymnasium_app.py      # ModalとFlaskを用いたメインのアプリケーションコード
├── bipedalwalker.html    # BipedalWalker用の画面（エンドポイント）
├── carracing.html        # CarRacing用の画面（エンドポイント）
├── cartpole.html         # CartPole用の画面（エンドポイント）
├── lunarlander.html      # LunarLander用の画面（エンドポイント）
└── mountaincar.html      # MountainCar用の画面（エンドポイント）
```

# デモ

https://kdix--gymnasium-portal-flask-app.modal.run/