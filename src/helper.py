import numpy as np
import matplotlib.pyplot as plt

def index_as_id(data_frame, suffix):
    '''讓index做為id，並獨立存在同一欄內'''

    data_frame[suffix + '_id'] = data_frame.index
    
    columns = data_frame.columns.tolist()
    columns = columns[-1:] + columns[:-1]
    data_frame = data_frame[columns]
    
    return data_frame

def draw_reporter_scores(scale, data, reporters, reporter_scores, reporter_weighted_scores):
    '''視覺化報導者可信度'''

    plt.subplot(1, 1, 1)
    plt.xticks(np.arange(0, len(reporters), 1.0))

    # 評分簡單平均計算
    plt.plot(reporter_scores, label = 'simple avg')
    
    # 評分*評分者可信度的加權平均計算
    plt.plot(reporter_weighted_scores, label = 'weighted avg')
    
    # 報導者可信度
    plt.plot(reporters['reporter_score'], 'k--', label = 'origin', c = '0.55')

    plt.ylim(scale.min, scale.max)
    plt.xlabel("Reporters")
    plt.ylabel("Scores")
    plt.title("Believability of Reporters")
    plt.legend(loc = 'upper right')
    plt.show()

def draw_user_weights(scale, weights):
    '''視覺化讀者可信度'''

    weights = list(weights)

    origin = list([scale.mean]) * len(weights)
    
    # 計算後的讀者權重
    plt.plot(weights)

    # 原始權重
    plt.plot(origin, 'k--', label = 'real', c = '0.55')

    plt.xticks(np.arange(0, len(weights), 1.0))
    plt.ylim(scale.min, scale.max)
    plt.ylabel("Weights")
    plt.xlabel("Readers")
    plt.title("Weights of Readers")
    plt.show()
