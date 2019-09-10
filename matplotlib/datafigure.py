import pandas as pd
import matplotlib.pyplot as plt

def data_plot():
    df = pd.read_json('/home/shiyanlou/Code/user_study.json')
    data = df.groupby('user_id').sum()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('StudyData')

    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
       
    ax.plot(data.index, data.index)

    plt.show()
    return ax
    

