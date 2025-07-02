from fastapi import FastAPI, WebSocket
import whisper
import tempfile
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

# Load Whisper model once
model = whisper.load_model("base")
api_key = os.getenv("GROQ_API_KEY")
# Groq client setup
client = Groq(api_key=api_key)
 # Replace with your real key

@app.websocket("/ws/audio")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        audio_bytes = await websocket.receive_bytes()

        # Save audio to temp fileoiu
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio.write(audio_bytes)
            temp_audio_path = temp_audio.name

        # Transcribe with Whisper
        result = model.transcribe(temp_audio_path)
        question = result["text"]
        print(f"You asked: {question}")

        # Send to Groq
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # You can change to another Groq-supported model
            messages=[
                {"role": "user", "content": question}
            ]
        )

        answer = response.choices[0].message.content
        print(" AI Answer:", answer)
        await websocket.send_text(answer)

    except Exception as e:
        print("Error:", e)
        await websocket.send_text("An error occurred on the server.")
        