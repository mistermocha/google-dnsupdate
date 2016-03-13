python_binary(
  name='dnsupdate',
  source='dnsupdate.py',
  dependencies=[':requests'],
)

python_requirement_library(
  name='requests',
  requirements=[
    python_requirement('requests>=2.9.1'),
    python_requirement('configparser'),
  ]
)
