#!/usr/bin/env python
#Written by: Adam Walsh
#Written on 4/2/14

from BeautifulSoup import BeautifulSoup
import requests
import sys
import os

class TBBUpdater:
    currentVersion = None
    installedVersion = None

    def detectLocalInstall(self):
        print("Detecting local install...")
#look in default location to find install, if not found ask user if a custom
#location install exists

    def getInstalledVersion(self, path):    #The looking for an installed version may
        if path == None:                    #be thrown out for additional security to
            print ("No local install found.")#prevent accidental use of a tampered
        print("Gathering version info for local install")#version of TBB on your local
                                                         #machine

    def getCurrentVersion(self):
        res = requests.get("https://www.torproject.org/dist/torbrowser/")
        soup = BeautifulSoup(res.text)
        versions = list()
        versionsNext = False
        for link in soup.findAll('a'):
            name = link.get('href')
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
        self.currentVersion = versions[selection]

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

if __name__=="__main__":
    updater = TBBUpdater()
    updater.getCurrentVersion()
    if updater.upToDate():
        print("Installed version is up-to-date")
        #no need to update, launch bundle
    #else:
        #updater.update()
    #updater.launchTBB()
