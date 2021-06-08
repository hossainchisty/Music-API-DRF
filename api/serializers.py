from rest_framework import serializers
from .models import Song,Singer

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['title','singer']

class SingerSerializer(serializers.HyperlinkedModelSerializer):
    song_by = SongSerializer(many=True)
    class Meta:
        model = Singer
        fields = ['artist','song_by']

