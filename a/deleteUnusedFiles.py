import os, time
from datetime import datetime
from dateutil.relativedelta import relativedelta

now = datetime.now()
ref_time = now - relativedelta(seconds = 10)
print(now)
#print(ref_time)

ext = { 'mp4':'Media', 'mkv':'Media', 'wmv':'Media', 'mpeg':'Media', 'flv':'Media',
        'avi':'Media', 'm4v':'Media', 'txt':'Text', 'srt':'Text', 'nfo':'Text',
        'url':'Shortcut','htm':'Shortcut', 'html':'Shortcut', 'website':'Shortcut',
        'jpg':'Media', 'png':'Media',
      }



def getAccessTime(stat):
    return datetime.fromtimestamp(stat.st_atime)


def deleteFiles():
    tree = os.walk(os.getcwd())
    print('Process ', os.getcwd())
    for dirName, subDirs, files in tree:
        print('Inside ', dirName)
        totalNumberOfFiles = len(files)
        filesVisited = 0
        for f in files:
            if f.split('.')[-1] in ext:
                filepath = os.path.join(dirName, f)
                access_time =  getAccessTime(os.stat(filepath))
                if access_time < ref_time:
                    print('Deleting ', f)
                    try:
                        os.remove(filepath)
                    except:
                        print('Error while deleting FILE ', f)
        if len(os.listdir(dirName)) == 0:
            print('Deleting directory')
            try:
                os.rmdir(dirName)
            except:
                print('Error while deleting DIRECTORY ', dirname)

deleteFiles()
#if __name__ == '__main__':

