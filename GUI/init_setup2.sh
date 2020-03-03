#!/bin/bash
#
# Copyright IBM Corp. All Rights Reserved.
#
# SPDX-License-Identifier: Apache-2.0

airport_client="$1"
ccd_client="$2"
users_client="$3"

CC_SRC_PATH="$PWD/chaincode/chain_person01"
CC_CCP_PATH="$PWD/chaincode/chain_person01/collections_config.json"
LANGUAGE="node"
chaincodeName="testv5"

ORG1_TOKEN=$(curl -s -X POST \
  http://localhost:4000/users \
  -H "content-type: application/x-www-form-urlencoded" \
  -d 'username='$airport_client'&orgName=airport')
ORG1_TOKEN=$(echo $ORG1_TOKEN | jq ".token" | sed "s/\"//g")
echo $ORG1_TOKEN

ORG2_TOKEN=$(curl -s -X POST \
  http://localhost:4000/users \
  -H "content-type: application/x-www-form-urlencoded" \
  -d 'username='$ccd_client'&orgName=ccd')
ORG2_TOKEN=$(echo $ORG2_TOKEN | jq ".token" | sed "s/\"//g")
echo $ORG2_TOKEN

ORG3_TOKEN=$(curl -s -X POST \
  http://localhost:4000/users \
  -H "content-type: application/x-www-form-urlencoded" \
  -d 'username='$users_client'&orgName=users')
ORG3_TOKEN=$(echo $ORG3_TOKEN | jq ".token" | sed "s/\"//g")
echo $ORG3_TOKEN

 # "POST request Create channel  ..."
curl -s -X POST \
  http://localhost:4000/channels \
  -H "authorization: Bearer $ORG3_TOKEN" \
  -H "content-type: application/json" \
  -d '{
	"channelName":"mychannel",
	"channelConfigPath":"../../channel-artifacts/channel.tx"
}'

sleep 1

# "POST request Join channel on Airport"
curl -s -X POST \
  http://localhost:4000/channels/mychannel/peers \
  -H "authorization: Bearer $ORG1_TOKEN" \
  -H "content-type: application/json" \
  -d '{
	"peers": ["peer0.airport.example.com","peer1.airport.example.com"]
}'


 # "POST request Join channel on CCD"

curl -s -X POST \
  http://localhost:4000/channels/mychannel/peers \
  -H "authorization: Bearer $ORG2_TOKEN" \
  -H "content-type: application/json" \
  -d '{
	"peers": ["peer0.ccd.example.com","peer1.ccd.example.com"]
}'

# "POST request Join channel on Users"

curl -s -X POST \
  http://localhost:4000/channels/mychannel/peers \
  -H "authorization: Bearer $ORG3_TOKEN" \
  -H "content-type: application/json" \
  -d '{
  "peers": ["peer0.users.example.com","peer1.users.example.com"]
}'

# "POST request Update anchor peers on Airport"

curl -s -X POST \
  http://localhost:4000/channels/mychannel/anchorpeers \
  -H "authorization: Bearer $ORG1_TOKEN" \
  -H "content-type: application/json" \
  -d '{
	"configUpdatePath":"../../channel-artifacts/airportanchors.tx"
}'


# "POST request Update anchor peers on CCD"

curl -s -X POST \
  http://localhost:4000/channels/mychannel/anchorpeers \
  -H "authorization: Bearer $ORG2_TOKEN" \
  -H "content-type: application/json" \
  -d '{
	"configUpdatePath":"../../channel-artifacts/ccdanchors.tx"
}'

# "POST request Update anchor peers on Users"

curl -s -X POST \
  http://localhost:4000/channels/mychannel/anchorpeers \
  -H "authorization: Bearer $ORG3_TOKEN" \
  -H "content-type: application/json" \
  -d '{
  "configUpdatePath":"../../channel-artifacts/usersanchors.tx"
}'

# "POST Install chaincode on Airport"

curl -s -X POST \
  http://localhost:4000/chaincodes \
  -H "authorization: Bearer $ORG1_TOKEN" \
  -H "content-type: application/json" \
  -d "{
	\"peers\": [\"peer0.airport.example.com\",\"peer1.airport.example.com\"],
	\"chaincodeName\":\"$chaincodeName\",
	\"chaincodePath\":\"$CC_SRC_PATH\",
	\"chaincodeType\": \"$LANGUAGE\",
	\"chaincodeVersion\":\"1.0\"
}"


# "POST Install chaincode on CCD"

curl -s -X POST \
  http://localhost:4000/chaincodes \
  -H "authorization: Bearer $ORG2_TOKEN" \
  -H "content-type: application/json" \
  -d "{
  \"peers\": [\"peer0.ccd.example.com\",\"peer1.ccd.example.com\"],
  \"chaincodeName\":\"$chaincodeName\",
  \"chaincodePath\":\"$CC_SRC_PATH\",
  \"chaincodeType\": \"$LANGUAGE\",
  \"chaincodeVersion\":\"1.0\"
}"

# "POST Install chaincode on Users"

curl -s -X POST \
  http://localhost:4000/chaincodes \
  -H "authorization: Bearer $ORG3_TOKEN" \
  -H "content-type: application/json" \
  -d "{
  \"peers\": [\"peer0.users.example.com\",\"peer1.users.example.com\"],
  \"chaincodeName\":\"$chaincodeName\",
  \"chaincodePath\":\"$CC_SRC_PATH\",
  \"chaincodeType\": \"$LANGUAGE\",
  \"chaincodeVersion\":\"1.0\"
}"

 # "POST instantiate chaincode on Airport"

curl -s -X POST \
  http://localhost:4000/channels/mychannel/chaincodes \
  -H "authorization: Bearer $ORG1_TOKEN" \
  -H "content-type: application/json" \
  -d "{
  \"peers\": [\"peer0.airport.example.com\"],
	\"chaincodeName\":\"$chaincodeName\",
	\"chaincodeVersion\":\"1.0\",
	\"chaincodeType\": \"$LANGUAGE\",
	\"args\":[\"init\"],
  \"collectionsConfig\":\"$CC_CCP_PATH\"
}"