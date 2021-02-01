import gwcomm as comm

lg = comm.logger(__name__)
comm.add_env(["API_HTTP", "API_HOST", "API_PORT",
              "API_DATA", "API_USR", "API_PWD"])


def get_token():
    import requests
    conf = comm.sysconf
    url = conf.get("api", {}).get("auth", "") if conf.get("api", {}).get(
        "auth", "") == "" else "{}://{}.{}/auth".format(conf.get("API_HTTP", ""), conf.get("API_HOST", ""), conf.get("API_PORT", ""))
    body = {"usr_cde": conf.get("API_USR", ""),
            "password": conf.get("API_USR", "")}
    lg.info(f"init - url: {url}")
    res = requests.post(url, json=body)
    if res.status_code != 200:
        lg.error(f"Error - {res.msg}")
        comm.sysconf["token"] = None
        return None
    token = res.json().get("access_token")
    comm.sysconf["token"] = token
    return token


def get_header(token=None):
    token = get_token() if token == None else token
    if token == None:
        lg.error("Error - no token")
        return {}
    return {"Authorization": f"Bearer {token}"}
