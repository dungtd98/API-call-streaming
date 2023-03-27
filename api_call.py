import requests
import json
import sseclient
API_KEY = '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'

def performRequestWithStreaming(model, prompt, max_tokens, temperature, stream=True):
    reqURL = 'https://api.openai.com/v1/completions'
    reqHeaders ={
        'Accept':'text/event-stream',
        'Authorization':'Bearer '+ API_KEY
    } 
    reqBody = {
        'model':model,
        'prompt':prompt,
        'max_tokens':max_tokens,
        'temperature':temperature,
        "stream":stream
    }
    req = requests.post(reqURL, headers= reqHeaders, json=reqBody, stream=True)
    print(req)
    client = sseclient.SSEClient(req)
    for event in client.events():
        if event.data !='[DONE]':
            print(json.loads(event.data)['choices'][0]['text'], end='', flush=True)
if __name__ == '__main__':
    performRequestWithStreaming(
        model='text-davinci-003',
        prompt='What is python?',
        max_tokens=100,
        temperature=0.5,
        stream=True
    )