"""
Topic: PyTorch Deep Learning & LSTM Forecasting
"""
import torch
import torch.nn as nn
import numpy as np

class LSTMPredictor(nn.Module):
    """LSTM for sequence prediction (time series)."""
    def __init__(self, input_size, hidden_size=64, num_layers=2, dropout=0.2):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers,
                             batch_first=True, dropout=dropout)
        self.fc = nn.Sequential(
            nn.Linear(hidden_size, 32),
            nn.ReLU(),
            nn.Linear(32, 1)
        )
    
    def forward(self, x):
        # x shape: (batch, seq_len, features)
        lstm_out, _ = self.lstm(x)
        last_hidden = lstm_out[:, -1, :]    # Take last time step
        return self.fc(last_hidden)

def test_model():
    model = LSTMPredictor(input_size=5)
    dummy_input = torch.randn(32, 20, 5) # Batch=32, SeqLen=20, Features=5
    output = model(dummy_input)
    print(f"Output shape: {output.shape}")

if __name__ == "__main__":
    test_model()





































































































































































