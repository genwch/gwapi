import gwcomm as comm

lg = comm.logger(__name__)
comm.add_env(["API_HTTP", "API_HOST", "API_PORT",
              "API_DATA", "API_USR", "API_PWD"])


def get(url):
    import requests
    from .auth import get_header
    conf = comm.sysconf
    dataurl = conf.get("api", {}).get("data", "") if conf.get("api", {}).get(
        "data", "") == "" else "{}://{}.{}{}".format(conf.get("API_HTTP", ""), conf.get("API_HOST", ""), conf.get("API_PORT", ""), conf.get("API_DATA", ""))
    url = "{}{}".format(dataurl, url)
    header = get_header(conf.get("token", None))
    lg.info(f"init - url: {url}")
    res = requests.get(url, headers=header)
    if res.status_code != 200:
        lg.error(f"Error - {res.json()}")
        comm.sysconf["token"] = None
        return {}
    return res.json()


def upsert(url, data):
    import requests
    from .auth import get_header
    conf = comm.sysconf
    dataurl = conf.get("api", {}).get("data", "") if conf.get("api", {}).get(
        "data", "") == "" else "{}://{}.{}{}".format(conf.get("API_HTTP", ""), conf.get("API_HOST", ""), conf.get("API_PORT", ""), conf.get("API_DATA", ""))
    url = "{}{}".format(dataurl, url)
    header = get_header(conf.get("token", None))
    lg.info(f"init - url: {url}")
    res = requests.post(url, json=data, headers=header)
    if res.status_code != 200:
        lg.error(f"Error - {res.json()}")
        comm.sysconf["token"] = None
        return False
    return True
