token="$1"
org="$2"
command="$3"

if [ "$command" = "createchannel" ]
then
	curl -s -X POST \
	  http://localhost:4000/channels \
	  -H "authorization: Bearer $token" \
	  -H "content-type: application/json" \
	  -d '{
		"channelName":"mychannel",
		"channelConfigPath":"../../channel-artifacts/channel.tx"
	}'

	sleep 5
fi


if [ "$command" = "joinchannel" ]
then
	curl -s -X POST \
	  http://localhost:4000/channels/mychannel/peers \
	  -H "authorization: Bearer $token" \
	  -H "content-type: application/json" \
	  -d '{
		"peers": ["peer0.'$org'.example.com","peer1.'$org'.example.com"]
	}'
fi

if [ "$command" = "updateanchorpeers" ]
then
	curl -s -X POST \
	  http://localhost:4000/channels/mychannel/anchorpeers \
	  -H "authorization: Bearer $token" \
	  -H "content-type: application/json" \
	  -d '{
		"configUpdatePath":"../../channel-artifacts/'$org'anchors.tx"
	}'
fi

CC_SRC_PATH="$PWD/chaincode/chain_person"
CC_CCP_PATH="$PWD/chaincode/chain_person/collections_config.json"
LANGUAGE="node"

if [ "$command" = "installchaincode" ]
then
	curl -s -X POST \
	  http://localhost:4000/chaincodes \
	  -H "authorization: Bearer $token" \
	  -H "content-type: application/json" \
	  -d "{
		\"peers\": [\"peer0.$org.example.com\",\"peer1.$org.example.com\"],
		\"chaincodeName\":\"chainv1_3\",
		\"chaincodePath\":\"$CC_SRC_PATH\",
		\"chaincodeType\": \"$LANGUAGE\",
		\"chaincodeVersion\":\"1.0\"
	}"
fi

if [ "$command" = "instantiatechaincode" ]
then
	curl -s -X POST \
	  http://localhost:4000/channels/mychannel/chaincodes \
	  -H "authorization: Bearer $token" \
	  -H "content-type: application/json" \
	  -d "{
	  \"peers\": [\"peer0.$org.example.com\"],
		\"chaincodeName\":\"chainv1_3\",
		\"chaincodeVersion\":\"1.0\",
		\"chaincodeType\": \"$LANGUAGE\",
		\"args\":[\"init\"],
	  \"collectionsConfig\":\"$CC_CCP_PATH\"
	}"
fi