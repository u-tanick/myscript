import os
import shutil
import datetime

# 対象の拡張子一覧
extensions = ['txt', 'png', 'jpg', 'pptx', 'xlsx', 'docx', 'pdf', 'mm', 'md']

# 移動元のデスクトップパス
desktop_path = os.path.expanduser("~/Desktop")

# 移動先のルートフォルダ
root_folder = "C:\\Users\\funky\\Documents\\_CollectFromDesktop"

# デスクトップのファイル一覧を取得する
desktop_files = os.listdir(desktop_path)

# ファイルを移動する
for file in desktop_files:
    # ファイルの拡張子を取得する
    ext = os.path.splitext(file)[1]

    # 拡張子が対象のリストに含まれる場合、対応するフォルダに移動する
    if ext[1:].lower() in extensions:
        # 拡張子毎のフォルダがなければ、作成する
        folder_path = os.path.join(root_folder, ext[1:].lower())
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        src_path = os.path.join(desktop_path, file)
        dst_path = os.path.join(folder_path, file)

        # 同じ名前のファイルが存在する場合は、ファイル名に日付を付与する
        if os.path.exists(dst_path):
            timestamp = datetime.datetime.today().strftime('_%Y%m%d')
            dst_name = os.path.splitext(file)[0] + timestamp + ext
            dst_path = os.path.join(folder_path, dst_name)

        shutil.move(src_path, dst_path)
