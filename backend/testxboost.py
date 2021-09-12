import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda, Compose
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import os
import io


training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
)

# Download test data from open datasets.
test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor(),
)


class testDataset(Dataset):
    """Face Landmarks dataset."""

    def __init__(self, csv_file, transform=None):
        """
        Args:
            csv_file (string): Path to the csv file with annotations.
            root_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        self.data = pd.read_csv(csv_file)
        print('dataaaaa=',self.data.iloc[0])
        self.X = self.data.iloc[:,:8].values
        self.y = self.data.iloc[:,-1].values
        self.transform = transform

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

       
        X = np.array([self.X])
        X = X.astype('float').reshape(-1, 8)
        y = np.array([self.y])
        y = y.astype('float').reshape(-1, 1)
        sample = {'data': X, 'label': y}

        if self.transform:
            sample = self.transform(sample)

        return sample




batch_size = 64

training_data=testDataset('archive2/train.csv')
#test_dataloader=testDataset('archive2/test.csv')
# Create data loaders.
train_dataloader = DataLoader(training_data, batch_size=batch_size)
#test_dataloader = DataLoader(test_data, batch_size=batch_size)

# for X, y in test_dataloader:
#     print("Shape of X [N, C, H, W]: ", X.shape)
#     print("Shape of y: ", y.shape, y.dtype)
#     break

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using {} device".format(device))

# Define model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(8, 50),
            nn.ReLU(),
            nn.Linear(50, 1),
            nn.ReLU(),
        )

    def forward(self, x):
        print(x.size())
        print(type(x))
        logits = self.linear_relu_stack(x)
        return logits

model = NeuralNetwork().to(device)
print(model)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

model=model.float()
def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    model.train()
    for (batch_idx, batch) in enumerate(dataloader):
        print("\nBatch = " + str(batch_idx))
        X = batch['data']  
        y = batch['label']   

        # Compute prediction error
        
        pred = model(X.float())
        loss = loss_fn(pred, y)

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch_idx % 8 == 0:
            loss, current = loss.item(), batch_idx * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")


def test(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for (batch_idx, batch) in enumerate(dataloader):
            print("\nBatch = " + str(batch_idx))
            X = batch['data']  
            y = batch['label']  
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")


epochs = 5
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train(train_dataloader, model, loss_fn, optimizer)
    #test(test_dataloader, model, loss_fn)
print("Done!")

torch.save(model.state_dict(), "model.pth")
print("Saved PyTorch Model State to model.pth")



model = NeuralNetwork()
model.load_state_dict(torch.load("model.pth"))


classes = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]

model.eval()
x, y = test_data[0][0], test_data[0][1]
with torch.no_grad():
    pred = model(x)
    predicted, actual = classes[pred[0].argmax(0)], classes[y]
    print(f'Predicted: "{predicted}", Actual: "{actual}"')















    
device = torch.device("cpu")
class Dataset(torch.utils.data.Dataset):

  def __init__(self, src_file, num_rows=None):
    train_data = pd.read_csv(src_file)

    x_tmp = train_data.iloc[:,:7].values
    y_tmp = train_data.iloc[:,-1].values
    sc = MinMaxScaler()
    sct = MinMaxScaler()
    x_tmp=sc.fit_transform(x_tmp.reshape(-1,7))
    y_tmp =sct.fit_transform(y_tmp.reshape(-1,1))

    self.x_data = torch.tensor(x_tmp,
      dtype=torch.float32).to(device)
    self.y_data = torch.tensor(y_tmp,
      dtype=torch.float32).to(device)

  def __len__(self):
    return len(self.x_data)  # required

  def __getitem__(self, idx):
    if torch.is_tensor(idx):
      idx = idx.tolist()
    preds = self.x_data[idx, 0:7]
    pol = self.y_data[idx]
    sample = \
      { 'predictors' : preds, 'political' : pol }
    return sample




from torch.utils.data import DataLoader
learning_rate = 1e-3
batch_size = 64
epochs = 5
train_dataset=Dataset('archive2/train.csv',9)
test_dataset=Dataset('archive2/test.csv',9)
train_dataloader = DataLoader(train_dataset, batch_size=64)
test_dataloader = DataLoader(test_dataset, batch_size=64)
def train_loop(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    for (batch_idx, batch) in enumerate(dataloader):
        print("\nBatch = " + str(batch_idx))
        X = batch['predictors']  # [3,7]
        # Y = T.flatten(batch['political'])  # 
        y = batch['political']   # [3]

    # Compute prediction and loss
        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        listEcart.append(loss.item())
        if batch_idx % 8 == 0:
            loss, current = loss.item(), batch_idx * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

def test(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for (batch_idx, batch) in enumerate(dataloader):
            print("\nBatch = " + str(batch_idx))
            X = batch['predictors']  # [3,7]
            # Y = T.flatten(batch['political'])  # 
            y = batch['political']   # [3]
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")



#train_loop(train_dataloader, model, l, optimizer)
epochs = 5
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train_loop(train_dataloader, model, loss_fn, optimizer)
    test(test_dataloader, model, loss_fn)
print("Done!")