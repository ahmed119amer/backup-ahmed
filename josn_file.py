import json
import os

def json_file (folder_path,file_name):
    # قاموس Python
    my_dict = {"1":{"src_folder_path": "", "dest_dir": ""},"2":{"src_folder_path": "", "dest_dir": ""}}

    if my_dict["1"]["src_folder_path"]=="":
        print ('it is empty')
        my_dict["src_folder_path"]=input(r'inter src_folder_path:')
        my_dict["dest_dir"]=input(r'inter dest_dir:')
        print (my_dict["src_folder_path"])

    # التأكد من وجود المجلد
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


    # حفظ البيانات في ملف JSON في المسار المحدد
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "w") as file:
        json.dump(my_dict, file)

    print(f"تم حفظ البيانات في ملف {file_path}")

def path_exists(folder_path):
    # التأكد من وجود المجلد
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

        
# مسار المجلد الذي تريد حفظ الملف فيه
folder_path = r"C:\Users\ahmed\Desktop\1\22"
# اسم الملف الذي تريد حفظ البيانات فيه
file_name = "data.json"

json_file (folder_path,file_name)