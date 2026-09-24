import json
import base64
from google import genai

class TTSModel:
    def __init__(self, credentials_path="./geminiCred.json"):
        self.api_key = self._load_credentials(credentials_path)
        self.client = genai.Client(api_key=self.api_key)

    def _load_credentials(self, path):
        with open(path, "r") as f:
            key_data = json.load(f)
            return key_data["key"]

    def generate_audio(self, text, style, output_filename="output.wav"):
        interaction = self.client.interactions.create(
            model="gemini-3.8-flash-tts",
            input=[{
                "type": "user_input",
                "content": [
                    {
                        "type": "text",
                        "text": text,
                        "annotations": [{
                            "type": "speech_metadata",
                            "style": style
                        }]
                    }
                ]
            }],
            response_format={
                "type": "audio",
                "mime_type": "audio/wav",
                "sample_rate": 24000
            },
            generation_config={
                "speech_config": [
                    {"voice": "Zephyr"}
                ]
            }
        )

        with open(output_filename, "wb") as f:
            f.write(base64.b64decode(interaction.output_audio.data))