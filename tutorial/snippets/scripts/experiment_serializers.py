from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

def run():
    snips = Snippet.objects.all()

    serial_snip = SnippetSerializer(snips)

    print(serial_snip[0])