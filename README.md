# Ray Tutorial - Parallel Processing

🚀 Learn how to speed up your Python code using Ray Framework

## Overview

This repository demonstrates the power of parallel processing with Ray, showing how to transform slow sequential code into fast concurrent execution.

## 📁 Files

- `01_parallel_processing.py` - Basic parallel processing comparison

## 🎯 What You'll Learn

- How to use Ray for parallel processing
- Comparing sequential vs parallel execution
- Managing CPU cores and concurrent tasks
- Real-world performance improvements

## 📊 Performance Comparison

| Method | Time | Speed Up |
|--------|------|----------|
| Basic for-loop | ~50 seconds | 1x |
| Ray Parallel (4 cores) | ~13 seconds | **3.8x faster** |

## 🚀 Quick Start

### Installation

```bash
pip install ray tqdm
```

### Run Example

```bash
python 01_parallel_processing.py
```

## 💡 Key Concepts

### 1. Initialize Ray
```python
import ray
ray.init(num_cpus=4)  # Use 4 CPU cores
```

### 2. Create Remote Function
```python
@ray.remote(num_cpus=1)  # Each task uses 1 CPU
def heavy_task(x):
    return x ** 2
```

### 3. Execute in Parallel
```python
# Submit tasks (non-blocking)
tasks = [heavy_task.remote(i) for i in range(500)]

# Get results (blocking)
results = ray.get(tasks)
```

## 🔑 How It Works

1. **Sequential Processing**: Tasks run one by one
   - 500 tasks × 0.1 seconds = 50 seconds

2. **Parallel Processing**: Multiple tasks run simultaneously
   - 500 tasks ÷ 4 cores × 0.1 seconds = 12.5 seconds
   - Limited by available CPU cores

## 📝 Code Example

```python
import ray
import time
from tqdm import tqdm

# Set the number of CPU cores to use
ray.init(num_cpus=4, ignore_reinit_error=True)

# Each task uses 1 CPU (limits concurrent tasks to 4)
@ray.remote(num_cpus=1)
def heavy_task(x):
    time.sleep(0.1)
    return x ** 2

print("=== Ray parallel ===")
start = time.time()
tasks = [heavy_task.remote(i) for i in tqdm(range(500))]
results = ray.get(tasks)
print(f"Time: {time.time() - start:.2f} seconds")
```

## 🎓 Use Cases

- **Data Processing**: Process large datasets in parallel
- **Machine Learning**: Parallel hyperparameter tuning
- **API Calls**: Concurrent API requests
- **Image Processing**: Batch image transformations
- **Monte Carlo Simulations**: Run multiple simulations simultaneously

## ⚙️ Configuration

### Adjust Number of Workers
```python
ray.init(num_cpus=8)  # Use 8 cores instead of 4
```

### Control Resource Usage per Task
```python
@ray.remote(num_cpus=2)  # Each task uses 2 CPUs
def cpu_intensive_task(x):
    return x ** 2
```

## 📈 Best Practices

1. **Match cores to workload**: Don't use more cores than your CPU has
2. **Balance task granularity**: Tasks should be neither too small nor too large
3. **Monitor resource usage**: Use Ray dashboard for insights
4. **Handle errors**: Implement proper error handling for remote functions
5. **Cleanup**: Call `ray.shutdown()` when done

## 🐛 Common Issues

### Issue: Ray already initialized
**Solution**: Use `ignore_reinit_error=True`
```python
ray.init(ignore_reinit_error=True)
```

### Issue: Tasks not running in parallel
**Solution**: Check CPU allocation
```python
# Make sure total CPUs in init >= CPUs per task × concurrent tasks
ray.init(num_cpus=4)
@ray.remote(num_cpus=1)  # 4 tasks can run concurrently
```

## 📚 Resources

- [Ray Documentation](https://docs.ray.io/)
- [Ray GitHub](https://github.com/ray-project/ray)
- [Ray Tutorial](https://docs.ray.io/en/latest/ray-core/walkthrough.html)

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

MIT License

---

Made with ❤️ using Ray Framework
