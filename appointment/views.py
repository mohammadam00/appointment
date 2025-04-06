from .models import Appointment, AppointmentDay
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AppointmentDaySerializer, AppointmentSerializer
# from .turn_maker import create_reservations


class AppointmentDayView(ListAPIView):
    queryset = AppointmentDay.objects.all()
    serializer_class = AppointmentDaySerializer
    # create_reservations()


class AppointmentTime(APIView):
    def get(self, request, pk):
        try:
            day = AppointmentDay.objects.get(id=pk)
            times = Appointment.objects.filter(day=day).values_list('time')
            return Response(times)
        except AppointmentDay.DoesNotExist:
            return Response({"error": "روز انتخاب شده وجود ندارد."}, status=status.HTTP_404_NOT_FOUND)


class CreateAppointment(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        day = request.data.get('day')
        time = request.data.get('time')

        if not Appointment.objects.filter(day_id=day, time=time).exists():
            return Response({"error": "زمان انتخاب شده پر شده است."}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
