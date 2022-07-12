%pip install
import matplotlib.pyplot as plt
#import matplotlib as plt
import IPython.display as ipd
import librosa
import librosa.display
%matplotlib inline 

filename = 'olivia_static.wav'


plt.figure(figsize=(14,5))
data, sample_rate = librosa.load(filename)
librosa.display.waveshow(data, sr=sample_rate)
ipd.Audio(filename)