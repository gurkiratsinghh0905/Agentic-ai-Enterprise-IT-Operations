def response_agent(state):

    state["execution_path"].append("response")

    # Build sources citation section
    sources = state.get("sources", [])
    sources_section = ""
    if sources:
        formatted = " | ".join(f"`{s}`" for s in sources)
        sources_section = f"\n\n---\n📄 **Sources:** {formatted}"

    # Build ticket section if a ticket was created
    ticket_section = ""
    ticket = state.get("tool_results", {}).get("ticket")
    if ticket:
        ticket_section = (
            f"\n\n---\n"
            f"🎫 **Support Ticket Created**\n"
            f"- Ticket ID: `{ticket['ticket_id']}`\n"
            f"- Status: `{ticket['status']}`"
        )

    # Build category + retry info for transparency
    meta_parts = []
    if state.get("category"):
        meta_parts.append(f"**Category:** {state['category']}")
    if state.get("retry_count", 0) > 0:
        meta_parts.append(f"**Tool Retries:** {state['retry_count']}")
    if state.get("error"):
        meta_parts.append(f"**⚠️ Error:** {state['error']}")
    meta_section = "  |  ".join(meta_parts)

    state["response"] = f"""## 🔍 Diagnosis

{state['diagnosis']}

---

## ✅ Resolution

{state['resolution']}
{sources_section}
{ticket_section}

---
{meta_section}
"""

    return state