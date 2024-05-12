import mysql.connector
import speech_recognition as sr

# Establish database connection
db_connection = mysql.connector.connect(
    host="your_host",
    user="your_user",
    password="your_password",
    database="your_database"
)

# Initialize speech recognition
recognizer = sr.Recognizer()

def get_user_input():
    # Get user input (either voice or text)
    try:
        with sr.Microphone() as source:
            print("Speak or type your query:")
            audio = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        user_input = input("Enter your query: ")

    return user_input

def search_database(query):
    cursor = db_connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def main():
    user_query = get_user_input()
    sql_query = f"SELECT * FROM your_table WHERE column_name LIKE '%{user_query}%'"
    search_result = search_database(sql_query)

    if search_result:
        print("Search results:")
        for row in search_result:
            print(row)
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
