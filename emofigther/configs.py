# 配置
#
# -*- coding:utf-8 -*-
#__author__ = 'akers'
import os,re

APP_CTX={
    "app_root": os.getcwd(),
    "resources": "resources"
}

def get_resource(path):
    if path.startswith("/") or path.startswith('\\'):
        path = path[1:]
    res_path = APP_CTX["resources"]
    res_path = res_path if res_path.startswith('/') or re.match(r'^[a-zA-Z]:[\\,/]{1,2}[^\\,/]*?$', res_path) else os.path.sep.join([os.getcwd(), res_path])
    sep = os.path.sep if not res_path.endswith(os.path.sep) else ""
    return sep.join([res_path, path])

CONFIGS={
    "emo":{
        "backgrounds":[
            {
                "name":"default",
                "path":get_resource("/background/pander/default.png"),
                "command":"default"
            },
            {
                "name":"cry",
                "path":get_resource("/background/pander/cry.png"),
                "command":"cry"
            },
            {
                "name":"doubt",
                "path":get_resource("/background/pander/doubt.png"),
                "command":"doubt"
            },
            {
                "name":"point",
                "path":get_resource("/background/pander/point.jpg"),
                "command":"point"
            }
        ],
        "faces":[
            {
                "name":"smail",
                "path":get_resource("/face/jgz/smail.png"),
                "command":"smail"
            },
            {
                "name": "awkward",
                "path": get_resource("/face/jgz/awkward.png"),
                "command": "awkward"
            },
            {
                "name":"diss",
                "path":get_resource("/face/jgz/diss.png"),
                "command":"diss"
            },
            {
                "name":"laugth",
                "path":get_resource("/face/jgz/laugth.png"),
                "command":"laugth"
            },
        ]
    }
}

if __name__ == "__main__":
    APP_CTX["resources"] = "C:\\\\"
    test_path = get_resource("resources/photo")
    print(test_path)