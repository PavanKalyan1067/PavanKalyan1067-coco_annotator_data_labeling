from google.cloud import storage

def upload_files_to_gcs(bucket_name, local_files, remote_directory):
    """Uploads multiple files to a specified GCS bucket."""
    Client = storage.Client.from_service_account_json(json_credentials_path='processed images\elevated-column-383306-2621b634ed67.json')

    # storage_client = storage.Client()
    bucket = Client.bucket(bucket_name)
    
    for local_file in local_files:
        blob_name = f"{remote_directory}/{local_file}"
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(local_file)
        
        print(f"Uploaded file: {local_file} to GCS: {blob_name}")
    
    print("Upload completed.")

# Specify the GCS bucket name
bucket_name = "processingcocojsonfile"

# Specify the local files to upload
local_files = [
'Vehicle image-11.json'
]

# Specify the remote directory in the GCS bucket
remote_directory = "coco_json_output_of_vehicle_images"

# Call the function to upload files to GCS
upload_files_to_gcs(bucket_name, local_files, remote_directory)
