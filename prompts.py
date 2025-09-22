def get_level_prompt(level):
    if level == "easy":
        return "Always ask very simple, beginner-friendly questions in one short sentence only."
    elif level == "moderate":
        return "Always ask intermediate, practical questions in 1–2 short sentences.Example:"
    elif level == "experienced":
        return "Always ask advanced, complex questions about system design, scalability, or trade-offs. Make it detailed and thought-provoking."
    return "Always ask one general  interview question in one short sentence."


def type_prompt(type):
    if type == "hr":
        return "Focus on behavioral questions,situation-based ,cultural fit, and soft skills."
    elif type == "technical":
        return "Focus on technical skills, problem-solving, and role-specific knowledge."
    return "Mix of behavioral and technical questions."

FOLLOW_UP = "Based on candidate's previous answers, ask relevant follow-up questions."
