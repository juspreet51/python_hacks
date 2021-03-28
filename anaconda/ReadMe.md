# Managing Environments:

1) To create an environment:
```python
conda create --name myenv
```
Or
```python
conda create -n myenv python=3.6
conda create -n myenv scipy numpy pandas matplotlib
onda create -n myenv scipy=0.15.0
conda create -n myenv python=3.6 scipy=0.15.0 pandas
```
Or
```python
conda env create -f environment.yml
```

2) View packages/Libraries:
```python
conda list -n myenv
conda list -n myenv scipy
```


3) Sharing an environment:
```python
conda env export > environment.yml
```

4) Removing an environment:
```python
conda remove --name myenv --all
```