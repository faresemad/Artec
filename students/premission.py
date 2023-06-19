from rest_framework import mixins, viewsets


class CreateRetrieveUpdate(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    """

    pass


class RetrieveUpdate(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    A viewset that provides default `retrieve()`, `update()`,
    """

    pass
