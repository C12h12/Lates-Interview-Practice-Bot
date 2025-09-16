from pdf_utils import extract_text_from_pdf
from interview import run_interview

resume_path = "C:\\Users\\Chaitanya\\Desktop\\Resume\\Chaitanya_Thakre.pdf"  # change if docx
job_desc_path ="C:\\Users\\Chaitanya\\Desktop\\full_stack_developer_job_description.txt"

resume_text = extract_text_from_pdf(resume_path)
job_desc_text = extract_text_from_pdf(job_desc_path)

level = input("Select interview difficulty (easy/moderate/experienced): ").lower()

if input("Start the interview? (y/n): ").lower() == "y":
    results = run_interview(level, job_desc_text, resume_text)
    print("\n✅ Evaluation Summary:")
    for r in results:
        print(r)
else:
    print("Interview canceled.")
