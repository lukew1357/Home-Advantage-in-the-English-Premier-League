import math
import scipy as sp
import numpy as np
import matplotlib as plt
import requests
from bs4 import BeautifulSoup
import pandas as pd

column_name = ['link_match']
df = pd.read_csv('EPL Workbook.csv', skipinitialspace=True, usecols=column_name)
data_list = df.values.tolist()


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0'}
url = data_list[0][0]
#r = requests.get(url, headers = headers)