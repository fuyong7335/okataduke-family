import os
import shutil
import datetime

def restore_py_files():
    # バックアップディレクトリ作成
    backup_dir = os.path.join(os.path.dirname(os.getcwd()), 'backup_' + datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
    os.makedirs(backup_dir, exist_ok=True)
    
    # カレントディレクトリ
    current_dir = os.getcwd()
    
    # 親ディレクトリ
    parent_dir = os.path.dirname(current_dir)
    
    # 保持するファイル
    keep_files = ['app.py', 'requirements.txt']
    
    # ファイル復元
    restored_files = 0
    
    for file in os.listdir(current_dir):
        # .pyファイルで、保持するファイル以外を元の場所に戻す
        if file.endswith('.py') and file not in keep_files:
            source_path = os.path.join(current_dir, file)
            dest_path = os.path.join(parent_dir, file)
            
            try:
                # 元のファイルをバックアップ
                if os.path.exists(dest_path):
                    backup_path = os.path.join(backup_dir, file)
                    shutil.copy2(dest_path, backup_path)
                    print(f"バックアップ: {dest_path} → {backup_path}")
                
                # 強制的に上書き
                shutil.copy2(source_path, dest_path)
                print(f"上書き復元: {source_path} → {dest_path}")
                restored_files += 1
            except Exception as e:
                print(f"エラー: {source_path} の復元に失敗 - {e}")
    
    print(f"合計 {restored_files} 個のファイルを上書き復元しました。")
    print(f"バックアップディレクトリ: {backup_dir}")

# スクリプト実行
restore_py_files()