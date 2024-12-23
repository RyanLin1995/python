# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import user_reco_pb2 as user__reco__pb2


class UserRecommendStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.user_recommend = channel.unary_unary(
            '/UserRecommend/user_recommend',
            request_serializer=user__reco__pb2.User.SerializeToString,
            response_deserializer=user__reco__pb2.Track.FromString,
        )
        self.article_recommend = channel.unary_unary(
            '/UserRecommend/article_recommend',
            request_serializer=user__reco__pb2.Article.SerializeToString,
            response_deserializer=user__reco__pb2.Similar.FromString,
        )


class UserRecommendServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def user_recommend(self, request, context):
        """feed recommend
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def article_recommend(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserRecommendServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'user_recommend': grpc.unary_unary_rpc_method_handler(
            servicer.user_recommend,
            request_deserializer=user__reco__pb2.User.FromString,
            response_serializer=user__reco__pb2.Track.SerializeToString,
        ),
        'article_recommend': grpc.unary_unary_rpc_method_handler(
            servicer.article_recommend,
            request_deserializer=user__reco__pb2.Article.FromString,
            response_serializer=user__reco__pb2.Similar.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'UserRecommend', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
