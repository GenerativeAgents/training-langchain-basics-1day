import streamlit as st
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, ToolMessage
from langchain_core.tools import create_retriever_tool
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langgraph.graph.graph import CompiledGraph
from langgraph.prebuilt import create_react_agent


def create_agent_chain() -> CompiledGraph:
    embedding = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = Chroma(
        embedding_function=embedding,
        persist_directory="./tmp/chroma",
    )
    retriever = vector_store.as_retriever()
    retriever_tool = create_retriever_tool(
        retriever=retriever,
        name="langchain-retriever",
        description="Retriever for langchain documents",
    )
    tools = [retriever_tool]

    model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    return create_react_agent(model=model, tools=tools)


def show_message(message: BaseMessage) -> None:
    if isinstance(message, HumanMessage):
        # ユーザーの入力の場合、そのまま表示する
        with st.chat_message(message.type):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        if len(message.tool_calls) == 0:
            # Function callingが選択されなかった場合、メッセージを表示する
            with st.chat_message(message.type):
                st.write(message.content)
        else:
            # Function callingが選択された場合、ツール名と引数を表示する
            for tool_call in message.tool_calls:
                with st.chat_message(message.type):
                    st.write(
                        f"'{tool_call['name']}' を {tool_call['args']} で実行します",
                    )
    elif isinstance(message, ToolMessage):
        # ツールの実行結果を折りたたんで表示する
        with st.chat_message(message.type):
            with st.expander(label="ツールの実行結果"):
                st.write(message.content)
    else:
        raise ValueError(f"Unknown message type: {message}")


def app() -> None:
    load_dotenv(override=True)

    st.title("RAG")

    # 会話履歴を初期化
    if "messages" not in st.session_state:
        st.session_state.messages = []
    messages: list[BaseMessage] = st.session_state.messages

    # 会話履歴を表示
    for message in messages:
        show_message(message)

    # ユーザーの入力を受け付ける
    human_message = st.chat_input()
    if not human_message:
        return

    # ユーザーの入力を表示
    with st.chat_message("human"):
        st.write(human_message)

    # ユーザーの入力を会話履歴に追加
    messages.append(HumanMessage(content=human_message))

    # 応答を生成
    agent = create_agent_chain()
    for s in agent.stream({"messages": messages}, stream_mode="values"):  # type: ignore[assignment]
        message = s["messages"][-1]

        # ユーザーの入力はスキップ
        if isinstance(message, HumanMessage):
            continue

        # 応答を表示
        show_message(message)

        # 会話履歴に追加
        messages.append(message)


app()
