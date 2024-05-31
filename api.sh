host="--host 0.0.0.0"
port="--port 7000"

while getopts h:p:r: flag
do
    case "${flag}" in
        h) host="--host ${OPTARG}";;
        p) port="--port ${OPTARG}";;
    esac
done
uvicorn api.app:app ${host} ${port}
