#!/bin/bash

token="$1"
command="$2"
arg="$3"

if [ $command = "revokeconsent" ]
then
	VALUES=$(curl -s -X POST \
	  http://localhost:4000/channels/mychannel/chaincodes/chainv1_3 \
	  -H "authorization: Bearer $token" \
	  -H "content-type: application/json" \
	  -d "{
	  \"peers\": [\"peer0.airport.example.com\",\"peer0.ccd.example.com\",\"peer0.users.example.com\"],
	  \"fcn\":\"revokeConsent\",
	  \"args\":[\"$arg\"]
	}")
	echo $VALUES
fi

if [ $command = "delete" ]
then
	VALUES=$(curl -s -X POST \
	  http://localhost:4000/channels/mychannel/chaincodes/chainv1_3 \
	  -H "authorization: Bearer $token" \
	  -H "content-type: application/json" \
	  -d "{
	  \"peers\": [\"peer0.airport.example.com\",\"peer0.users.example.com\"],
	  \"fcn\":\"deletePerson\",
	  \"args\":[\"$arg\"]
	}")
	echo $VALUES
fi
