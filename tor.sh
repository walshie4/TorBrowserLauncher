#!/usr/bin/env bash
#Written by: Adam Walsh 2013
#Maintained at https://github.com/walshie4/TorBrowserUpdater

PATH_TO_TOR='/Applications' #Put your path to where your tor application lives
LANG='en-US' #Put the language code for your tor build here
OS='osx' #Changing this is experimental and has NOT been tested!
BIT='32' #Changing this is experimental and has NOT been tested!
baseURL='https://www.torproject.org/dist/torbrowser/' #Do not change this (unless you really want to...It will lower the security of this system)

upgrade () {
    cd $PATH_TO_TOR
    rm -R TorBrowserBundle_en-US.app
    installTor
}

installTor () {
    cd $PATH_TO_TOR
    curl -o tor $URL
    unzip tor
    rm tor
}

if [ -f "$PATH_TO_TOR/TorBrowserBundle_en-US.app/Docs/sources/versions" ]; then
    localVersion=$(more "$PATH_TO_TOR/TorBrowserBundle_en-US.app/Docs/sources/versions" | grep TORBROWSER_VERSION | cut -f 2 -d '=')
else
    echo "Local install not found"
fi
curl -o page $baseURL
BUILD=`more page | cut -d '<' -f3 | grep href | cut -d '>' -f2 | head -n 1 | cut -f1 -d '/'`
rm page
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
open "${PATH_TO_TOR}/TorBrowserBundle_en-US.app"
