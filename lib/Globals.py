from lib.ColoredObject import Color

port = 10101
ColorObj = Color()
headers = lambda x: {
    'X-Forwarded': x,
    'X-Forwarded-By': x,
    'X-Forwarded-For': x,
    'X-Forwarded-For-Original': x,
    'X-Forwarded-Host': x,
    'X-Forwarded-Server': x,
    'X-Forwarder-For': x,
    'X-Forward-For': x,
    'X-Real-Ip': x,
    'X-Host': x,
    'X-Original-Url': x,
    'X-Proxy-Url': x,
    'X-Rewrite-Url': x,
    'X-Real-Ip': x,
    'X-Remote-Addr': x,
    'Referer': x,
}
