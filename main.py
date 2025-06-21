from dotenv import load_dotenv
import contextualsearch as rag

def main():
    load_dotenv()
    print("Running ai-fest app...")
    #rag.chat_using_simple_questions()
    #rag.chat_about_web_page_data()
    rag.chat_about_pdf_document()

if __name__ == "__main__":
    main()
