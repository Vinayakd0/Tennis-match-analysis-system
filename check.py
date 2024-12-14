import torch

# Check if PyTorch is installed and CUDA is available
print("PyTorch version:", torch.__version__)
print("Is CUDA available:", torch.cuda.is_available())

# If CUDA is available, print the GPU name
if torch.cuda.is_available():
    print("GPU Name:", torch.cuda.get_device_name(0))
