### Apply with Confidence

This project is inspired by the Deeplearning.ai course on using LLM with CrewAI in a multi-agent system.

Generative AI has revolutionized job applications. With tools like ChatGPT, you can quickly create a resume tailored to a job posting. However, this has made it hard for recruiters to sift through thousands of AI-generated resumes. Often, resumes are so embellished that the first phone interview is a waste of time for both the applicant and recruiter. The goal is to align your resume with the job posting honestly, without exaggerating your credentials.

#### Here are some common issues in the job application process:

Not all of your experiences are relevant to the role.
You might not be sure which of your experiences align with the job.
Manually aligning your resume to each role takes time, especially when applying to multiple jobs.
This application helps you confidently send out resumes. It aligns your profile with the job posting without adding or exaggerating skills and experiences. The guardrails ensure your resume remains honest, helping you feel prepared for the interview stages that follow.

![image info](./img/honesty_check.png)
*Guardrail against embellishment*


This tool uses a hierarchical, multi-agent system with CrewAI and GPT-4. Each agent has a task, relying on previous tasks, and it uses context RAG (not vector RAG) to analyze the applicant’s profile and job posting. You can tweak agent parameters and prompts to guide the entire process.


![image info](./img/multi_agent_job_helper.png)
*Multi-Agentic Job Application Helper with CrewAI and OpenAI GPT-4*


#### What You'll Need:
**Resume/Work Profile/CV**: A detailed profile covers all your skills and qualifications, letting the AI pick what's relevant.

**Job Posting Details**: Include as much information as possible about the position, company culture, etc.

**Cover Letter Guide**: Provide guidance for your cover letter instead of letting the AI generate a generic one. Authenticity matters to hiring managers.

#### What It Will Generate:
A tailored, honest resume that fits the job posting.
A cover letter that aligns with your resume, the job posting, and your additional inputs.
Interview preparation material.


Remember, you control your job-hunting strategy. This tool is just one resource; it shouldn't replace intentionality in your applications. Confidence and integrity are still key to a healthy career.

