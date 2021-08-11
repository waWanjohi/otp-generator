# Quickly create a kafka topic for a specified container
# Usage: ./create.sh -n <topic_name> -c <container_name>

while getopts n:c: flag
do
    case "${flag}" in
        n) name=${OPTARG};;
        c) container=${OPTARG};;
    esac
done
echo "Create topic $name on $container"
docker exec -it $container kafka-topics.sh --bootstrap-server :9092 --create --topic $name