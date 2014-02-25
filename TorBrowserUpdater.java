/**
 * TorBrowserUpdater.java
 *
 * A simple program that checks for a Tor Browser Bundle
 * install, then checks torproject.org for a new release
 * and if there is one it will download it, delete the old
 * one and verify the signature of the new release.
 */

/**
 * Written by: Adam Walsh
 * Written on: 2/25/14
 * Maintained at: https://github.com/walshie4/TorBrowserUpdater
 */

public class TorBrowserUpdater {
    /**
     * launchTBB() - launch Tor Browser Bundle
     *
     * @return true if launched successfully, else false
     */
    public boolean launchTBB() {
        //launch
    }
    /**
     * verifySignature() - verify PGP signature
     *
     * @param File containing signature data
     *
     * @return true if verified, else false
     */
    public boolean verifySignature(File signature) {
        //verify
    }
    /**
     * installNew() - installs new version of TBB
     *
     * @return true if install is successful, else false
     */
    public boolean installNew() {
        //install
    }
    /**
     * deleteLocalInstall() - deletes the local TBB install
     *
     * @return true if deleted, else false
     */
    public boolean deleteLocalInstall() {
        //delete
    }
    /**
     * outOfDate() - check if local install is old
     *
     * @param local String containing local version number
     * @param current String containing current version number
     *
     * @return true when out-of-date, false when install is current
     */
    public boolean outOfDate(String local, String current) {
        //compare
    }
    /**
     * checkForLocalInstall() -
     *
     * Prompt user for path to installed TBB
     * (if one is installed) and return a
     * string containing the version number
     *
     * @return A string containing the version number of the local TBB
     *          or "" if no install is found
     */
    public String checkForLocalInstall() {

    }
    /**
     * getVersion()
     *
     * Get the most recent version from torproject.org
     * and return it as a string
     *
     * @return A string containing the version number of current TBB release
     */
    public String getVersion() {

    }
    /**
     * Main method - runs the program
     *
     * @param args - Command-line arguments
     *
     */
    public static void main(String[] args) {
        System.out.println("Checking for local install");
        //check for install
        System.out.println("Checking torproject.org for current version");
        //get version
        if(outOfDate(local, current)) {
            //update and delete old version
        }
        else {
            //local is up-to-date
        }
        System.out.println("Launching TorBrowserBundle");
        //launch TBB
    }
}
