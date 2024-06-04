# OpenAI 

curl https://api.openai.com/v1/chat/completions  \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{      
    "model": "gpt-4o",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Why is the sky blue?"
      }
    ]
}' | jq '.'
  
# VLLM

curl http://34.142.153.101/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer abc123" \
  -d '{       
    "model": "meta-llama/Meta-Llama-3-8B-Instruct",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Why is the sky blue?"
      }
    ]
  }' | jq '.'

# Ollama

curl http://localhost:11434/api/chat \
  -H "Content-Type: application/json" \
  -d '{       
    "model": "llama3",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Why is the sky blue?"
      }
    ],
    "stream": false
  }' | jq '.'


# TGI

curl http://34.142.153.101/generate \
    -H 'Content-Type: application/json' \
    -d '{
        "inputs":"Whis the sky blue?"
    }' | jq '.'
    
curl http://34.142.153.101/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{       
    "model": "meta-llama/Meta-Llama-3-8B-Instruct",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Why is the sky blue?"
      }
    ]
  }' | jq '.'    

# LLama.cpp

curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer abc123" \
  -d '{
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Why is the sky blue?"
      }
    ]
  }' | jq '.'    