### Setup

There are a few typical libraries that one might use while solving Cryptography challenges

```bash
# used for connecting to server
python3 -m pip install pwntools

# used for generating primes, converting numbers to bytes and vice versa
# also used for generating encryptions of common standards
python3 -m pip install pycryptodome

# similar to above, but the syntax can be a bit nicer
python3 -m pip install libnum
```

### Verification

If you can run the following code in your python environment, you are good to go

```py

from pwn import *
from Crypto.Util.number import *
from libnum import *


```
