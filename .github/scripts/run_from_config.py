import os
import subprocess
import yaml

#Define the path to the config file
config_file_path = "config.txt"

# Read and parse the config file
with open(config_file_path,"r") as file:
  lines = file.readlines()

#Process each line
for line in lines:
  appname,region,scripts_str = line.strip().split("***")
  directory, *scripts = scripts_str.split("-")

  if(directory == "API"):
    print(f"Running API scripts for {appname} in region {region} for directory {directory}")
  elif(directory == "UI"):
    print(f"Running UI scripts for {appname} in region {region} for directory {directory}")
  else:
    continue

  # Process the scripts to run
  scripts = scripts[0].split(",")

  #Define the directory and scripts to execute
  script_directory = os.path.join(".",directory)
  os.makedirs(script_directory,exist_ok=True)

  # Execute each script in the directory
  for script in scripts:
    script_path = os.path.join(script_directory,script)
    print(f"Running {script} in directory {directory} for {appname} in region {region}")

    try:
      result = subprocess.run(
        ["python3",script_path],
        check = True,
        capture_output=True,
        text=True,
        env={"APPNAME": appname, "REGION": region, "DIRECTORY":directory}
      )
      print(result.stdout)
    except subprocess.CalledProcessError as e:
      print(f"Error executing {script}: {e.stderr}")
