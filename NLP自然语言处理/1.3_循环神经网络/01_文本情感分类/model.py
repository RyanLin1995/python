"""构建模型"""

import torch.nn as nn
import config
import torch.nn.functional as F


class ImdbModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.embedding = nn.Embedding(
            num_embeddings=len(config.ws), embedding_dim=100, padding_idx=config.ws.PAD
        )
        self.fc = nn.Linear(config.max_len * 200, 2)

    def forward(self, input_data):
        """
        :param input_data:[batch_size,max_len]
        :return:
        """
        input_embedding = self.embedding(
            input_data
        )  # input embedding :[batch_size,max_len,200]

        # 变形
        input_embedding_viewed = input_embedding.view(input_embedding.size(0), -1)

        # 全连接
        out = self.fc(input_embedding_viewed)
        return F.log_softmax(out, dim=-1)

    def __len__(self):
        return len(self.embedding)
