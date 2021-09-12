import torch
import torch.nn as nn 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import torch.nn.functional as F
from torch.utils.data import Dataset

class RegressionModel(torch.nn.Module):

    def __init__(self):
        super(RegressionModel, self).__init__()
        self.hid1 = torch.nn.Linear(8, 10)  # 8-(10-10)-1
        self.hid2 = torch.nn.Linear(10, 10)
        self.oupt = torch.nn.Linear(10, 1)

        torch.nn.init.xavier_uniform_(self.hid1.weight)
        torch.nn.init.zeros_(self.hid1.bias)
        torch.nn.init.xavier_uniform_(self.hid2.weight)
        torch.nn.init.zeros_(self.hid2.bias)
        torch.nn.init.xavier_uniform_(self.oupt.weight)
        torch.nn.init.zeros_(self.oupt.bias)

    def forward(self, x):
        z = torch.relu(self.hid1(x))
        z = torch.relu(self.hid2(z))
        z = self.oupt(z)  # no activation
        return z

    # def __init__(self,  input_dim, output_dim):
    #     super(RegressionModel, self).__init__()
    #    # self.linear = torch.nn.Linear(6, 1)  # One in and one out
    #     # First fully connected layer
    #     self.fc1 = nn.Linear(input_dim, 512)
    #     # Second fully connected layer that outputs our 10 labels
    #     self.fc2 = nn.Linear(512, 100)

    #     self.fc3 = nn.Linear(100, output_dim)

    # def forward(self, x):
    #     x = self.fc1(x)
    #     x = F.relu(x)
    #     x = self.fc2(x)
    #     x = F.relu(x)
    #     x = self.fc3(x)
    #     output = F.log_softmax(x, dim=1)
    #     return output

def train_loop(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        # Compute prediction and loss
        pred = model(X.float())
        loss = loss_fn(pred, y.float())
        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if batch % 100 == 0:
            loss, current = loss.item(), batch * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")
    

def test_loop(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    test_loss, correct = 0, 0

    with torch.no_grad():
        for X, y in dataloader:
            pred = model(X.float())
            test_loss += loss_fn(pred, y.float()).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()

    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")

train_data = pd.read_csv('archive2/train.csv')
test_data = pd.read_csv('archive2/test.csv')


input_dim = 8
output_dim = 1


import torch.utils.data as data_utils
labelRow=6
csvFile='archive2/train.csv'
df = pd.read_csv(csvFile)
target = torch.tensor(df['TARGET(PRICE_IN_LACS)'].values)
features = torch.tensor(df.drop('TARGET(PRICE_IN_LACS)', axis=1).values)





learning_rate = 1e-3
batch_size = 10
epochs = 5
print(features)

train = data_utils.TensorDataset(features, target)
train_loader = data_utils.DataLoader(train, batch_size=batch_size, shuffle=True)


model=RegressionModel(input_dim,output_dim)
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)



epochs = 10
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train_loop(train_loader, model, loss_fn, optimizer)
    test_loop(train_loader, model, loss_fn)
print("Done!")
# my_nn = RegressionModel(input_size,output_size)
# result = my_nn(random_data)
# print (result)





