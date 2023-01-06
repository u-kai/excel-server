#!/bin/bash

PORT = 5051
# start server
dist/main PORT

# run client
./client/target/release/client PORT
