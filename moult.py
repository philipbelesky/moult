from xml.etree.ElementTree import ElementTree
import os

def ProcessGHXFile(definition_path, base_filename):
    # Loads the file and sets up the XML parser
    the_file = open(definition_path)
    the_directory = os.path.dirname(definition_path)
    the_tree = ElementTree()
    the_tree.parse(the_file)
    IsolateTheScript(the_tree, the_directory, base_filename)
    the_file.close()


def WriteOutScript(target_directory, name, extension, contents, script_guid, definition_filename):
    # Name and writing each component's file
    filename = "%s___%s___%s.%s" % (definition_filename, name, script_guid[:4],  extension)
    filename = os.path.join(target_directory, filename)
    script = open(filename, 'w')
    script.write(contents)
    script.close
    global total_components
    total_components += 1


def DebugMessage(inst, script_type, the_directory, script_nickname, extension, script_content, script_guid, definition_filename):
    # Debug printouts. Probably not needed anymore
    print "EXCEPION: %s" % type(inst)
    print "name is \t\t%s" % script_nickname
    print "language is \t\t%s" % script_type
    print "contents are \t\t%s" % script_content[:10]
    print "guid is \t\t%s" % script_guid
    print "\n"


def IsolateTheScript(the_tree, the_directory, definition_filename):
    # Traversing the XML tree to find code elements
    for element in the_tree.iterfind('.//*[@name="Object"]'):
        # Find the primary nodes, then trawl down to check if they are scripts
        script_type = element.find('.//*item[@name="Name"].[@type_name="gh_string"]').text
        script_nickname = element.find('.//*item[@name="NickName"].[@type_name="gh_string"]').text
        script_guid = element.find('.//*item[@name="InstanceGuid"].[@type_name="gh_guid"]').text

        extension = None
        if script_type == "Python Script":
            extension = "py"
            try:
                script_content = element.find('.//*item[@name="CodeInput"].[@type_name="gh_string"]').text
            except:
                script_content = None

        if script_type == "VB Script":
            extension = "vb"
            try:
                script_content = element.find('.//*item[@name="AdditionalSource"].[@type_name="gh_string"]').text
            except:
                script_content = None

        if script_type == "C# Script":
            extension = "cs"
            try:
                script_content = element.find('.//*item[@name="AdditionalSource"].[@type_name="gh_string"]').text
            except:
                script_content = None

        # The crawler has issues if the component contains no code yet, hence all the exceptions and None checking
        if (extension is not None and script_content is not None):
            try:
                WriteOutScript(the_directory, script_nickname, extension, script_content, script_guid, definition_filename)
            except Exception as inst:
                DebugMessage(inst, script_type, the_directory, script_nickname, extension, script_content, script_guid, definition_filename)




directory = os.getcwd()
total_components = 0
total_definitions = 0

for path, subdirs, files in os.walk(directory):
    for the_file in files:
        # Matching grasshopper definitions, but excluding backup files
        if the_file.endswith(".ghx") and not the_file.endswith("].ghx"):
            total_definitions +=1
            file_location = os.path.join(path,the_file)
            the_filename = os.path.basename(the_file)
            base_filename = os.path.splitext(the_filename)[0]

            # deleting old versions of the file (ie removed components)
            sibling_files = [s for s in os.listdir(path) if os.path.isfile(s)]
            for s in sibling_files:
                if s.startswith(base_filename  + "___") and (s.endswith(".py") or s.endswith(".cs") or s.endswith(".vb")):
                     os.remove(s)

            ProcessGHXFile(file_location, base_filename)

print "Extracted %i script components from %i files" % (total_components, total_definitions)