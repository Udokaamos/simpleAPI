from rest_framework import serializers

from blog.models import Post


# class SongSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Song
#         fields = '__all__'
        
        

class PostSerializer(serializers.ModelSerializer):
    song_detail = serializers.ReadOnlyField()
    
    class Meta:
        model = Post
        fields = '__all__'
        # depth=1