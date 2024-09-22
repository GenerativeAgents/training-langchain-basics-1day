import streamlit as st
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders import GitLoader
from langchain_openai import OpenAIEmbeddings


def app() -> None:
    load_dotenv(override=True)

    st.title("Indexing")

    clicked = st.button("実行")
    if not clicked:
        return

    def file_filter(file_path: str) -> bool:
        return file_path.endswith(".mdx")

    loader = GitLoader(
        clone_url="https://github.com/langchain-ai/langchain",
        repo_path="./tmp/langchain",
        branch="master",
        file_filter=file_filter,
    )

    with st.spinner("Loading documents..."):
        documents = loader.load()

    st.info(f"{len(documents)} documents loaded.")

    embedding = OpenAIEmbeddings(model="text-embedding-3-small")

    with st.spinner("Indexing documents..."):
        Chroma.from_documents(
            documents=documents,
            embedding=embedding,
            persist_directory="./tmp/chroma",
        )

    st.success("Indexing completed.")


app()
