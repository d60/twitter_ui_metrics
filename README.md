# UI Metrics Solver

**main.py**
```python
import time

from ui_metrics import solve_ui_metrics

with open('ui_metrics.js', 'r', encoding='utf-8') as f:
    ui_metrics = f.read()

t = time.time()
print(solve_ui_metrics(ui_metrics))
print(time.time() - t)
```
**Result**
```
{'rf': {'aa50bf510106183903ec36dde902b43d7b60ac817a86a91fd96e0920a222885f': 22, 'acf36d8c8feb9ac0806372591b561790ecad0ab4657f15e68217b3085470418e': -154, 'ae124976132ff3d6ad403b942840bb6400b103bbc75ee86e0632dc950fd2f102': 0, 'facf2f4be2837a7383f6c9b606649dbc493291664728d086cb8518266a31d821': -138}, 's': '27ovmMyvTpCkCQmoIvnfKzFulUeuXLWMQVWDDTOHluLenq8btBtTFOwQBH6H41sybsQKXDGYIKrIZsKpcZo1eG5z7xoZxMd_Bw411CIQOrr3hgaWCjmMxEeVyzfIbREBtj2Z-5pTZT9SzFfInM0dRAFuEYY_I2tmzr127s8KfPAR0_8cyf-xLPtTU7JYKePo1UJk_V15W2MieRBnMW2FT6KbkmL5GexIKwIql3GfVk3mJsmmG7ut_bQaNA_ZpPtPmEmxp1Rr7-UuvswmRZ28XYEP1kSNW5g5JSOCuHkyo67_c_ngoNsd4FLzPA81iFUi6Yv8PIKqvGuDFjK7apEeGwAAAZTWScGA'}
0.17166352272033691
```
#
You will get the same results as if you had run it in a browser:


![](https://github.com/d60/twitter_ui_metrics/blob/main/sc.png?raw=true)