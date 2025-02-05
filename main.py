import time

from ui_metrics import solve_ui_metrics

with open('ui_metrics.js', encoding='utf-8') as f:
    ui_metrics = f.read()

t = time.time()
print(solve_ui_metrics(ui_metrics))
print(time.time() - t)
