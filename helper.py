import os
from os import path

import json

from .customErrors import *

from pathlib import Path 
BASE_DIR = Path(__file__).resolve().parent
from pathlib import Path

def createFile(filepath):
    '''The function only creates the file at the desired. The contents of the file are not overwritten if the files already exists.'''
    path = Path(filepath)

    path.parent.mkdir(parents=True, exist_ok=True)

    try:
        path.touch(exist_ok=False)  
    except FileExistsError:
        pass

def deleteFile(filepath):
    '''The  function deletes the file if it exists.'''
    path = Path(filepath)

    if path.exists():
        path.unlink()
    else:
        raise FileNotFoundError
    
def readJsonFile(filepath):
    """The function returns the data present in the json file. If the json file is empty it returns dict()."""
    path = Path(filepath)

    if path.exists():
        try:
            with open(path , 'r') as f:
                data =  json.load(f) 
        except:
            data = dict()

        return data

    else:
        raise FileNotFoundError

def readTxtfile(filepath):
    """The function returns the data present in the txt file. If the txt file is empty it returns '' """
    path = Path(filepath)

    if path.exists():
        try:
            with open(path , 'r')as f:
                data = f.read()
        except:
            data = ''

        return data
    else:
        raise FileNotFoundError

def writeJsonFile(filepath , data ,  createok = True):
    """The function is used to overwrite the contents of the file to the new data provided"""
    path = Path(filepath)

    if createok or path.exists():
        with open(path , 'w') as f:
            json.dump(data , f)

    else:
        raise UnableToWriteToFile
    
def writeTxtFile(filepath , data ,  createok = True):
    """The function is used to overwrite the contents of the file to the new data provided"""
    path = Path(filepath)

    if createok or path.exists():
        with open(path , 'w') as f:
            f.write(data)

    else:
        raise UnableToWriteToFile

def appendJsonFile(filepath , data , createok = True):
    """The function is used to append/update data to the file. It creates a new file in case no such file exists."""
    path = Path(filepath)

    if path.exists():
        do = True
    else:
        if createok:
            do = True
            createFile(path)
        else:
            do = False

    if do:
        temp = readJsonFile(path)
        temp.update(data)
        writeJsonFile(path, temp)

def appendTxtFile(filepath , data , createok = True):
    """The function is used to append/update data to the file. It creates a new file in case no such file exists."""
    path = Path(filepath)
    if path.exists():
        do = True
    else:
        if createok:
            do = True
            createFile(path)
        else:
            do = False
    if do:
        temp = readTxtfile(path)
        temp += data
        writeTxtFile(path , temp)

def checkPassword(attemptPass:str , correctPass:str , errorinfo:str):
    if attemptPass == correctPass:
        return True 
    
    if errorinfo:
        raise WrongPassword(errorinfo)