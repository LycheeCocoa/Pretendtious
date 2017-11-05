import boto3

# Create an SNS client
client = boto3.client(
    "sns",
    aws_access_key_id="AKIAJWF5KX6Q22U6WJCQ",
    aws_secret_access_key="Iqd0RHRK1FnzR3RyDfKS9jJZ1KbPVO0jFJAZCOD6",
    region_name="us-east-1"
)

# Send your sms message.
client.publish(
    PhoneNumber="+12512293283",
    Message ="Fruit salad, yummy yummy."
)


