import fitz


def extract_text_from_pdf(pdf_file):
    text = ""
    doc = fitz.open(pdf_file)
    for page in doc:
        text += page.get_text()
    return text

# Extract text from your PDF documents
document1_content = extract_text_from_pdf("semaphores.pdf")
document2_content = extract_text_from_pdf("exact model.pdf")

import openai
openai.api_key = "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"

def chat_with_gpt3(user_input, document_content):
    prompt = f"User: {user_input}\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        context=document_content,
    )
    return response.choices[0].text

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = chat_with_gpt3(user_input, document1_content + document2_content)
    print("AI:", response)

