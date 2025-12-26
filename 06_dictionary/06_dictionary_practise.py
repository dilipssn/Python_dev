# CI/CD Pipeline Status Tracker - Dictionary Practice Exercises
# Complete these exercises to master Python dictionaries!

# ============================================================================
# INITIAL PIPELINE DATA
# ============================================================================

pipeline = {
    "build": {
        "status": "success",
        "duration": "2m 15s",
        "timestamp": "2025-12-20 10:30:00",
        "logs_url": "https://ci.example.com/logs/build/123"
    },
    "test": {
        "status": "success",
        "duration": "5m 30s",
        "timestamp": "2025-12-20 10:35:00",
        "logs_url": "https://ci.example.com/logs/test/123"
    },
    "security_scan": {
        "status": "failed",
        "duration": "3m 20s",
        "timestamp": "2025-12-20 10:40:00",
        "logs_url": "https://ci.example.com/logs/security/123"
    },
    "deploy": {
        "status": "pending",
        "duration": None,
        "timestamp": None,
        "logs_url": None
    }
}

# ============================================================================
# EXERCISE 1: Basic Access and Modification
# ============================================================================
print("=" * 60)
print("EXERCISE 1: Basic Access and Modification")
print("=" * 60)

# TODO 1.1: Print the status of the "build" stage
pipe_build_status = pipeline["build"]["status"]
print (f'The status of the "build" stage of Pipeline is : {pipe_build_status}')

# The status of the "build" stage of Pipeline is : success


# TODO 1.2: Print the duration of the "test" stage

pipe_test_duration = pipeline["test"]["duration"]
print (f'The status of the "build" stage of Pipeline is : {pipe_test_duration}')

# The status of the "build" stage of Pipeline is : 5m 30s


# TODO 1.3: Update the "deploy" stage status to "running"

pipe_build_status = pipeline["build"]["status"]
print (f'Current status of Build stage of Pipeline - "{pipe_build_status}"')

# Current status of Build stage of Pipeline - "success"

pipeline["build"]["status"] = "running"
pipe_build_status_updated = pipeline["build"]["status"]
print (f'Current status of Build stage of Pipeline after Updated - "{pipe_build_status_updated}"')

# Current status of Build stage of Pipeline after Updated - "running"




# TODO 1.4: Add a new key "started_by" with value "jenkins" to the "build" stage

pipe_build_dict = pipeline["build"]
print (f'Current status of Build stage of Pipeline - \n {pipe_build_dict}')

# Current status of Build stage of Pipeline -
# {'status': 'running', 'duration': '2m 15s', 'timestamp': '2025-12-20 10:30:00', 'logs_url': 'https://ci.example.com/logs/build/123'}
 
pipe_build_dict.update({'started_by': 'jenkins'})

print (f'Updated a new key "started_by" with value "jenkins" to the "build" stage: \n\n {pipe_build_dict}')

Updated a new key "started_by" with value "jenkins" to the "build" stage:

# {'status': 'running', 'duration': '2m 15s', 'timestamp': '2025-12-20 10:30:00', 'logs_url': 'https://ci.example.com/logs/build/123', 'started_by': 'jenkins'}


# TODO 1.5: Print the entire "security_scan" stage dictionary

pipe_sec_scan = pipeline["security_scan"]
print(f'The Current entire "security_scan" stage dictionary {pipe_sec_scan}')

# The Current entire "security_scan" stage dictionary {'status': 'failed', 'duration': '3m 20s', 'timestamp': '2025-12-20 10:40:00', 'logs_url': 'https://ci.example.com/logs/security/123'}


print("\n")

# ============================================================================
# EXERCISE 2: Using get() method safely
# ============================================================================
print("=" * 60)
print("EXERCISE 2: Using get() Method")
print("=" * 60)

# TODO 2.1: Get the duration of "deploy" stage using get() with a default value "Not started"
# .get(key)   does not throw key error, it returns None

pipe_build_dict = pipeline["build"]
pipe_build_dict_duration = pipe_build_dict.get("duration","Not started")
print (f'The duration of "deploy" stage using get method : {pipe_build_dict_duration}')

# The duration of "deploy" stage using get method : 2m 15s



# TODO 2.2: Try to get a non-existent stage "package" using get() with default "Stage not found"

pipe_get_error_check = pipeline.get("package","Not started")
print (f'The non-existent  of "package" stage from Pipeline retrieve using get method : {pipe_get_error_check}')

# The non-existent  of "package" stage from Pipeline retrieve using get method : Not started


# TODO 2.3: Get the "error_message" from "security_scan" stage with default "No error message"

pipe_sec_scan_dict = pipeline["security_scan"]
pipe_check_sec_scan = pipe_sec_scan_dict.get("location","No error message")
print (f'The non-existent action from "security_scan" stage Pipeline retrieve using get method : {pipe_check_sec_scan}')

