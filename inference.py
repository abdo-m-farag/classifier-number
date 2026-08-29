import torch 
from torch import nn
from PIL import Image
from torchvision import transforms 

from model import classficationModel

device = "cuda" if torch.cuda.is_available() else "cpu"

model = classficationModel().to(device)

model.load_state_dict(torch.load( "classification_model.pth",map_location=device))

transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((28,28)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])
])

def predict(image):
    image=transform(image)
    image=image.unsqueeze(0).to(device)
    with torch.inference_mode():
        output=model(image)
        predict=output.argmax(dim=1).item()

    return predict
