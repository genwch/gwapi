# api functions

This api functions written by python

## Configuration
- Setup as **OS environment variable** with **PY_** prefix
    - Replace **[]** with your value
~~~
PY_API_HTTP=[https|http]
PY_API_HOST=[apihost]
PY_API_PORT=[443:80]
PY_API_DATA=[/api/v1/data]
PY_API_USR=[apiuser]
PY_API_PWD=[apipwd]
~~~
- Setup as ./conf/sysconf.json
    - Replace **[]** with your value
~~~
{
    "API_HTTP": "[https|http]",
    "API_HOST": "[apihost]",
    "API_PORT": "[443:80]",
    "API_DATA": "[/api/v1/data]",
    "API_USR": "[apiuser]",
    "API_PWD": "[apipwd]"
}
~~~

## Dependancies
Read more [requirements.txt](./requirements.txt)