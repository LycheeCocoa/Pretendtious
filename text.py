import boto3

client = boto3.client(
    "sns",
    aws_access_key_id="AKIAJOD3QFUXOUAZOIDA",
    aws_secret_access_key="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",
    region_name="us-east-1"
)

if __name__ == "__main__":

    client.publish(
        PhoneNumber="+12512293283",
        Message ="Fruit saslad, yummy yummy."
    )


