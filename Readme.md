# 🤖 LangChain AI Chat with SQL Database

An **AI-powered conversational SQL application** built with **Python, Streamlit, LangChain, and Groq LLM** that allows users to interact with SQL databases using natural language.

Instead of writing SQL queries manually, users can simply ask questions such as:

> "Show me all students."

> "How many students are there?"

> "Which student has the highest marks?"

The LangChain SQL Agent understands the user's question, generates the required SQL query, executes it against the connected database, and returns the result in a conversational format.

---

## 🚀 Features

* 🤖 **AI-powered SQL Agent**
* 🦜🔗 **LangChain SQL Agent integration**
* ⚡ **Groq LLM with Llama 3.3 70B**
* 💬 **Natural Language Database Chat**
* 🗄️ **SQLite3 database support**
* 🐬 **MySQL database support**
* 🔐 **Secure Groq API key input**
* 🔑 **MySQL authentication**
* 📊 **Automatic SQL query generation**
* 🔍 **Database schema understanding**
* ⚡ **Streaming LLM responses**
* 🧠 **Conversational chat history**
* 🧹 **Clear chat history functionality**
* 🎨 **Interactive Streamlit UI**
* 🔎 **LangChain Streamlit callback visualization**

---

# 🏗️ Architecture


                    ┌──────────────────────┐
                    │        User          │
                    │ Natural Language     │
                    │       Query          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Streamlit UI     │
                    │     Chat Interface   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    LangChain SQL     │
                    │        Agent         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Groq LLM        │
                    │ Llama 3.3 70B Model  │
                    └──────────┬───────────┘
                               │
                         SQL Generation
                               │
                               ▼
              ┌────────────────────────────────┐
              │          SQL Database           │
              │                                │
              │      ┌───────────────┐         │
              │      │    SQLite     │         │
              │      └───────────────┘         │
              │               OR               │
              │      ┌───────────────┐         │
              │      │     MySQL     │         │
              │      └───────────────┘         │
              └────────────────┬───────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Query Results     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   AI Generated       │
                    │      Response        │
                    └──────────────────────┘
```

---

# 🛠️ Tech Stack

| Technology       | Purpose                          
| ---------------- | -------------------------------  |
| 🐍 Python        | Application development         |
| 🎨 Streamlit     | Web interface                   |
| 🦜🔗 LangChain  | LLM orchestration and SQL agent |
| ⚡ Groq          | Fast LLM inference              |
| 🧠 Llama 3.3 70B | Natural language understanding  |
| 🗄️ SQLite3       | Local database                  |
| 🐬 MySQL         | Remote/production database      |
| 🔗 SQLAlchemy    | Database connection layer       |
| 🔐 Python-dotenv | Environment variable management |

---

# 🧠 How the Application Works

The application follows a simple AI-to-database workflow.

### 1. Select Database

The user can choose between:

```text
SQLite3 Database
        OR
