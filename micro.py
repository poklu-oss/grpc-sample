from gen import  micro_pb2_grpc,micro_pb2
import os
import grpc
from concurrent import futures
import time
from gen.micro_pb2_grpc import  SearchServiceServicer

class SearchServicer(SearchServiceServicer):
    def __init__(self, *args, **kwargs):
        self.server_port = 46001
    def Search(self,request,content):
        print("hello")
        res = micro_pb2.FooResponse(req=request)
        return res
    def ToFro(self, request_iterator, context):
        for request in request_iterator:
            res = micro_pb2.FooResponse(req=request)
            return res;


    def start_server(self):
        """
        Function which actually starts the gRPC server, and preps
        it for serving incoming connections
        """
        # declare a server object with desired number
        # of thread pool workers.
        with open('keys/server.key', 'rb') as f:
            private_key = f.read()
        with open('keys/server.crt', 'rb') as f:
            certificate_chain = f.read()

        # create server credentials
        server_credentials = grpc.ssl_server_credentials(((private_key, certificate_chain, ), ))

        digestor_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        # This line can be ignored
        micro_pb2_grpc.add_SearchServiceServicer_to_server(self, digestor_server)

        # bind the server to the port defined above
        #digestor_server.add_insecure_port('[::]:{}'.format(self.server_port))
        digestor_server.add_secure_port('[::]:{}'.format(self.server_port),server_credentials)
        # start the server
        digestor_server.start()
        print ('Digestor Server running ...')

        try:
            # need an infinite loop since the above
            # code is non blocking, and if I don't do this
            # the program will exit
            while True:
                time.sleep(60 * 60 * 60)
        except KeyboardInterrupt:
            digestor_server.stop(0)
            print('Digestor Server Stopped ...')

if __name__ == '__main__':

    try:
        curr_server = SearchServicer()
        curr_server.start_server()

    except  Exception as e:
        print(e)