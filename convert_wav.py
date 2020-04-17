import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import subprocess


def mp4_to_wav(video_path):
    #wav 파일로 변환    
    #video_name=sub
    command = "ffmpeg -i "+video_path+" -ab 160k -ac 2 -ar 44100 -vn "+video_path[:-4]+".wav"
    subprocess.call(command, shell=True)


# Sample rate (샘플레이트)
# 이는 샘플의 빈도 수 입니다.
# 즉, 1초당 추출되는 샘플 개수라고 할 수 있습니다.
# 오디오에서 44.1KHz(44100Hz), 22KHz(22050Hz)를 뜻합니다.
# 괄호안에 값은 좀더 정확하게 표현한 값입니다.
#print( 'sampling rate: ', samplerate)

# 3-다 
# 따라서 데이터 전체의 개수에서 sample rate를 나누어 주면됩니다.
#print ('time : ', times[-1])