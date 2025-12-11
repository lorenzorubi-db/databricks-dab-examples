# Install Databricks Assert Bundles package locally
# pip install databricks-bundles==0.275.0
#
# copy contents into resources/airflow_dynamic_task_mapping.py
from databricks.bundles.jobs import Job


airflow_dynamic_task_mapping = Job.from_dict(
    {
        "name": "airflow_dynamic_task_mapping",
        "tasks": [
            {
                "task_key": "extract",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/lorenzo.rubio@databricks.com/airflow/dynamic_task_mapping/get_dates",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "process_item",
                "depends_on": [
                    {
                        "task_key": "extract",
                    },
                ],
                "for_each_task": {
                    "inputs": "{{tasks.extract.values.indexes}}",
                    "concurrency": 10,
                    "task": {
                        "task_key": "process_item_iteration",
                        "notebook_task": {
                            "notebook_path": "/Workspace/Users/lorenzo.rubio@databricks.com/airflow/dynamic_task_mapping/process_item",
                            "base_parameters": {
                                "index": "{{input}}",
                            },
                            "source": "WORKSPACE",
                        },
                    },
                },
            },
        ],
        "queue": {
            "enabled": True,
        },
        "parameters": [
            {
                "name": "lookup_file_name",
                "default": "/Volumes/users/lorenzo_rubio/hotchpotch/my_file.json",
            },
        ],
        "performance_target": "PERFORMANCE_OPTIMIZED",
    }
)

