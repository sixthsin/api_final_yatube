from rest_framework import mixins, viewsets


class CreateListViewSet(viewsets.GenericViewSet,
                        mixins.CreateModelMixin,
                        mixins.ListModelMixin):
    pass
