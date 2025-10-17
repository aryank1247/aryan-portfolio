
import streamlit as st

# ----- Page Configuration -----
st.set_page_config(page_title="Aryan Kohli | Portfolio", page_icon="🌐", layout="wide")

# ----- Custom CSS for Styling -----
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #0a8f8f, #003b70);
        color: #f5f5f5;
    }
    .main {
        background: transparent;
    }
    .project-card {
        padding: 1.5rem;
        background-color: rgba(255, 255, 255, 0.07);
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        transition: all 0.3s ease-in-out;
    }
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.5);
    }
    h1, h2, h3, h4 {
        color: #e8f9f9;
        font-weight: 600;
    }
    footer {
        text-align: center;
        padding-top: 2rem;
        font-size: 0.9rem;
        opacity: 0.8;
        color: #cde3e3;
    }
    </style>
""", unsafe_allow_html=True)

# ----- Navigation -----
tabs = st.tabs(["🏠 Home", "🧠 Projects", "📫 Contact"])

# ----- Home Section -----
with tabs[0]:
    st.title("👋 Hi, I'm Aryan Kohli")
    st.markdown(
        """
        I'm a **Health Sciences student** and aspiring **AI developer** passionate about building data‑driven solutions that merge 
        technology, healthcare, and innovation.
        
        This site showcases some of my projects — feel free to explore and connect with me!
        """
    )

# ----- Projects Section -----
with tabs[1]:
    st.header("💡 My Projects")
    st.markdown("*(You can fill in descriptions and links later)*")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='project-card'><h3>🧩 AI Study Assistant</h3><p>Project placeholder — add your details here.</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='project-card'><h3>📈 Stock Predictor App</h3><p>Project placeholder — add your details here.</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='project-card'><h3>📊 Analytical Dashboard</h3><p>Project placeholder — add your details here.</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='project-card'><h3>💼 Business Report</h3><p>Project placeholder — add your details here.</p></div>", unsafe_allow_html=True)

# ----- Contact Section -----
with tabs[2]:
    st.header("📫 Get in Touch")
    st.markdown("""
    <p>Let's connect or collaborate! You can reach me here:</p>
    <ul>
        <li>🌐 <a href="https://www.linkedin.com/in/aryan-kohli-2296932b6/" target="_blank" style="color:#9ef0f0;">LinkedIn</a></li>
        <li>💻 <a href="https://github.com/aryank1247" target="_blank" style="color:#9ef0f0;">GitHub</a></li>
    </ul>
    """, unsafe_allow_html=True)

# ----- Footer -----
st.markdown("<footer>© 2025 Aryan Kohli — All Rights Reserved</footer>", unsafe_allow_html=True)
