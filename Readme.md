## 生成requirements.txt
pip freeze > requirements.txt
# how to use this project
python3 -m venv myvenv  
source ./myvenv/bin/python3  
pip install --user --requirement requirements.txt  
python3 ./de2.py  
deactivate
#### Writed under Ubuntu18.04