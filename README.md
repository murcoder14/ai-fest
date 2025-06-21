# AI Workout using Langchain and OpenAI

*Generative AI* typically works on tasks that are narrow and well-defined, such as answering a question, text summarization, text generation and generating a digital image or audio. This project demonstrates a few techniques of Generative AI using *Langchain*, a popular Python framework. 

#### Prerequisites
1. A Windows, Linux or Mac machine
2. [Python 3.13.x or higher](https://www.python.org/downloads/)
3. [Langchain](https://python.langchain.com/docs/introduction/) - Langchain is a Python framework that enables AI integration by connecting data and APIs with Large Language Models from several vendors. 
4. [Milvus Vector Database](https://milvus.io/) - Milvus is an open-source vector database built for Generative AI applications. It supports fast searches, and can scale to tens of billions of vectors with minimal performance loss.
5. [Docker Desktop](https://www.docker.com/get-started/)  - Milvus shall run inside the Docker container.
6. [bs4](https://pypi.org/project/beautifulsoup4/) - Beautiful Soup is a library that enables the extraction of content from web pages.
7. [uv](https://docs.astral.sh/uv/) - uv is an extremely fast Python package and project management tool that is optimized for *Python Developer happiness*. It enables the creation of projects, virtual environments and dependency management. With uv, there is no need to install separate packages like pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, and others as uv consolidates the functionality of several Python tools into one unified solution.
8. OpenAI API Key

*Note - Only a basic knowledge of Python is required to understand and complete this project. There is no proficiency required in the usage of Langchain, Docker, Milvus or uv. All the steps to install and use these tools are explained in the sections below.*

#### Setup

1. Install Docker Desktop by following the instructions [here](https://docs.docker.com/desktop/setup/install/windows-install/). Separate instructions are available for [Linux](https://docs.docker.com/desktop/setup/install/linux/) and [Mac](https://docs.docker.com/desktop/setup/install/mac-install/) users. 
2. Start Docker Desktop and ensure it is up and running.
3. Install Milvus and run it is a Docker Container by following the instructions below.
   
    Windows 
    + Create a folder, *c:\tools\milvus* in the Windows filesystem. 
    + Download the *standalone_embed.bat* file from [here](https://github.com/milvus-io/milvus/tree/master/scripts) and copy it to the *c:\tools\milvus* folder.
    +  Open a Powershell session in Windows and navigate to the folder, *c:\tools\milvus*.
       ```sh
       cd c:\tools\milvus
       ```
    +  Run the downloaded file to start Milvus as a Docker container. Milvus listens on HTTP port 19530. Do not exit this shell session until the entire project is implemented and tested.
       ```sh
       C:\tools\milvus\>standalone_embed.bat start
       Wait for Milvus starting...
        Start successfully.
       ```     
   Linux/Mac 
   + Follow the instructions [here](https://milvus.io/docs/install_standalone-docker.md) to install and run Milvus.

   
4. While this project uses OPEN AI as the LLM Provider, this project can integrate with any LLM Provider by making subtle changes within the code.  Obtain the OPENAI_API_KEY from [here](https://platform.openai.com/api-keys). The value of this key is used in the *.env* file in step 7 below and allows 
   the Python Langchain code to connect to the LLM hosted by OPEN AI. 
       
   
5. Install uv as follows.

   Windows 
    + Create a folder, *c:\tools\uv* in the Windows filesystem. 
    + Open a new Powershell session in Windows, navigate to the folder, *c:\tools\uv* and install uv.
      ```sh
      cd c:\tools\uv
      c:\tools\uv\>powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
      ```  
   Exit the Powershell session after uv is installed successfully.

   Linux/Mac (TODO)
   
6. Create a Python project,*ai-fest*.
   
    Windows
    + Create a folder, *c:\pythonprojects* in the Windows filesystem. 
    + Open a new Powershell session, navigate to the folder, *c:\pythonprojects* and execute the following 
       ```sh
       cd c:\pythonprojects
       # Create a new Python project called ai-fest using uv.
       c:\pythonprojects> uv init ai-fest
       # Switch to the ai-fest project folder.
       c:\pythonprojects> cd ai-fest
       # Create a new Python virtual environment using uv.
       c:\pythonprojects\ai-fest> uv venv
       # Activate the Python virtual environment.
       c:\pythonprojects\ai-fest> source .venv/bin/activate
       # Add the desired Python packages to new Python virtual environment using uv.
       # Note that the addition of packages via uv finishes in milliseconds. Contrast this with pip, poetry or conda. uv is written in Rust and hence its performance speaks for itself.
       (ai-fest) tmuralic:\pythonprojects\ai-fest>  uv add langchain langchain-core langchain-community langchain-text-splitters langchain-milvus langchain-openai bs4 dotenv
       # This completes the creation of the project,*ai-fest*. uv has yielded a main.py file with all the project dependencies in the pyproject.toml file. List all the files in the ai-fest folder using dir.
       c:\pythonprojects\ai-fest>dir
       main.py  pyproject.toml  README.md  uv.lock
       # Run the main.py using uv to ensure that the project is configured correctly.
       c:\pythonprojects\ai-fest>uv run main.py 
       Hello from ai-fest!
       ```.  

7. Copy the following files from GitHub location,   to the ai-fest folder. Note that the main.py has to be overwritten with the same file from the GitHub.
    + main.py
    + simple_rag.py
    + README.md
   
   Create a *.env* (dot env) file in the ai-fest folder and add the OPEN_API_KEY value obtained from step 4 above to it. (*Note that the key value below is shown only for illustration and does not represent an actual key*)
    + OPENAI_API_KEY=skYUacdfER34&MLOPsqzx71hlpwyuq 

8. Run the application and watch Retrieval Augmented Generation in action. Review simply_rag.py to understand how RAG is implemented using Langchain.
    ```sh
    # Run the main.py. 
    c:\pythonprojects\ai-fest>uv run main.py
     Running ai-fest app...
     2025-06-21 14:02:00,211 [DEBUG][_create_connection]: Created new connection using: 08216138f2004f599a36f8cf740a3d43 (async_milvus_client.py:599)
     If you have completed Linear Algebra Honors (MA650HO) and Multivariable Calculus Honors (MA670HO) at Choate Rosemary Hall, you are eligible to take the Applied Differential Equations, Honors (MA660HO) course.
    ```

9. When all experimentation and testing have been completed, shut down the Milvus Vector Database by typing Control-C in the Windows Powershell session where Milvus was launched.
    

#### Reference Documentation
For further reference, please consider the following:

* [Vectors and Embeddings](https://www.ibm.com/think/topics/vector-embedding)
* [Retrieval Augmented Generation](https://www.youtube.com/watch?v=u47GtXwePms)
* [OpenAI's Playground](https://platform.openai.com/playground/prompts?models=gpt-4o)
* [Official Langchain Documentation](https://docs.spring.io/spring-ai/reference/index.html)
* [Prompt Engineering Guide](https://www.promptingguide.ai/)
* [User, System and Assistant Roles in LLMs](https://www.baeldung.com/cs/chatgpt-api-roles)

## License

MIT

**Free Software, Hell Yeah!**
