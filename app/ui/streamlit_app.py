import sys
import os

# Ensure the project root is on the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import streamlit as st
from app.workflows.graph import graph
from app.tools.system_status_tool import get_system_status

st.set_page_config(
    page_title="Enterprise IT Copilot",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Premium custom CSS styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    font-family: 'Outfit', sans-serif;
    background-color: #0b0f19 !important;
    color: #e2e8f0;
}

.block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
}

.glass-card {
    background: rgba(17, 24, 39, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    margin-bottom: 16px;
}

.header-container {
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    padding: 35px;
    margin-bottom: 25px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
}

.header-title {
    font-size: 2.6rem;
    font-weight: 700;
    background: linear-gradient(to right, #38bdf8, #a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0 0 8px 0;
}

.header-subtitle {
    font-size: 1.05rem;
    color: #94a3b8;
    margin: 0;
}

div.stButton > button {
    background: linear-gradient(to right, #0284c7, #7c3aed);
    color: white !important;
    font-weight: 600;
    border: none !important;
    padding: 10px 28px !important;
    border-radius: 8px !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 4px 14px rgba(124, 58, 237, 0.3) !important;
}

div.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(124, 58, 237, 0.5) !important;
    background: linear-gradient(to right, #0369a1, #6d28d9) !important;
    border: none !important;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background-color: rgba(15, 23, 42, 0.4);
    padding: 6px;
    border-radius: 10px;
    border: 1px solid rgba(255, 255, 255, 0.05);
}

.stTabs [data-baseweb="tab"] {
    height: 44px;
    background-color: transparent;
    border-radius: 8px;
    color: #94a3b8;
    font-weight: 500;
    border: none;
    transition: all 0.2s ease;
    padding-left: 16px;
    padding-right: 16px;
}

.stTabs [aria-selected="true"] {
    background-color: rgba(124, 58, 237, 0.15) !important;
    color: #c084fc !important;
    border: 1px solid rgba(124, 58, 237, 0.3) !important;
}

.pipeline-container {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 12px;
    margin: 20px 0;
}

.pipeline-step {
    background: rgba(30, 41, 59, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 10px 18px;
    border-radius: 8px;
    font-size: 0.85rem;
    font-weight: 600;
    color: #cbd5e1;
}

.pipeline-step.active {
    background: linear-gradient(135deg, rgba(124, 58, 237, 0.2) 0%, rgba(56, 189, 248, 0.2) 100%);
    border: 1px solid rgba(124, 58, 237, 0.4);
    color: #c084fc;
    box-shadow: 0 0 15px rgba(124, 58, 237, 0.15);
}

.pipeline-arrow {
    color: #475569;
    font-weight: bold;
    font-size: 1.1rem;
}

.metric-card {
    background: rgba(17, 24, 39, 0.8);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 10px;
    padding: 14px 18px;
    text-align: center;
}

.metric-label {
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #64748b;
    margin-bottom: 4px;
}

.metric-value {
    font-size: 1.3rem;
    font-weight: 700;
    color: #c084fc;
}
</style>
""", unsafe_allow_html=True)

# ── Header ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-container">
    <h1 class="header-title">Enterprise IT Operations Copilot</h1>
    <p class="header-subtitle">Multi-Agent RAG Orchestration · LangGraph · ChromaDB · Hugging Face Llama 3.1</p>
</div>
""", unsafe_allow_html=True)

# ── Live Service Status Dashboard ───────────────────────────────────────────
st.markdown("### 🖥️ Live Service Operations Dashboard")
status_info = get_system_status.invoke({})
cols = st.columns(len(status_info))
for i, (svc, stat) in enumerate(status_info.items()):
    with cols[i]:
        badge_color = "#10b981" if str(stat).upper() == "UP" else "#ef4444"
        st.markdown(f"""
        <div class="glass-card" style="text-align: center; padding: 14px 10px; margin-bottom: 20px;">
            <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; color: #94a3b8; margin-bottom: 6px;">{svc} STATUS</div>
            <div style="font-size: 1.25rem; font-weight: 700; color: {badge_color}; display: flex; align-items: center; justify-content: center; gap: 8px;">
                <span style="height: 10px; width: 10px; background-color: {badge_color}; border-radius: 50%; display: inline-block;"></span>
                {stat}
            </div>
        </div>
        """, unsafe_allow_html=True)

# ── Query Input ──────────────────────────────────────────────────────────────
st.markdown("### 💬 Submit IT Support Query")
query = st.text_area(
    "Describe the technical issue, request, or symptom you are experiencing:",
    placeholder="e.g. VPN not connecting after software update, or I need to reset my password.",
    height=100
)

if st.button("🚀 Submit Query"):
    if not query.strip():
        st.warning("Please describe your issue first.")
    else:
        # Updated initial state with all new fields
        state = {
            "query":           query,
            "rewritten_query": "",
            "retrieved_docs":  [],
            "sources":         [],
            "diagnosis":       "",
            "category":        "",
            "tool_results":    {},
            "resolution":      "",
            "response":        "",
            "execution_path":  [],
            "monitoring":      {},
            "need_tool":       False,
            "route":           "",
            "retry_count":     0,
            "error":           "",
            "start_time":      0.0,
        }

        with st.spinner("🤖 Orchestrating agents — classifying, retrieving, diagnosing, resolving..."):
            result = graph.invoke(state)

        monitoring = result.get("monitoring", {})

        # ── Quick Metrics Row ─────────────────────────────────────────────
        st.markdown("### 📈 Run Summary")
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown(f"""<div class="metric-card">
                <div class="metric-label">Category</div>
                <div class="metric-value">{result.get('category', 'N/A')}</div>
            </div>""", unsafe_allow_html=True)
        with m2:
            st.markdown(f"""<div class="metric-card">
                <div class="metric-label">Latency</div>
                <div class="metric-value">{monitoring.get('latency_seconds', '—')}s</div>
            </div>""", unsafe_allow_html=True)
        with m3:
            status_color = "#10b981" if monitoring.get("workflow_status") == "success" else "#ef4444"
            st.markdown(f"""<div class="metric-card">
                <div class="metric-label">Status</div>
                <div class="metric-value" style="color:{status_color}">{monitoring.get('workflow_status', 'N/A').upper()}</div>
            </div>""", unsafe_allow_html=True)
        with m4:
            st.markdown(f"""<div class="metric-card">
                <div class="metric-label">Tool Retries</div>
                <div class="metric-value">{result.get('retry_count', 0)}</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### 🔍 Investigation Results")

        tab1, tab2, tab3, tab4 = st.tabs([
            "📋 Diagnostic Response",
            "📖 Retrieved Knowledge Base",
            "🛠️ System Tools & Integration",
            "📊 Agent Monitoring"
        ])

        # ── Tab 1: Response ───────────────────────────────────────────────
        with tab1:
            st.markdown("""
            <div class="glass-card" style="border-left: 4px solid #7c3aed; padding-top: 15px;">
                <div style="font-size: 1.1rem; font-weight: 700; color: #c084fc; margin-bottom: 12px;">AI Resolution Output</div>
            """, unsafe_allow_html=True)
            st.markdown(result["response"])
            st.markdown("</div>", unsafe_allow_html=True)

        # ── Tab 2: Retrieved Docs ─────────────────────────────────────────
        with tab2:
            st.markdown("#### 📖 Matching Knowledge Articles")
            retrieved = result.get("retrieved_docs", [])
            sources = result.get("sources", [])

            if not retrieved:
                st.info("No knowledge articles were retrieved for this query.")
            else:
                for idx, doc_text in enumerate(retrieved):
                    source_name = sources[idx] if idx < len(sources) else "Unknown Source"
                    st.markdown(f"""
                    <div class="glass-card" style="border-left: 4px solid #38bdf8; margin-bottom: 12px; padding: 18px;">
                        <div style="font-weight: 600; color: #38bdf8; margin-bottom: 8px; font-size: 0.95rem;">
                            📄 Article {idx + 1}: <span style="color: #cbd5e1; font-weight: normal;">{source_name}</span>
                        </div>
                        <div style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.6; white-space: pre-wrap;">{doc_text}</div>
                    </div>
                    """, unsafe_allow_html=True)

        # ── Tab 3: Tools ──────────────────────────────────────────────────
        with tab3:
            st.markdown("#### 🛠️ Automated Tools Executed")
            tool_results = result.get("tool_results", {})
            if not tool_results:
                st.info("No integration tools were required to resolve this query.")
            else:
                col1, col2 = st.columns(2)
                if "system_status" in tool_results:
                    with col1:
                        st.markdown("""
                        <div class="glass-card" style="border-left: 4px solid #f59e0b;">
                            <h5 style="margin: 0 0 12px 0; color: #f59e0b;">🖥️ System Diagnostics</h5>
                        """, unsafe_allow_html=True)
                        st.json(tool_results["system_status"])
                        st.markdown("</div>", unsafe_allow_html=True)
                if "ticket" in tool_results:
                    with col2:
                        st.markdown("""
                        <div class="glass-card" style="border-left: 4px solid #10b981;">
                            <h5 style="margin: 0 0 12px 0; color: #10b981;">🎫 IT Support Ticket</h5>
                        """, unsafe_allow_html=True)
                        st.json(tool_results["ticket"])
                        st.markdown("</div>", unsafe_allow_html=True)
                # Extra tools if present
                for key in ["software_check", "asset_info"]:
                    if key in tool_results:
                        st.markdown(f"**{key.replace('_', ' ').title()}:**")
                        st.json(tool_results[key])

            if result.get("error"):
                st.error(f"⚠️ Tool Error: {result['error']}")

        # ── Tab 4: Monitoring ─────────────────────────────────────────────
        with tab4:
            st.markdown("#### 📊 Agent Execution Pipeline")
            path = result.get("execution_path", [])
            pipeline_html = '<div class="pipeline-container">'
            for i, step in enumerate(path):
                pipeline_html += f'<div class="pipeline-step active">{step.upper()}</div>'
                if i < len(path) - 1:
                    pipeline_html += '<div class="pipeline-arrow">➔</div>'
            pipeline_html += '</div>'
            st.markdown(pipeline_html, unsafe_allow_html=True)

            st.markdown("#### ⏱️ Monitoring Metadata")
            st.json(monitoring)

            if result.get("sources"):
                st.markdown("#### 📄 Knowledge Sources Used")
                for s in result["sources"]:
                    st.markdown(f"- `{s}`")