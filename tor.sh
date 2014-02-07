#!/usr/bin/env bash
#Written by: Adam Walsh 2013

rm -R ~/TorBrowser_en-US.app
curl -o tor.zip https://www.torproject.org/dist/torbrowser/osx/TorBrowser-2.3.25-15-osx-x86_64-en-US.zip	
unzip tor
rm tor
open TorBrowser_en-US.app
