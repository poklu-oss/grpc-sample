import grpc
from gen import micro_pb2, micro_pb2_grpc


class DigestorClient(object):
    """
    Client for accessing the gRPC functionality
    """

    def __init__(self):
        # configure the host and the
        # the port to which the client should connect
        # to.
        self.host = 'localhost'
        self.server_port = 46001

        # instantiate a communication channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client to the server channel
        self.stub = micro_pb2_grpc.SearchServiceStub(self.channel)

    def get_digest(self):
        """
        Client function to call the rpc for GetDigest
        """
        message = micro_pb2.FooRequest(foo=1, bar="hello")
        return self.stub.Search(message)

if __name__=="__main__":
    cl = DigestorClient()
    message=micro_pb2.FooRequest(foo=1,bar="hello")
    data = (cl.get_digest())
    print (data)
