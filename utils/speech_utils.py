import pyaudio
import wave


CHUNK = 1024


def play_pcm(file_path, channels=1, rate=16000, width=2):
    p = pyaudio.PyAudio()

    # Open stream
    stream = p.open(format=p.get_format_from_width(width),
                    channels=channels,
                    rate=rate,
                    output=True)

    with open(file_path, 'rb') as pcmfile:
        data = pcmfile.read(1024)
        while data:
            stream.write(data)
            data = pcmfile.read(1024)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()

    # Terminate the PortAudio interface
    p.terminate()


def record_audio(filename, duration):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("Recording...")
    frames = []
    for _ in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Recording finished.")
    stream.stop_stream()
    stream.close()
    audio.terminate()
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

def pcm_to_wav(pcm_file_path, wav_file_path):
    sample_rate = 16000  # 例如 16 kHz
    bit_depth = 16       # 例如 16-bit

    # 读取 PCM 数据
    with open(pcm_file_path, 'rb') as f:
        pcm_data = f.read()
    
    # 根据位深度将 PCM 数据转换为 numpy 数组
    dtype = np.int16 if bit_depth == 16 else np.uint8
    audio_data = np.frombuffer(pcm_data, dtype=dtype)

    # 保存为 WAV 文件
    write(wav_file_path, sample_rate, audio_data)

def play_wav_file(file_path):
    # 打开 .wav 文件
    wf = wave.open(file_path, 'rb')

    # 创建 PyAudio 流
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # 读取并播放音频数据
    chunk = 1024
    data = wf.readframes(chunk)
    while data:
        stream.write(data)
        data = wf.readframes(chunk)

    # 关闭流和 PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()