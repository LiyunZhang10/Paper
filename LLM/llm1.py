from preset import get_completion
history = []
def main(requirment):
     global history
     prompt_sys=f"""You are an CAD assistant helping users to decide or design an ISA. The 
      user can either ask you to use an existing ISA or give you user instructions to design one, where the user input is {requirment}.
If the user wants to use an existing ISA, your output should simply be the name of the ISA without any other content.
If the user wants to design an ISA, your output should be the content of the ISA. """
     try:
          response,history=get_completion(prompt_sys,history)
          response=filter(response)
          return response
     except Exception as e:
        error_info=(type(e), str(e))
        prompt1_1=f"""contents delimited by triple backticks are the output errors for deciding or designing an ISA using gpt-4,you have several tasks, first, apologize for generating errors.
        second,trying to explain why errors occurred by analyzing the output
        , if the output is not completed , your response should be disconnect from gpt-4.
            '''{error_info}'''
        """
        response1=filter(get_completion(prompt1_1))
        return response1