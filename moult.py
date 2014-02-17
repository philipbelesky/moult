from xml.etree.ElementTree import ElementTree
import os

directory = os.getcwd()

def ProcessGHXFile(file_path):
    the_file = open(file_path)
    the_directory = os.path.dirname(file_location)
    the_tree = ElementTree()
    the_tree.parse(the_file)
    IsolateTheScript(the_tree, the_directory)
    the_file.close()


def WriteOutScript(the_directory, name, extension, contents):
    filename = "%s.%s" % (name, extension)
    filename = os.path.join(the_directory, filename)
    script = open(filename, 'w')
    script.write(contents)
    script.close()

def DebugMessage(inst, language, script_nickname):
    print "\n EXCEPION:"
    print type(inst)
    print inst.args
    print inst
    print "problem with writing %s script named %s" % (language, script_nickname)

def IsolateTheScript(the_tree, the_directory):
    # Traverse the XML tree to find instances of script components

    for element in the_tree.iterfind('.//*[@name="Object"]'):
        # Find the primary nodes, then trawl down to check if they are scripts
        script_type = element.find('.//*item[@name="Name"].[@type_name="gh_string"]')
        script_nickname = element.find('.//*item[@name="NickName"].[@type_name="gh_string"]')

        if script_type.text == "Python Script":
            script_contents = element.find('.//*item[@name="CodeInput"].[@type_name="gh_string"]')
            try:
                WriteOutScript(the_directory, script_nickname.text, "py", script_contents.text)
            except Exception as inst:
                DebugMessage(inst, "python", script_nickname)

        if script_type.text == "VB Script":
            script_contents = element.find('.//*item[@name="AdditionalSource"].[@type_name="gh_string"]')
            try:
                WriteOutScript(the_directory, script_nickname.text, "vb", script_contents.text)
            except Exception as inst:
                DebugMessage(inst, "VB", script_nickname)

        if script_type.text == "C# Script":
            script_contents = element.find('.//*item[@name="AdditionalSource"].[@type_name="gh_string"]')
            try:
                WriteOutScript(the_directory, script_nickname.text, "cs", script_contents.text)
            except Exception as inst:
                DebugMessage(inst, "C++", script_nickname)


for r,d,f in os.walk(directory):
    for the_file in f:
        if the_file.endswith(".ghx"):
            file_location = os.path.join(r,the_file)
            ProcessGHXFile(file_location)

