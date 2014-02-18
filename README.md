# Moult

A script that extracts the contents of Python, VB, and C# components within [Grasshopper](http://www.grasshopper3d.com/) and writes them out to files.

I find it useful because it means (when combined with version control) that I can use a diff tool to compare between different revisions to a script inside a component. YMMV.

## Installation

You'll need Python installed in order to use this. You'll then need to open up a shell, navigate to where your Grasshopper files are, and then execute the script. As an example:

    $ cd "c:\Grasshopper Project\"
    $ python "c:\Script Location\moult.py"

## Usage

If you execute the file it will traverse down all the folders within the directory it is placed. Each time it encounters a **GHX** file it will extract its the scripts and write them to a file in the same directory tree.

*Note that you must Save As your Grasshopper files as "Grasshopper Xml (.ghx)" for this to work"*

*Note that each time this script is run it deletes and then regenerates the old versions of its files. This means that if you delete a component containing a script in the definition, and then re-run this script its file will be removed. Comment out lines 88-91 if you want to stop this behaviour*