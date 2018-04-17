from rest_framework import permissions, generics

from .models import Member
from .serializers import MemberDetailSerializer


__all__ = (
    'MovieMemberDetailView',
)


class MovieMemberDetailView(generics.RetrieveAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    queryset = Member.objects.all()
    serializer_class = MemberDetailSerializer

    def get_serializer_context(self):
        print('url의 pk값: ', self.kwargs['pk'])  # url의 pk값 출력하기
        return {'login_user': self.request.user}
