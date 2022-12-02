#In the case of changing the key in the decryption process, we will not get the original text "before encryption" because it depends mainly on the key.
 #If changing the key in decryption was possible, it would be easy to decrypt the code without having to try (0-25) times to find out the appropriate key.
from scipy.io import wavfile
from Ipython.display import audio
from matplot.pyplot import pyplotas plt
f_name="/cosntant/drive/mydrive/mydrive/mlprojects/speech recognition/07a7c2a8d_nahash_0.wav"
fs,wav=wavfile.read(f_name)
print(fs)
plt.plot(wav)
audio(f_name,autoplay=true)
