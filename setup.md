# セットアップ手順書
以下の手順でセットアップを行う。  
なお、以下の環境で動作したことを確認した。
## 動作確認環境

* **OS**: macOS バージョン15.5（24F74）
* **Python**: 3.13.5
* **パッケージ管理ツール**: uv 0.9.4

### 依存ライブラリ (Dependencies)

必要なライブラリとそのバージョンは `requirements.txt` ファイルに記載されている。

## セットアップ手順
1. 仮想環境(venv)の構築

    test.py実行用の仮想環境を構築する。今回はpythonの仮想環境であるvenvを使用する。

    ```bash
    python -m venv 仮想環境名
    ```
    
1. 仮想環境の有効化

    test.py実行用に仮想環境を有効化する。

    - macOS
        ```bash
        source ./仮想環境名/bin/activate
        ```
    有効化する際のpathについては仮想環境を構築したpathに依存するため注意する。

1. ライブラリのインストール

    有効化した仮想環境にライブラリをインストールする。

    ```bash
    # パッケージ管理ツールuvのインストール
    pip install uv

    # uvを使ってライブラリを一括インストール
    uv pip install -r requirements.txt
    ```

以上でtest.pyを実行するための仮想環境を構築することができる。  
test.pyの実行方法についてはtest.mdを参照すること。
また、実行終了後に仮想環境を無効化したい場合は以下のコマンドを使用する。

- macOS
    ```bash
    deactivate
    ```