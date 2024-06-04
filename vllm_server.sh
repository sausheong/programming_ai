sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 5000
python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 5000 --model meta-llama/Meta-Llama-3-8B-Instruct --api-key abc123

python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 5000 --model casperhansen/llama-3-8b-instruct-awq --api-key abc123
