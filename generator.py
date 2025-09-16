import re
from config import generator, tokenizer

def generate_next_question(history):
    # Try pipeline style first, fallback to simple call
    try:
        response = generator(
            history,
            max_new_tokens=200,
            do_sample=True,
            temperature=0.7,
            pad_token_id=(getattr(tokenizer, "eos_token_id", None) or getattr(tokenizer, "pad_token_id", None))
        )
    except TypeError:
        response = generator(history)

    # Normalize response
    if isinstance(response, list) and len(response) > 0:
        if isinstance(response[0], dict) and "generated_text" in response[0]:
            generated_text = response[0]["generated_text"]
        else:
            generated_text = str(response[0])
    else:
        generated_text = str(response)

    # Remove the input history part
    new_part = generated_text.replace(history, "").strip()

    # Strip unwanted prefixes like "Interviewer:" or "**Interviewer:**"
    new_part = re.sub(r'^\**\s*Interviewer:\**\s*', "", new_part, flags=re.IGNORECASE)

    # Take only the first line as the question
    match = re.search(r'^(.*?)(?:\n|$)', new_part)
    return match.group(1).strip() if match else None
