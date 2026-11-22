##import numpy as np
##ls = [1,2,3,4,5]
##arr = np.array(ls)
##print("--------------")
##print(arr)
##print("Mean =", arr.mean())
####-----------------------------------
##import pandas as pd
##data = {'Name': ['Ahmad', 'Sara', 'Ali'],'score': [85, 90, 78]}
##df = pd.DataFrame(data)
##print(df)
##print("-------------")
##print(df['score'].mean())
######################################
##import pandas as pd
##import matplotlib.pyplot as plt
##data = {'Name': ['Ahmad', 'Sara', 'Ali', 'Khalid'],'score': [85, 90, 78, 100]}
##df = pd.DataFrame(data)
##colors = ['gold' if x == 100 else 'green' if x >=80 else 'red' for x in df['score']]
##plt.bar(df['Name'], df['score'],color=colors)
##plt.title("Score -  gold = 100, Green = pass , Red = fail")
##for i, v in enumerate(df['score']):
##    plt.text(i,v + 2, str(v), ha='center', fontweight='bold')    
##plt.ylabel("Score")
##plt.show()
####df['Result'] = ['pass' if x >=80 else 'fail' for x in df['score']]
##print(df)
##print("-------------")
##print("الناجحين فقط")
##print(df[df['score'] < 80])
##-----------
##import pandas as pd
##import matplotlib.pyplot as plt
##data = {'Name': ['Ahmad', 'Sara', 'Ali', 'FADL'],'score': [85, 90, 78, 100]}
##df = pd.DataFrame(data)
##colors = ['gold' if x == 100 else 'green' if x >=80 else 'red' for x in df['score']]
##plt.bar(df['Name'], df['score'],color=colors, edgecolor='black', linewidth=1.5)
##plt.title("Score -  gold = 100, Green = pass , Red = fail")
##for i, v in enumerate(df['score']):
##    plt.text(i,v + 2, str(v), ha='center', fontweight='bold', color='gold')
##    plt.text(3, 108, "*TOPPER*", ha='center',fontsize=10, fontweight='bold', color='gold')
##plt.ylabel("Score")
##plt.ylim(0,120)
##plt.tight_layout()
##plt.show()
##

import pandas as pd
import matplotlib.pyplot as plt
data = {'Name': ['Ahmad', 'Sara', 'Ali', 'FADL'],'score': [85, 90, 78, 100]}
df = pd.DataFrame(data)
colors = ['gold' if x == 100 else 'green' if x >=80 else 'red' for x in df['score']]
plt.bar(df['Name'], df['score'],color=colors, edgecolor='black', linewidth=1.5)
plt.title("Score -  gold = 100, Green = pass , Red = fail")
for i, v in enumerate(df['score']):
    plt.text(i,v + 2, str(v), ha='center', fontweight='bold', color='gold')
    plt.text(3, 108, "*TOPPER*", ha='center',fontsize=10, fontweight='bold', color='gold')
plt.ylabel("Score")
plt.ylim(0,120)
plt.tight_layout()
plt.show()




