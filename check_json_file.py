import os

from json_save import json_write, open_json


dis={
    "src_folder_path": None,
    "dest_dir":None,
}

def check_json_file(file_path):
    """
    تحقق مما إذا كان الملف المحدد موجودًا وهو ملف JSON.
    
    :param file_path: مسار الملف المراد التحقق من وجوده.
    :return: True إذا كان الملف موجودًا وهو ملف JSON، و False إذا لم يكن.
    """
    if os.path.exists(file_path) and os.path.isfile(file_path):
        print ("is exists !!!!!!!!!!!!!!!!!")
        dis_json = open_json("json_data.json")
        #print (dis_json)
        return dis_json
    else:
        json_data = json_write(dis,"json_data.json")
        print("is not exists??????????????????")
        return json_data


# استخدام الدالة للتحقق من وجود ملف JSON
#file_path = 'path/to/your/file.json'  # قم بتعيين مسار الملف الخاص بك هنا
#if check_json_file(file_path):
#    print("الملف JSON موجود.")
#else:
#    print("الملف JSON غير موجود أو ليس ملف JSON.")


#print(check_json_file("json_data.json")["src_folder_path"])