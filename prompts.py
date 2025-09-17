def get_level_prompt(level):
    if level == "easy":
        return "Ask basic, beginner-friendly interview questions.Give Only 1 small sentence as overall response."
    elif level == "moderate":
        return "Ask intermediate-level questions focusing on understanding and practical experience.Give Only 2 small sentences as overall response."
    elif level == "experienced":
        return "Ask advanced-level questions about architecture, decision-making, and deep technical topics.Give Only Hard,complex responses."
    return "Ask general questions."

def type_prompt(type):
    if type == "hr":
        return "Focus on behavioral questions,situation-based ,cultural fit, and soft skills."
    elif type == "technical":
        return "Focus on technical skills, problem-solving, and role-specific knowledge."
    return "Mix of behavioral and technical questions."

FOLLOW_UP = "Based on candidate's previous answers, ask relevant follow-up questions."
