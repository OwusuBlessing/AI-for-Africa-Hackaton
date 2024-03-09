from fastapi import FastAPI,Form, Request,HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from typing import Optional,Dict,List
from pydantic import BaseModel
from utils import save_dict_as_json,load_json_as_dict
from openai_llm.ai_suggestion import collect_ai_suggest_sections

app = FastAPI()

# Jinja2 template
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return templates.TemplateResponse("home.html", {"request": dict()})

@app.get("/project", response_class=HTMLResponse)
async def get_project_form(request: Request):
    return templates.TemplateResponse("project_info.html", {"request": request})


@app.post("/submit_project_info", response_class=HTMLResponse)
async def submit_project_info(request: Request,
                              projectTitle: str = Form(...),
                              projectType: str = Form(...),
                              academicLevel: str = Form(...),
                              subjectArea: str = Form(...),
                              researchMethodology: str = Form(...),
                              purposeGoal: str = Form(...),
                              audience: str = Form(...),
                              dataSource: str = Form(...),
                              scope: str = Form(...),
                              timeline: str = Form(""),
                              keyChallenges: Optional[str] = Form(""),
                              desiredImpact: Optional[str] = Form(...),
                              additionalInfo: Optional[str] = Form("")):
    form_data = {
        "Project Title": projectTitle,
        "Project Type": projectType,
        "Academic Level": academicLevel,
        "Subject Area": subjectArea,
        "Research Methodology": researchMethodology,
        "Purpose/Goal": purposeGoal,
        "Audience": audience,
        "Data Source": dataSource,
        "Scope": scope,
        "Timeline": timeline,
        "Key Challenges": keyChallenges,
        "Desired Impact": desiredImpact,
        "Additional Information": additionalInfo
    }
    #print(form_data)
    save_dict_as_json(data_dict=form_data,file_name="project_general_info.json")
    return templates.TemplateResponse("sections.html", {"request": request,"form_data":form_data})

@app.get("/custom_sections", response_class=HTMLResponse)
async def get_project_form(request: Request):
    return templates.TemplateResponse("custom_sections.html", {"request": request})



class Section(BaseModel):
    name: str
    description: str

class SubmitSections(BaseModel):
    sections: List[Section]

@app.post("/submit_custom_sections")
async def submit_custom_sections(submit_sections: SubmitSections):
    try:
        # Here you could process the submission as needed.
        print("Received sections:", submit_sections.sections)

        dict_sections = {}

        for section in submit_sections.sections:
            dict_sections[section.name] = section.description
        
        print(dict_sections)
        save_dict_as_json(data_dict=dict_sections,file_name="sections.json")

        # Respond with a URL for redirection.
        return JSONResponse(content={"message": "Sections submitted successfully", "redirect_url": "/success"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    #return templates.TemplateResponse("Final_sections_for_content_generation.html", {"request": request,"sections":section_dict})

@app.get("/ai_suggested_sections", response_class=HTMLResponse)
async def get_project_form(request: Request):
    try: 
        collect_ai_suggest_sections()
     # Respond with a URL for redirection.
        return JSONResponse(content={"message": "Sections submitted successfully", "redirect_url": "/success"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    #sections = load_json_as_dict(file_name="sections.json")

    #return templates.TemplateResponse("ai_sections.html", {"request": request,'sections':sections})#,"sections":section_dict})


@app.get("/success", response_class=HTMLResponse)
async def get_project_form(request: Request):
    sections = load_json_as_dict(file_name="sections.json")
    
    print(sections)
    return templates.TemplateResponse("Final_sections_for_content_generation.html", {"request": request,'sections':sections})#,"sections":section_dict})






class Section(BaseModel):
    sectionName: str
    description: str

@app.post("/post_section")
async def post_section(section: Section):
    try:
        # Process the section here. For example, save it to a database.
        print(section.sectionName, section.description)
        return {"message": "Section received successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    



@app.get("/ch", response_class=HTMLResponse)
async def home():
    return """
    <html>
    <head>
        <title>Chatbot</title>
        <script>
            async function sendMessage() {
                const userInput = document.getElementById("userInput").value;
                document.getElementById("userInput").value = "";
                const response = await fetch("/chat", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ message: userInput })
                });
                const data = await response.json();
                document.getElementById("chat").innerHTML += `<p><strong>User:</strong> ${userInput}</p>`;
                document.getElementById("chat").innerHTML += `<p><strong>Bot:</strong> ${data.message}</p>`;
            }
        </script>
    </head>
    <body>
        <h1>Chatbot</h1>
        <div id="chat"></div>
        <input type="text" id="userInput" />
        <button onclick="sendMessage()">Send</button>
    </body>
    </html>
    """

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data["message"]
    bot_response = "Hi"
    return {"message": bot_response}
