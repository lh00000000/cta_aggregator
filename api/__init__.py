from json import JSONEncoder
from uuid import UUID

# fix uuid jsonization
JSONEncoder_builtin_default = JSONEncoder.default
def JSONEncoder_extended_default(self, o):
    if isinstance(o, UUID): return str(o)
    return JSONEncoder_builtin_default(self, o)

JSONEncoder.default = JSONEncoder_extended_default
