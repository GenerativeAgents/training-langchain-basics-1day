# 環境構築手順

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

### Jupyter のインストール

ハンズオンで Jupyter を使用するため、以下のコマンドでインストールしてください。

```console
uv add --dev jupyter==1.1.1
```

以下のコマンドで Jupyter を起動することができます。

```console
uv run jupyter notebook --ip 0.0.0.0 --port 8080 --no-browser
```

TODO: Cloud9 の場合の開き方を追記

### その他のパッケージのインストール

以下のコマンドでその他のパッケージをインストールできます。

```
uv add \
  python-dotenv==1.0.1 \
  openai==1.40.6 \
  langchain-core==0.2.30 \
  langchain-openai==0.1.21 \
　langchain-community==0.2.12 \
　langchain-text-splitters==0.2.2 \
　langchain-chroma==0.1.2 \
　streamlit==1.38.0
```

### TODO: .env ファイルの記述
