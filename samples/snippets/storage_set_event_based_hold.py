#!/usr/bin/env python

# Copyright 2019 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

# [START storage_set_event_based_hold]
from google.cloud import storage


def set_event_based_hold(bucket_name, blob_name):
    """Sets a event based hold on a given blob"""
    # bucket_name = "my-bucket"
    # blob_name = "my-blob"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    metageneration_match_precondition = None

    # Optional: set a metageneration-match precondition to avoid potential race
    # conditions and data corruptions. The request to patch is aborted if the
    # object's metageneration does not match your precondition.
    blob.reload()  # Fetch blob metadata to use in metageneration_match_precondition.
    metageneration_match_precondition = blob.metageneration

    blob.event_based_hold = True
    blob.patch(if_metageneration_match=metageneration_match_precondition)

    print(f"Event based hold was set for {blob_name}")


# [END storage_set_event_based_hold]


if __name__ == "__main__":
    set_event_based_hold(bucket_name=sys.argv[1], blob_name=sys.argv[2])
