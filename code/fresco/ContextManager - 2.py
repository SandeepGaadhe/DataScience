from zipfile import ZipFile 


# Define 'writeTo' function below, such that 
# it writes input_text string to filename.
def writeTo(filename, input_text):
    with open(filename,'w') as f:
        f.write(input_text)

# Define the function 'archive' below, such that
# it archives 'filename' into the 'zipfile'
def archive(zfile, filename):
    with ZipFile(zfile,'w') as zip:
        zip.write(filename)  