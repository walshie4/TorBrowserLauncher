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
     * checkForLocalInstall() -
     *
     * Prompt user for path to installed TBB
     * (if one is installed) and return a
     * string containing the version number
     *
     * @return A string containing the version number of the local TBB
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
    }
}
