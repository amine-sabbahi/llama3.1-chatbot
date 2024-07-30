# Llama 3.1 Chatbot

This repository contains a Streamlit application for a chatbot powered by [Llama3.1-405B](https://replicate.com/meta/meta-llama-3.1-405b-instruct) llm from meta hosted in [replicate plateforme](https://replicate.com). The application is structured to include configuration files, application code, and dependencies required to run the chatbot.

You can try it live at this link: [llama3-1-chatbot](llama3-1-chatbot.streamlit.app)

![app-interface](src/app1.png)

![app-interface](src/app2.png)

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.12
- Streamlit
- replicate

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/amine-sabbahi/llama3.1-chatbot.git
    cd llama3.1-chatbot
    ```

2. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Install the dependencies:**

    ```bash
    streamlit run app.py
    ```

### Configuration

1. **Edit the Streamlit configuration files:**

    - `.streamlit/config.toml`: Here you can customize your Streamlit app theme.
    - `.streamlit/secrets.toml`: You can add your replicate api key in here.


## Usage

Once the application is running, you can interact with the Llama 3.1 Chatbot through the Streamlit interface.
you will just need a replicate api key that you can get from [here](https://replicate.com/account/api-tokens)


## Contact

If you have any questions or suggestions, please feel free to contact [me](https://github.com/amine-sabbahi).
