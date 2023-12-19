import json
from websocket import create_connection


message_0 = {
    "delta": True,
    "handle": -1,
    "method": "OpenDoc",
    "params": ["74a8ae0b-233d-44e6-b341-1f718d19802f", "", "", "", False],
    "id": 1,
    "jsonrpc": "2.0",
}

message_1 = {
    "delta": True,
    "handle": 1,
    "method": "GetObject",
    "params": ["McTcJt"],
    "id": 2,
    "jsonrpc": "2.0",
}

message_2 = {
    "delta": True,
    "handle": 2,
    "method": "GetLayout",
    "params": [],
    "id": 3,
    "jsonrpc": "2.0",
}

message_3 = {
    "delta": True,
    "handle": 3,
    "method": "GetHyperCubeData",
    "params": [
        "/qHyperCubeDef",
        [
            {"qTop": 0, "qLeft": 0, "qHeight": 24, "qWidth": 1},
            {"qTop": 0, "qLeft": 1, "qHeight": 24, "qWidth": 1},
            {"qTop": 0, "qLeft": 2, "qHeight": 24, "qWidth": 1},
            {"qTop": 0, "qLeft": 3, "qHeight": 24, "qWidth": 1},
            {"qTop": 0, "qLeft": 4, "qHeight": 24, "qWidth": 1},
            {"qTop": 0, "qLeft": 5, "qHeight": 24, "qWidth": 1},
            {"qTop": 0, "qLeft": 6, "qHeight": 24, "qWidth": 1},
            {"qTop": 0, "qLeft": 7, "qHeight": 24, "qWidth": 1},
            {"qTop": 0, "qLeft": 8, "qHeight": 24, "qWidth": 1},
            {"qTop": 0, "qLeft": 9, "qHeight": 24, "qWidth": 1},
        ],
    ],
    "id": 4,
    "jsonrpc": "2.0",
}




url = "wss://paineistransparencia.tce.sc.gov.br/app/74a8ae0b-233d-44e6-b341-1f718d19802f?reloadUri=https%3A%2F%2Fpaineistransparencia.tce.sc.gov.br%2Fextensions%2FappDespesasMunicipaisExternoNovo%2Findex.html"
ws = create_connection(url)

ws.send(json.dumps(message_0))
ws.recv()
ws.recv()
ws.recv()

ws.send(json.dumps(message_1))
ws.recv()

ws.send(json.dumps(message_2))
ws.recv()

ws.send(json.dumps(message_3))
