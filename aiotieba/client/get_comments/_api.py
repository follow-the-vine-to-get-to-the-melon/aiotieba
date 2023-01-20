import aiohttp
import yarl

from .._core import APP_BASE_HOST, TbCore
from .._exception import TiebaServerError
from .._helper import APP_NON_SECURE_SCHEME, pack_proto_request, send_request
from ._classdef import Comments
from .protobuf import PbFloorReqIdl_pb2, PbFloorResIdl_pb2


def pack_proto(core: TbCore, tid: int, pid: int, pn: int, is_floor: bool) -> bytes:
    req_proto = PbFloorReqIdl_pb2.PbFloorReqIdl()
    req_proto.data.common._client_type = 2
    req_proto.data.common._client_version = core.main_version
    req_proto.data.tid = tid
    if is_floor:
        req_proto.data.spid = pid
    else:
        req_proto.data.pid = pid
    req_proto.data.pn = pn

    return req_proto.SerializeToString()


async def request_http(connector: aiohttp.TCPConnector, core: TbCore, proto: bytes) -> bytes:

    request = pack_proto_request(
        core,
        yarl.URL.build(
            scheme=APP_NON_SECURE_SCHEME, host=APP_BASE_HOST, path="/c/f/pb/floor", query_string="cmd=302002"
        ),
        proto,
    )

    body = await send_request(request, connector, read_bufsize=8 * 1024)

    return body


def parse_body(body: bytes) -> Comments:
    res_proto = PbFloorResIdl_pb2.PbFloorResIdl()
    res_proto.ParseFromString(body)

    if code := res_proto.error.errorno:
        raise TiebaServerError(code, res_proto.error.errmsg)

    data_proto = res_proto.data
    comments = Comments()._init(data_proto)

    return comments
