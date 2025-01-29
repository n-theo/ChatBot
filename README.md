### Simple Joke ChatBot
**1. Clone Project (If not present locally)**:
```bash
git clone https://github.com/n-theo/ChatBot.git
cd ChatBot
```
**2. Install dependencies:**
```
# Assuming they do not exist

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
**3. Download config and spin up Milvus:**
```
# Assuming docker is already installed 

curl -O https://github.com/milvus-io/milvus/releases/download/v2.5.4/docker-compose.yml
docker-compose up -d
```
Alternatively, on Windows follow the instructions [here](https://milvus.io/docs/v2.1.x/check_collection.md)

**4. Run application:**
```
# If venv is not activated
source venv/bin/activate
```
Run script:
```
cd src
python run.py
```
Running the above will prompt the user to enter a prompt. If the latter is joke related, a response will be fetched. This is determined using vector similarity

The project has a simple structure:
```
├── README.md               # Project overview and instructions (you are here now).
├── requirements.txt        # List of dependencies for the project.
└── src/
    ├── __init__.py         # Package
    ├── constants.py        # Defines constant variables
    ├── joke_fetcher.py     # Fetches random joke from API.
    ├── milvus_connector.py # Manages the connection and interactions with the Milvus database.
    ├── milvus_params.py    # Vector search related parameters.
    └── run.py              # Entry point script to execute the main functionality of the project.
```