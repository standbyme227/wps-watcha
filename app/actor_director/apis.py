from rest_framework import permissions, generics

from .models import Member
from .serializers import MemberDetailSerializer


__all__ = (
    'MovieMemberDetailView',
)


class MovieMemberDetailView(generics.RetrieveAPIView):
    # 배우나 감독의 Detail을 자세히 볼 수 있는 View다.
    # 좀 더 유연한 generic view로 짰고 수정이나 생성, 삭제가 필요없어서 조회만 가능한 RetrieveAPIView로 구성했다.
    permission_classes = (
        # generic에서만 그런지 API에서도 이렇게 class를 지정하고 안에 permission을 넣는지는 아직 잘 모르겠지만
        # 일단 이렇게 처리했다.
        permissions.IsAuthenticated,
        # Token으로 인증된 사용자. 즉, 로그인 사용자만 허용되는 permission이다.
    )

    queryset = Member.objects.all()
    # queryset은 배우와 감독이 있는 Member의 objects들로 한다.
    serializer_class = MemberDetailSerializer
    # serializer란 현재 저장되어있는 데이터를 API에 맞게 Json데이터로 변환해서 정보전달이 용이하도록 만들어주는 녀석이다.
    # 물론 그 과정에서 다양한 옵션들을 부과해서 좀 더 유용하게 사용할 수 있다.
    # 여기서는 배우랑 감독의 디테일을 가져올 수 있게 설정해놓지 않았나 싶다.

    def get_serializer_context(self):
        print('url의 pk값: ', self.kwargs['pk'])  # url의 pk값 출력하기
        # url의 pk값을 왜 출력할까????
        return {'login_user': self.request.user}
        # 반환 값은 dict로 key로는 login_user, value로는 request.user로 한다.
