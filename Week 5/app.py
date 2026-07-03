import streamlit as st
import os

from src.agent import run_agent
from src.utils import save_uploaded_file, clear_uploads_folder
from src.pdf_loader import extract_text
from src.chunker import create_chunks
from src.embeddings import get_embeddings
from src.vector_store import store_chunks, delete_by_document

st.set_page_config(page_title="Week 5: Agentic RAG")

st.title("Self-Correcting Research Agent")

if "indexed_files" not in st.session_state:
    st.session_state.indexed_files = set()

with st.sidebar:
    st.header("Document Upload")
    uploaded_files = st.file_uploader("Upload PDFs for local search", type=["pdf"], accept_multiple_files=True)
    
    if st.button("Process Documents", disabled=not uploaded_files):
        with st.spinner("Processing..."):
            clear_uploads_folder()
            for pdf in uploaded_files:
                try:
                    file_path = save_uploaded_file(pdf)

                    if pdf.name in st.session_state.indexed_files:
                        delete_by_document(pdf.name)

                    pages = extract_text(file_path)
                    chunks = create_chunks(pages)

                    texts = [c["text"] for c in chunks]
                    embeddings = get_embeddings(texts)

                    store_chunks(chunks, embeddings, pdf.name)

                    st.session_state.indexed_files.add(pdf.name)
                except Exception as e:
                    st.error(f"Error indexing {pdf.name}: {e}")
            st.success("Documents ready for search!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        if msg.get("logs"):
            with st.expander("View Agent Logs"):
                st.code(msg["logs"], language="text")
        st.markdown(msg["content"])

query = st.chat_input("Ask a research question (try math, web search, or doc search)...")

if query:
    st.session_state.chat_history.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)
        
    with st.chat_message("assistant"):
        st_placeholder = st.empty()
        
        log_msgs = []
        def update_log(msg):
            log_msgs.append(msg)
            st_placeholder.code("\n".join(log_msgs), language="text")
            
        with st.spinner("Agent is working..."):
            final_report = run_agent(query, update_callback=update_log)
            
        st.markdown("### Final Report")
        st.markdown(final_report)
        
    st.session_state.chat_history.append({
        "role": "assistant", 
        "content": final_report,
        "logs": "\n".join(log_msgs)
    })
