from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class DataView(generics.ListCreateAPIView):
    queryset=DataModel.objects.all()
    serializer_class=DataSerializer
    
    
    def perform_create(self, serializer):
        contact = serializer.save()

        # Send the email
        title = contact.title
        email = contact.email
        message = contact.message
        subject = 'New Contact Form Submission'
        recipient_email = 'vasuvirani54@gmail.com'  # Replace with your email address
        message_body = f"Title: {title}\nEmail: {email}\nMessage: {message}"
        send_mail(subject, message_body, email, [recipient_email])


    
# class DataView(APIView):
#     def post(self, request):
#         serializer = DataSerializer(data=request.data)
#         if serializer.is_valid():
#             title = serializer.validated_data['title']
#             email = serializer.validated_data['email']
#             message = serializer.validated_data['message']

#             # Save the contact form data to the database
#             contact = DataModel(title=title, email=email, message=message)
#             contact.save()

#             # Send the email
#             subject = 'New Contact Form Submission'
#             recipient_email = 'vasuvirani54@gmail.com'  # Replace with your email address
#             message_body = f"Title: {title}\nEmail: {email}\nMessage: {message}"
#             send_mail(subject, message_body, email, [recipient_email])

#             return Response({'success': 'Contact form submitted successfully'}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 