# The non-existent action from "security_scan" stage Pipeline retrieve using get method : No error message


# TODO 2.4: Check if "build" stage has "retry_count" key, if not, set it to 0

def check_update_build_stage(pipeline: dict):
    pipe_build_dict = pipeline["build"]
    
    for action in pipe_build_dict:
        if action == "retry_count":
            return f"Found retry_count at 'Build' stage"
    pipeline["build"]["retry_count"] = 0
    return pipeline["build"]
    
check_update_build_stage(pipeline)

# {'status': 'running', 'duration': '2m 15s', 'timestamp': '2025-12-20 10:30:00', 'logs_url': 'https://ci.example.com/logs/build/123', 'retry_count': 0}

check_update_build_stage(pipeline)
# "Found retry_count at 'Build' stage"



print("\n")

# ============================================================================
# EXERCISE 3: Looping through dictionaries
# ============================================================================
print("=" * 60)
print("EXERCISE 3: Looping Through Dictionaries")
print("=" * 60)

# TODO 3.1: Print all stage names (keys only)
pipeline.keys()

#dict_keys(['build', 'test', 'security_scan', 'deploy'])


# TODO 3.2: Print all stage statuses (values only - just the status field)

def print_dict_value_status(pipeline: dict):

    for key_1, value_1 in pipeline.items():
        for key, value in value_1.items():
            if key == "status":
                print(f"{key_1} stage's  {key} is : {value}")


print_dict_value_status(pipeline)

# build stage's  status is : success
# test stage's  status is : success
# security_scan stage's  status is : failed
# deploy stage's  status is : pending


# TODO 3.3: Print stage name and status using items()

def print_dict_key_value_status(pipeline: dict):

    for key,value in pipeline.items():
        print(key, value)

print_dict_value_status(pipeline)

"""
print_dict_key_value_status(pipeline)

build {'status': 'success', 'duration': '2m 15s', 'timestamp': '2025-12-20 10:30:00', 'logs_url': 'https://ci.example.com/logs/build/123'}
test {'status': 'success', 'duration': '5m 30s', 'timestamp': '2025-12-20 10:35:00', 'logs_url': 'https://ci.example.com/logs/test/123'}
security_scan {'status': 'failed', 'duration': '3m 20s', 'timestamp': '2025-12-20 10:40:00', 'logs_url': 'https://ci.example.com/logs/security/123'}
deploy {'status': 'pending', 'duration': None, 'timestamp': None, 'logs_url': None}

"""

# TODO 3.4: Print all stages with their complete information in a formatted way

def print_dict_key_value_status(pipeline: dict):

    for key,value in pipeline.items():
        print(json.dumps ((key, value), indent=4))

print_dict_value_status(pipeline)

"""
print_dict_key_value_status(pipeline)

[
    "build",
    {
        "status": "success",
        "duration": "2m 15s",
        "timestamp": "2025-12-20 10:30:00",
        "logs_url": "https://ci.example.com/logs/build/123"
    }
]
[
    "test",
    {
        "status": "success",
        "duration": "5m 30s",
        "timestamp": "2025-12-20 10:35:00",
        "logs_url": "https://ci.example.com/logs/test/123"
    }
]
[
    "security_scan",
    {
        "status": "failed",
        "duration": "3m 20s",
        "timestamp": "2025-12-20 10:40:00",
        "logs_url": "https://ci.example.com/logs/security/123"
    }
]
[
    "deploy",
    {
        "status": "pending",
        "duration": null,
        "timestamp": null,
        "logs_url": null
    }
]
"""


print("\n")

# ============================================================================
# EXERCISE 4: Checking existence with 'in' operator
# ============================================================================
print("=" * 60)
print("EXERCISE 4: Checking Existence")
print("=" * 60)

# TODO 4.1: Check if "test" stage exists in pipeline

pipeline.keys()

# dict_keys(['build', 'test', 'security_scan', 'deploy'])

# TODO 4.2: Check if "integration_test" stage exists

def check_stage_int_test(pipeline: dict):
    pipeline_keys = pipeline.keys()
    
    if "integration_test" in pipeline_keys:
        print ("Yes, 'integration_test' stage exists in Pipeline")
    print("No, 'integration_test' stage is NOT exists in Pipeline")

check_stage_int_test(pipeline)

# No, 'integration_test' stage is NOT exists in Pipeline

# TODO 4.3: Check if "build" stage has a "timestamp" key
def pipeline_build_timestamp (pipeline: dict):
    pipe_build_dict = pipeline["build"]

    for key in pipe_build_dict:
        if key == "timestamp":
            return f"Yes, the Build stage has got 'timestamp' detail in it"
    return f"Sorry, the Build stage has NOT got 'timestamp' detail in it"

pipeline_build_timestamp (pipeline)

