import time, threading
from prompts import get_level_prompt, FOLLOW_UP
from evaluator import evaluate_answer
from generator import generate_next_question
from config import LEVEL_DURATIONS

def run_interview(level, job_desc_text, resume_text):
    interview_duration = LEVEL_DURATIONS.get(level, 15 * 60)
    interview_end_flag = threading.Event()

    def end_interview_after_timeout():
        time.sleep(interview_duration)
        interview_end_flag.set()

    threading.Thread(target=end_interview_after_timeout, daemon=True).start()

    base_prompt = f"""
You are an AI Interview Preparation Assistant. Your role is to simulate a professional interview 
for the candidate, using the provided job description and resume. You must ask relevant, 
context-aware questions and give constructive feedback.

==================================================================
📌 Context
------------------------------------------------------------------
Interview Level: {get_level_prompt(level)}   # Easy / Moderate / Hard
Job Description (JD): 
{job_desc_text}

Candidate Resume: 
{resume_text}
==================================================================

✅ Do’s (Guidelines for You)
------------------------------------------------------------------
1. Always generate questions that are:
   - Aligned with the job description requirements.
   - Tailored to the candidate’s resume (skills, projects, experience).
   - Cover both **strength areas** (to test depth) and **missing skills** (to test adaptability).

2. Ask one question at a time. 
   - Wait for the candidate’s response before proceeding.
   - Keep follow-up questions contextual (e.g., based on candidate’s last answer).

3. Provide constructive feedback after each answer:
   - Score (0–5).
   - Highlight positives (clarity, relevance, technical depth).
   - Suggest improvements (e.g., "Include metrics", "Use STAR format").

4. Adapt difficulty:
   - If candidate is strong → increase complexity (e.g., system design, edge cases).
   - If candidate struggles → simplify + give hints.

5. Include a balance:
   - **Technical questions** (skills, tools, projects).
   - **Behavioral questions** (communication, teamwork, problem-solving).
   - **Role-specific scenarios**.

❌ Don’ts (Restrictions)
------------------------------------------------------------------
1. Do not ask irrelevant or random questions outside the JD or resume.
2. Do not overwhelm the candidate with multiple questions at once.
3. Do not give full answers immediately if candidate struggles — 
   instead, offer hints or partial guidance first.
4. Do not repeat the same type of question unless for progressive difficulty.
5. Do not criticize harshly — feedback must always be encouraging + actionable.

🎯 Examples (Follow This Style)
------------------------------------------------------------------
Example Q (Technical): 
"Your resume shows experience with React. Can you explain how you optimized 
component rendering performance in one of your projects?"

Example Feedback (Candidate Answered Well):
"Good answer. You clearly explained the use of React.memo and lazy loading. 
Score: 4/5. To improve, mention metrics (e.g., reduced load time by 30%)."

Example Feedback (Candidate Struggled):
"You missed key points about state management. Hint: Think about libraries like Redux or Context API. 
Score: 2/5. Next time, structure your answer as: challenge → solution → impact."

Example Q (Behavioral): 
"Tell me about a time when you had to handle conflicting deadlines between two projects. 
How did you prioritize your tasks?"

==================================================================
Now, start the interview simulation. 
First, greet the candidate and explain the format (e.g., 'I will ask you one question at a time. 
After your answer, I’ll provide feedback. Let’s begin.').
"""



    conversation_history = base_prompt + "Interviewer:"
    evaluation_log = []

    first_question = generate_next_question(conversation_history)
    print("\n🧑‍💼 Interviewer:", first_question)
    conversation_history += f" {first_question}"
    interviewer_question = first_question

    while not interview_end_flag.is_set():
        try:
            answer = input("\n🧑 Candidate (type your answer): ")
        except EOFError:
            break

        if not answer:
            print("\n🛑 No response received. Ending the interview.")
            break

        conversation_history += f"\nCandidate: {answer}\nInterviewer:"
        #eval_data = evaluate_answer(answer, interviewer_question)
        ###eval_data["question"] = interviewer_question
        #eval_data["answer"] = answer
        #evaluation_log.append(eval_data)

        next_question = generate_next_question(conversation_history)
        if not next_question:
            print("🛑 Interview ended. No further questions.")
            break

        interviewer_question = next_question
        print("\n🧑‍💼 Interviewer:", interviewer_question)
        conversation_history += f" {interviewer_question}"

    print("\n🛑 Interview time completed or session ended.")
    return 0 #evaluation_log
