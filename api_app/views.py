from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .serializer import *
from .models import Car, CarPlan, Posts, PostRates
from rest_framework import status
from django.db.models import Q
from django.core.mail import send_mail
from threading import Thread
import requests
from django.shortcuts import get_object_or_404
# Create your views here.


#functions
@api_view()    #(['POST', 'GET'])
@permission_classes([AllowAny])
# @authentication_classes([TokenAuthentication])
def messager(request):
    print(request.query_params)
    print(request.query_params['num'])
    number = request.query_params['num']
    new_num = number * 2
    return Response({'message': 'Hello world', 'number':new_num})


#classes

class Message(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        print(request.query_params)
        print(request.query_params['num'])
        number = int(request.query_params['num'])
        new_num = number * 3
        return Response({'message': 'Hello world', 'number': new_num})


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
   
    def get_queryset(self):
        car = Car.objects.all()
        return car
    

    # def retrieve(self, request, *arg, **kwargs):  
    #     params = kwargs
    #     print(params['pk'])
    #     params_list = params['pk'].split('-')
    #     cars = Car.objects.filter(brand= params_list[0], car_model = params_list[1], engine_type=params_list[2])
    #     serializer = CarSerializer(cars, many=True)
    #     return Response(serializer.data)   
         

    def create(self, request, *args, **kwargs):
        car_data = request.data
        
        new_car = Car.objects.create(car_plan=CarPlan.objects.get(id=car_data['car_plan']), 
                                     brand = car_data['brand'],
                                     car_model=car_data['car_model'],
                                     production_year=car_data['production_year'],
                                     car_body = car_data['car_body'],
                                     engine_type = car_data['engine_type'],
                                     )
        new_car.save()
        serializer = CarSerializer(new_car)

        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        data= request.data
        car_object = self.get_object()
        car_plan = CarPlan.objects.get(plan_name=data['plan_name'])
        
        car_object.car_plan = car_plan
        car_object.brand = data['brand']
        car_object.car_model = data['car_model']
        car_object.production_year = data['production_year']
        car_object.car_body = data['car_body']
        car_object.engine_type = data['engine_type']
        car_object.save()

        serializer = CarSerializer(car_object)

        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        data = request.data

        car_object = self.get_object()
        
        try:
            car_plan = CarPlan.objects.get(plan_name=data['plan_name'])
            car_object.car_plan = car_plan
        except KeyError:
            pass

        car_object.brand = data.get('brand' , car_object.brand)
        car_object.car_model = data.get('car_model' , car_object.car_model)
        car_object.production_year = data.get('production_year' , car_object.production_year)
        car_object.car_body = data.get('car_body' , car_object.car_body)
        car_object.engine_type = data.get('engine_type' , car_object.engine_type)
        car_object.save()

        serializer = CarSerializer(car_object)

        return Response(serializer.data)
    

    def destroy(self, request, *args, **kwargs):
        if request.user == 'admin':
           car = self.get_object()
           car.delete()
           message = {'message':'item deleted'}
        else:
           message = {'message':'Not Allowed'} 
        return Response(message)


class CarApiView(APIView):
     serializer_class = CarSerializer
     permission_classes = [AllowAny]
     throttle_scope = 'api_app'

     def get_queryset(self):
         return Car.objects.all()
     
     

     def get(self, request, *args, **kwargs):
         try:
            id = request.query_params['id']
            if id != None:
              car = Car.objects.get(id=id)
              serializer = CarSerializer(car, many=False)
         except:   
             cars = self.get_queryset()
             serializer = CarSerializer(cars, many=True)    

         return Response(serializer.data)
     
    
     def post(self, request, *args, **kwargs):
         car_data = request.data
         cars = Car.objects.create(car_plan=CarPlan.objects.get(id=car_data['car_plan']), 
                                     brand = car_data['brand'],
                                     car_model=car_data['car_model'],
                                     production_year=car_data['production_year'],
                                     car_body = car_data['car_body'],
                                     engine_type = car_data['engine_type'],
                                     )
         cars.save()
         serializer = CarSerializer(cars)

         return Response(serializer.data)
     
     def put(self, request, *args, **kwargs):
         id  = request.query_params['id']
         data = request.data
         car_object = Car.objects.get(id=id)
         car_plan = CarPlan.objects.get(plan_name=data['plan_name'])

         car_object.car_plan = car_plan
         car_object.brand = data['brand']
         car_object.car_model = data['car_model']
         car_object.production_year = data['production_year']
         car_object.car_body = data['car_body']
         car_object.engine_type = data['engine_type']

         car_object.save()

         serializer = CarSerializer(car_object)
         return Response(serializer.data)
     
     def patch(self, request, *args, **kwargs):
         id = request.query_params['id']
         data = request.data
         car_object = Car.objects.get(id=id)

         try:
            car_plan = CarPlan.objects.get(plan_name = data['plan_name'])
            car_object.car_plan = car_plan
         except KeyError:
             pass
     
         
         car_object.brand = data.get('brand', car_object.brand)
         car_object.car_model = data.get('car_model', car_object.car_model)
         car_object.production_year = data.get('production_year', car_object.production_year)
         car_object.car_body = data.get('car_body', car_object.car_body)
         car_object.engine_type = data.get('engine_type', car_object.engine_type)

         car_object.save()

         serializer = CarSerializer(car_object)

         return Response(serializer.data)


     
     def delete(self, request, *args, **kwargs):
         id = request.query_params['id']
         car_object = Car.objects.get(id=id)
         car_object.delete()
         return Response('Item Deleted Succesfully')


class CarPlanApiView(APIView):
    serializer_class = CarPlanSerializer
    
    def get_queryset(self):
        return CarPlan.objects.all()
    
    def get(self, request):
        carplan = self.get_queryset()
        serializer = CarPlanSerializer(carplan, many=True)
        return Response(serializer.data)
    


class HandleNotification(Thread):

    def __init__(self, subject, message, recipient_list):
        self.subject = subject
        self.message = message
        self.recipient_list = recipient_list
        Thread.__init__(self)

        
    def run(self):
        from_email = 'tonyblair246@gmail.com'
        send_mail(self.subject, self.message, from_email,self.recipient_list, fail_silently=False)
         

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostsSerializer

    def send_email(self, subject, message, recipient_list):
        from_email = 'tonyblair246@gmail.com'
        send_mail(subject, message, from_email,recipient_list, fail_silently=False)

    def get_queryset(self):
        return Posts.objects.all()

    # def retrieve(self, request, *args, **kwargs):
    #     posts = self.get_queryset()
    #     serializer = PostsSerializer(posts, many=True)
    #     return Response(serializer.data)

    def list(self, request):
        posts = self.get_queryset()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        posts = self.get_queryset()
        user = get_object_or_404(posts, pk=pk)
        serializer = PostsSerializer(user)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        post_data = request.data

        new_rates = PostRates.objects.create(likes = 0, #post_data['rates']['likes'],
                                             dislikes = 0) #post_data['rates']['dislikes'])
        new_rates.save()

        new_post = Posts.objects.create(post_title = post_data['post_title'],
                                        post_body = post_data['post_body'],
                                        rates = new_rates
                                        )
        new_post.save()
        # self.send_email('Note from Tony', 'this is the only blaination', ['tonyblair246@gmail.com',])
        HandleNotification('Note from Tony', 'this is blaination django', ['tonyblair246@gmail.com',]).start()

        serializer = PostsSerializer(new_post)
        return Response(serializer.data)


class PostRatesViewSet(viewsets.ModelViewSet):
    serializer_class = PostRatesSerializer


    def get_queryset(self):
        return PostRates.objects.all()

    def retrieve(self, request, *args, **kwargs):
        postrates = self.get_queryset()
        serializer = PostRatesSerializer(postrates, many=True)
        return Response(serializer.data)    
    
    def create(self, request, *args, **kwargs):
        data = request.data
        new_postrates = PostRates.objects.create(likes=data['likes'],
                                                 dislikes=data['dislikes']
                                                 )
        new_postrates.save()
        serializer = PostRatesSerializer(new_postrates)
        return Response(serializer.data)


class StudentsViewSet(viewsets.ModelViewSet):
    serializer_class = StudentsSerializer

    def get_queryset(self):
        return Students.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        new_student = Students.objects.create(name=data['name'], age=data['age'], grade=data['grade'])
        new_student.save()

        for module in data['modules']:
            module_obj = Modules.objects.get(module_name = module['module_name'])
            new_student.modules.add(module_obj)
            
        
        serializer = StudentsSerializer(new_student)
        return Response(serializer.data)
    

class ModulesViewSet(viewsets.ModelViewSet):
    serializer_class = ModulesSerializer

    def get_queryset(self):
        return Modules.objects.all()
    
   
class ForecastViewset(viewsets.ModelViewSet):
    serializer_class = ForecastSerializer

    def get_queryset(self):
        return Forecast.objects.all()

    def _get_weather_data(self):
        url = 'https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=9af44f63ea84404d3a13b76322440a1f'
        api_request = requests.get(url)

        try:
            api_request.raise_for_status()
            return api_request.json()
        except:
            return None

    def save_data(self):
        weather_data = self._get_weather_data()
        if weather_data is not None:
            try:
                weather_object = Forecast.objects.create(temperature=weather_data['main']['temp'],
                                                         description=weather_data['weather'][0]['description'],
                                                         city=weather_data['name'])
                weather_object.save()
            except:
                pass  
        # serializer = ForecastSerializer(weather_object)
        # return Response(serializer.data)       
        
