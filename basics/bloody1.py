import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




if __name__ == '__main__':
    fname = 'd01_frame_I300'
    #fname = 'd01_comparison_I350'
    record = np.load(f'{fname}.npz')
    
    data = record['data']
    X = np.reshape(data, (-1, data.shape[-1]))
    
    print(X)
    print(X.shape)    
