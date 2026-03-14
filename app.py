from src.rag_pipeline import build_rag, query_rag


def main():

    pdf_path = input("Enter PDF path: ")

    index, chunks = build_rag(pdf_path)

    while True:

        question = input("\nAsk a question (type exit to quit): ")

        if question.lower() == "exit":
            break

        answer = query_rag(index, chunks, question)

        print("\nAnswer:\n")
        print(answer)


if __name__ == "__main__":
    main()