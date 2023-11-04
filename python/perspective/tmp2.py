import pyarrow as pa
import pyarrow.json
from io import BytesIO

b = BytesIO()
b.write("{}".encode())
b.seek(0)

table = pyarrow.json.read_json(b)
stream = pa.BufferOutputStream()
writer = pa.RecordBatchStreamWriter(stream, table.schema, use_legacy_format=False)
writer.write_table(table)
writer.close()
stream.getvalue().to_pybytes()
