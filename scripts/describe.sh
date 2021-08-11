# Quickly describe a topic for a kafka container
# Usage: ./describe.sh -n <topic_name> -c <container_name>


while getopts n:c: flag
do
    case "${flag}" in
        n) name=${OPTARG};;
        c) container=${OPTARG};;
    esac
done
echo "Describe topic $name on $container"

docker exec -it $container kafka-topics.sh --bootstrap-server :9092 --describe --topic $name