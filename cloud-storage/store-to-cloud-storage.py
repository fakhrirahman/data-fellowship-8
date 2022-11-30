from google.cloud import storage
import wget
import io, os
import warnings
warnings.filterwarnings("ignore", "Your application has authenticated using end user credentials")

project_id = 'df-8-370013'
bucket_name = 'data-fellowship-8-fakhri'
destination_blob_name = 'practice/covid1.csv'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="creds.json"
os.environ["GCLOUD_PROJECT"]=project_id
storage_client = storage.Client()

source_file_name = 'https://api.covidtracking.com/v1/us/20200501.csv'

def upload_blob(bucket_name, source_file_name, destination_blob_name):   
    filename = wget.download(source_file_name, 'covid.csv')

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(filename)
    os.remove(filename)

upload_blob(bucket_name, source_file_name, destination_blob_name)