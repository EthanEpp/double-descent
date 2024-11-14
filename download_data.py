import torchvision.datasets as datasets

# This will download and place MNIST in the specified directory.
datasets.MNIST(root='data/mnist', train=True, download=True)
datasets.MNIST(root='data/mnist', train=False, download=True)
