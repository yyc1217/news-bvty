import numpy as np
import pandas as pd

class ReaderWeightHolder:
    '''讀者權重管理'''
    
    # 目前的權重
    weights = {}
    
    # 過去的權重
    past_weights = {}

    # 保留多久以前的權重
    reader_pass_weight_window = 10

    def __init__(self, readers, init_mean, reader_pass_weight_window = 10):
        self.readers = readers
        self.reader_pass_weight_window = reader_pass_weight_window
        self.init_mean = init_mean

        self.reset()

    def reset(self):
        self.past_weights = {
            reader_id: np.repeat(self.init_mean, self.reader_pass_weight_window).tolist() for reader_id in self.readers['reader_id']
            }

        self.weights = {
            reader_id: self.init_mean for reader_id in self.readers['reader_id']
            }

    def get(self, reader_id):
        '''取得讀者權重'''
        return self.weights[reader_id]

    def inserts(self, new_weights):
        '''採先進先出更新讀者權重'''

        for reader_id, new_weight in new_weights.items():  
            self.past_weights[reader_id].pop(0)
            self.past_weights[reader_id].append(new_weight)
            # TODO 簡單平均數、加權平均數、做對事情，權重越高
            self.weights[reader_id] = sum(self.past_weights[reader_id]) / self.reader_pass_weight_window

    def print_weights(self, n = 5):
        return pd.DataFrame.from_dict(self.weights, orient = 'index', columns = ['weight']).rename_axis('user_id').head(n)
    
    def print_past_weights(self, n = 5):
        return pd.DataFrame.from_dict(self.past_weights, orient = 'index').rename_axis('user_id').head(n)

    def print_all(self):
        print(self.weights)
        print(self.past_weights)