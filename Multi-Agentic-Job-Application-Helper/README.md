## Apply with confidence!


![image info](./img/multi_agent_job_helper.png)
*Multi-Agentic Job Application Helper with CrewAI and OpenAI GPT-4*


Pain points when applying for a job posting:
1. The applicant's work profile does not exactly match job role and descriptions.
2. Not all of the applicant's experiences are relevant to what the role is looking for.
3. The applicant is not sure what experiences he/she has that align with the role
4. Manualy aligning your resume to the role may be a good practice but puts you at a disadvantage with regards to time

Generative AI definitely has change the landscape of job applications. Using chatgpt, you can easily prompt your way to create a tailored resume based on a job posting. It became a nightmare to a recruiter on how to distinguish between thousands of ai generated resume. And when they pick one potential good resume, it is embellished to a point that the first phone call interview ends up being a waste of time for both the applicant and the recruiter. 

This application aims to help an applicant be confident with the resume they are sending to each application. It has a guardrail to make sure the generated tailored resume is honest with regards to the applicants profile. It will try to align the applicant's profile to the job posting without embellishment and insertion of new skills, fields, industries or experiences just to fit the job posting. 

![image info](./img/honesty_check.png)
*One of the agent puts a guardrail against embelishment to make sure the generated resume is honest and with integirity.*

Another goal of this application is to put the applicant in good shape for the rounds of interview he/she certainly will face. This will happen when the applicant is confident that he/she has an honest resume tailored for the job posting.

This application utilize an hierarchal agentic approach using CrewAI and GPT-4 where each agent has a task and each task is dependent on prior task/s. It uses context RAG instead of vector RAG and that means it relies on LLM to analyze contexts such as the applicants profile and job posting. It is also encouraged to play with agent parameters and prompts to guide the behavior of the whole pipeline. 



What it needs:
* Resume/Work Profile/CV
* Cover letter Guide
* Job Posting Details

What it will generate:
* A tailored resume fit to the job posting, honest and with integrity
* Cover letter that takes into consideration the generated tailored resume, job posting and your cover letter additional inputs
* Interview preparation material

Eventually