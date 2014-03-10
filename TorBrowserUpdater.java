/**
 * TorBrowserUpdater.java
 *
 * A simple program that checks for a Tor Browser Bundle
 * install, then checks torproject.org for a new release
 * and if there is one it will download it, delete the old
 * one and verify the signature of the new release.
 */
import java.io.File;
import java.net.URI;
import java.net.URISyntaxException;
/**
 * Written by: Adam Walsh
 * Written on: 2/25/14
 * Maintained at: https://github.com/walshie4/TorBrowserUpdater
 */

public class TorBrowserUpdater {
    private File TBB; /**Stores the location of local TBB install*/
    private final String urlBase; /**Base of url to download new TBB releases*/
    private String version; /**String representation of current installed version*/
    private String current; /**String representation of most current release
                               available*/
    /**
     * constructor - Creates a new TorBrowserUpdater object
     *
     * @return new TorBrowserUpdater object
     */
    public TorBrowserUpdater() {
        this.urlBase = "https://www.torproject.org/dist/torbrowser/";
    }
    /**
     * launchTBB() - launch Tor Browser Bundle
     *
     * @return true if launched successfully, else false
     */
    private boolean launchTBB() {
        //launch
    }
    /**
     * verifySignature() - verify PGP signature
     *
     * @param File containing signature data
     *
     * @return true if verified, else false
     */
    private boolean verifySignature(File signature) {
        //verify
    }
    /**
     * installNew() - installs new version of TBB
     *
     * @return true if install is successful, else false
     */
    private boolean installNew() {
        //install
    }
    /**
     * deleteLocalInstall() - deletes the local TBB install
     *
     * @return true if deleted, else false
     */
    private boolean deleteLocalInstall() {
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
    private boolean outOfDate(String local, String current) {
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
    private String checkForLocalInstall() {

    }
    /**
     * getVersion()
     *
     * Get the most recent version from torproject.org
     * and return it as a string
     *
     * @return A string containing the version number of current TBB release
     */
    private String getVersion() {

    }
    /**
     * Main method - runs the program
     *
     * @param args - Command-line arguments
     *
     */
    public static void main(String[] args) {
        //run program
    }
}
