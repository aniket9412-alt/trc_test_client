# Copyright 2015, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""The Python implementation of the GRPC helloworld.Greeter client."""

import argparse

import grpc

import helloworld_pb2
import helloworld_pb2_grpc
import os

from opencensus.ext.grpc import client_interceptor
from opencensus.ext.stackdriver import trace_exporter as stackdriver_exporter
from opencensus.trace.tracer import Tracer


def run(host, api_key):
    channel = grpc.insecure_channel(host)
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    metadata = []
    if api_key:
        metadata.append(('x-api-key', api_key))
    
    exporter = stackdriver_exporter.StackdriverExporter()
    tracer = Tracer(exporter=exporter)
    tracer_interceptor = client_interceptor.OpenCensusClientInterceptor(tracer,host_port=host)

    response = stub.SayHello(
        helloworld_pb2.HelloRequest(name='you'))
    print('Greeter client received: ' + response.message)

    response = stub.SayHelloAgain(
        helloworld_pb2.HelloRequest(name='you'))
    print('Greeter client received: ' + response.message)

    response = stub.SayHelloNew(
        helloworld_pb2.HelloRequest(name='you'))
    print('Greeter client received: ' + response.message)


    response = stub.SayHelloIndia(
        helloworld_pb2.HelloRequest(name='you'))
    print('Greeter client received: ' + response.message)

    response = stub.SayHelloIndiaAgain(
        helloworld_pb2.HelloRequest(name='you'))
    print('Greeter client received: ' + response.message)

    response = stub.SayHelloIndiaNew(
        helloworld_pb2.HelloRequest(name='you'))
    print('Greeter client received: ' + response.message)

# Insert the HOST_PORT value= <hello svc external IP>:80
HOST_PORT = os.environ['HOST']
#Insert the api key from google cloud
API="AIzaSyA4jzysHmODxOuQyylt1DEYZynbL7O0JtM"

if __name__ == '__main__':
    run(HOST_PORT, API)