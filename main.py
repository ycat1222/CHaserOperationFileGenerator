from CHaser_operation_file_generator import CHaserOperationFileGenerator


user_names_file = "ユーザー名一覧.txt"
server_ip = "127.0.0.1"

# ユーザー名の一覧をtxtファイルから読み込み、CHaser競技部門の運営用のファイルを生成する
# is_name_number=True の場合、ディレクトリ名が3桁の番号+ユーザー名になる
# (001_佐藤、002_鈴木，...)
CHaserOperationFileGenerator(user_names_file=user_names_file, server_ip=server_ip, is_name_number=True)
