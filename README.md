### Simple Joke ChatBot
**1. Clone Project**:
```bash
git clone https://github.com/n-theo/ChatBot.git
cd ChatBot
```
**2. Install dependencies:**
```bash
pip install -r requirements.txt
```
**3. Download and spin up Milvus:**
```bash
curl -O https://github.com/milvus-io/milvus/releases/download/v2.3.0/docker-compose.yml
docker-compose up -d
```
Alternatively, on Windows follow the instructions [here](https://milvus.io/docs/v2.1.x/check_collection.md)

**4. Run application:**
```bash
cd src
python run.py
```
