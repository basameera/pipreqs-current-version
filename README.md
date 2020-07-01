# pipreqs version correction

Python package `pipreqs` [[link](https://github.com/bndr/pipreqs)] can be used to generate the `requirements.txt` for python project.

But sometimes the version of the python package in the generated `requirements.txt` is different from the version used in the project.

The `pipreqs.py` will fix that.

**NOTE:** `pipreqs` is required. `pip install pipreqs`

Example output of `pipreqs` = `pipreqs.txt`

```bash
numpy==1.18.5
torchvision==0.3.0
matplotlib==3.2.2
joblib==0.15.1
torch==1.1.0
Pillow==7.2.0
```

Corrected output of `pipreqs` = `requirements.txt`

```bash
numpy==1.18.5
torchvision==0.3.0
matplotlib==3.2.2
joblib==0.15.1
torch==1.1.0
Pillow==7.1.2
```

---

**How to use this**

`python pipreqs.py`