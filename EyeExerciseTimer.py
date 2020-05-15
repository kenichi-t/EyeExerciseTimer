import time
import numpy as np
import pyaudio


class Beep:
    def __init__(
        self,
        sampling_rate=44100,
        sound_frequency=440.0,
        play_time_second=0.1,
        gain=1.0
    ):
        slen = int(play_time_second*sampling_rate)
        t = float(sound_frequency)*np.pi*2/sampling_rate
        self.samples = (
            np.sin(np.arange(slen)*t)*gain).astype(np.float32).tostring()

        p = pyaudio.PyAudio()
        self.stream = p.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=sampling_rate,
            frames_per_buffer=1024,
            output=True)

    def __call__(self):
        self.stream.write(self.samples)


def EyeExerciseTimer(interval, cycle):
    beep_interval_high = Beep(sound_frequency=660.0)
    beep_interval_low = Beep(sound_frequency=440.0)
    beep_finish = Beep(play_time_second=0.4)
    time_start = time.time()
    for ii in range(cycle):
        beep_interval_high()
        time.sleep(time_start + interval * (ii*2+1) - time.time())
        beep_interval_low()
        time.sleep(time_start + interval * (ii*2+2) - time.time())
    beep_finish()


EyeExerciseTimer(10, 10)
