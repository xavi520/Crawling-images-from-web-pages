"""
A tool to read table, download image from url and save the image in terms of the given name
Fangyi Chen @ CMU
19 June 2021 
first Written for Yongxin Zhang
"""
import pandas as pd
import os
import urllib


def read_table(path):
    table = []
    dfs = pd.read_excel(path)
    assert len(dfs['Image']) == len(dfs['Mfr Part #'])
    for im, name in zip(dfs['Image'], dfs['Mfr Part #']):
        table.append([im, name])
    print('there are total {} imgs in table'.format(len(table)))
    return table

def surgery(url):
    url = url.replace(' ', '%20') # legit url format for space
    if url.startswith('https:https:'):
        url = url[6:]
    return url
    

def download_save(table, save_path):

    for i, (url, name) in enumerate(table):
        if url == '-':
            continue
        url = 'https:' + url
        url = surgery(url)
        try:
            save_name = os.path.join(save_path, name) + '.jpg'
        except:
            print(i, name, url, 'not named\n')        
        print(i, name)
        try:
            urllib.request.urlretrieve(url, save_name)
        except:
            print(i, name, url)        


if __name__ == "__main__":
    tabel_path = "1.xlsx"
    save_path = "./save"
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    table = read_table(tabel_path)
    ct = 0
    for i, (url, name) in enumerate(table):
        if url =='-':
             ct += 1
    print(ct)
    # download_save(table, save_path)

