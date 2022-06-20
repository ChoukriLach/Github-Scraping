from Data import Data
import pandas as pd





def main():
    data = Data('https://github.com/topics')
    df = pd.DataFrame(data.data, columns = ['Topics', 'Descriptions', 'Topics_url'])
    df.to_csv('data.csv', index=False)

    


if __name__ == '__main__':
    main()






