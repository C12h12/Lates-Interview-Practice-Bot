import time, threading
from prompts import get_level_prompt, FOLLOW_UP
from evaluator import evaluate_answer
from generator import generate_next_question
from config import LEVEL_DURATIONS

def run_interview(level, job_desc_text, resume_text):
    interview_duration = LEVEL_DURATIONS.get(level, 10 * 60)
    interview_end_flag = threading.Event()

    def end_interview_after_timeout():
        time.sleep(interview_duration)
        interview_end_flag.set()

    threading.Thread(target=end_interview_after_timeout, daemon=True).start()

    base_prompt = f"""
You are a professional interview bot conducting a job interview.

Rules:
- Ask one question at a time.
- Use professional tone.
- {get_level_prompt(level)}

Job Description:
{job_desc_text}

Candidate Resume:
{resume_text}

Begin the interview.

Interviewer:"""

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
        eval_data = evaluate_answer(answer, interviewer_question)
        eval_data["question"] = interviewer_question
        eval_data["answer"] = answer
        evaluation_log.append(eval_data)

        next_question = generate_next_question(conversation_history)
        if not next_question:
            print("🛑 Interview ended. No further questions.")
            break

        interviewer_question = next_question
        print("\n🧑‍💼 Interviewer:", interviewer_question)
        conversation_history += f" {interviewer_question}"

    print("\n🛑 Interview time completed or session ended.")
    return evaluation_log
