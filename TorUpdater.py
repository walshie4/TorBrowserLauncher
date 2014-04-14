#!/usr/bin/env python
#Written by: Adam Walsh
#Written on 4/2/14

from BeautifulSoup import BeautifulSoup
import requests
import sys
import os as OS
import platform
import urllib
from subprocess import Popen, PIPE

class TBBUpdater:
    FINGERPRINT = "8738 A680 B84B 3031 A630  F2DB 416F 0610 63FE E659"
    def getLocalInstall(self):
        localPath = raw_input("Please enter the path to the local TBB install\n"
                       + "a simple way to do this is to drag the file onto this terminal\n"
                       + "or just press enter if no local install exists.\n")
        if localPath == '':
            return None
        else:
            return localPath

    def getCurrentVersion(self):
        res = requests.get("https://www.torproject.org/dist/torbrowser/")
        soup = BeautifulSoup(res.text)
        versions = list()
        versionsNext = False
        for link in soup.findAll('a'): #find all links
            name = link.get('href') #get href contents
            if versionsNext:
                versions.append(name)
            elif name == '/dist/':
                versionsNext = True
        mostRecent = versions[0]
        print "Current available versions are:"
        index = 0
        for version in versions:                            #This choice system may
            print str(index) + " ~ " + version              #be replaced with an
            index += 1                                      #automatic choice to use
                                                            #the newest available
        selection = int(raw_input("Please select which build you would like to run: "))
        print("Selected version: " + versions[selection])
        return versions[selection][:-1] #chop last char (it's a /)

    def upToDate(self, local, current, os): #local should be the path to local install or None
        if local == None:               #if no local install exists. current should be the
            return False                #path to the current version download
        if os == 'win':
            print("Because of Windows using an .exe installer the automated\n"
                + "comparison of your installed version to the current version\n"
                + "you've selected cannot be done. Please install using the .exe\n"
                + "(don't worry the signature has been verified) and then enter the\n"
                + "path to that install here:")
            path = raw_input("-> ")
        elif os == 'mac':
            print "Unzipping selected verison of the TBB"
        elif os == 'linux':
            print "Unarchiving selected version of the TBB"
        else:
            print("Because your OS is not currently supported, the automated\n"
                + "comparison of your installed version to the current version\n"
                + "you've selected cannot be done. Please report this issue on\n"
                + "the Github project page. Sorry!")

    def getLang(self):
        supported = {'Arabic' : 'ar',
                     'German' : 'de',
               'English (US)' : 'en-US',
        'Spanish (Castilian)' : 'es-ES',
                    'Farsi'   : 'fa',
                    'French'  : 'fr',
                    'Italian' : 'it',
                    'Korean'  : 'ko',
                    'Dutch'   : 'nl',
                    'Polish'  : 'pl',
      'Portuguese (Portugal)' : 'pt-Pt',
                   'Russian'  : 'ru',
                 'Vietnamese' : 'vi',
                'Chinese (S)' : 'zh-CN'}
        index = 0
        for lang in supported:
            print str(index) + ' ~ ' + lang
            index += 1
        selected = int(raw_input("Please select which language pack you "
            + "would like to use: "))
        keys = supported.keys()
        return supported[keys[selected]]

    def getOS(self):
        name = platform.system().lower()
        if name == 'windows':
            return 'win'
        elif name == 'darwin':
            return 'mac'
        elif name.lower().find('linux') > -1:
            return 'linux'
        else:
            return None

    def getArch(self):#A bug exists that affects this (http://bugs.python.org/issue7860)
        archs = {'AMD64' : 64, 'x86_64': 64, 'i386': 32, 'x86': 32}
        machine = platform.machine()
        return archs.get(machine, None)

    def getDLURL(self, os, arch, version, lang):
        url = "https://www.torproject.org/dist/torbrowser/"
        url += version + "/"
        if os == 'win': #build windows DL URL
            url += 'torbrowser-install-'
            suffix = '.exe'
            url += version + '_'
            url += lang
            url += suffix
            return url
        elif os == 'mac': #build mac DL URL
            url += 'TorBrowserBundle-'
            suffix = '.zip'
            url += version + '-osx32_'
            url += lang
            url += suffix
            return url
        elif os == 'linux': #build linux DL URL
            url += 'tor-browser-'
            suffix = '.tar.xz'
            if arch == 32:
                url += 'linux32-'
            elif arch == 64:
                url += 'linux64-'
            else:
                print ("Unsupported architecture detected...using 32-bit")
                url += 'linux32-'
            url += version + '_'
            url += lang
            url += suffix
            return url
        else:
            raise ValueError("Unsupported OS detected")

    def generateHash(self, filepath): #generate a sha-256 hash for the file at param filepath
        sha256 = hashlib.sha256()
        f = open(filepath, 'rb')
        try:
            sha256.update(f.read())
        finally:
            f.close()
        return sha256.hexdigest()

    def downloadFileAt(self, url):
        pieces = url.split('/')
        name = pieces[len(pieces)-1] #get filename from url
        print "Downloading " + name + " ..."
        urllib.urlretrieve(url, name)
        print "Download complete."
        return open(name).name #return filepath

    def verifySignature(self, currentTBB, os): #sig should be filepath to sig file (.asc)
        sigStream = open(sig, "rb")
        print("Verifying signature...")
        print("Fetching TBB signer's key...")
        getKeyCmd = "gpg --keyserver x-hkp://pool.sks-keyservers.net --recv-keys 0x416F061063FEE659"
        (stdout, stderr) = Popen(getKeyCmd, stdout=PIPE, shell=True).communicate()
        print stdout
        print("Verifying the key needed to verify the signature")
        verifyKeyCmd = "gpg --fingerprint 0x416F061063FEE659"
        (stdout, stderr) = Popen(verifyKeyCmd, stdout=PIPE, shell=True).communicate()
        if not self.verifyKeySig(stdout, os):#key is not valid
        #    if not os == 'linux':
            raise ValueError("The key you have does not match the known fingerprint!")
        #    else: #try linux's secondary key
        #        print("Fetching linux's secondary key")
        #        getKeyCmd = "gpg --keyserver x-hkp://pool.sks-keyservers.net --recv-keys 0x140C961B"
        #        (stdout, stderr)
        print("Verifying signature file...")
        verifySigCmd = "gpg --verify " + currentTBB + "{.asc,}"
        (stdout, stderr) = Popen(verifySigCmd, stdout=PIPE, shell=True).communicate()
        print stdout

    def verifyKeySig(self, keySig, os):
        if keySig.find(self.FINGERPRINT):
            return True
        else:
            return False

if __name__=="__main__":
    updater = TBBUpdater()
    os = updater.getOS()
    arch = updater.getArch()
    current = updater.getCurrentVersion()
    lang = updater.getLang()
    currentURL = updater.getDLURL(os, arch, current, lang)
    currentTBB = updater.downloadFileAt(currentURL)
    sig = updater.downloadFileAt(currentURL + '.asc')
    updater.verifySignature(currentTBB, os)
    localPath = updater.getLocalInstall()
    if updater.upToDate(localPath, currentTBB, os):
        print("Installed version is up-to-date")
        #no need to update, launch bundle
    #else:
        #updater.update()
    #updater.launchTBB()
    updater.getLanguage()
