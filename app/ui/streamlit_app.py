import streamlit as st

from app.workflows.graph import graph

st.set_page_config(
    page_title="Enterprise IT Copilot",
    layout="wide"
)

st.title(
    "Enterprise IT Operations Copilot"
)

st.markdown(
    "Multi-Agent RAG + LangGraph + ChromaDB"
)

query = st.text_area(
    "Describe your IT issue"
)

if st.button("Submit"):

    state = {

        "query": query,

        "retrieved_docs": [],

        "diagnosis": "",

        "tool_results": {},

        "resolution": "",

        "response": "",

        "execution_path": [],

        "monitoring": {},

        "need_tool": False,

        "route": "",

        "error": ""
    }

    with st.spinner(
        "Running agents..."
    ):

        result = graph.invoke(
            state
        )

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Response",
            "Retrieved Docs",
            "Tools",
            "Monitoring"
        ]
    )

    with tab1:

        st.markdown(
            result["response"]
        )

    with tab2:

        for doc in result["retrieved_docs"]:

            st.write(
                doc.page_content
            )

    with tab3:

        st.json(
            result["tool_results"]
        )

    with tab4:

        st.json(
            result["monitoring"]
        )

        st.write(
            result["execution_path"]
        )