# "Yes, the Build stage has got 'timestamp' detail in it"

# TODO 4.4: Check if "deploy" stage has "error_message" key

def pipeline_deploy_err_msg(pipeline: dict):
    pipe_deploy_dict = pipeline["deploy"]

    for key in pipe_deploy_dict:
        if key == "error_message":
            return f"Yes, the deploy stage has got 'error_message' detail in it"
    return f"Sorry, the deploy stage has NOT got 'error_message' detail in it"


pipeline_deploy_err_msg(pipeline)

# "Sorry, the deploy stage has NOT got 'error_message' detail in it"     


print("\n")

# ============================================================================
# EXERCISE 5: Adding new stages and nested data
# ============================================================================
print("=" * 60)
print("EXERCISE 5: Adding New Stages")
print("=" * 60)

# TODO 5.1: Add a new stage "integration_test" with status "pending", duration None


# TODO 5.2: Add a nested dictionary "artifacts" to "build" stage with keys:
#           "binary": "app.jar", "size_mb": 45.2


# TODO 5.3: Add a list of "failed_tests" to "test" stage: ["test_login", "test_api"]


# TODO 5.4: Create a complete new stage "performance_test" with all fields


print("\n")

# ============================================================================
# EXERCISE 6: Updating and modifying values
# ============================================================================
print("=" * 60)
print("EXERCISE 6: Updating Values")
print("=" * 60)

# TODO 6.1: Update "security_scan" status from "failed" to "success"


# TODO 6.2: Update multiple fields at once using update() method for "deploy" stage
#           Set: status="success", duration="1m 30s", timestamp="2025-12-20 10:45:00"


# TODO 6.3: Increment a retry_count for "security_scan" (if it doesn't exist, start at 1)


# TODO 6.4: Add 30 seconds to the test duration (convert "5m 30s" to seconds, add 30, convert back)
#           Hint: This is challenging! Parse the string first


print("\n")

# ============================================================================
# EXERCISE 7: Removing items from dictionaries
# ============================================================================
print("=" * 60)
print("EXERCISE 7: Removing Items")
print("=" * 60)

# TODO 7.1: Remove the "integration_test" stage using del


# TODO 7.2: Remove and return the "logs_url" from "build" stage using pop()


# TODO 7.3: Remove "failed_tests" from "test" stage using pop() with a default value


# TODO 7.4: Remove the last inserted stage using popitem() (Python 3.7+)


print("\n")

# ============================================================================
# EXERCISE 8: Copying dictionaries
# ============================================================================
print("=" * 60)
print("EXERCISE 8: Copying Dictionaries")
print("=" * 60)

# TODO 8.1: Create a shallow copy of pipeline called pipeline_backup


# TODO 8.2: Modify the original pipeline and observe the backup
#           Change build status to "failed" in original


# TODO 8.3: Create a deep copy using copy.deepcopy (import copy first)


# TODO 8.4: Modify nested data in original and check if deep copy is affected


print("\n")

# ============================================================================
# EXERCISE 9: Dictionary comprehensions
# ============================================================================
print("=" * 60)
print("EXERCISE 9: Dictionary Comprehensions")
print("=" * 60)

# TODO 9.1: Create a new dict with only stage names and their statuses


# TODO 9.2: Create a dict of only failed stages (status == "failed")


# TODO 9.3: Create a dict with stages that have duration (duration is not None)


# TODO 9.4: Create a dict with stage names in uppercase as keys


print("\n")

# ============================================================================
# EXERCISE 10: Working with nested dictionaries
# ============================================================================
print("=" * 60)
print("EXERCISE 10: Nested Dictionary Operations")
print("=" * 60)

# Add some test data for this section
pipeline["build"]["metrics"] = {
    "code_coverage": 85.5,
    "test_pass_rate": 98.2,
    "build_size_mb": 120
}

pipeline["test"]["metrics"] = {
    "tests_total": 450,
    "tests_passed": 442,
    "tests_failed": 8
}

# TODO 10.1: Access the code_coverage from build metrics


# TODO 10.2: Add a new metric "vulnerability_count": 3 to security_scan


# TODO 10.3: Calculate total tests run across all stages that have metrics


# TODO 10.4: Print all stages that have metrics


print("\n")

# ============================================================================
# EXERCISE 11: setdefault() method
# ============================================================================
print("=" * 60)
print("EXERCISE 11: Using setdefault()")
print("=" * 60)

# TODO 11.1: Use setdefault to add "environment" key to build stage with default "production"


# TODO 11.2: Use setdefault to ensure "deploy" has a "rollback_enabled" key (default: True)


# TODO 11.3: Use setdefault to add an empty list "warnings" to test stage


# TODO 11.4: Try setdefault on a key that already exists and observe behavior


print("\n")

