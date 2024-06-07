import json
import os


# الكتابة واذا لم يوجد يقوم بالسؤال عن مكان البكب
def json_write(dic,file_name):
    

    dic["src_folder_path"]=input("folder you want backup it:") 
    dic["dest_dir"]=input("path backups :")

    json_dis = json.dumps(dic,indent=1)

    # حفظ البيانات في ملف JSON في المسار المحدد
    #file_path = os.path.join(folder_path, file_name)

    with open (file_name , "w") as outfile :
        outfile.write(json_dis)


#لغرض قراءة json 
def open_json(file_name):
    with open (file_name , "r") as openfile :
        json_open = json.load(openfile)

    #print(json_open)
    return json_open

#print(open_json())


#json_write(dis,r"C:\Users\ahmed\Desktop\1","json_data.json")

#open_json(r"C:\Users\ahmed\Desktop\1","json_data.json")