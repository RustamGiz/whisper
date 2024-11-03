import whisper

model = whisper.load_model("turbo")
result = model.transcribe("20241002_185106.m4a")
print(result["text"])

