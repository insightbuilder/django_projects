#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# class SnippetSerializer(serializers.Serializer):
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template':'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES,default='friendly')
    created = serializers.CharField(required=False)

    def create(self, validated_data):
        #Create an dreturn a new 'Snippet' instance given valid data

        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #Update and return an existing 'snippet' instance given validated data
        instance.title = validated_data.get('title',instance.title)
        instance.code= validated_data.get('code',instance.code)
        instance.linenos= validated_data.get('linenos',instance.linenos)
        instance.language= validated_data.get('language',instance.language)
        instance.style= validated_data.get('style',instance.style)
        instance.created= validated_data.get('created',instance.style)
        instance.save()

        return instance
    """
