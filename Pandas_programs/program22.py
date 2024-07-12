"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to iterate data in a DataFrame.

"""


def iterate_data(exam_data, labels):

    """

    description:
        This function is used to iterate data in the DataFrame.


    parameters:
        labels(list), exam_data(dict) : labels, exam_data that is going to frame a data frame.
            
    return:
        none

    """

    import pandas as pd
    
    data = pd.DataFrame(exam_data, index=labels)
    for index, rows in data.iterrows():
        print(index)
        print(rows)
    
def main():
    import numpy as np
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    iterate_data(exam_data, labels)


if __name__ == "__main__":
    main()