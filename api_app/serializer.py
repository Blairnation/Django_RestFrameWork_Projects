from rest_framework import serializers
from .models import Car, CarPlan, Posts, PostRates, Modules, Students, Forecast
highest_age = 1

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        #['brand', 'car_model', 'production_year', 'car_body', 'engine_type']
        depth = 1

class CarPlanSerializer(serializers.ModelSerializer):
    # car = serializers.StringRelatedField(many=True)

    class Meta:
        model = CarPlan
        fields = '__all__'
  
class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__' 
        depth = 1 

class PostRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostRates
        fields = '__all__' 


class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = '__all__'

class StudentsSerializer(serializers.ModelSerializer): 

    oldest = serializers.SerializerMethodField('_get_oldest_student')


    def _get_oldest_student(self, student_object):
        global highest_age
        
        age = getattr(student_object, 'age')
        if age and age > highest_age:
            highest_age = age
            return highest_age
        else:
            return highest_age

    class Meta:
        model =  Students
        fields = ['id', 'name', 'age', 'grade','oldest', 'modules']
        depth = 1
                
class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = ['id', 'timstamp', 'temperature', 'description', 'city']