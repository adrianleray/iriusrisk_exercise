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

# How-to
## API 
https://fmmamnf131.execute-api.eu-west-3.amazonaws.com/process-text
Example with cURL:
curl -X POST https://fmmamnf131.execute-api.eu-west-3.amazonaws.com/process-text -data "text"
