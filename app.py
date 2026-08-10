import streamlit as st
from pathlib import Path
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq
from urllib.parse import quote_plus
from langchain_community.utilities.sql_database import SQLDatabase
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="LangChain SQL Chat",
    page_icon="🤖",
    layout="centered"
)

st.title("LangChain: Chat with SQL Database")

# ==========================================
# GROQ API KEY
# ==========================================


groq_api = st.secrets.get("GROQ_API_KEY", "")

if not groq_api:
    st.error("GROQ_API_KEY is not configured in Streamlit Secrets.")
    st.stop()

# ==========================================
# DATABASE SELECTION
# ==========================================

LOCALDB = "USE_LOCALDB"
MYSQLDB = "USE_MYSQL"

radio_option = [
    "Use SQLite3 Database(student.db)",
    "Connect To MySQL Database"
]

selected_option = st.sidebar.radio(
    "Choose the DB you want to chat with",
    options=radio_option
)

# ==========================================
# MYSQL CONFIGURATION
# ==========================================

if selected_option == "Connect To MySQL Database":

    db_uri = MYSQLDB

    mysql_host = st.sidebar.text_input(
        "Provide MySQL Hostname",
        value="127.0.0.1"
    )

    mysql_user = st.sidebar.text_input(
        "Provide MySQL Username",
        value="root"
    )

    mysql_password = st.sidebar.text_input(
        "Provide MySQL Password",
        type="password"
    )

    mysql_db = st.sidebar.text_input(
        "Provide MySQL Database Name"
    )

else:

    db_uri = LOCALDB

# ==========================================
# GROQ MODEL
# ==========================================

model = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    groq_api_key=groq_api,
    streaming=True
)

# ==========================================
# DATABASE CONFIGURATION
# ==========================================

@st.cache_resource(ttl=7200)
def configure_db(
    db_uri,
    mysql_host=None,
    mysql_user=None,
    mysql_password=None,
    mysql_db=None
):

    # ------------------------------
    # SQLITE DATABASE
    # ------------------------------

    if db_uri == LOCALDB:

        dbfilepath = (
            Path(__file__).parent / "student.db"
        ).absolute()

        creator = lambda: sqlite3.connect(
            f"file:{dbfilepath}?mode=ro",
            uri=True
        )

        return SQLDatabase(
            create_engine(
                f"sqlite:///{dbfilepath}",
                creator=creator
            )
        )

    # ------------------------------
    # MYSQL DATABASE
    # ------------------------------

    elif db_uri == MYSQLDB:

        if not (
            mysql_host
            and mysql_user
            and mysql_db
        ):
            st.error(
                "Please provide Host, Username and Database Name."
            )
            st.stop()

        if mysql_password:

            encoded_password = quote_plus(
                mysql_password
            )

            connection_str = (
                f"mysql+mysqlconnector://"
                f"{mysql_user}:{encoded_password}"
                f"@{mysql_host}:3306/"
                f"{mysql_db}"
            )

        else:

            connection_str = (
                f"mysql+mysqlconnector://"
                f"{mysql_user}@{mysql_host}:3306/"
                f"{mysql_db}"
            )

        try:

            db = SQLDatabase(
                create_engine(connection_str)
            )

            st.success(
                "Connected to MySQL Database"
            )

            return db

        except Exception as e:

            st.error(
                f"Error connecting to MySQL Database: {e}"
            )

            st.stop()


# ==========================================
# INITIALIZE DATABASE
# ==========================================

if db_uri == MYSQLDB:

    db = configure_db(
        db_uri,
        mysql_host=mysql_host,
        mysql_user=mysql_user,
        mysql_password=mysql_password,
        mysql_db=mysql_db
    )

else:

    db = configure_db(db_uri)


# ==========================================
# SQL TOOLKIT
# ==========================================

toolkit = SQLDatabaseToolkit(
    db=db,
    llm=model
)

# ==========================================
# SQL AGENT
# ==========================================

agent = create_sql_agent(
    llm=model,
    toolkit=toolkit,
    agent_type="tool-calling",
    verbose=True
)

# ==========================================
# CHAT HISTORY
# ==========================================

if (
    "messages" not in st.session_state
    or st.sidebar.button("Clear Message History")
):

    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "Hello! How can I help you today?"
        }
    ]

# Display existing messages
for msg in st.session_state["messages"]:

    st.chat_message(
        msg["role"]
    ).write(
        msg["content"]
    )

# ==========================================
# CHAT INPUT
# ==========================================

user_query = st.chat_input(
    placeholder="Ask a question from your database..."
)

if user_query:

    # Add user message
    st.session_state["messages"].append(
        {
            "role": "user",
            "content": user_query
        }
    )

    st.chat_message(
        "user"
    ).write(user_query)

    # Assistant response
    with st.chat_message("assistant"):

        streamlit_callback = (
            StreamlitCallbackHandler(
                st.container()
            )
        )

        try:

            response = agent.invoke(
                {"input": user_query},
                config={
                    "callbacks": [
                        streamlit_callback
                    ]
                }
            )

            response_text = response["output"]

            st.session_state["messages"].append(
                {
                    "role": "assistant",
                    "content": response_text
                }
            )

            st.write(response_text)

        except Exception as e:

            st.error(
                f"Error: {e}"
            )
