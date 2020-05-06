import os
import sys

print(sys.platform)

for k, v in os.environ.items():
    print(f"{k}={v}")
