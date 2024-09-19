from functions import *
import time
import datetime

print("Starting data pipeline at ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print("------------------------------------------------")

# Step 1: extract video IDs
print("Step 1: Running...")
t0 = time.time()
getVideoIDs()
t1 = time.time()
print("Step 1: Done")
print("---> Video IDs downloaded in", str(t1-t0), "seconds", "\n")

# Step 2: extract transcripts for videos
print("Step 2: Running...")
t0 = time.time()
getVideoTranscripts()
t1 = time.time()
print("Step 2: Done")
print("---> Transcripts downloaded in", str(t1-t0), "seconds", "\n")

# Step 3: Transform data
print("Step 3: Running...")
t0 = time.time()
transformData()
t1 = time.time()
print("Step 3: Done")
print("---> data Transformed in", str(t1-t0), "seconds", "\n")

# Step 4: Generate text embeddings
print("Step 4: Running...")
t0 = time.time()
createTextEmbeddings()
t1 = time.time()
print("Step 4: Done")
print("---> Embeddings generated in", str(t1-t0), "seconds", "\n")