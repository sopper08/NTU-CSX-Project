#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 18:13:33 2018

@author: sopper
"""

import pandas as pd
import numpy as np
import sys

inputdata = str(sys.argv[1])

df_input = pd.read_csv(inputdata)
df_output = pd.DataFrame(index=df_input.index)

# survived
try:
    df_output['survived'] = df_input['survived'].copy()
    print('Transform trainingData ')
except:
    print('Transform testingData ')
# fare: 不處理直接使用。
meanFare = 39
df_input['fare'] = df_input['fare'].replace({np.nan:meanFare})
df_output['fare'] = df_input['fare'].copy()

# age:  缺漏值使用平均年齡。
meanAge = 31
df_input['age'] = df_input['age'].replace({np.nan:meanAge})
df_output['age'] = df_input['age'].copy()

# sex: female->1, male->0.
df_output['sex'] = 0
df_output['sex'][df_input['sex']=='female'] = 1

# sibsp: change to [sibsp1, sibsp2, sibsp3, sibsp4, sibsp5], 其中 0 : [0, 0, 0, 0, 0]。
for index in range(1,6):
    df_output['sibsp%d'%index] = 0
    df_output['sibsp%d'%index][df_input['sibsp']==index] = 1
    
# parch: change to [parch1, parch2, parch3, parch4, parch5, parch6], 其中 0 : [0, 0, 0, 0, 0, 0]。
for index in range(1,7):
    df_output['parch%d'%index] = 0
    df_output['parch%d'%index][df_input['parch']==index] = 1

# embarked: change to [C, Q], 其中 S: [0, 0]。
embarked_list = ['C', 'Q']
for embarked in embarked_list:
    df_output['%s'%embarked] = 0
    df_output['%s'%embarked][df_input['embarked']==embarked] = 1

# boat: change to [A, B, C, D, boat1, boat2, boat3, … boat12]。
boat_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',\
            '11', '12', '13', '14', '15', '16', 'A', 'B', 'C', 'D']
for boat in boat_list:
    df_output['boat%s'%boat] = 0
    df_output['boat%s'%boat][df_input['boat']==boat] = 50

df_output.to_csv(sys.argv[2], index=False)
print('Transfer data finish!')