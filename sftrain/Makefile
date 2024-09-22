PYTHON = python
CXX = g++

all: python_pb

python_pb: sftrain/proto/elastic_training.proto
	$(PYTHON) -m grpc_tools.protoc -I. \
	    sftrain/proto/elastic_training.proto --python_out=. --grpc_python_out=.
