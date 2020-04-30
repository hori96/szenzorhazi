# szenzorhazi

RPI:

pip3 install -r requirements.txt

Laptop:
Docker:

  docker build -t szenzor:latest .
  
  docker run --name szenzor -d -p 5000:5000 szenzor:latest


Test:

curl -X GET http://<IP>:<PORT>/temperature

curl -X POST -H "accept: */*" -H "Content-Type: application/json" -d "{\"data\":\"train\"}" http://<IP>:<PORT>/train
