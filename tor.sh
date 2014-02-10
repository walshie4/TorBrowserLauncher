#!/usr/bin/env bash
#Written by: Adam Walsh 2013
#Maintained at https://github.com/walshie4/TorBrowserUpdater

PATH_TO_TOR='/Applications' #Put your path to where your tor application lives
LANG='en-US' #Put the language code for your tor build here
OS='osx' #Changing this is experimental and has NOT been tested!
BIT='32' #Changing this is experimental and has NOT been tested!
baseURL='https://www.torproject.org/dist/torbrowser/' #Do not change this (unless you really want to...It will lower the security of this system)

DEBUG=FALSE

confirm () {
    echo "Confirming build signature"
    curl -o hash $1 > /dev/null
    verify=`gpg --verify hash` > /dev/null
    echo $verify #debug print
}

upgrade () {
    echo "Upgrading TBB..."
    cd $PATH_TO_TOR
    rm -R TorBrowserBundle_en-US.app > /dev/null 
    installTor
}

installTor () {
    echo "Installing new build of TBB.."
    cd $PATH_TO_TOR
    curl -o tor $URL > /dev/null
    confim "$URL.asc"
    unzip tor > /dev/null
    rm tor > /dev/null
}

if [ -f "$PATH_TO_TOR/TorBrowserBundle_en-US.app/Docs/sources/versions" ]; then
    localVersion=$(more "$PATH_TO_TOR/TorBrowserBundle_en-US.app/Docs/sources/versions" | grep TORBROWSER_VERSION | cut -f 2 -d '=')
    echo "Local install found! Version $localVersion"
else
    echo "Local install not found"
fi
curl -o page $baseURL > /dev/null
BUILD=`more page | cut -d '<' -f3 | grep href | cut -d '>' -f2 | head -n 1 | cut -f1 -d '/'`
echo "The current build is $BUILD"
rm page > /dev/null
URL="${baseURL}${BUILD}/TorBrowserBundle-${BUILD}-${OS}${BIT}_${LANG}.zip"
#echo $localVersion
#echo $BUILD
if [ ! -z $localVersion ]; then #checks if the localVersion variable is set
    if [[ "$localVersion" != "$BUILD" ]]; then #compares the installed with most up to date version
        upgrade
    fi
else
    installTor
fi
echo "Starting TBB..."
open "${PATH_TO_TOR}/TorBrowserBundle_en-US.app"
