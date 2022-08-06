# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: autoware_protobuf/geometry_msgs/msg/pose_stamped.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from autoware_protobuf.std_msgs.msg import header_pb2 as autoware__protobuf_dot_std__msgs_dot_msg_dot_header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='autoware_protobuf/geometry_msgs/msg/pose_stamped.proto',
  package='geometry_msgs.msg',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n6autoware_protobuf/geometry_msgs/msg/pose_stamped.proto\x12\x11geometry_msgs.msg\x1a+autoware_protobuf/std_msgs/msg/header.proto\"Z\n\x0bPoseStamped\x12$\n\x06header\x18\x01 \x01(\x0b\x32\x14.std_msgs.msg.Header\x12%\n\x04pose\x18\x02 \x01(\x0b\x32\x17.geometry_msgs.msg.Pose\"f\n\x04Pose\x12*\n\x08position\x18\x01 \x01(\x0b\x32\x18.geometry_msgs.msg.Point\x12\x32\n\x0borientation\x18\x02 \x01(\x0b\x32\x1d.geometry_msgs.msg.Quaternion\"(\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\"8\n\nQuaternion\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\t\n\x01w\x18\x04 \x01(\x01\x62\x06proto3')
  ,
  dependencies=[autoware__protobuf_dot_std__msgs_dot_msg_dot_header__pb2.DESCRIPTOR,])




_POSESTAMPED = _descriptor.Descriptor(
  name='PoseStamped',
  full_name='geometry_msgs.msg.PoseStamped',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='geometry_msgs.msg.PoseStamped.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pose', full_name='geometry_msgs.msg.PoseStamped.pose', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=212,
)


_POSE = _descriptor.Descriptor(
  name='Pose',
  full_name='geometry_msgs.msg.Pose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='geometry_msgs.msg.Pose.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='geometry_msgs.msg.Pose.orientation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=214,
  serialized_end=316,
)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='geometry_msgs.msg.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='geometry_msgs.msg.Point.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='geometry_msgs.msg.Point.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='geometry_msgs.msg.Point.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=318,
  serialized_end=358,
)


_QUATERNION = _descriptor.Descriptor(
  name='Quaternion',
  full_name='geometry_msgs.msg.Quaternion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='geometry_msgs.msg.Quaternion.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='geometry_msgs.msg.Quaternion.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='geometry_msgs.msg.Quaternion.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='w', full_name='geometry_msgs.msg.Quaternion.w', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=360,
  serialized_end=416,
)

_POSESTAMPED.fields_by_name['header'].message_type = autoware__protobuf_dot_std__msgs_dot_msg_dot_header__pb2._HEADER
_POSESTAMPED.fields_by_name['pose'].message_type = _POSE
_POSE.fields_by_name['position'].message_type = _POINT
_POSE.fields_by_name['orientation'].message_type = _QUATERNION
DESCRIPTOR.message_types_by_name['PoseStamped'] = _POSESTAMPED
DESCRIPTOR.message_types_by_name['Pose'] = _POSE
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['Quaternion'] = _QUATERNION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PoseStamped = _reflection.GeneratedProtocolMessageType('PoseStamped', (_message.Message,), dict(
  DESCRIPTOR = _POSESTAMPED,
  __module__ = 'autoware_protobuf.geometry_msgs.msg.pose_stamped_pb2'
  # @@protoc_insertion_point(class_scope:geometry_msgs.msg.PoseStamped)
  ))
_sym_db.RegisterMessage(PoseStamped)

Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), dict(
  DESCRIPTOR = _POSE,
  __module__ = 'autoware_protobuf.geometry_msgs.msg.pose_stamped_pb2'
  # @@protoc_insertion_point(class_scope:geometry_msgs.msg.Pose)
  ))
_sym_db.RegisterMessage(Pose)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), dict(
  DESCRIPTOR = _POINT,
  __module__ = 'autoware_protobuf.geometry_msgs.msg.pose_stamped_pb2'
  # @@protoc_insertion_point(class_scope:geometry_msgs.msg.Point)
  ))
_sym_db.RegisterMessage(Point)

Quaternion = _reflection.GeneratedProtocolMessageType('Quaternion', (_message.Message,), dict(
  DESCRIPTOR = _QUATERNION,
  __module__ = 'autoware_protobuf.geometry_msgs.msg.pose_stamped_pb2'
  # @@protoc_insertion_point(class_scope:geometry_msgs.msg.Quaternion)
  ))
_sym_db.RegisterMessage(Quaternion)


# @@protoc_insertion_point(module_scope)
