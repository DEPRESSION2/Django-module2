from rest_framework import serializers


#class ProductSerializers(serializers.Serializers):
	#slug = serializers.SlugzFied(reguired=True, read_only=True, urite_only=True
	#name = serializers.CharFied()



class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']