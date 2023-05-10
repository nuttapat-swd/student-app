from core.models import Student, Address
from rest_framework import serializers

class AddressSerializer(serializers.ModelSerializer):
    """Serializer for Address"""
    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ['id', 'is_deleted', 'deleted_at', 'created_at', 'updated_at']

class AddressForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'detail', 'sub_district', 'district', 'city', 'zip_code')
        read_only_fields = ['id']

class StudentSerializer(serializers.ModelSerializer):
    """Serializer for Student"""
    # count = serializers.SerializerMethodField()
    address = AddressForUserSerializer(required=False)
    class Meta:
        model = Student
        fields = ('id', 'created_at', 'updated_at', 'first_name', 'last_name', 'student_id', 'description', 'address')
        read_only_fields = ['id','created_at', 'updated_at']
    
    def _get_or_create_student(self, address, student):
        """Handle getting or creaing tags"""
        address_obj, created = Address.objects.get_or_create(**address)
        student.address = address_obj
        student.save()

    def create(self, validated_data):
        """custom create method"""
        address = validated_data.pop('address', None)
        student = Student.objects.create(**validated_data)
        self._get_or_create_student(address, student)
        return student

    def update(self, instance, validated_data):
        """update student"""
        address = validated_data.pop('address', None)
        if address is not None:
            self._get_or_create_student(address, instance)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance

class StudentDetailSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = '__all__'

    def get_address(self, instance):
        if instance.address :
            return AddressForUserSerializer(instance.address).data
        else:
            return None
        
    def _get_or_create_student(self, address, student):
        """Handle getting or creaing tags"""
        address_obj, created = Address.objects.get_or_create(**address)
        student.address = address_obj
        student.save()

    def update(self, instance, validated_data):
        """update student"""
        address = validated_data.pop('address', None)
        print(address)
        if address is not None:
            print("find address")
            self._get_or_create_student(address, instance)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
        
            



    
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data_dict = data
    #     if instance.address :
    #         data_dict.update({'address':AddressSerializer(instance.address).data})
    #     else:
    #         data_dict.update({'address':None})
    #     return data_dict


