#!/usr/bin/env python
#Written by: Adam Walsh
#Written on 4/2/14

from BeautifulSoup import BeautifulSoup
import requests
import sys
import os as OS
import platform
import urllib
from subprocess import Popen, PIPE, call
from shutil import move
from shutil import rmtree as remove

class TBBUpdater:
#The following output variables hold the expected output of running the command
# gpg --fingerprint KEY
#Where KEY is either 0x416F061063FEE659 (for the key most used to sign the TBB)
#or 0x140C961B (for the key sometimes used to sign the linux TBB)
    OUTPUT = """pub   2048R/63FEE659 2003-10-16
      Key fingerprint = 8738 A680 B84B 3031 A630  F2DB 416F 0610 63FE E659
uid                  Erinn Clark <erinn@torproject.org>
uid                  Erinn Clark <erinn@debian.org>
uid                  Erinn Clark <erinn@double-helix.org>
sub   2048R/EB399FD7 2003-10-16

"""
    LINUX_OUTPUT = """pub   4096R/C5AA446D 2010-07-14
      Key fingerprint = 261C 5FBE 7728 5F88 FB0C  3432 66C8 C2D7 C5AA 446D
uid                  Sebastian Hahn <sebastian@torproject.org>
uid                  Sebastian Hahn <mail@sebastianhahn.net>
sub   2048R/A2499719 2010-07-14
sub   2048R/140C961B 2010-07-14

"""
    def run(self): #run updater
                                #Order of operations:   (implemented?)
                                #get sys info (os, arch)
                                #get desired build
                                #get desired lang
                                #download build and sig
                                #verify signature
                                #install/unarchive new build
                                #delete install file/archive file
                                #get local install path
                                #move new build to location of local build
                                #delete extra files
                                #launch new build
                                #exit
        print "Running..."
        os = self.getOS()
        arch = self.getArch()
        current = self.getCurrentVersion()
        lang = self.getLang()
        currentURL = self.getDLURL(os, arch, current, lang)
        currentTBB = self.downloadFileAt(currentURL)
        sig = self.downloadFileAt(currentURL + '.asc')
        if not self.verifySignature(currentTBB, os):#if verification fails
            print("Exiting...")
            sys.exit()
        newPath = self.install(currentTBB, os)
        localPath = self.getLocalInstall()
        self.update(localPath, currentTBB)
        print("Cleaning up extra files...")
        self.cleanUp(sig, currentTBB)
        print("Launching TBB...")
        self.launchTBB(localPath)
        print("Exiting...")

    def update(self, local, current):
        if local == None: #no local install
            location = raw_input("Where would you like your TBB install located?\n"
                    + "Simpliest method for this is drag n drop a folder\n-> ")
            print("Moving current version to \"" + location + "\"")
            move(current, location)
        else:
            print("Deleting local install found @ \"" + local + "\"")
            remove(local)
            print("Moving current version to same location as local install was located")
            move(current, local)#move current to location of where local was

    def launchTBB(self, local, os):
        print("Launching TBB...")
        #launch TBB @ path `local`

    def cleanUp(self, sig, currentTBB):
        print("Deleting extra files no longer needed (downloaded installers, sig, etc.)")
        #delete files used in the install process (archive downloaded, installer, etc.)

    def getLocalInstall(self):
        localPath = raw_input("Please enter the path to the local TBB install\n"
                       + "a simple way to do this is to drag the file onto this terminal\n"
                       + "or just press enter if no local install exists.\n-> ")
        if localPath == '':
            return None
        else:
            return localPath.rstrip()#get rid of ending whitespace

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

    def downloadFileAt(self, url):
        pieces = url.split('/')
        name = pieces[len(pieces)-1] #get filename from url
        print "Downloading " + name + " ..."
        urllib.urlretrieve(url, name)
        print "Download complete."
        return open(name).name #return filepath

    def verifySignature(self, currentTBB, os): #sig should be filepath to sig file (.asc)
        print("Verifying signature...")
        print("Fetching TBB signer's key...")
        getKeyCmd = "gpg --keyserver x-hkp://pool.sks-keyservers.net --recv-keys 0x416F061063FEE659"
        (stdout, stderr) = Popen(getKeyCmd, stdout=PIPE, shell=True).communicate()
        print stdout
        if os == 'linux':
            print("Fetching TBB's secondary linux key...")
            getKeyCmd = "gpg --keyserver x-hkp://pool.sks-keyservers.net --recv-keys 0x140C961B"
            (stdout, stderr) = Popen(getKeyCmd, stdout=PIPE, shell=True).communicate()
            print stdout
            if not stdout == self.LINUX_OUPUT:#linux key is not valid
                raise ValueError("The key you have does not match the known fingerprint!")
        print("Verifying the key needed to verify the signature")
        verifyKeyCmd = "gpg --fingerprint 0x416F061063FEE659"
        (stdout, stderr) = Popen(verifyKeyCmd, stdout=PIPE, shell=True).communicate()
        if not stdout == self.OUTPUT:#key is not valid (for non-linux)
            raise ValueError("The key you have does not match the known fingerprint!")
        print("Verifying signature file...")
        verifySigCmd = "gpg --verify " + currentTBB + "{.asc,}"
        (stdout, stderr) = Popen(verifySigCmd, stdout=PIPE, shell=True).communicate()
        print stdout
        if stdout.find("Good signature"):
            print("Signature verified.")
            return True
        else:
            print("Signature was not verified!")
            return False

if __name__=="__main__":
    updater = TBBUpdater()
    updater.run()
