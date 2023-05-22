from rest_framework import generics


from blogs.models import LikeDislike
from blogs.serializers import LikeDislikeSerializer, LikeDislikeDetailSerializer


class LikeDislikeListCreateView(generics.ListCreateAPIView):
    queryset = LikeDislike.objects.order_by("-id")

    def get_serializer_class(self):
        if self.request.method == "POST":
            return LikeDislikeDetailSerializer
        return LikeDislikeSerializer


class LikeDislikeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LikeDislike.objects.all()
    lookup_field = "id"

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return LikeDislikeDetailSerializer
        return LikeDislikeSerializer
