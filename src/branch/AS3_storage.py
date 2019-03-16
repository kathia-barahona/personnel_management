from storages.backends.s3boto3 import S3Boto3Storage

class FacadeImageStorage(S3Boto3Storage):
    location = 'facade_images'
    default_acl = 'public-read'
    file_overwrite = False