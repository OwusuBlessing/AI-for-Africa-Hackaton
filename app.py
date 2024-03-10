from fastapi import FastAPI,Form, Request,HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from typing import Optional,Dict,List
from pydantic import BaseModel
from utils import save_dict_as_json,load_json_as_dict
from openai_llm.ai_suggestion import collect_ai_suggest_sections
from openai_llm.ai_outlines import generate_outline
from langchain.schema import HumanMessage, SystemMessage,AIMessage
from openai_llm.generate_response import info, sections,current_section,outlines,chat_history,setup_agent, generate_output


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
    #try: 
    collect_ai_suggest_sections()
     # Respond with a URL for redirection.
       # return JSONResponse(content={"message": "Sections submitted successfully", "redirect_url": "/success"})
    #except Exception as e:
        #raise HTTPException(status_code=500, detail=str(e))
    sections = load_json_as_dict(file_name="sections.json")

    return templates.TemplateResponse("ai_sections.html", {"request": request,'sections':sections})#,"sections":section_dict})


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

        current_section = {section.sectionName: section.description}
        save_dict_as_json(current_section, file_name="current_section.json")
         
        info = load_json_as_dict(file_name="project_general_info.json")
        sections = load_json_as_dict(file_name="sections.json")
        # Generate outlines
        outlines = generate_outline(info=info, sections=sections, current_section=current_section)
        save_dict_as_json(outlines, file_name="outlines.json")
        print(outlines)
        print(section.sectionName, section.description)

        # Redirect to success page
        #return RedirectResponse(url="/content_page")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/content_page", response_class=HTMLResponse)
async def post_content_page(request: Request):
    # Handle POST request for content_page route if nseeded
    return RedirectResponse(url="/content_page")

@app.get("/content_page", response_class=HTMLResponse)
async def get_content_page(request: Request):
    outlines = load_json_as_dict(file_name="outlines.json")
    return templates.TemplateResponse("content_page.html", {"request": request, 'outlines': outlines})

#,"sections":section_dict})

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data["message"]
    print(message)
    style = data["style"]  # Get the selected referencing style(s)
    ref_style = HumanMessage(content=f"Citation style to use  : {style}")
    chat_history.append(ref_style)
    print(style)
    response = generate_output(message)
    return JSONResponse(content={"message": response})