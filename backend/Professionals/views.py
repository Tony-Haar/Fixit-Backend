from Professionals.models import Professional 
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions, authentication

from .models import Profile, ExperienceBackground
from .serializers import ProfessionalSerializer, ProfileSerializer, ExperienceBackgroundSerializer
from .permissions import IsProfessional


# Professionals views
class ProfessionalListCreateAPIView(generics.ListCreateAPIView):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer 
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProfessionalDetailAPIView(generics.RetrieveAPIView):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProfessionalUpdateAPIView(generics.UpdateAPIView):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsProfessional]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", True) # Ensure partial updates are allowed
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data, partial = partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ProfessionalDestroyAPIView(generics.DestroyAPIView):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsProfessional]


# Profile views
class ProfileCreateAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsProfessional]

class ProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ProfileUpdateAPIView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsProfessional]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data, partial = partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# Experience Background view
class ExperienceBackgroundCreateAPIView(generics.CreateAPIView):
    queryset = ExperienceBackground.objects.all()
    serializer_class = ExperienceBackgroundSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsProfessional]

class ExperienceBackgroundDetailAPIView(generics.RetrieveAPIView):
    queryset = ExperienceBackground.objects.all()
    serializer_class = ExperienceBackgroundSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ExperienceBackgroundListAPIView(generics.ListAPIView):
    serializer_class = ExperienceBackgroundSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """ 
        Assuming your ExperienceBackground model is related to the 
        Profile model, and the Profile model is related to the Professional 
        model, the relationship is likely established through ForeignKey fields.

        To filter ExperienceBackground objects by a field in the Professional 
        model, you need to traverse through the relationships. This is done 
        using double underscores (__) to follow the ForeignKey relationships.

        Why Not professional_id Directly?
        There is no direct professional_id field in the ExperienceBackground 
        model. The field professional_id doesn't exist in the ExperienceBackground 
        model; instead, there is a profile field that is related to a Profile 
        object, which in turn is related to a Professional object.

        Therefore, to query ExperienceBackground objects based on a Professional's ID, 
        you need to follow the chain of relationships using profile__professional__id.

        This is a common technique in Django for handling complex queries 
        involving related models.
        """
        professional_id = self.kwargs['professional_id']
        return ExperienceBackground.objects.filter(profile__professional__id = professional_id)

class ExperienceBackgroundUpdateAPIView(generics.UpdateAPIView):
    queryset = ExperienceBackground.objects.all()
    serializer_class = ExperienceBackgroundSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsProfessional]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data, partial = partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ExperienceBackgroundDestroyAPIView(generics.DestroyAPIView):
    queryset = ExperienceBackground.objects.all()
    serializer_class = ExperienceBackgroundSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsProfessional]