# ============================================================================
# EXERCISE 12: keys(), values(), items() methods
# ============================================================================
print("=" * 60)
print("EXERCISE 12: Dictionary View Objects")
print("=" * 60)

# TODO 12.1: Get all stage names using keys() and convert to a list


# TODO 12.2: Get all stage info dictionaries using values()


# TODO 12.3: Use items() to iterate and print stage name with its status


# TODO 12.4: Find the stage with longest duration (parse duration strings)


print("\n")

# ============================================================================
# EXERCISE 13: Merging dictionaries
# ============================================================================
print("=" * 60)
print("EXERCISE 13: Merging Dictionaries")
print("=" * 60)

default_stage_config = {
    "timeout": "10m",
    "retry_count": 3,
    "notify_on_failure": True
}

custom_config = {
    "timeout": "15m",
    "parallel": True
}

# TODO 13.1: Merge default_stage_config with custom_config using update()


# TODO 13.2: Merge using the ** unpacking operator (create new dict)


# TODO 13.3: Merge using | operator (Python 3.9+)


# TODO 13.4: Apply merged config to all pipeline stages


print("\n")

# ============================================================================
# EXERCISE 14: Complex nested operations
# ============================================================================
print("=" * 60)
print("EXERCISE 14: Complex Operations")
print("=" * 60)

# Add execution history
pipeline["build"]["execution_history"] = [
    {"run_id": 1, "status": "success", "duration": "2m 10s"},
    {"run_id": 2, "status": "failed", "duration": "1m 30s"},
    {"run_id": 3, "status": "success", "duration": "2m 15s"}
]

# TODO 14.1: Get the latest execution status from build history (last item)


# TODO 14.2: Count how many times build was successful in history


# TODO 14.3: Add a new execution to the history


# TODO 14.4: Find average duration from execution history (parse durations)


print("\n")

# ============================================================================
# EXERCISE 15: Real-world scenarios
# ============================================================================
print("=" * 60)
print("EXERCISE 15: Real-World Scenarios")
print("=" * 60)

# TODO 15.1: Create a function to get pipeline health status
#            Return "healthy" if all stages are success, "unhealthy" if any failed
def get_pipeline_health(pipeline):
    pass


# TODO 15.2: Create a function to calculate total pipeline duration
def calculate_total_duration(pipeline):
    # Parse duration strings and sum them up (skip None values)
    pass


# TODO 15.3: Create a function to generate a summary report
def generate_summary_report(pipeline):
    # Print: Total stages, Success count, Failed count, Pending count
    pass


# TODO 15.4: Create a function to find bottleneck stage (longest duration)
def find_bottleneck_stage(pipeline):
    pass


# TODO 15.5: Create a function to retry failed stages
def retry_failed_stages(pipeline):
    # Set status to "running" for all failed stages
    pass


print("\n")

# ============================================================================
# EXERCISE 16: Advanced - Working with multiple pipelines
# ============================================================================
print("=" * 60)
print("EXERCISE 16: Multiple Pipelines")
print("=" * 60)

pipelines = {
    "pipeline_123": pipeline,
    "pipeline_124": {
        "build": {"status": "success", "duration": "1m 45s"},
        "test": {"status": "running", "duration": None},
        "deploy": {"status": "pending", "duration": None}
    },
    "pipeline_125": {
        "build": {"status": "failed", "duration": "3m 10s"},
        "test": {"status": "pending", "duration": None}
    }
}

# TODO 16.1: Count total number of stages across all pipelines


# TODO 16.2: Find all pipelines with at least one failed stage


# TODO 16.3: Get average build duration across all pipelines


# TODO 16.4: Create a summary dict: {pipeline_id: overall_status}


print("\n")

# ============================================================================
# BONUS EXERCISES: Challenge Problems
# ============================================================================
print("=" * 60)
print("BONUS EXERCISES")
print("=" * 60)

# BONUS 1: Create a function to compare two pipeline runs
def compare_pipeline_runs(run1, run2):
    # Return a dict showing what changed between runs
    pass


# BONUS 2: Create a function to validate pipeline structure
def validate_pipeline_structure(pipeline):
    # Check if all required keys exist (status, duration, timestamp, logs_url)
    pass


# BONUS 3: Create a pipeline configuration generator
def create_pipeline_template(stages_list):
    # Given a list of stage names, create a pipeline dict with default values
    pass


# BONUS 4: Implement a stage dependency checker
def check_dependencies(pipeline, stage_dependencies):
    # stage_dependencies = {"deploy": ["build", "test"], "test": ["build"]}
    # Check if all dependencies are successful before running a stage
    pass


print("\n")
print("=" * 60)
print("EXERCISES COMPLETE!")
print("=" * 60)
print("Now try solving these exercises one by one.")
print("Start with Exercise 1 and work your way up!")
print("Don't forget to test your solutions by runn
