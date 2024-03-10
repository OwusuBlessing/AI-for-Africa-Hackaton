
<!-- PROJECT LOGO -->
<br />
<div align="center">

  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://img.freepik.com/premium-photo/ultimate-workspace-companion-chatgpt-robotic-technology-nextlevel-performance-generative-ai_634358-1134.jpg?size=626&ext=jpg" alt="Logo">
  </a>

  <h3 align="center">AI-Powered Research Assistant</h3>

  <p align="center">
    An awesome companion to help you with your research work!
    <br />
    <br />
    <br />
    <a href="https://youtu.be/NgFFzwT6uVI">View Demo</a>
  
</div>

## Folder Structure

The project follows a structured organization with the following directories:

```plaintext
project_root/
│
├── Project_info/
│   ├── sections.json
│   └── outlines.py
│   |__project_general_info.json
|   |__current_sections.json
|
|___notebooks
|   |__research.ipynb
|
├── openai_llm/
│   ├── ai_outlines.py
│   ├── ai_suggestions.py
|   |__ generate_response.py
│
├── utils.py
│
├── templates/
│   ├── home.html
│   └── ... (other HTML files)
│
├── app.py
│
├── images
│
├── requirements.txt

```

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">Project Description</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## Project Description
The Research Assistant is a cutting-edge web application designed to enhance research efficiency and organization for scholars, students, and professionals alike. Leveraging the power of Large Language Models (LLMs), this intuitive platform offers personalized responses to project inquiries, facilitating deep dives into specific chapters or sections of interest. Whether you're exploring complex topics or seeking succinct summaries, Research Assistant tailors its guidance to meet your unique project requirements.
## Features

**Interactive Chat Interface
- Engage with our AI-powered bot to ask questions, seek clarifications, or explore topics. The interface is user-friendly, making it easy for anyone to start their research journey.
**Dynamic Outline Creation
- Users can generate and interact with an outline of key points tailored to their selected chapter or section, enhancing their understanding and focus on crucial aspects.
**Custom Citation Generator
- Need citations? Select your preferred reference style (APA, MLA, Chicago, Harvard, or none) and receive ready-to-use citations for your research, streamlining the writing process.
**Drafting Space
- Utilize the sliding arrow and text space feature on the left side of the page to paste and manage drafts or copied text from your interactions with the Research Assistant. This tool aims to simplify note-taking and content organization.


### Built With
* Python
* Langchain
* FastAPI
* HTML
* openai Api integration


<!-- GETTING STARTED -->
## Getting Started

To get started, sign up for an OpenAI account and generate an API key. This key will allow you to access and utilize the OpenAI API effectively. Finally, clone the repository to your local machine using the `git clone` command with the repository URL.
```sh
git clone https://github.com/OwusuBlessing/Code-Analysis-LLM.git
```

### Prerequisites
To set up a virtual environment, you can choose to use either Python's built-in virtual environment tools or Anaconda, depending on your preference. Open your terminal and navigate to the cloned repository directory. From there, create your virtual environment using your preferred method
* Using Python's venv Module write the following command one after the other:
  ```sh
  python -m venv myenv
  
  myenv\Scripts\activate
  
  source myenv/bin/activate

  ```
  

* Using Anaconda write the following command one after the other:
  ```sh
  conda create --name myenv
  
  conda activate myenv
  ```



After setting up your environment, ensure you have:
- An OpenAI account for API access.
- A GitHub account for repository integration.
- Python installed on your machine for running the project.

### Step 1: Sign Up for OpenAI and Generate an API Key

1. Visit [OpenAI's website](https://openai.com/) and sign up for an account.
2. Navigate to the API section and generate a new API key.
3. Safely store the API key for later use.

### Step 2: Clone the Repository

Clone IntelliReview to your local machine:

```sh
git clone https://github.com/OwusuBlessing/Code-Analysis-LLM.git
cd Langchain-Project


### Installation


1. Get your API Key at [https://platform.openai.com/](https://platform.openai.com/)
2. Clone the repo
   ```sh
   git clone https://github.com/OwusuBlessing/Langchain-Project.git
   ```
3. Install packages after activating your virtual environment and run:
   ```sh
   pip install -r requirements.txt
   ```
4. Enter your API toknes  in `.env`
5. 
open `.env` file  and paste your tokens

   ```env
   OPENAI_API_KEY="ENTER YOUR OPENAI API"
   ```
To launch the application, open your terminal and enter the following command:
```
uvicorn test_app:app --reload
```
This will initiate a local server, allowing you to access the application through your web browser."
<!-- USAGE EXAMPLES -->
## Usage

**Customized Content Generation:
- At its core, the application prompts ChatGPT with your specific project information. This allows for the creation of content that's not just relevant but also aligned with your research goals, whether it's for academic papers, professional reports, or personal inquiries.

**Interactive Content Sections: 
- Navigate through intelligently organized sections of content, each designed to enhance your understanding and engagement with the material. From in-depth analysis to succinct summaries, the application adapts to your preferred depth of exploration.

**Content Enhancement and Optimization:
- The platform goes beyond basic information retrieval. It offers suggestions for content improvement and optimization, ensuring that your research is not only comprehensive but also of the highest quality.

**Citation Generation: 
- With an integrated citation generator, the application supports a variety of referencing styles, including APA, MLA, Chicago, and Harvard. This feature simplifies the often tedious process of citation, making it seamless to credit sources accurately and efficiently.



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- CONTACT -->
## Contact
Name - Owusu Samule Blessing
Email - owususammy509@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Here is a list of resources that proven to be really helpful in implementing this project

* [Langchain documentation](https://python.langchain.com/docs/get_started/introduction/)
* [FastAPI documentation](https://fastapi.tiangolo.com/)
<p align="right">(<a href="#readme-top">back to top</a>)</p>

