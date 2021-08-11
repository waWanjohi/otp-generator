# List the topics on a container
# Usage: ./list.sh -n <container_name> 

while getopts n: flag
do
    case "${flag}" in
        n) name=${OPTARG};;
    esac
done
echo "Showing topics in $name ..."
docker exec -it $name kafka-topics.sh --list --bootstrap-server :9092