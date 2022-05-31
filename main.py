from flask import Flask
from google.protobuf.text_format import MessageToString, MessageToBytes, Parse
from google.protobuf import json_format
from python_proto import Person_pb2
import logging

simple_proto_api = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)
MESSAGE_BYTES = b''
MESSAGE_STR = ""
MESSAGE_JSON = {}


@simple_proto_api.route('/')
def root_page():
    print("Welcome to the Root page, initializing the Data")
    person_1 = Person_pb2.Person(id=1, name="Logesh", age=21)
    print("Protobuf object")
    print(person_1)

    global MESSAGE_BYTES, MESSAGE_STR, MESSAGE_JSON
    MESSAGE_BYTES = MessageToBytes(person_1)
    MESSAGE_STR = MessageToString(person_1)
    MESSAGE_JSON = json_format.MessageToJson(person_1)
    print(f"Message in bytes\n{MESSAGE_BYTES}")
    print(f"Message in str\n{MESSAGE_STR}")
    print(f"Message to JSON\n{MESSAGE_JSON}")
    return "Successfully initialized the Protobuf data object and made the conversion to bytes, strings and json.\n" \
           "try /str_msg and /b_msg /json_msg URL"


@simple_proto_api.route('/str_msg')
def msg_page():
    print("Data from str msg page")
    str_to_msg = Parse(MESSAGE_STR, Person_pb2.Person())
    print(str_to_msg)
    return {"Message in str": MESSAGE_STR}


@simple_proto_api.route('/b_msg')
def bytes_msg_page():
    print("Data from bytes msg page")
    bytes_to_msg = Parse(MESSAGE_BYTES, Person_pb2.Person())
    print(bytes_to_msg)
    return MESSAGE_BYTES


@simple_proto_api.route('/json_msg')
def json_msg_page():
    print("Data from json msg page")
    json_to_msg = json_format.Parse(MESSAGE_JSON, Person_pb2.Person())
    print(json_to_msg)
    return MESSAGE_JSON
