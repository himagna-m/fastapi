import streamlit as st
import sounddevice as sd
import numpy as np
import wave
import asyncio
import websockets
import io
import os
from datetime import datetime

st.title(" Ask Your Question with Voice")

def record_audio(duration=20, fs=44100):
    st.info("Recording... Speak now!")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype="int16")
    sd.wait()
    st.success("Recording complete!")
    return audio, fs

def save_audio(audio, fs, filename="latest_recording.wav"):
    buf = io.BytesIO()
    with wave.open(buf, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(fs)
        wf.writeframes(audio.tobytes())
    audio_bytes = buf.getvalue()

    # Save locally for reference
    path = os.path.join("recordings", filename)
    os.makedirs("recordings", exist_ok=True)
    with open(path, "wb") as f:
        f.write(audio_bytes)

    return audio_bytes

async def send_audio(audio_bytes):
    uri = "ws://localhost:8000/ws/audio"
    try:
        async with websockets.connect(uri) as ws:
            await ws.send(audio_bytes)
            response = await ws.recv()
            return response
    except Exception as e:
        return f" WebSocket Error: {e}"

if st.button("Record and Ask"):
    audio, fs = record_audio()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"recording_{timestamp}.wav"
    audio_bytes = save_audio(audio, fs, filename=filename)

    st.audio(audio_bytes, format="audio/wav")

    with st.spinner("Transcribing and getting AI response..."):
        result = asyncio.run(send_audio(audio_bytes))
        st.subheader(" AI Response:")
        st.write(result)
