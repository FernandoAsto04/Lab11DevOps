import json
from core import payload
from workers import Response

#Comentario para el commit
def on_fetch(request):
    return Response(json.dumps(payload()),
                    headers={"content-type": "application/json"})
