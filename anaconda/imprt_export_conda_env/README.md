## <font color="gold"><ins><b>Conda Environment Creation and Exporting</b></ins></font>
```python
> conda info
> conda update conda
> conda install PACKAGENAME 
> conda update PACKAGENAME 

> conda env list 
> conda list --name ENVNAME
> conda activate env_name
```

# Sharing environment with others
```python
> conda env export --name your_env_name > exporting_file_name.yml
# Curretnly activated env
> conda env export > exporting_file_name.yml

```

# Creating env from .yml
```python
# create the environment from the env_file_name.yml file:
> conda env create -f env_file_name.yml
```
# Create clone of existing env
```python
> conda create --name new_env_name --clone existing_env
```

# Delete an entire environment
```python
> conda remove --name ENVNAME --all 
```