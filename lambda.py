import json
import boto3

bucket_name = "fx8574iv9k"
file_name = "result.json"

def lambda_handler(text, context):
  
    text_list = normalize(text)
    
    result_dict = {}
    
    for word in text_list:
        count_words = text_list.count(word)
        if word not in result_dict:
            result_dict[word] = count_words
            
    result_dict = sort_and_reduce(result_dict)
            
    saveS3(result_dict)
    
    return f"https://{bucket_name}.s3.eu-west-3.amazonaws.com/{file_name}"

def normalize(text):
    return text.replace('.', '').replace(',', '').split(' ')
    
def saveS3(result):
    s3 = boto3.resource("s3")
    result = s3.Bucket(bucket_name).put_object(Key=file_name, Body=json.dumps(result))
    print(result)
    
def sort_and_reduce(dict_list):
    return sorted(dict_list.items(), key=lambda item: item[1], reverse=True)[0:10]
