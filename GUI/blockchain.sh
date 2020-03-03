#!/bin/bash

# Copyright IBM Corp. All Rights Reserved.
#
# SPDX-License-Identifier: Apache-2.0
#


ORG_TOKEN="$1"
command="$2"
search="$3"

if [ $command = "blocknum" ]
then
	VALUES=$(curl -s -X GET \
	  "http://localhost:4000/channels/mychannel/blocks/$search?peer=peer0.airport.example.com" \
	  -H "authorization: Bearer $ORG_TOKEN" \
	  -H "content-type: application/json")
	echo $VALUES | jq '.header.data_hash'
fi

if [ $command = "blocktx" ]
then
	VALUES=$(curl -s -X GET http://localhost:4000/channels/mychannel/transactions/$search?peer=peer0.airport.example.com \
	  -H "authorization: Bearer $ORG_TOKEN" \
	  -H "content-type: application/json")
	echo $VALUES
fi

if [ $command = "chaininfo" ]
then
	VALUES=$(curl -s -X GET \
	  "http://localhost:4000/channels/mychannel?peer=peer0.airport.example.com" \
	  -H "authorization: Bearer $ORG_TOKEN" \
	  -H "content-type: application/json")
	echo $VALUES
fi