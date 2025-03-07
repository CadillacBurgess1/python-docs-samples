#  Copyright 2024 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# This is an ingredient file. It is not meant to be run directly. Check the samples/snippets
# folder for complete code samples that are ready to be used.
# Disabling flake8 for the ingredients file, as it would fail F821 - undefined name check.
# flake8: noqa

from google.cloud import compute_v1


# <INGREDIENT create_hyperdisk_from_pool>
def create_hyperdisk_from_pool(
    project_id: str,
    zone: str,
    disk_name: str,
    storage_pool_name: str,
    disk_size_gb: int = 100,
) -> compute_v1.Disk:
    """Creates a Hyperdisk from a specified storage pool in Google Cloud.
    Args:
        project_id (str): The ID of the Google Cloud project.
        zone (str): The zone where the disk will be created.
        disk_name (str): The name of the disk you want to create.
        storage_pool_name (str): The name of the storage pool from which the disk will be created.
        disk_size_gb (int): The size of the disk in gigabytes.
    Returns:
        compute_v1.Disk: The created disk from the storage pool.
    """
    disk = compute_v1.Disk()
    disk.zone = zone
    disk.size_gb = disk_size_gb
    disk.name = disk_name
    disk.type = f"projects/{project_id}/zones/{zone}/diskTypes/hyperdisk-balanced"
    disk.storage_pool = (
        f"projects/{project_id}/zones/{zone}/storagePools/{storage_pool_name}"
    )
    # Optional parameters
    # disk.provisioned_iops = 10000
    # disk.provisioned_throughput = 140

    disk_client = compute_v1.DisksClient()
    operation = disk_client.insert(project=project_id, zone=zone, disk_resource=disk)
    wait_for_extended_operation(operation, "disk creation")

    new_disk = disk_client.get(project=project_id, zone=zone, disk=disk.name)
    print(new_disk.status)
    print(new_disk.provisioned_iops)
    print(new_disk.provisioned_throughput)
    # Example response:
    # READY
    # 3600
    # 290

    return new_disk


# </INGREDIENT>
