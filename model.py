import torch 
from torch import nn

class classficationModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.flat=nn.Flatten()
        self.layers=nn.Sequential(
            nn.Linear(28*28,164),nn.ReLU(),
            nn.Linear(164,164),nn.ReLU(),
            nn.Linear(164,128),nn.ReLU(),
            nn.Linear(128,128),nn.ReLU(),
            nn.Linear(128,64),nn.ReLU(),
            nn.Linear(64,10)
        )
    def forward(self,x:torch.Tensor)->torch.Tensor:
        x=self.flat(x)
        return self.layers(x)