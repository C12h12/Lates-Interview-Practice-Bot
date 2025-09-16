def get_level_prompt(level):
    if level == "easy":
        return "Ask basic, beginner-friendly interview questions."
    elif level == "moderate":
        return "Ask intermediate-level questions focusing on understanding and practical experience."
    elif level == "experienced":
        return "Ask advanced-level questions about architecture, decision-making, and deep technical topics."
    return "Ask general questions."

FOLLOW_UP = "Based on candidate's previous answers, ask relevant follow-up questions."
