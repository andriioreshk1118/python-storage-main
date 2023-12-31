#!/usr/bin/env python

# Copyright 2020 Google Inc. All Rights Reserved.
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

# [START storage_set_metadata]
from google.cloud import storage


def set_blob_metadata(bucket_name, blob_name):
    """Set a blob's metadata."""
    # bucket_name = 'your-bucket-name'
    # blob_name = 'your-object-name'

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.get_blob(blob_name)
    metageneration_match_precondition = None

    # Optional: set a metageneration-match precondition to avoid potential race
    # conditions and data corruptions. The request to patch is aborted if the
    # object's metageneration does not match your precondition.
    metageneration_match_precondition = blob.metageneration

    metadata = {'color': 'Red', 'name': 'Test'}
    blob.metadata = metadata
    blob.patch(if_metageneration_match=metageneration_match_precondition)

    print(f"The metadata for the blob {blob.name} is {blob.metadata}")


# [END storage_set_metadata]

if __name__ == "__main__":
    set_blob_metadata(bucket_name=sys.argv[1], blob_name=sys.argv[2])
