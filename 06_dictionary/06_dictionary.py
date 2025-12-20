# Claude 
# https://claude.ai/share/c3b5bd6e-5152-47e6-a904-4630d84f3f5d

import json

from pprint import pprint

# duration_pipeline = {
#     "build": "success",
#     "test": "failure",
# }

# last_5_pipeline_status = {
#     "build": ["success", "success", "success", "failure", "success"],
#     "test": ["success", "success", "failure", "failure", "success"]
# }

# Track pipeline stages and their status
pipeline = {
    "build": {
        "status": "success", 
        "duration": "2m 15s"
    },
    "test": {
        "status": "success", 
        "duration": "5m 30s"
    },
    "security_scan": {"status": "running", "duration": "1m 45s"},
    "deploy": {"status": "pending", "duration": None}
}

# Check pipeline progress
# for stage, info in pipeline.items():
#     print(f"{stage}: {info['status']} ({info['duration']})")


# Update stage status
sec_scan_dict = pipeline["security_scan"]
sec_scan_dict["status"] = "success"

# pipeline["security_scan"]["duration"] = "3m 20s"

print(json.dumps(pipeline, indent=4))


# Find the dictionary for a deployment time of a product
app_a_deploy_window = {
    "start": "2024-10-15 14:30:00",
    "end": "2024-10-15 16:30:00"
}

# Find the dictionary for a deployment times for today 
app_a_deploys_today = [
    {
        "start": "2024-10-15 14:30:00",
        "end": "2024-10-15 18:00:00",
    },
    {
        "start": "2024-10-15 20:00:00",
        "end": "2024-10-15 22:00:00",
    }
]

jobs_queue = [
    {"job_name": "data_backup", "priority": "high", "time": "02:00"},
    {"job_name": "log_cleanup", "priority": "low", "time": "03:00", "failure": "log_reload"},
    {"job_name": "system_update", "priority": "medium", "time": "04:00"},
]

# When to use a list:
# ✅ Searching by key is not required
# ✅ Order matters
# ✅ Duplicates are allowed/expected
# ✅ Access by position (first, last, nth item)

# When to use a dictionary:
# ✅ Need fast lookup by key (not position)
# ✅ Order does not matter# 
# ✅ Access by key


# Monitor pod health status
pods_status = {
    "api-deployment-7d8f9": {
        "namespace": "production",
        "status": "Not Running",
        "restarts": 0,
        "cpu_usage": "45%",
        "memory_usage": "512Mi"
    },
    "worker-deployment-4k2m1": {
        "namespace": "production",
        "status": "CrashLoopBackOff",
        "restarts": 5,
        "cpu_usage": "10%",
        "memory_usage": "128Mi"
    }
}

# Find unhealthy pods

# deprecated - looping over dict key 
# use it only when keys are needed 

# for name in pods_status:
#     info = pods_status[name]
#     if info['status'] != 'Running' or info['restarts'] > 3:
#         print(f"Pod {name} is unhealthy with status {info['status']} and restarts {info['restarts']}")

for name, info_dict in pods_status.items():
    # Condition to check unhealthy pods
    # Status is not 'Running' or 
    # restarts more than 3
    if info_dict['status'] != 'Running' or info_dict['restarts'] > 3:
        print(f"""Pod {name} is unhealthy. 
    Status {info_dict['status']}
    Restarts {info_dict['restarts']}
""")

prod_01_conf = {
    "ip": "192.168.1.10",
    "role": "web",
    "environment": "production",
    "memory_gb": 16,
    "cpu_cores": 8,
    "status": "active"
}

# Tasks for todays lesson in dictionary:

# 1. Access and print the IP address of the server.
prod_01_ip = prod_01_conf["ip"]
print(f"Server IP Address: {prod_01_ip}")

# 2. Update the server status to 'maintenance'.
print(f'Server status before: {prod_01_conf["status"]}')
prod_01_conf["status"] = "maintenance"  # modify 
print(f'Server status after: {prod_01_conf["status"]}')


# 3. Add a new key-value pair for 'disk_space_gb' with a value of 500.
prod_01_conf["disk_space_gb"] = 500
print(f"Dictionary after disk space added: \n{json.dumps(prod_01_conf, indent=4)}")
pprint(prod_01_conf)


# 4. Decrease the memory_gb by 4 GB
# write a function that will reduce the memory by given units
def reduce_memory(config, reduce_size):
    """The function accepts a config and reduces memory_gb parameter by reduce_size units"""

    # validate presence of memory_gb in config    
    if "memory_gb" not in config:
        print(f"memory_gb is not present in input dictionary. Not performing modification")
        # raise Exception("memory_gb should be present in config input")
        return config

    # reduce
    config["memory_gb"] = config["memory_gb"] - reduce_size
    return config


# prod_01_conf["memory_gb"] = prod_01_conf["memory_gb"] - 4

# prod_01_conf = reduce_memory(prod_01_conf, 8)
# print(f'After size reduction  \n{json.dumps(prod_01_conf, indent=4)}')


prod_01_conf = reduce_memory({"name": "swadhi"}, 8)
print(f'After size reduction  \n{json.dumps(prod_01_conf, indent=4)}')
