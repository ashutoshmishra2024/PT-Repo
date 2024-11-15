import os
import json

config_file = os.environ.get("CONFIG_FILE","config.txt")


# Prepare job outputs
api_jobs = []
ui_jobs = []

# Read the config file
with open('config.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        appname, region, scripts_str = line.strip().split("***")
        directory, scripts = scripts_str.split("-")
        scripts_list = scripts.split(",")

        # Create dynamic job definitions
        job_data = {
            "appname": appname,
            "region": region,
            "directory": directory,
            "scripts": scripts_list,
              }

        if directory == "API":
            api_jobs.append(job_data)
        elif directory == "UI":
            ui_jobs.append(job_data)

          # Set outputs for subsequent jobs
    print("::set-output name=api-jobs::" + json.dumps(api_jobs))
    print("::set-output name=ui-jobs::" + json.dumps(ui_jobs))
