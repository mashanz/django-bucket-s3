from django.shortcuts import render
from app.settings import BUCKET_ACCESS_KEY, BUCKET_NAME, BUCKET_SECRET_KEY, BUCKET_URL
import boto3

# Create your views here.
def index(request):
    context = {}

    if request.method=='GET':
        return render(request, 'app_storage/index.html', context)
    
    file_to_upload = request.FILES.get('file')
    bucket_file = 'django_app/' + file_to_upload.name 

    # credentials
    session = boto3.session.Session()
    s3_client = session.client(
        service_name = 's3',
        aws_access_key_id = BUCKET_ACCESS_KEY,
        aws_secret_access_key = BUCKET_SECRET_KEY,
        endpoint_url = BUCKET_URL
    )
    
    # upload file
    s3_client.put_object(
        Key=bucket_file,
        Body=file_to_upload, 
        Bucket=BUCKET_NAME
    )
    
    context = {
        "status": "success"
    }

    return render(request, 'app_storage/index.html', context)