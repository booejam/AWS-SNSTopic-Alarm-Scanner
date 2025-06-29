import boto3
import os

# ====== Replace this with your SNS Topic ARN 
sns_topic_arn = 'arn:aws:sns:ap-southeast-1:AccountNumber:SNSTopic'

cw = boto3.client('cloudwatch')
paginator = cw.get_paginator('describe_alarms')
alarms_with_topic = []

for page in paginator.paginate():
    for alarm in page['MetricAlarms']:
        if sns_topic_arn in alarm.get('AlarmActions', []):
            alarms_with_topic.append(alarm['AlarmName'])

output_file = 'sns_alarm_list.txt'

with open(output_file, 'w') as f:
    if alarms_with_topic:
        for name in alarms_with_topic:
            f.write(name + '\n')
        print(f"✅ Found {len(alarms_with_topic)} alarm(s) using the SNS topic.")
    else:
        f.write("No alarms found using the specified SNS topic.\n")
        print("No alarms found using the specified SNS topic.")

print(f"\n Output saved to: {output_file}")
print("📥 To download this file, click the file icon in CloudShell (left panel), then find and download:")
print(f"   {os.getcwd()}/{output_file}")
