import io
import matplotlib.pyplot as plt
from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles
import numpy as np

from torchvision import datasets, transforms

# Define data transformation
transform = transforms.Compose([
    transforms.ToTensor(),  # Convert PIL image or numpy.ndarray to tensor
    transforms.Normalize((0.5,), (0.5,))  # Normalize tensor with mean and std
])


app = FastAPI()

# Download and load the MNIST training dataset
train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True).data

@app.get("/prediction")
async def root():
    return np.loadtxt("kmeans",).tolist()

@app.get("/tsne")
async def root():
    return np.loadtxt("tsne",).tolist()

@app.get("/original")
async def root():
    return np.loadtxt("original",).tolist()

@app.get("/image/{item_idx}")
async def image(item_idx: int):
    # Save the plot as an image in memory
    img_bytes = io.BytesIO()
    plt.imshow(train_dataset.data[item_idx])
    plt.savefig(img_bytes, format='png')
    plt.close()

    # Set the content type header to image/png
    response = Response(content=img_bytes.getvalue(), media_type="image/png")
    return response

app.mount("/", StaticFiles(directory="static"), name="static")
