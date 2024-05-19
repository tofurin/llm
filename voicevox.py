import json
import requests
import wave
import time
import soundfile as sf
import sounddevice as sd
import edge_tts
import tracemalloc



def generate_wav(text, speaker=14, filepath='audio.wav'):
    host = 'localhost'
    port = 50021
    params = (
        ('text', text),
        ('speaker', speaker),
    )

    response1 = requests.post(
        f'http://{host}:{port}/audio_query',
        params=params,
    )


    response_JSON_dict = dict(response1.json())

    response_JSON_dict["speedScale"] =1.1

    response_JSON_dict['intonationScale'] = 1.8

    headers = {'Content-Type': 'application/json',}
    response2 = requests.post(
        f'http://{host}:{port}/synthesis',
        headers=headers,
        params=params,
        data=json.dumps(response_JSON_dict),

    )


    wf = wave.open(filepath, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(24000)
    wf.writeframes(response2.content)
    wf.close()


    return filepath

import asyncio
import edge_tts

async def generate_edge_async(text, voice="en-GB-SoniaNeural", output_file="output.mp3"):

    communicate = edge_tts.Communicate(text, voice)
    await asyncio.to_thread(communicate.save, output_file)

    #sig, sr = sf.read(OUTPUT_FILE, always_2d=True)
    #sd.play(sig, sr)
    #sd.wait()


def play(text):
    sig, sr = sf.read(generate_wav(text), always_2d=True)
    sd.play(sig, sr)
    sd.wait()



if __name__ == '__main__':
    text = "In my leisure time, I find solace in the pages of books. There's something magical about getting lost in a story, exploring new worlds, and discovering different perspectives through the words of authors. Reading not only entertains me but also broadens my understanding of the world and enriches my imagination."
    generate_edge_async(text)
    #play(text)