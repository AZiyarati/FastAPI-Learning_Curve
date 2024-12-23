# env
# You could create an env var MY_NAME withexport MY_NAME="Wade Wilson"
# Then you could use it with other programs, likeecho "Hello $MY_NAME"
# Hello Wade Wilson


# Read env vars in Python
import os

name = os.getenv("MY_NAME", "World")
print(f"Hello {name} from Python")

# By default it reutrns None, in this case "World" is the default value.
