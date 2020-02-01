'''
@Author: W.Y.P.
@Date: 2020-2-1 16:04:34
@LastEditTime: 2019-11-28 17:17:30
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \DigitalSignalProcessingGXQDYM\Ex1_3_4.py
'''

from scipy import signal
import matplotlib.pyplot
import numpy
import scipy

Fs  = 2000
Wn  = 300
n   = 4

b,a = scipy.signal.butter(n,Wn,btype='lowpass',analog=True)
bz,az   = scipy.signal.bilinear(b,a,Fs)

Wd, Hd  = signal.freqz(bz,az,512,Fs)

fig, ax1 = matplotlib.pyplot.subplots()
ax1.set_title('frequency response')
ax1.plot(Wd/numpy.pi, 20 * numpy.log10(abs(Hd)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [pi*rad/sample]')
ax1.set_xlim([0,1])

ax2 = ax1.twinx()
angles = numpy.angle(Hd, deg=True)
ax2.plot(Wd/numpy.pi, angles, 'g')
ax2.set_ylabel('Angle (degrees)', color='g')
ax2.grid()
ax2.axis('tight')
ax2.set_xlim([0,1])

matplotlib.pyplot.show()

# EOF