MySQL Database
```

The application provides a sidebar interface for selecting the database.

---

### 2. Configure Database

### SQLite

The application automatically connects to:

```text
student.db
```

The SQLite database is opened in **read-only mode** to prevent accidental modification.

### MySQL

The user can provide:

```text
MySQL Host
MySQL Username
MySQL Password
MySQL Database Name
```

The application then creates a MySQL connection using SQLAlchemy.

---

### 3. Provide Groq API Key

The user enters their Groq API key through the Streamlit sidebar.

The application uses:

```text
Llama 3.3 70B Versatile
```

for natural-language understanding and SQL reasoning.

The API key is not hardcoded into the application.

---

### 4. LangChain SQL Agent

The application creates a SQL toolkit:

```python
toolkit = SQLDatabaseToolkit(
    db=db,
    llm=model
)
```

The SQL agent is then created using:

```python
agent = create_sql_agent(
    llm=model,
    toolkit=toolkit,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
```

This allows the LLM to interact with the database through LangChain's SQL tools.

---

### 5. Natural Language Query

The user can ask questions directly from the chat interface.

For example:

```text
How many students are in the database?
```

The agent determines what SQL operation is required.

Conceptually:

```text
User Question
      ↓
LLM Reasoning
      ↓
SQL Query Generation
      ↓
Database Execution
      ↓
Result
      ↓
Natural Language Answer
```

---

# 💬 Example Queries

You can ask questions such as:

```text
Show all students.
```

```text
How many students are there?
```

```text
Show the students with marks greater than 80.
```

```text
Who has the highest marks?
```

```text
What is the average marks of all students?
```

```text
Show the top 5 students.
```

For MySQL databases, you can ask questions based on your own database tables and data.

---

# 📂 Project Structure

Recommended project structure:

```text
AI-SQL-Chatbot/
│
├── app.py
├── student.db
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

### File Description

| File               | Description                |
| ------------------ | -------------------------- |
| `app.py`           | Main Streamlit application |
| `student.db`       | Local SQLite database      |
| `requirements.txt` | Required Python packages   |
| `.env`             | Environment variables      |
| `.gitignore`       | Files excluded from Git    |
| `README.md`        | Project documentation      |

> If your Python file has a different name, replace `app.py` with your actual filename.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Move into the project directory:

```bash
cd YOUR_REPOSITORY
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

Create a `requirements.txt` file containing:

```text
streamlit
langchain
langchain-community
langchain-groq
sqlalchemy
mysql-connector-python
python-dotenv
```

You can generate the file automatically from your environment with:

```bash
pip freeze > requirements.txt
```

---

# 🔑 Groq API Key

You can obtain a Groq API key from the Groq developer platform.

For local development, you can store it in a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

However, your current application also allows the user to enter the API key directly through the Streamlit sidebar.

### ⚠️ Important

Never upload your actual API key to GitHub.

Add the following to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

---

# 🗄️ SQLite Database

The application looks for:

```text
student.db
```

in the same directory as the Python application.

The database is accessed using:

```python
dbfilepath = (
    Path(__file__).parent / "student.db"
).absolute()
```

The application uses a read-only SQLite connection:

```python
creator = lambda: sqlite3.connect(
    f"file:{dbfilepath}?mode=ro",
    uri=True
)
```

This helps prevent accidental modifications to the local database.

---

# 🐬 MySQL Configuration

To use MySQL, select:

```text
Connect To MySQL Database
```

from the Streamlit sidebar.

Then provide:

```text
Hostname
Username
Password
Database Name
```

The application creates a connection using:

```text
mysql+mysqlconnector://
```

Example:

```text
mysql+mysqlconnector://username:password@127.0.0.1:3306/database_name
```

The password is URL-encoded using Python's `quote_plus()` before being added to the connection string.

---

# ▶️ Run the Application

Start Streamlit using:

```bash
streamlit run app.py
```

The application will open in your browser.

You should see:

```text
Langchain: Chat with SQL Database
```

---

# 🖥️ Application Workflow

```text
Launch Application
       ↓
Select Database
       ↓
┌───────────────────────┐
│ SQLite3 OR MySQL      │
└───────────┬───────────┘
            ↓
     Configure Database
            ↓
      Enter Groq API Key
            ↓
       Initialize LLM
            ↓
     Initialize SQL Agent
            ↓
      Ask Database Query
            ↓
     LangChain Reasoning
            ↓
       Execute SQL
            ↓
      Return AI Response
```

---

# 🔄 Chat History

The application maintains conversation history using Streamlit session state:

```python
st.session_state["messages"]
```

This allows previous user and assistant messages to remain visible during the session.

The sidebar also provides:

```text
Clear Message History
```

to reset the conversation.

---

# ⚡ Streaming Responses

The application uses:

```python
streaming=True
```

with the Groq chat model.

It also integrates:

```python
StreamlitCallbackHandler
```

to display the agent's execution process within the Streamlit interface.

---

# 🔐 Security

This project is designed primarily for learning and demonstration purposes.

For production deployment, consider implementing:

* 🔒 Read-only database credentials
* 🔐 Secret management
* 🛡️ SQL query validation
* 👤 User authentication
* 🚫 Restrictions on destructive SQL commands
* 🔑 Role-based database access
* 📊 Query logging and monitoring
* ⏱️ Rate limiting

**Do not provide unrestricted database credentials to an LLM-powered application in a production environment.**

---

# 🚀 Future Improvements

Possible enhancements include:

* 📊 Automatic data visualization
* 📈 Generate charts from SQL results
* 📥 Export query results to CSV/Excel
* 🧠 Improved conversation memory
* 🔐 User authentication
* 🗃️ PostgreSQL support
* ☁️ Cloud database integration
* 🎤 Voice-based database queries
* 📱 Improved responsive UI
* 📜 SQL query history
* 🧪 Automated testing
* 🛡️ Advanced SQL safety layer

---

# 🎯 Learning Outcomes

Through this project, I gained practical experience with:

* Generative AI
* Large Language Models
* LangChain
* AI Agents
* SQL Databases
* Natural Language to SQL
* Groq API
* Llama models
* SQLAlchemy
* MySQL
* SQLite
* Streamlit
* Python
* API integration
* Environment variable management
* Conversational AI

---

# 📸 Screenshots

Add your application screenshots here.

Recommended structure:

```text
screenshots/
│
├── home.png
├── sqlite-chat.png
├── mysql-connection.png
└── query-result.png
```

Then add them to the README:

```markdown
## 📸 Screenshots

![Home](screenshots/home.png)

![SQL Chat](screenshots/sqlite-chat.png)

![MySQL Connection](screenshots/mysql-connection.png)
```

---

# 🌟 Why This Project?

Traditional SQL databases require users to understand SQL syntax.

This project demonstrates how **Generative AI can act as a natural-language interface for structured databases**, allowing users to interact with their data without manually writing SQL queries.

It combines:

```text
Generative AI
      +
LLM
      +
LangChain
      +
SQL
      +
Database
      +
Streamlit
```

to create a practical **AI-powered database assistant**.

---

# 👨‍💻 Author

**Shashank Shekhar Choudhary**

B.Tech Computer Science / Data Science

### Areas of Interest

* 🤖 Generative AI
* 🧠 Machine Learning
* 📊 Data Science
* 🦜🔗 LangChain
* 🗄️ SQL & Databases
* 🐍 Python
* 💻 AI Application Development

---

# ⭐ Show Your Support

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is intended for educational and development purposes.
