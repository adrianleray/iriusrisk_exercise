# Proposal
This repository contain lambda function code to resolve technical challenge. The proposal of this repository is share lambda function code.

# Exercise
Create a serverless app and its infrastructure in AWS or GCP that will receive a POST call with
a parameter containing a text. It should save in a json file the top 10 most frequent words and
return to the user the URL to download the file.
Tell us how to access the real application so we could test it. Provide all the necessary
documentation and files so we could inspect it.
Note: You can use an AWS or GCP temporary free tier account that should stay available for 2
weeks.

# Solution
In order to bring a solution for this exercise, I create the next architecture in AWS:
|Component|Description|
|---|---|
|Lambda function|Process text and write in a file in S3 the ouput of process|
|S3 Bucket|Save and share output of landa process|
|API Gateway|Offers a interface as an API to execute lambda process|

# How-to
API request is available here:
https://fmmamnf131.execute-api.eu-west-3.amazonaws.com/process-text

Example how to send a request with cURL:
curl -X POST https://fmmamnf131.execute-api.eu-west-3.amazonaws.com/process-text -H "Content-type:text/plain" -d '"text"'

Response is a URL with output of lambda function process.
