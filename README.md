will loop to try and pull all mod ugc's from a broken shack server then remove them loops delay is asjustable and add password ect in config.py 

install 

```
cd ~

git clone https://github.com/JTWP-org/removeModLoop.git

pip install async-pavlov

cd removeModLoop
```


```
nano config.py
```

```
IP_ADDRESS = "127.0.0.1"
PORT = 0000
PASSWORD = "your_password_here"
DELAY = 10
```

```
cd ~/removeModLoop/
python3 modloop.py
```
