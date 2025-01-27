import boto3
import json


def main():
    boto_client = boto3.client(
        service_name="bedrock",
        region_name="us-east-1",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    bedrock_client = boto3.client(
        service_name="bedrock-runtime",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-east-1",
    )
    model_id = "us.anthropic.claude-3-5-sonnet-20241022-v2:0"

    chart_data = """

    """

    explanation = """

    """

    prompt = f"
      """

    payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 256,
    }

    response = bedrock_client.invoke_model(
        modelId=model_id,
        body=json.dumps(payload),
    )

    response_body = json.loads(response.get("body").read())
    result = response_body.get("completion")

    print(result)
    print(response_body)


if __name__ == "__main__":
    main()
