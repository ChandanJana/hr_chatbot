from sql_search import execute_query


def main():

    while True:

        question = input("\nAsk SQL query (or exit): ").strip()

        if question.lower() == "exit":
            break

        try:

            rows = execute_query(question)

            print("\nResult:\n")

            for row in rows:

                print(row)

        except Exception as e:

            print("Error:", e)


if __name__ == "__main__":

    main()