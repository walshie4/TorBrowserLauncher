<b>TorBrowserUpdater</b>

<b>Note</b>: This is Mac only as of right now.  Following a re-write (probably sometime this week) in either Java or C this will become cross platform. 

<b>Who</b>: This is for someone who uses the Tor Browser Bundle, and does not want to deal with the hassle of checking for / installing updates.  This script has been tested on Mac OS X 10.9. Linux support is unknown, and Windows support is essentially non-existant.

<b>What</b>: Checks for an update of the tor browser bundle for your currnt selected build, and then downloads the update, verifys the signature (requires GPG), and installs it (deleting the old install).  After that it launches the bundle.

<b>Why</b>: The purpose of this is to keep users of the Tor Browser Bundle up to date when using their Tor Browser as running an outdated build can put your security at risk.

<b>How</b>: Just configure the config section (soon to be a config file) and then launch the application.

To Verify Signatures:
Follow the instructions here -> 'https://www.torproject.org/docs/verifying-signatures.html.en'
