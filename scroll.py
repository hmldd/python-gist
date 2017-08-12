# coding:utf-8

from elasticsearch import Elasticsearch
import json

# Define config
host = "127.0.0.1"
port = 9202
timeout = 1000
index = "index"
doc_type = "type"
size = 1000
body = {}

# Init Elasticsearch instance
es = Elasticsearch(
    [
        {
            'host': host,
            'port': port
        }
    ],
    timeout=timeout
)


# Process hits here
def process_hits(hits):
    for item in hits:
        print(json.dumps(item, indent=2))


# Check index exists
if not es.indices.exists(index=index):
    print("Index " + index + " not exists")
    exit()

# Init scroll by search
data = es.search(
    index=index,
    doc_type=doc_type,
    scroll='2m',
    size=size,
    body=body
)

# Get the scroll ID
sid = data['_scroll_id']
scroll_size = len(data['hits']['hits'])

# Before scroll, process current batch of hits
process_hits(data['hits']['hits'])

while scroll_size > 0:
    "Scrolling..."
    data = es.scroll(scroll_id=sid, scroll='2m')

    # Process current batch of hits
    process_hits(data['hits']['hits'])

    # Update the scroll ID
    sid = data['_scroll_id']

    # Get the number of results that returned in the last scroll
    scroll_size = len(data['hits']['hits'])
