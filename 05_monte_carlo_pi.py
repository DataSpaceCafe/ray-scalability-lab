# 05_monte_carlo_pi.py
import ray
import random

ray.init(ignore_reinit_error=True)

@ray.remote
def count_in_circle(n):
    inside = 0
    for _ in range(n):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x*x + y*y <= 1:
            inside += 1
    return inside

tasks = [count_in_circle.remote(2_000_000) for _ in range(20)]  # รวม 40 ล้านจุด
total_inside = sum(ray.get(tasks))
pi = 4 * total_inside / (20 * 2_000_000)
print(f"π ≈ {pi:.10f}")