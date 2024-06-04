sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 5000
volume=$PWD/data
model=meta-llama/Meta-Llama-3-8B-Instruct
token=<your huggingface token>
docker run \
    --gpus all \
    --shm-size 1g \
    --env HUGGING_FACE_HUB_TOKEN=$token \
    --publish 5000:80 \
    --volume $volume:/data ghcr.io/huggingface/text-generation-inference:2.0 \
    --model-id $model