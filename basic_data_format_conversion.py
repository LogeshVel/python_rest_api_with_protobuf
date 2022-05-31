from google.protobuf import json_format
from google.protobuf.internal.well_known_types import Timestamp
from google.protobuf.text_format import MessageToString, MessageToBytes, Parse
from python_proto import Person_pb2

person_1 = Person_pb2.Person()
print("Printing uninitialized Person object")
print(person_1)

person_1.id = 1
print("Initialized only one field in Person 1")
print(person_1)

person_1.name = "Logesh"
person_1.age = 21
print("Fully initialized Person 1")
print(person_1)

print("Message in bytes")
print(MessageToBytes(person_1))
print("++++++++++++++++++++++++++++++++++++")

print("\nInitialized second Person at the beginning")
person_2 = Person_pb2.Person(id=2, name="Logesh Vel", age=22)
print(person_2)

print("In bytes")
person_2_in_bytes = MessageToBytes(person_2)
print(person_2_in_bytes)
print(type(person_2_in_bytes))

print("Bytes to Person type")
person_2_bytes_to_msg = Parse(person_2_in_bytes, Person_pb2.Person())
print(person_2_bytes_to_msg)
print(type(person_2_bytes_to_msg))

print("Message to Json format")
msg_in_json = json_format.MessageToJson(person_2)
print(msg_in_json)

print("JSON to msg")
print(json_format.Parse(msg_in_json, Person_pb2.Person()))

print("Message to Dict")
msg_in_dict = json_format.MessageToDict(person_2)
print(msg_in_dict)

print("Dict to Message")
print(json_format.ParseDict(msg_in_dict, Person_pb2.Person()))

print("Message to String")
person_2_in_str = MessageToString(person_2)
print(person_2_in_str)
print(type(person_2_in_str))

print("String to message")
person_2_str_to_msg = Parse(person_2_in_str, Person_pb2.Person())
print(person_2_str_to_msg)
print(type(person_2_str_to_msg))

