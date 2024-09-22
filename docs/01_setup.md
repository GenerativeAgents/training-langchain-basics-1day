# 環境構築手順

ハンズオン環境の構築手順です。

AWS Cloud9 (Amazon Linux 2023) を想定しています。

## uv のインストール

Python の特定バージョンのインストールやパッケージの管理のため、[uv](https://github.com/astral-sh/uv) をインストールします。

以下のコマンドを実行してください。

```console
curl -LsSf https://astral.sh/uv/0.4.14/install.sh | sh
```

上記のスクリプトによる `~/.bashrc` の変更を反映するため、以下のコマンドでシェルを起動しなおしてください。

```console
exec "$SHELL"
```

以下のコマンドで uv のバージョンが表示されれば、インストール完了です。

```console
uv --version
```

## Python 3.10.12 のインストール

uv で Python の特定バージョンをインストールします。
以下のコマンドを実行してください。

```console
uv python install 3.10.12
```

以下のコマンドで Python のバージョンが表示されれば、インストール完了です。

```console
uv run python --version
```

## 作業ディレクトリ作成

以下のコマンドで、作業用のディレクトリを作成してください。

```console
mkdir langchain-basics
```

以下のコマンドで、作業用のディレクトリに移動してください。

```console
cd langchain-basics
```

## プロジェクト初期化

uv を使う Python プロジェクトを初期化します。
以下のコマンドを実行してください。

```console
uv init
```

`hello.py` というファイルが生成されるので、実行してみます。
以下のコマンドを実行してください。

```console
uv run python hello.py
```

## 使用するパッケージのインストール

講座内で使用するパッケージをインストールしてください。

```console
uv add \
  python-dotenv==1.0.1 \
  openai==1.40.6 \
  langchain-core==0.2.30 \
  langchain-openai==0.1.21 \
　langchain-community==0.2.12 \
　langchain-text-splitters==0.2.2 \
　langchain-chroma==0.1.2 \
　streamlit==1.38.0 \
  protobuf==3.20.3
```

## Jupyter のインストール

ハンズオンで Jupyter を使用するため、以下のコマンドでインストールしてください。

```console
uv add --dev jupyter==1.1.1
```

以下のコマンドで Jupyter を起動することができます。

```console
uv run jupyter notebook --ip 0.0.0.0 --port 8080 --no-browser
```

Cloud9 の「Preview」>「Preview Running Application」をクリックしてください。

TODO: 画面キャプチャ

※このプレビューではうまく表示されないのは想定通りです。

右上の「Pop Out Into New Window」でブラウザの別のタブで開きます。

TODO: 画面キャプチャ

## Jupyter の動作確認

Jupyter 上で以下のコマンドを実行して、想定通りの Python のバージョンが表示されるか確認してください。

```
!python --version
```

Jupyter 上で以下のコマンドを実行して、Python が動作するか確認してください。

```python
print("hello")
```

## .env ファイルの記述

langchain-basics ディレクトリに .env という名前のファイルを作成してください。

[.env.template](../.env.template) の内容をコピーして .env ファイルに貼り付けてください。

OPENAI_API_KEY の値を記入してください。

> [!NOTE]
> LANGCHAIN_API_KEY はあとで記入するので、ひとまず空のままで大丈夫です。

## langchain リポジトリの clone

講座の一部で langchain リポジトリのデータを読み込んで使います。

langchain-basics ディレクトリで以下のコマンドを実行して、langchain リポジトリを clone するディレクトリを作成してください。

```console
mkdir -p tmp
```

langchain-basics ディレクトリで以下のコマンドを実行して、langchain リポジトリを clone してください。

```console
git clone --depth 1 https://github.com/langchain-ai/langchain.git ./tmp/langchain
```
