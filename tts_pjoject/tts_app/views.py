from django.http import JsonResponse, HttpResponse
from django.views import View

# from google.cloud import texttospeech
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import uuid
import requests
# from deepgram import DeepgramClient, SpeakOptions

DEEPGRAM_API_KEY = os.environ["DEEPGRAM_API_KEY"]

# class TextToSpeechView(View):
#     def post(self, request, *args, **kwargs):
#         text = request.POST.get("text")
#         if not text:
#             return JsonResponse({"error": "No text provided"}, status=400)

#         client = texttospeech.TextToSpeechClient()
#         # client is connected above, so there is a different
#         # way to connect to google services

#         input_text = texttospeech.SynthesisInput(text=text)

#         voice = texttospeech.VoiceSelectionParams(
#             language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
#         )
#         audio_config = texttospeech.AudioConfig(
#             audio_encoding=texttospeech.AudioEncoding.MP3
#         )

#         response = client.synthesize_speech(
#             input=input_text, voice=voice, audio_config=audio_config
#         )

#         filename = "output.mp3"
#         with open(filename, "wb") as out:
#             out.write(response.audio_content)

#         with open(filename, "rb") as out:
#             response = HttpResponse(out.read(), content_type="audio/mpeg")
#             response["Content-Disposition"] = f'attachment; filename="{filename}"'
#             os.remove(filename)
#             return response


@method_decorator(csrf_exempt, name="dispatch")
class TextToSpeechView(View):
    def post(self, request, *args, **kwargs):
        text = request.POST.get("text")
        if not text:
            return JsonResponse({"error": "No text provided"}, status=400)

        # Deepgram API call
        deepgram_api_key = os.getenv("DEEPGRAM_API_KEY")
        headers = {
            "Authorization": f"Token {deepgram_api_key}",
            "Content-Type": "application/json",
        }
        json_data = {
            "text": text,
        }

        try:
            response = requests.post(
                "https://api.deepgram.com/v1/speak?model=aura-asteria-en",
                headers=headers,
                json=json_data,
            )
            response.raise_for_status()  # Raises an error for bad HTTP status codes

            filename = f"{uuid.uuid4()}.mp3"
            filepath = os.path.join(settings.MEDIA_ROOT, filename)
            with open(filepath, "wb") as out:
                out.write(response.content)

            audio_url = request.build_absolute_uri(f"/media/{filename}")
            return JsonResponse({"audio_url": audio_url})
        except Exception as e:
            print(f"Exception: {e}")
            return JsonResponse(
                {
                    "error": "Failed to generate speech via Deepgram API",
                    "details": str(e),
                },
                status=500,
            )
        # not required, as the API is writing it by itself
        # with open(filepath, "wb") as out:
        #     out.write(response.audio_content)
