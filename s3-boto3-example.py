def lambda_handler(event, context):
    # TODO implement
    import boto3
    s3 = boto3.client('s3')
    data = s3.get_object(Bucket = Bucket='your_bucket_name_here', Key='your_key_name_here')
    contents = data['Body'].read()
    print(contents)







 
