### Setup

Usually for binary exploitation, you need a Linux VM, which if you're on a windows can be accessed via Windows Subsystem for Linux (WSL), or any other VM provider, like Virtual Box. 

For me, I prefer using Kali Linux because its designed for offensive security already and has some useful tools inside it.

There are a whole bunch of tools that make solving pwn challenges less pain, but the most important is `pwntools`, which helps you craft payloads, and interact with local executables and remote servers.

install it with 

```bash
python3 -m pip install pwntools
```

To find out more, you can check out my [notes on github](https://github.com/jontay999/binary-exploitation) (which is actually pretty mediocre) but other good online resources can just be found by doing a [google search](https://www.google.com/search?q=binary+exploitation+beginner)