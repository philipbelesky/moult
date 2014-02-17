# Moult

A script to extract the contents of Python, VB, and C# components within [Grasshopper](http://www.grasshopper3d.com/) and writes them to a file.

I'm not sure what this is useful for. Personally I find it useful because it means (when combined with version control) that I can use a diff tool to compare between different revisions to a script. It also makes Github repo's full of Grasshopper files look a bit more lively.

## Installation

You'll need Python installed in order to use this. You'll then need to open up a shell, navigate to where your Grasshopper files are, and then execute the script. Like so:

    $ cd "c:/Grasshopper Project/"
    $ python "c:/Script Location/moult.py"

## Usage

If you execute the file it will traverse down all the folders within the directory it is placed. Each time it encounters a **GHX** file it will extract its the scripts and write them to a file in the same directory tree.

*Note that this only works when your Grasshopper files as saved in the GHX format*

*Note that the filenames of each file come from the name you give the component. So they'll need to be unique within each definition and between different definitions within the same directory*

