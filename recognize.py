from google.cloud import speech_v1
from google.cloud.speech_v1 import enums

import io
import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import wave
import subprocess

def sample_recognize(file_path):
    
    client = speech_v1.SpeechClient()
    #언어 설정
    language_code = "ko-KR"
    #샘플레이트 계산
    #sample_rate_hertz = cal_samplerate(file_path)
    #wav파일 오디오 채널 계산
    wave_read=wave.open(file_path,'rb')
    audio_channel_count=wave_read.getnchannels()
    wave_read.close()
    #인코딩
    encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    #wav파일의 설정값
    config = {
        "language_code": language_code,
        "sample_rate_hertz": 44100,
        "encoding": encoding,
        "audio_channel_count": audio_channel_count, 
    }
    #텍스트 추출
    with io.open(file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}
   # audio = {"uri": file_path}
    response = client.recognize(config, audio)
    #텍스트 txt파일에 저장
    f = open("content.txt", 'w')
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))
        f.write(format(alternative.transcript))
    f.close()
    

def cal_samplerate(file_path):
    # wav 파일 읽기
    samplerate, data = sio.wavfile.read(file_path) 
    #데이터/샘플레이트(1초에 표현되는 데이터 양)
    times = np.arange(len(data))/float(samplerate)
    return samplerate    
    
    

#export GOOGLE_APPLICATION_CREDENTIALS=""  인증키