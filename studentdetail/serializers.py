from core.models import Student, Address
from rest_framework import serializers

class AddressSerializer(serializers.ModelSerializer):
    """Serializer for Address"""

    class Meta:
        model = Address
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    """Serializer for Student"""
    count = serializers.SerializerMethodField()

    def get_count(self, stundent):
        return

    class Meta:
        model = Student
        fields = '__all__'

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     queryset = self.Meta.model.objects.all()
    #     # print(queryset.query.__str__())
    #     # print(instance.address.detail)
    #     data['count'] = queryset.count()
    #     data_dict = {'count': data['count'], 'students': [data]}
    #     return data_dict

class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data_dict = data
        data_dict.update({'address':AddressSerializer(instance.address).data})
        return data_dict


