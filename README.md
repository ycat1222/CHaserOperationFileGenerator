# CHaser Operation File Generator
## 概要
CHaser競技部門の運営用のファイル、ディレクトリを自動で生成するプログラムです。

## 使い方
```python
from CHaser_operation_file_generator import CHaserOperationFileGenerator

user_names_file = "ユーザー名一覧.txt"
server_ip = "127.0.0.1"

# ユーザー名の一覧をtxtファイルから読み込み、CHaser競技部門の運営用のファイルを生成する
# is_name_number=True の場合、フォルダ名が3桁の番号+ユーザー名になる
# (001_佐藤、002_鈴木，...)
CHaserOperationFileGenerator(user_names_file=user_names_file, server_ip=server_ip, is_name_number=True)
```
## ファイル構成
clientとutilsフォルダは、CHaser競技部門の運営用のファイルを生成するために必要なファイルです。
消すとプログラムが動作しないため、消さないでください。

その他のフォルダは、実行時に生成されるサンプルです。実際に大会に利用する際は削除してからご利用ください。

## 秋葉原大会で配布されているものからの変更点
### client/CHaser.py
スペルミス(Responce→Response)を修正。

### client/ChaserClient.py
TURN_START、TURN_END、GAME_ENDがグローバルに定義されていたため、クラス内で定義するように変更し、グローバル変数を削除。また、その名前を__TURN_ENDのようにアンダーバーを2つ追加し、プライベート変数に変更。

### client/ChaserSimpleClient.py
TURN_ENDがグローバルに定義されていたため、クラス内で定義するように変更し、グローバル変数を削除。また、その名前を__TURN_ENDのようにアンダーバーを2つ追加し、プライベート変数に変更。

### utils/Connection.py
BUFFER_SIZEがグローバルに定義されていたため、クラス内で定義するように変更し、グローバル変数を削除。また、その名前を__BUFFER_SIZEのようにアンダーバーを2つ追加し、プライベート変数に変更。
