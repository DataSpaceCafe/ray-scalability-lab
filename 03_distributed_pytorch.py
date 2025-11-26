# 03_distributed_pytorch.py - Simplified version for Windows
import ray
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

ray.init(ignore_reinit_error=True)

# Sample data
X = torch.randn(20000, 50)
y = torch.randint(0, 2, (20000,))
dataset = TensorDataset(X, y)

@ray.remote
def train_model(X_subset, y_subset, worker_id):
    """Train model on a subset of data"""
    model = nn.Sequential(
        nn.Linear(50, 100), 
        nn.ReLU(), 
        nn.Linear(100, 1), 
        nn.Sigmoid()
    )
    optimizer = optim.Adam(model.parameters(), lr=0.003)
    criterion = nn.BCELoss()
    
    subset_dataset = TensorDataset(X_subset, y_subset)
    loader = DataLoader(subset_dataset, batch_size=256, shuffle=True)
    
    print(f"Worker {worker_id} starting training on {len(X_subset)} samples...")
    
    for epoch in range(8):
        epoch_loss = 0
        for batch_x, batch_y in loader:
            batch_y = batch_y.float().unsqueeze(1)
            pred = model(batch_x)
            loss = criterion(pred, batch_y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            epoch_loss = loss.item()
        
        if epoch % 2 == 0:
            print(f"Worker {worker_id}, Epoch {epoch}, Loss: {epoch_loss:.4f}")
    
    return epoch_loss, model.state_dict()

# Split data into 4 parts for parallel training
num_workers = 4
chunk_size = len(X) // num_workers

print(f"=== Parallel Training with {num_workers} Ray workers ===")
tasks = []
for i in range(num_workers):
    start_idx = i * chunk_size
    end_idx = start_idx + chunk_size if i < num_workers - 1 else len(X)
    
    X_subset = X[start_idx:end_idx]
    y_subset = y[start_idx:end_idx]
    
    tasks.append(train_model.remote(X_subset, y_subset, i))

# Get results from all workers
results = ray.get(tasks)

print("\n=== Training Complete ===")
for i, (loss, _) in enumerate(results):
    print(f"Worker {i} final loss: {loss:.4f}")

avg_loss = sum(loss for loss, _ in results) / len(results)
print(f"\nAverage final loss across all workers: {avg_loss:.4f}")