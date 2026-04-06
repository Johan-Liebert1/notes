import hashlib

events = [
    b"MokList\0",
]

def sha256(x):
    return hashlib.sha256(x).digest()

# compute digests
digests = []
for i, e in enumerate(events, 1):
    d = sha256(e)
    print(f"Event {i} digest: {d.hex()}")
    digests.append(d)

# PCR replay
pcr = b"\x00" * 32
for i, d in enumerate(digests, 1):
    pcr = sha256(pcr + d)
    print(f"PCR after event {i}: {pcr.hex()}")

print("\nFinal PCR8:")
print("0x" + pcr.hex())
