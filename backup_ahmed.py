import shutil
import os
from datetime import datetime

def copy_and_rename_folder(src_folder_path, dest_dir):
    # التأكد من وجود المجلد المصدر
    if not os.path.isdir(src_folder_path):
        print(f"المجلد المصدر غير موجود: {src_folder_path}")
        return
    
    # التأكد من وجود المجلد الوجهة، إذا لم يكن موجودًا، يتم إنشاؤه
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # الحصول على التاريخ والوقت الحاليين بالتنسيق المطلوب (نظام 24 ساعة)
    current_datetime = datetime.now().strftime('%Y-%m-%d_%I-%M-%S_%p')
    
    # الحصول على اسم المجلد بدون المسار
    base_name = os.path.basename(src_folder_path)

    # إنشاء اسم المجلد الجديد بتنسيق التاريخ والوقت
    new_folder_name = f"{current_datetime}-{base_name}"
    
    # إنشاء المسار الكامل للمجلد الجديد
    dest_folder_path = os.path.join(dest_dir, new_folder_name)
    
    # نسخ المجلد مع تغيير اسمه
    shutil.copytree(src_folder_path, dest_folder_path)
    
    print(f"تم نسخ المجلد وتغيير اسمه: {dest_folder_path}")
