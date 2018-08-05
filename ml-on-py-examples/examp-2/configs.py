# 配置
#
# -*- coding:utf-8 -*-
#__author__ = 'akers'
import os

APP_CTX={
    "app_root": os.getcwd(),
    "resources": os.path.sep.join([os.getcwd(), "/resources"])
}
CONFIGS={
    "emo":{
        "backgrounds":[
            {
                "name":"cry",
                "path":"".join([APP_CTX["resources"], "/background/pander/cry.png"]),
                "command":"cry"
            },
            {
                "name":"default",
                "path":"".join([APP_CTX["resources"], "/background/pander/default.png"]),
                "command":"default"
            },
            {
                "name":"doubt",
                "path":"".join([APP_CTX["resources"], "/background/pander/doubt.png"]),
                "command":"doubt"
            },
            {
                "name":"point",
                "path":"".join([APP_CTX["resources"], "/background/pander/point.png"]),
                "command":"point"
            }
        ],
        "faces":[
            {
                "name": "awkward",
                "path": "".join([APP_CTX["resources"], "/face/jgz/awkward.png"]),
                "command": "awkward"
            },
            {
                "name":"diss",
                "path":"".join([APP_CTX["resources"], "/face/jgz/diss.png"]),
                "command":"diss"
            },
            {
                "name":"laugth",
                "path":"".join([APP_CTX["resources"], "/face/jgz/laugth.png"]),
                "command":"laugth"
            },
            {
                "name":"smail",
                "path":"".join([APP_CTX["resources"], "/face/jgz/smail.png"]),
                "command":"smail"
            }
        ]
    }
}