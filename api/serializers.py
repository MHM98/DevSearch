from rest_framework import fields, serializers
from projects.models import project , Tag ,Review
from users.models import profile


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'


class tagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'

class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model=profile
        fields='__all__'

class projectSerializer(serializers.ModelSerializer):
    owner=profileSerializer(profile,many=False)
    tags=tagSerializer(Tag,many=True)
    reviews=serializers.SerializerMethodField() # create a serialized field that you can add any type of method that you want.warning:you have to follow the exat way to define functin for initial this field.
    
    class Meta:
        model=project
        fields='__all__'

    def get_reviews(self,obj):
        reviews=obj.review_set.all()
        serializer=ReviewSerializer(reviews,many=True)
        return serializer.data

