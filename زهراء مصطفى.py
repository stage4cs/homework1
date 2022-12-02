from Scipy.io import wavfile
from ipython.display import Audio
from matplot.pyplot import pyplotasplt
f_name="/contant/drive/MyDrive/myDrive/MLPROJECTS/SpeechRecognition/0a7c2a8d_nahash_0.Wav"
fs,wav=wavfile.read(f_name)
print(fs)
plt.plot(wav)
Audio(f_name,autoplay=true)

"َQ2
     "عندما نشفر كلمة في
     "5 مثلا قيمه نصوص+key 
    "سوف تظهر كلمة مشفرة و عندما يتم فك التشفير لكن ب
    " مختلف عن الاصلي key
    "يتم استخدام الارقام
    " 0_25 
    "لكي نرى اي رقم من الارقام حتى يظهر نص مفهوم فستظهر كلمة غير مفهومة
    "الا اذا تم استخدام نفس key
    "الذي تم استخدامه في التشفير
    