token="$1"
org="$2"
arg="$3"
chaincodeName="testv10"

if [ \( "$org" = "airport" \) -o \( "$org" = "users" \) ]
then
	curl -s -X GET \
	  "http://localhost:4000/channels/mychannel/chaincodes/$chaincodeName?peer=peer0.airport.example.com&fcn=readPrivatePerson&args=%5B%22$arg%22%5D" \
	  -H "authorization: Bearer $token" \
	  -H "content-type: application/json"
fi

if [ "$org" = "ccd" ]
then
	curl -s -X GET \
	  "http://localhost:4000/channels/mychannel/chaincodes/$chaincodeName?peer=peer0.airport.example.com&fcn=readPerson&args=%5B%22$arg%22%5D" \
	  -H "authorization: Bearer $token" \
	  -H "content-type: application/json"
fi
