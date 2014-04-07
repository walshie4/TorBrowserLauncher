#!/usr/bin/env python
#Written by: Adam Walsh
#Written on 4/2/14

from BeautifulSoup import BeautifulSoup
import requests
import sys
import os
import platform
import gnupg
import urllib

class TBBUpdater:
    def getLocalInstall(self):
        localPath = raw_input("Please enter the path to the local TBB install\n"
                       + "or just press enter if no local install exists")
        if localPath == '':
            return None
        else:
            return localPath

    def getInstalledVersion(self, path, os):
        if path == None:
            print "No local install found."
            return None
        print "Gathering version info for local install"
        if os == 'win':
            #find version info
        elif os == 'mac':
            #find version info
        elif os == 'linux':
            #find version info
        else:
            print "Local install could not be detected because of an\n"
                + "unsupported OS."

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

    def upToDate(self):
        if self.currentVersion == None or self.installedVersion == None:
            print("Either current version or installed version variable is null.\n"
                    + "This means either a local install has not been found or\n"
                    + "checks are being made before getting both the current and\n"
                    + "installed version numbers of the TBB.")
        elif self.currentVersion == self.installedVersion:
            return True
        else:
            return False

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

    def downloadFileAt(url):
        pieces = url.split('/')
        name = pieces[len(pieces)-1] #get filename from url
        urllib.retrieve(url, name)
        return open(name).name #return filepath

if __name__=="__main__":
    updater = TBBUpdater()
    os = updater.getOS()
    arch = updater.getArch()
    current = updater.getCurrentVersion()
    lang = updater.getLang()
    currentURL = updater.getDLURL(os, arch, current, lang)
    if updater.upToDate():
        print("Installed version is up-to-date")
        #no need to update, launch bundle
    #else:
        #updater.update()
    #updater.launchTBB()
    updater.getLanguage()
