import time

from .helper import  *
from .customErrors import *

from pympler import asizeof

from pathlib import Path 
BASE_DIR = Path(__file__).resolve().parent

class Database:
    def createTrunk(name , password):
        Trunk(name , password)

    def connectTrunk(name , password):
        expectedLocation:Path = BASE_DIR / 'Trunks' / name 
        if not expectedLocation.exists():
            raise TrunkNotExists(f'The requested Trunk : {name} does not exists or cannot be found')

        crtpass = readJsonFile(expectedLocation / 'INFO.json')['password']

        checkPassword(attemptPass=password  , correctPass=crtpass,
                       errorinfo=f'Wrong Password , Unable to connect to the Trunk : {name}')
        
        return Trunk(name , password)

    def listTrunks():
        return [tr for tr in BASE_DIR.iterdir() if tr.is_dir()]
    
class Trunk:
    def __init__(self , name:str , password:str):
        self.name = name
        self.InfofileLocation = BASE_DIR / 'Trunks' /  self.name / 'INFO.json'

        if not self.InfofileLocation.exists():
            self.establishCreation(password)

    @property
    def password(self):
        return readJsonFile(self.InfofileLocation)['password']

    def establishCreation(self , password):
        createFile(self.InfofileLocation)
        writeJsonFile(filepath=self.InfofileLocation, data =  {'name' : self.name , 'password' : password})

    def createBranch(self , name , password = None):
        if password == None:
            password = self.password

        Branch(name , password , self.InfofileLocation.parent)

    def connectBranch(self , name , password):
        expectedLocation = self.InfofileLocation.parent / name
        if not expectedLocation.exists():
            raise BranchNotExixts

        crtpass = readJsonFile(expectedLocation / 'INFO.json')['password']
        
        checkPassword(attemptPass=password , correctPass=crtpass,
                      errorinfo=f'Wrong Password , Unable to connect to the Trunk : {name}')

        return Branch(name , password , self.InfofileLocation.parent)

    def listBranches(self):
        TrunkFolder:Path = self.InfofileLocation.parent

        return [br for br in TrunkFolder.iterdir() if br.is_dir()]

    
class Branch:
    def __init__(self , name , password ,parentFolderLocation) -> None:
        self.parentFolderLocation =  parentFolderLocation

        self.name = name

        self.datafileLocation = parentFolderLocation / name / 'DATA.json'
        self.InfofileLocation = parentFolderLocation / name / 'INFO.json'
        self.LogfileLocation = parentFolderLocation / name / 'LOG.txt'

        if not self.InfofileLocation.exists():
            self.establishCreation(password)

    @property
    def password(self):
        return readJsonFile(self.InfofileLocation)['password']

    def establishCreation(self , password):
        createFile(self.datafileLocation)
        createFile(self.InfofileLocation)

        writeJsonFile(filepath = self.InfofileLocation  , data = {'name' : self.name , 'password' : password})

        self.log(f'establishCreation: time : {time.time()}')

    def read(self , PassedPass):
        checkPassword(attemptPass=PassedPass , correctPass=self.password ,
                        errorinfo=f"Wrong Password for reading data from Branch {self.name}")

        self.log("Read")
        return readJsonFile(self.datafileLocation)

    def append(self , append_data , PassedPass):
        #The update function also is inbuilt in this method
        checkPassword(attemptPass=PassedPass , correctPass=self.password ,
                        errorinfo=f'Wrong Password for appending data to Branch {self.name}')

        appendJsonFile(self.datafileLocation , append_data)

        self.log(f'Append : {asizeof.asizeof(append_data)}')

    def write(self , new_data , PassedPass):
        #The update function also is inbuilt in this method 
        checkPassword(attemptPass=PassedPass , correctPass=self.password ,
                        errorinfo=f'Wrong Password for writting data to Branch {self.name}')

        writeJsonFile(self.datafileLocation , new_data)
        self.log(f"write : {asizeof.asizeof(new_data)}")

    def rename(self, newName, PassedPass):
        checkPassword(
            attemptPass=PassedPass, correctPass=self.password,
            errorinfo=f"Wrong Password input for renaming of Branch {self.name}"
        )

        old_folder = self.InfofileLocation.parent
        new_folder = old_folder.parent / newName

        if new_folder.exists():
            raise BranchNameNotAccepted(f"Branch '{newName}' already exists.")
        oldName = self.name

        old_folder.rename(new_folder)

        self.name = newName
        self.InfofileLocation = new_folder / "INFO.json"
        self.datafileLocation = new_folder / "DATA.json"
        self.LogfileLocation = new_folder / "LOG.txt"

        appendJsonFile(self.InfofileLocation , {'name' : newName} , createok=False)
        self.log(f"rename: previous:{oldName}     new: {newName}")


    def changePassword(self , PassedPass, newPassword):
        checkPassword(attemptPass=PassedPass , correctPass=self.password ,
                      errorinfo='Authentication Failed for chaging to new Password , Unsucessfull')

        appendJsonFile(self.InfofileLocation , {'password' : newPassword})

        self.log("changePassword")

    def deleteItSelf(self , PassedPass):
        checkPassword(attemptPass=PassedPass , correctPass=self.password , 
                      errorinfo=f'Wrong Password input for deletion of Branch {self.name}')

        deleteFile(self.InfofileLocation)
        deleteFile(self.datafileLocation)
        deleteFile(self.LogfileLocation)

        self.InfofileLocation.parent.rmdir()

    def getValue(self , key , PassedPass):
        checkPassword(attemptPass=PassedPass , correctPass=self.password ,
                      errorinfo=f'Wrong Password to get value from the Branch {self.name}')
        try:
            self.log(f"getValue :  key : {key}")
            print(readJsonFile(self.datafileLocation))
            return readJsonFile(self.datafileLocation)[key]
        except KeyError:
            raise ValueNotFound

    def deleteKey(self , key , PassedPass):
        checkPassword(attemptPass=PassedPass , correctPass=self.password ,
                      errorinfo=f'Wrong Password to delete key from the Branch {self.name}')
        try:
            data = readJsonFile(self.datafileLocation)
            data.pop(key)
            writeJsonFile(self.datafileLocation , data)
            self.log(f"deleteKey : key : {key}")
        except:
            raise KeyNotFound

    def log(self , value):
        appendTxtFile(self.LogfileLocation , '\n' + value)