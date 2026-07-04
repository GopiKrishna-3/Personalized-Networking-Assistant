import streamlit as st
import requests

API_URL = "http://localhost:8000/api/v1"

st.set_page_config(
    page_title="Networking Assistant",
    page_icon="🤝",
    layout="wide"
)

# Custom CSS injected for better styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    /* Apply modern typography and dark background */
    html, body, [class*="css"], .stApp {
        font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
        background-color: #0A0A0B !important;
        color: #F3F4F6 !important;
    }
    
    .title-text {
        background: -webkit-linear-gradient(135deg, #F9F5E8 0%, #D4AF37 50%, #AA7C11 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.2rem;
        font-weight: 800;
        margin-bottom: 0.1rem;
        letter-spacing: -0.5px;
    }
    
    .subtitle {
        color: #9CA3AF;
        font-size: 1.2rem;
        margin-bottom: 2.5rem;
        line-height: 1.6;
    }
    
    .starter-card {
        background: #16161A;
        border: 1px solid rgba(212, 175, 55, 0.15);
        padding: 1.5rem 1.75rem;
        border-radius: 1rem;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.7);
        border-left: 6px solid #D4AF37;
        margin-bottom: 1.25rem;
        color: #E5E7EB;
        font-size: 1.15rem;
        line-height: 1.6;
        transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.2s ease, border-color 0.2s ease;
    }
    
    .starter-card:hover {
        transform: translateY(-2px) scale(1.01);
        box-shadow: 0 15px 35px -5px rgba(212, 175, 55, 0.15), 0 10px 20px -10px rgba(0, 0, 0, 0.8);
        border-left-color: #F9F5E8;
        border-color: rgba(212, 175, 55, 0.4);
    }
    
    /* Make buttons premium and matched with theme colors */
    .stButton>button {
        border-radius: 0.75rem !important;
        font-weight: 600 !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    /* Primary buttons get the gradient and glow */
    .stButton>button[kind="primary"] {
        background: linear-gradient(135deg, #F9F5E8 0%, #D4AF37 50%, #AA7C11 100%) !important;
        border: none !important;
        color: #0A0A0B !important;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.25) !important;
    }
    
    .stButton>button[kind="primary"]:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4) !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title-text'>🤝 Personalized Networking Assistant</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Generate smart, context-aware conversation starters for your next professional event.</div>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["💡 Generate Starters", "🔍 Quick Fact Check", "📜 History"])

# ----------------- TAB 1: GENERATE STARTERS -----------------
with tab1:
    st.header("Event Details")
    event_description = st.text_area(
        "Event Description", 
        placeholder="e.g., A summit focusing on AI advancements in the healthcare sector..."
    )
    
    interests_input = st.text_input(
        "Your Interests (comma-separated)",
        placeholder="e.g., machine learning, biotech, startups"
    )
    
    if st.button("Generate Starters", type="primary"):
        if not event_description.strip():
            st.warning("Please provide an event description.")
        else:
            interests = [i.strip() for i in interests_input.split(",") if i.strip()]
            
            with st.spinner("Analyzing event and generating starters..."):
                try:
                    res = requests.post(f"{API_URL}/generate-conversation", json={
                        "event_description": event_description,
                        "interests": interests
                    })
                    if res.status_code == 200:
                        data = res.json()
                        st.session_state["generation_id"] = data["generation_id"]
                        st.session_state["starters"] = data["starters"]
                        st.session_state["themes"] = data["themes"]
                        st.success(f"Detected Themes: {', '.join(data['themes'])}")
                    else:
                        st.error(f"Error generating starters: {res.text}")
                except Exception as e:
                    st.error(f"Connection error: {e}")

    # Display generated starters if they exist in session state
    if "starters" in st.session_state:
        st.markdown("### ✨ Your Conversation Starters")
        for i, starter in enumerate(st.session_state["starters"]):
            st.markdown(f"<div class='starter-card'>{starter}</div>", unsafe_allow_html=True)
            
        st.write("Was this helpful?")
        col1, col2, _ = st.columns([1, 1, 8])
        with col1:
            if st.button("👍 Yes"):
                requests.post(f"{API_URL}/feedback", json={
                    "starter_id": st.session_state["generation_id"],
                    "useful": True
                })
                st.toast("Feedback submitted! Thanks.")
        with col2:
            if st.button("👎 No"):
                requests.post(f"{API_URL}/feedback", json={
                    "starter_id": st.session_state["generation_id"],
                    "useful": False
                })
                st.toast("Feedback submitted! Thanks.")

# ----------------- TAB 2: FACT CHECK -----------------
with tab2:
    st.header("Quick Fact Check")
    st.markdown("Look up a quick fact or topic before you talk about it.")
    
    query = st.text_input("Topic to look up", placeholder="e.g., Generative AI")
    
    if st.button("Search Wikipedia"):
        if not query.strip():
            st.warning("Please enter a topic.")
        else:
            with st.spinner(f"Looking up '{query}'..."):
                try:
                    res = requests.get(f"{API_URL}/fact-check", params={"query": query})
                    if res.status_code == 200:
                        data = res.json()
                        if data.get("error"):
                            st.warning(data["summary"])
                        else:
                            st.success("Found it!")
                            st.write(data["summary"])
                            if data.get("source_url"):
                                st.markdown(f"[Read more on Wikipedia]({data['source_url']})")
                    else:
                        st.error(f"Error: {res.text}")
                except Exception as e:
                    st.error(f"Connection error: {e}")


# ----------------- TAB 3: HISTORY -----------------
with tab3:
    st.header("Your Past Conversations")
    if st.button("Refresh History"):
        st.experimental_rerun()
        
    try:
        res = requests.get(f"{API_URL}/history")
        if res.status_code == 200:
            history = res.json().get("history", [])
            if not history:
                st.info("No past generations found.")
            else:
                for entry in reversed(history):
                    with st.expander(f"📅 {entry['timestamp'][:16].replace('T', ' ')}"):
                        st.write(f"**Event**: {entry['event_description']}")
                        if entry.get("themes"):
                            st.write(f"**Themes**: {', '.join(entry['themes'])}")
                        st.write("**Starters generated:**")
                        for s in entry['starters']:
                            st.write(f"- {s}")
                            
                        useful = entry.get("useful")
                        if useful is True:
                            st.write("Feedback: 👍 Useful")
                        elif useful is False:
                            st.write("Feedback: 👎 Not useful")
                        else:
                            st.write("Feedback: None")
    except Exception as e:
        st.error(f"Could not load history: {e}")
