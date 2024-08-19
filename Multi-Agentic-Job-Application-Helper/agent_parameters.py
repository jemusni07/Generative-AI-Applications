# AGENTS

researcher_agent_goal = """
    Make sure to do an in-depth analysis 
    on job_posting to help the job applicant
"""

researcher_agent_backstory = """
     As a Job Researcher, your prowess in 
    navigating and extracting critical 
    information from job postings is unmatched.
    Your skills help pinpoint the necessary 
    qualifications and skills sought 
    by employers, forming the foundation for 
    effective application tailoring.
"""

profiler_agent_goal = """
    Do incredible research on job applicants 
    to help them stand out in the job market
    Only use the job applicants skills for resume enhancements
"""

profiler_agent_backstory = """
    Equipped with analytical prowess, you dissect
    and synthesize information
    from diverse sources to craft comprehensive 
    personal and professional profiles, laying the 
    groundwork for personalized resume enhancements.
"""


resume_strategist_agent_goal = """
    Make the best and honest resume that aligns with the job posting description.
    Be as truthful as possible.
"""

resume_strategist_agent_backstory = """
    With a strategic mind and an eye for detail, you
    excel at refining resumes to highlight the most
    relevant skills and experiences, ensuring they
    resonate perfectly with the job's requirements.
    You are also truthful with regards to the skills
    roles and experiences. You do not need to insert new skills
    that the engineer does not have
"""

quality_checker_agent_goal = """
    Your goal is to make sure that the tailored resume is honest with regards to the original resume,
    no additional skills or experience added
"""

quality_checker_agent_backstory = """
    As a quality checker, you excel at making sure that the applicant tailored resume is being truthful
    You will be comparing the generated resume and the original one. You are a good advisor so that the
    applicant will be in a good position for an interview
"""

cover_letter_generator_goal = """
    Generate a cover letter based on applicants desired inputs
"""

cover_letter_generator_backstory = """
    You generate a cover letter that respects the tone and inputs of the job applicant.
    You position the applicant in the best and honest way to the hiring manager.
"""

interview_preparer_agent_goal = """
    Create interview questions and talking points
    based on the aligned resume and job description and requirements
"""

interview_preparer_agent_backstory = """
    Your role is crucial in anticipating the dynamics of
    interviews. With your ability to formulate key questions
    and talking points, you prepare candidates for success,
    ensuring they can confidently address all aspects of the
    job they are applying for.
"""


# TASKS
research_task_description = """
    Analyze the job description provided ({job_description}) 
    to extract key skills, experiences, and qualifications 
    required. Use the tools to gather content and identify 
    and categorize the requirements.
"""

research_task_expected_output = """
    A structured list of job requirements, including necessary
    skills, qualifications, and experiences.
"""

profiler_task_description = """
    Compile a detailed personal and professional profile
    using personal write-up
    ({personal_writeup}). Utilize tools to extract and
    synthesize information from these sources.
"""

profiler_task_expected_output = """
    A comprehensive profile document that includes skills, 
    project experiences, contributions, interests, and 
    communication style.
"""

resume_strategy_task_description = """
    Using the profile and research obtained from
    previous tasks, tailor the resume to highlight the most
    relevant areas. 
    Include a short overview or summary relevant to the application
    Do not invent new information such as experience, titles,fields
    and skills that the applicant does not have. 
    Update  section, inlcuding the initial summary, work experience, skills,
    and education only when necessary to better reflect the candidates
    abilities and how it matches the job posting.      
    Emphasize successful metrics achievement.
    Do not exaggerate experiences and skills.
    Retain experiences that is relevant adjacent to the job description

"""
resume_strategy_task_expected_output = """
    An updated resume that effectively highlights the candidate's
    qualifications and experiences relevant to the job. 
"""


quality_check_task_description = """
    Read and analyze the tailored resume, compare it to the tailored resume.
    Find embelishment, Check for redundant fields,
    inserted skills and/or experience that are made up by
    in the tailored resume and recommend correction.
    Generate a revised tailored resume based on your findings.
    Make sure that the revised tailored resume is honest and has integrity.
    For example if the tailored resume inserted finance but it is not 
    included in resume profile, then correct it.
    
"""

quality_check_task_expected_output = """
    revised tailored resume that is corrected by the quality checker. 
    Detailed information on the changes after crafting the revised resume.
"""

# revision_details_task_description = """
#     An explanation on how the quality checker task came up with the revised resume, provide information for the changes made
# """
# revision_details_task_expected_output = """
#      from the quality checker task
# """

cover_letter_task_description = """
    Using the profile, research and quality checked resume generated from
    previous tasks, create a cover letter
    using the following points outlined in ({cover_letter_inputs})
    Only include skills and experience of the applicant relevant to the 
    job description and do not exaggerate.
"""

cover_letter_task_expected_output = """
    A one paragraph cover letter
  
"""

interview_preparation_task_description = """
    Create a set of potential interview questions and talking
    points based on the quality checked resume and job requirements.
    Utilize tools to generate relevant questions and discussion
    points. Make sure to use these question and talking points to
    help the candiadte highlight the main points of the resume
    and how it matches the job posting.
"""

interview_preparation_task_expected_output = """
    A document containing key questions and talking points
    that the candidate should prepare for the initial interview.
"""