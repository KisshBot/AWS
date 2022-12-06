import boto3
region = 'ap-south-1'
topic_arn = "arn:aws:sns:ap-south-1:354059899241:New-Topic"
ec2 = boto3.resource('ec2', region_name=region)
sns = boto3.client("sns", region_name=region)

def lambda_handler(event, context):
#print('Into DescribeEc2Instance')
    instances = ec2.instances.filter(Filters=[{'Name': 'tag:Scheduled', 'Values': ["True"]}])
    Ins_id = [instance.id for instance in instances]
    ec2.instances.start(InstanceIds=Ins_id)
    flag=True
    if flag:
        for server in Ins_id:
        # send sns notification
            sns.publish(TopicArn=topic_arn, Message=server+" Server started", Subject="Servers Started")
            print(server+" Server started")
