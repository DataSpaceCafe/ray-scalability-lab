# 04_ray_serve_api.py
from ray import serve
from starlette.responses import JSONResponse
import ray

ray.init(ignore_reinit_error=True)
serve.start()

@serve.deployment(num_replicas=4, route_prefix="/")
class QuickAPI:
    def __init__(self):
        self.model = lambda x: x ** 2 + 123 

    async def __call__(self, request):
        data = await request.json()
        result = self.model(data["x"])
        return JSONResponse({"result": result})

QuickAPI.deploy()

print("API พร้อมแล้ว! ลองเรียก:")
print('curl -X POST http://127.0.0.1:8000/ -H "Content-Type: application/json" -d "{\"x\": 10}"')
input("กด Enter เพื่อปิด...")  