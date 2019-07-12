'''讓index做為id，並獨立存在同一欄內'''
def index_as_id(data_frame, suffix):

    data_frame[suffix + '_id'] = data_frame.index
    
    columns = data_frame.columns.tolist()
    columns = columns[-1:] + columns[:-1]
    data_frame = data_frame[columns]
    
    return data_frame