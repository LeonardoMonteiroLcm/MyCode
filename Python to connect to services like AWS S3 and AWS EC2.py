import boto3

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

bucket = s3.Bucket('my-bucket')
for obj in bucket.objects.all():
    print(obj.key)
    
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    print(instance.id, instance.state)

