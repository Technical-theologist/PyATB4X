import os

# Create a new directory
os.mkdir("New Dir")

# Change the working directory to the new directory
os.chdir("New Dir")

# Go back to the parent directory
os.chdir("../..")

# Remove the directory (which should be empty)
os.rmdir("New Dir")
