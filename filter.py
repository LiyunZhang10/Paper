from llm.preset import *
import re
def censorship(user_prompt):
    prompt_sys=f""" 
    {user_prompt} is the user prompt for the LLM,your task is to check whether it has moral or other safety problems.
    if it has, please output 0 and provide a brief explanation of the problem and suggest a solution. If not,simply output 1.
    example :
    user: {{user_prompt}}
    you: 1
    user: {{another_user_prompt}}
    you: 0 the user prompt contains some sensitive information, please remind the user to avoid using sensitive information.
    user:{user_prompt}
    you:
    """
    response=get_completion(prompt_sys)
    number= re.findall(r'\d+', response)
    return number[0],response
def filter(stage_response):
    prompt_sys=f""" 
    {stage_response} is the stage response of the LLM, your task is to check whether it has moral or other safety problems.
    if it has, please modify the response without changing the original format to avoid these prblems. If not,simply output the original {stage_response} without changing anything or telling the user it does not have problems.
    
    """
    response=get_completion(prompt_sys)
    
    return response