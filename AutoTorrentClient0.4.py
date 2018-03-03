#-*- coding:latin-1 -*-
import os,sys ,glob,string
import paramiko as par
from codecs import Codec
print sys.platform
try:
    import androidhelper as android
except:
    import android
droid=android.Android()

    
host=droid.dialogGetInput(title="Serveur",defaultText="retropie").result
droid.DialogShow()
droid.dialogDissMiss() 
mdp=droid.dialogGetPassword(title='mot de passe',message='Celui du compte "Pi"').result
sprt=droid.dialogGetInput(title='port' ,defaultText='22').result
#print mdp
#print sprt

se=os.name
global remd,locf,remf
hme=os.getenv('HOME')

user='pi'
#mdp=raw_input('mot de passe: ')
#sprt=raw_input('port: ')


print hme
print se
def testdir():
    test=os.path.exists('Torrents')
    if test==False : os.mkdir('Torrents')
    else : print 'Dossier Torrents existant'
        
def defaultdir():
    os.chdir('Torrents')

def istor():
    return os.listdir('../Torrents/')
    
    

prt=int(sprt)
print 'server: '+user+'@'+host+':'+sprt

testdir()
defaultdir()
locd=os.getcwd()+'/'

print locd
print 'torrent:'
tor=istor()
loc= str(tor[0])
print loc
locf=tor[0]
remf=locf.encode('latin-1')

client=par.client
SSH=client.SSHClient()
pol=client.AutoAddPolicy()
SSH.set_missing_host_key_policy(pol)

SSH.connect(host,port=prt,username=user,password=mdp)
SFTP=SSH.open_sftp()

SFTP.chdir('/home/pi/AutoTorrent/')
cwd=SFTP.getcwd()
remd=cwd+'/'

print 'dossier distant: '+cwd

if locf != ' ':
    SFTP.put(remf,remd+remf)
else : print 'rien a transferer dans :'

print SFTP.listdir()
'''cmd='/home/pi/AutoTorrent/./Autotorrent '
stdin,stdout,stderr=SSH.exec_command('sudo '+cmd+remf+' 1')

rout=stdout.read()
rerr=stderr.read()
print rout
print rerr'''
    
SFTP.close()
SSH.close()
exit()