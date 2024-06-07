


# مثال على الاستخدام



#src_folder_path =  r"C:\Users\ahmed\Desktop\1\11\old"   # قم بتحديد مسار المجلد المصدر هنا
#dest_dir =   r"c:\Users\ahmed\Desktop\1\22"   # قم بتحديد مسار المجلد الوجهة هنا

from backup_ahmed import copy_and_rename_folder
from check_json_file import check_json_file


src_folder_path=check_json_file("json_data.json")["src_folder_path"]
dest_dir= check_json_file("json_data.json")["dest_dir"]

copy_and_rename_folder(src_folder_path, dest_dir)


