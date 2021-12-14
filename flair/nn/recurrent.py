from torch import nn


rnn_layers = {"lstm": nn.LSTM, "gru": nn.GRU}


def create_recurrent_layer(layer_type, initial_size, hidden_size, nlayers, dropout=0, **kwargs):
    layer_type = layer_type.lower()
    assert layer_type in rnn_layers.keys()
    module = rnn_layers[layer_type]

    if nlayers == 1:
        dropout = 0

    return module(initial_size, hidden_size, nlayers, dropout=dropout, **kwargs)
