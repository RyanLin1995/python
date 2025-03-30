"""
进行模型的训练
"""

from model import ImdbModel
from dataset import get_dataloader
from torch.optim import Adam
from tqdm import tqdm
import torch
import torch.nn.functional as F

model = ImdbModel()
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'Using device: {device}')
model = model.to(device)
optimizer = Adam(model.parameters())


def train(epoch):
    train_dataloader = get_dataloader(is_train=True)
    bar = tqdm(train_dataloader, total=len(train_dataloader))
    for idx, (input_data, target) in enumerate(bar):
        optimizer.zero_grad()
        # 确保 input_data 是数值类型的张量
        if isinstance(input_data[0], str):
            input_data = [int(i) for i in input_data]
        input_data = torch.LongTensor(input_data).to(device)
        target = target.to(device)
        output = model(input_data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        bar.set_description(
            "epcoh:{}  idx:{}   loss:{:.6f}".format(epoch, idx, loss.item())
        )


if __name__ == "__main__":
    for i in range(21):
        train(i)
    torch.save(model.state_dict(), 'models/model.pth')
