from flask import Flask, request, jsonify, render_template
import tiktoken

app = Flask(__name__)

def get_tokenizer(model):
    return tiktoken.encoding_for_model(model)

def process_text(text, tokenizer):
    ids = tokenizer.encode(text)
    tokens = [tokenizer.decode([id_]) for id_ in ids]
    return {'token_ids': ids, 'tokens': tokens}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_input():
    data = request.get_json()
    text = data.get('text', '')

    tokenizers = {
        'gpt2': get_tokenizer('gpt-2'),
        'gpt35': get_tokenizer('gpt-3.5'),
        'gpt4o': get_tokenizer('gpt-4o')
    }

    results = {}
    for key, tokenizer in tokenizers.items():
        results[key] = process_text(text, tokenizer)

    return jsonify({
        'gpt2': {
            'token_ids': f'{results["gpt2"]["token_ids"]}', 
            'tokens': f'{results["gpt2"]["tokens"]}'
        },
        'gpt35': {
            'token_ids': f'{results["gpt35"]["token_ids"]}', 
            'tokens': f'{results["gpt35"]["tokens"]}'
        },
        'gpt4o': {
            'token_ids': f'{results["gpt4o"]["token_ids"]}', 
            'tokens': f'{results["gpt4o"]["tokens"]}'
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
