# QNA over web Articles
This repository contains a proof-of-concept project developed for a gig on [UPWORK.com](https://www.upwork.com/). The primary objective of this project is to demonstrate the creation of a central vector database of articles, facilitating the seamless updating of new articles as needed. Additionally, the project aims to enable conversational question-and-answer (QnA) interactions leveraging the RAG (Retriever, Answerer, Generator) functionality using the OpenAI API and embeddings.
<br><br>
## Key Features:
#### Central Vector Database: 
The project establishes a central repository for storing articles in vector form. This database allows for efficient storage and retrieval of articles, enabling easy updates and additions as required.

#### Conversational QnA: 
Leveraging the RAG functionality provided by the OpenAI API and embeddings, the project enables conversational QnA interactions. Users can ask questions related to the stored articles, and the system responds with relevant answers.

#### Streamlit UI: 
The project utilizes Streamlit, a popular Python library for building interactive web applications, to provide a user-friendly interface for interacting with the central vector database and conducting QnA sessions.

#### Langchain Components: 
Langchain has been used as key enabler for the entire RAG setup, with the help of different elements like [WebBaseLoader](https://python.langchain.com/docs/integrations/document_loaders/web_base/), [Character Splitter](https://python.langchain.com/docs/modules/data_connection/document_transformers/character_text_splitter/) and the OpenAI wrappers.



<br><br>
## Setup and installation

### 1. Clone the Repository:

Start by cloning this repository in your local machine
```bash
   git clone https://github.com/ameyGujre/QNA-over-web-Article
```
### 2. Docker Installation:

Install docker engine on your machine from [here.](https://docs.docker.com/engine/install/)

### 3. Navigate to the Project Directory:

Navigate to the cloned directory and open a terminal on the same path.

### 4. Build Docker Image:

Run below command in terminal to build docker Image

```bash
    docker build -t article_qna .
```

### 5.Run Docker Container:

Once the Docker Image is build, use below command in the terminal to actually run the streamlit app.
```bash
  docker run -p 8501:8501 article_qna
```

### 6. Access the Streamlit App:

Finally, open a web browser and navigate to [http://localhost:8501](http://localhost:8501) to access the app.

<br><br>
## Working and Previews

### 1. Enter your OpenAI API Key:

As this project uses OpenAI's gpt3.5turbo for inference and text-ada-002 for embedding, you need to have an OpenAI API Key with active credits to use this app.
![image](https://github.com/ameyGujre/QNA-over-web-Article/assets/29010086/5bdafe02-f898-4ddd-a886-3c108f38a1ea)

### 2. Submit webpage URL of the Article:

On the left sidebar, by clicking on the Update Articles page you can update new article in the database. The index will be saved inside embeddings/ folder.
#### By default there is not a single Index present in this repo, for first time use you must need to create one by submitting the URL here.

![image](https://github.com/ameyGujre/QNA-over-web-Article/assets/29010086/97322919-3778-4b2d-9913-d52c1c1073c6)

Once index is created, it will be stored in the local as well and made available for future inference. When you update new article URLs, the index of that would be merged with the existing database as well.


### 3. Perform Question and answering:

Once you are done updating the articles, and indexes are created successfully, you can switch to Assistant Page from the left sidebar.

![image](https://github.com/ameyGujre/QNA-over-web-Article/assets/29010086/8e25a15c-f753-4b58-9991-895a2a4ab4e3)


![image](https://github.com/ameyGujre/QNA-over-web-Article/assets/29010086/27214b85-8d2d-44cb-9cf3-7c13c70274d7)

![image](https://github.com/ameyGujre/QNA-over-web-Article/assets/29010086/4a0ec3e9-4a71-456f-97d9-576d5a703a11)



#### The assistant will only response from the context provided inside the index, or whatever articles were submitted to it. If there isn't any information available it will respond with "I don't know"

![image](https://github.com/ameyGujre/QNA-over-web-Article/assets/29010086/cafc4c21-c141-4933-90c2-0b80abb2f088)



## Contact:

Thankyou for hanging in. 
If you have any query, concern or feedback feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/amey-gujre-400412162/)

author
[Amey Gujre](https://www.linkedin.com/in/amey-gujre-400412162/)
