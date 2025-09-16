import re, json
from config import generator

def evaluate_answer(answer, question):
    eval_prompt = f"""
You are an interview evaluator. Only respond with a JSON object, and nothing else.

Evaluate the following candidate answer based on:
- Relevance (0–5)
- Technical Correctness (0–5)
- Communication Clarity (0–5)

Question: {question}
Answer: {answer}
"""

    try:
        eval_result = generator(eval_prompt, max_new_tokens=300, temperature=0.7)[0]['generated_text']
        json_matches = re.findall(r"\{.*?\}", eval_result, re.DOTALL)
        json_str = json_matches[-1] if json_matches else None

        if json_str:
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                return {"relevance": 0, "technical_correctness": 0, "clarity": 0, "comment": "Invalid JSON."}
        else:
            return {"relevance": 0, "technical_correctness": 0, "clarity": 0, "comment": "No JSON found."}
    except Exception as e:
        return {"relevance": 0, "technical_correctness": 0, "clarity": 0, "comment": f"Error: {e}"}
