import json


def main():
    # Store JSON-format string
    api_response = """
    {
        "id": "req_123",
        "status": "success",
        "result": {
            "text": "Hello world",
            "confidence": 0.98
        }
    }
    """

    # JSON string into Python object
    data = json.loads(api_response)

    # Extracting required values
    request_id = data["id"]
    status = data["status"]
    text_result = data["result"]["text"]
    confidence_score = data["result"]["confidence"]

    # Print extracted values
    print("Request ID:", request_id)
    print("Status:", status)
    print("Text:", text_result)
    print("Confidence:", confidence_score)

    # Check confidence threshold
    if confidence_score < 0.9:
        print("⚠ Warning: Confidence score is below 0.9")

    # Create follow-up dictionary and convert to JSON
    follow_up_result = {
        "request_id": request_id,
        "processed": True,
        "confidence_checked": confidence_score >= 0.9
    }

    json_output = json.dumps(follow_up_result, indent=4)

    # Write JSON output to file
    with open("response.json", "w") as file:
        file.write(json_output)


if __name__ == "__main__":
    main()