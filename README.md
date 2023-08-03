# Chat with my data
Testing LLM models and tools to query my documents

List of free ML books: https://www.kdnuggets.com/2020/03/24-best-free-books-understand-machine-learning.html


## Setup
### Requirements
- the latest version of [WSL (Windows Subsystem for Linux)](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
- Conda as the Python environment manager: [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution)

### Steps
To run this project, follow these steps:
1. Clone the project:
  ```bash
  git clone https://github.com/matthiaskozubal/Chat_with_my_data.git
  ```
2. Navigate into the project directory:
  ```bash
  cd Chat_with_my_data
  ```
3. Create and activate a Conda environment with Python. 
  ```bash
  conda create -n chat python=3.10
  conda activate chat
  ```
4. Install Poetry, if you haven't already:
  ```bash
  curl -sSL https://install.python-poetry.org | bash
  ```
5. Install the project dependencies:
  ```bash
  <!-- poetry config virtualenvs.create True -->
  <!-- poetry env use python3.10 -->
  poetry install
  ```
6. Download the sample data
  ```bash
  wget -P data/pdfs/ https://hastie.su.domains/ISLRv2_website.pdf
  ```
7. Enter your OpenAI API key (from https://platform.openai.com/account/api-keys) to the .env file
  ```bash
  echo "OPEN_API_KEY=your_OpenAI_API_key" > .env
  ```
8. a) Run the project demo file in wsl (within the conda virtual environment):
    ```bash
    python demo.py
    ```
8. b) Run the Jupyter demo notebook included with this project in VS Code:
  ```bash
  code demo.ipynb
  ```
  ```
  Ctrl+Shift+P -> Select Interpreter -> Python 3.10.12 ('chat')
  click `run all`    
  ```
10. Start/restart VS Code


## Links
### Discussion
- https://www.reddit.com/r/LocalLLaMA/comments/14niv66/using_an_llm_just_for_your_own_data/
- https://www.reddit.com/r/LocalLLaMA/

### LLMs
- ChatGPT
  - https://platform.openai.com/docs/guides/gpt
  - 
- LLaMa (Meta AI)
  - https://www.reddit.com/r/LocalLLaMA/comments/11o6o3f/how_to_install_llama_8bit_and_4bit/
  - https://discord.com/invite/Y8H8uUtxc3
  - https://www.reddit.com/r/LocalLLaMA/wiki/models/

### Tools
- LangChain
  - https://python.langchain.com/docs/get_started/introduction.html
  - https://python.langchain.com/docs/modules/model_io/models/llms/
  - https://python.langchain.com/docs/modules/model_io/models/
- LlaMaIndex
- https://github.com/jerryjliu/llama_index


## Fun
- https://llmboxing.com/question/b7306819-3d39-4083-9f78-4f389d0da857


## License
[MIT](https://choosealicense.com/licenses/mit/)


<!-- ## Problems
### Python version when using conda
1. Check the available Python version:
  ```bash
  pyenv versions
  ```
2. Use the compatible Python version
  ```bash
  poetry env use 3.10
  ``` -->
