from rest_framework import serializers
from .models import Room, Booking

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','name','description','price','type','created_at','modified_at']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
    
    def to_representation(self, instance):
        representation = dict()
        representation["id"] = instance.id
        representation["customer_name"] = instance.customer_name
        representation["room_id"] = instance.room_id.id
        representation["room_name"] = instance.room_id.name
        representation["start_date"] = instance.start_date
        representation["start_date_string"] = instance.start_date.strftime('%B %d %Y')
        representation["start_time_string"] = instance.start_date.strftime('%H:%M')
        representation["end_date"] = instance.end_date
        representation["end_date_string"] = instance.end_date.strftime('%B %d %Y')
        representation["end_time_string"] = instance.end_date.strftime('%H:%M')
        representation["created_at"] = instance.created_at
        representation["modified_at"] = instance.modified_at

        return representation