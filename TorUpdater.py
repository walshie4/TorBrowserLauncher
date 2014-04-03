#!/usr/bin/env python
#Written by: Adam Walsh
#Written on 4/2/14

class TBBUpdater:
    def __init__:
        self.currentVersion = getCurrentVersion()
        self.installedVersion = getInstalledVersion()

    def detectLocalInstall:
#look in default location to find install, if not found ask user if a custom
#location install exists

    def getInstalledVersion(path):
#get current version using path to local install

    def getCurrentVersion:
#get newest version from torproject.org

if __name__=="__main__":
    updater = TBBUpdater()
    if updater.upToDate():
        #no need to update, launch bundle
    else
        updater.update()
    updater.launchTBB()
