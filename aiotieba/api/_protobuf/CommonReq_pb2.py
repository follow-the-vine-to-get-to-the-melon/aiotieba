"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 27, 0, '', 'CommonReq.proto')

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0f\x43ommonReq.proto"\xc6\x06\n\tCommonReq\x12\x14\n\x0c_client_type\x18\x01 \x01(\x05\x12\x17\n\x0f_client_version\x18\x02 \x01(\t\x12\x12\n\n_client_id\x18\x03 \x01(\t\x12\x13\n\x0b_phone_imei\x18\x05 \x01(\t\x12\r\n\x05_from\x18\x06 \x01(\t\x12\x0c\n\x04\x63uid\x18\x07 \x01(\t\x12\x12\n\n_timestamp\x18\x08 \x01(\x03\x12\r\n\x05model\x18\t \x01(\t\x12\r\n\x05\x42\x44USS\x18\n \x01(\t\x12\x0b\n\x03tbs\x18\x0b \x01(\t\x12\x10\n\x08net_type\x18\x0c \x01(\x05\x12\x10\n\x08pversion\x18\x18 \x01(\t\x12\x13\n\x0b_os_version\x18\x19 \x01(\t\x12\r\n\x05\x62rand\x18\x1a \x01(\t\x12\x18\n\x10lego_lib_version\x18\x1c \x01(\t\x12\x0f\n\x07\x61pplist\x18\x1d \x01(\t\x12\x0e\n\x06stoken\x18\x1e \x01(\t\x12\x0c\n\x04z_id\x18\x1f \x01(\t\x12\x14\n\x0c\x63uid_galaxy2\x18  \x01(\t\x12\x10\n\x08\x63uid_gid\x18! \x01(\t\x12\x0e\n\x06\x63\x33_aid\x18# \x01(\t\x12\x11\n\tsample_id\x18$ \x01(\t\x12\r\n\x05scr_w\x18% \x01(\x05\x12\r\n\x05scr_h\x18& \x01(\x05\x12\x0f\n\x07scr_dip\x18\' \x01(\x01\x12\x0e\n\x06q_type\x18( \x01(\x05\x12\x13\n\x0bis_teenager\x18) \x01(\x05\x12\x0f\n\x07sdk_ver\x18* \x01(\t\x12\x15\n\rframework_ver\x18+ \x01(\t\x12\x15\n\rnaws_game_ver\x18, \x01(\t\x12\x18\n\x10\x61\x63tive_timestamp\x18\x31 \x01(\x03\x12\x1a\n\x12\x66irst_install_time\x18\x32 \x01(\x03\x12\x18\n\x10last_update_time\x18\x33 \x01(\x03\x12\x11\n\tevent_day\x18\x35 \x01(\t\x12\x12\n\nandroid_id\x18\x36 \x01(\t\x12\r\n\x05\x63mode\x18\x37 \x01(\x05\x12\x14\n\x0cstart_scheme\x18\x38 \x01(\t\x12\x12\n\nstart_type\x18\x39 \x01(\x05\x12\x0c\n\x04idfv\x18< \x01(\t\x12\r\n\x05\x65xtra\x18= \x01(\t\x12\x12\n\nuser_agent\x18> \x01(\t\x12\x1f\n\x17personalized_rec_switch\x18? \x01(\x05\x12\x14\n\x0c\x64\x65vice_score\x18\x46 \x01(\tb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CommonReq_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_COMMONREQ']._serialized_start = 20
    _globals['_COMMONREQ']._serialized_end = 858
