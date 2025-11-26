import ray
import time
from tqdm import tqdm

ray.init(ignore_reinit_error=True)

@ray.remote
def heavy_task(x):
    time.sleep(0.1)
    return x ** 2

def slow_task(x):
    time.sleep(0.1)
    return x ** 2

print("=== basic for-loop ===")
start = time.time()
results1 = [slow_task(i) for i in tqdm(range(500))]
print(f"basic for-loop Time Process: {time.time() - start:.2f} seconds.")

print("\n=== Ray parallel ===")
start = time.time()
tasks = [heavy_task.remote(i) for i in tqdm(range(500))]
results2 = ray.get(tasks)
print(f"Ray parallel Time Process : {time.time() - start:.2f} seconds.")