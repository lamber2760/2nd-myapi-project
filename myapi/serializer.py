from rest_framework import serializers
from myapi.models import MyTodo


class TodoSerializer(serializers.ModelSerializer):
    class Meta():
        model = MyTodo
        fields = "__all__"