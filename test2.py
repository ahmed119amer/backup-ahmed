import schedule
import time
import threading
import sys

def print_word():
    print("Hello, this is your weekly word!")

# جدولة المهمة لتعمل كل أسبوع يوم الأحد الساعة 9 صباحًا
#schedule.every().sunday.at("09:00").do(print_word)

# وقت توقف البرنامج بعد ساعة واحدة (3600 ثانية)
stop_time = 20


schedule.every(3).seconds.do(print_word)


# دالة لإيقاف تشغيل البرنامج بعد فترة محددة
def stop_program():
    print("Stopping the program...")
    sys.exit()

# إنشاء خيط جديد لإيقاف تشغيل البرنامج بعد وقت محدد
stop_thread = threading.Timer(stop_time, stop_program)
stop_thread.start()

while True:
    schedule.run_pending()
    time.sleep(1)
    print("1")

    # إلغاء الخيط الذي يقوم بإيقاف تشغيل البرنامج بعد انتهاء الوقت المحدد
    if not stop_thread.is_alive():
        stop_thread.cancel()
        break
