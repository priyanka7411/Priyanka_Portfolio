import streamlit as st
from PIL import Image
import base64
import os
import re
from datetime import datetime

# ---------------------- CONFIG ------------------------
st.set_page_config(
    page_title="Priyanka Malavade Portfolio", 
    page_icon="📊", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for visitor counter
if 'visitors' not in st.session_state:
    st.session_state.visitors = 0
st.session_state.visitors += 1

# ---------------------- SIDEBAR -----------------------
st.sidebar.title("📂 Portfolio Navigation")
page = st.sidebar.radio("Go to", 
    ["🏠 Home", "👩‍💼 About Me", "📁 Projects", "📄 Resume", "📜 Certifications", "📬 Contact"])

# Visitor counter in sidebar
st.sidebar.markdown("---")
st.sidebar.caption(f"👀 Visitors: {st.session_state.visitors}")

# ---------------------- UTILITY FUNCTIONS ------------------------
@st.cache_data
def load_pdf(file_path):
    """Cache PDF loading for better performance"""
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode('utf-8')
    except Exception as e:
        st.error(f"Error loading file: {str(e)}")
        return None

def validate_email(email):
    """Simple email validation"""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# ---------------------- HOME --------------------------
if page == "🏠 Home":
    # Hero Section
    st.markdown("## Hi, I'm Priyanka Malavade 👋")
    st.markdown("#### Data Analyst | Business Intelligence | Data Storyteller")

    st.write("""
    I'm passionate about transforming raw data into meaningful insights that drive impactful business decisions. 
    With a keen eye for detail and a love for visualization, I specialize in analyzing complex datasets, 
    uncovering trends, and turning numbers into compelling stories.
    """)

    st.markdown("---")

    # At A Glance Section
    st.markdown("""
    <div style="background-color:#f0f2f6;padding:20px 30px;border-radius:10px">
        <h4 style="color:#2e4053;margin-top:0;">🔍 At A Glance</h4>
        <ul style="font-size:16px; line-height:1.8">
            <li>5+ Data Projects Completed</li>
            <li>3 Professional Certifications</li>
            <li>Proficient in Python, SQL, Power BI, and Data Visualization</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Quick Navigation Cards
    st.subheader("🚀 Explore My Portfolio")

    cols = st.columns(4)
    card_styles = [
        ("e3f2fd", "👩‍💻 About", "My background & skills"),
        ("e8f5e9", "📂 Projects", "Data analysis work samples"),
        ("fff8e1", "📜 Certifications", "My qualifications"),
        ("f3e5f5", "📬 Contact", "Let’s connect!")
    ]

    for i, (color, title, desc) in enumerate(card_styles):
        with cols[i]:
            st.markdown(f"""
            <div style="background-color:#{color};padding:15px 10px;border-radius:10px;height:110px">
                <h5 style="margin-bottom:5px;">{title}</h5>
                <p style="font-size:14px;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # Call to Action Section
    st.markdown("""
    <div style="text-align:center;padding:25px;background-color:#f5f5f5;border-radius:10px">
        <h3 style="color:#2e4053;">📈 Ready to collaborate?</h3>
        <p style="font-size:16px;">
            Explore my projects or get in touch to discuss how I can add value to your data-driven goals.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------- ABOUT -------------------------
elif page == "👩‍💼 About Me":
    st.header("👩‍💼 About Me", anchor=False)
    
    # Intro Section
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.markdown("""
        <div style="font-size:18px;">
        A results-driven <strong>Data Analyst</strong> with a passion for transforming complex datasets into strategic business insights.<br><br>
        I specialize in <strong>data visualization, predictive analytics</strong>, and crafting clear, data-driven stories that empower business decision-makers.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color:#f0f2f6;padding:15px;border-radius:10px">
        <h4 style="color:#2e4053;margin-top:0;">🔍 Profile Highlights</h4>
        <p>• 1+ Years in Data Analytics & BI</p>
        <p>• Certified in Power BI, SQL & Data Science</p>
        <p>• 5+ Projects & Predictive Models</p>
        <p>• Communicates insights clearly to all stakeholders</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Professional Summary
    st.subheader("📌 Professional Summary")
    st.markdown("""
    <div style="background-color:#f8f9fa;padding:15px;border-radius:10px;border-left:4px solid #4285f4">
    - 1+ years of hands-on experience in <strong>data analysis</strong> and <strong>business intelligence</strong><br>
    - Certified in <strong>Power BI, SQL</strong> and <strong>Data Science</strong> from GUVI<br>
    - Developed 5+ end-to-end data projects including dashboards and predictive models<br>
    - Strong foundation in <strong>statistics, data mining</strong> and <strong>machine learning</strong> concepts<br>
    - Excellent at communicating insights to both technical and non-technical stakeholders
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Education Section
    st.subheader("🎓 Education")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color:#f0f7ff;padding:15px;border-radius:10px">
        <strong>Bachelor of Computer Applications (BCA)</strong><br>
        <em>Oxford College of Computer Applications</em> | 2021–2024<br>
        CGPA: 9.03/10<br>
        <strong>Relevant Coursework:</strong> DBMS, Statistics, Data Structures, Business Analytics
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div style="background-color:#f5f0ff;padding:15px;border-radius:10px">
        <strong>Pre-University (PUC)</strong><br>
        <em>MES Chaitanya PU College</em><br>
        Percentage: 76%<br>
        <strong>Focus:</strong> Mathematics & Computer Science
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Skills Overview
    st.subheader("🛠️ Technical Toolkit")
    cols = st.columns(3)
    
    skills = [
        ("e3f2fd", "📊 Data Analysis", [
            "Python (Pandas, NumPy)",
            "SQL (Advanced)",
            "R Programming",
            "Statistics"
        ]),
        ("e8f5e9", "📈 Visualization", [
            "Power BI (Certified)",
            "Tableau",
            "Matplotlib/Seaborn",
            "Plotly"
        ]),
        ("fff8e1", "🛠️ Tools & Platforms", [
            "Excel (Advanced)",
            "Google BigQuery",
            "Jupyter Notebooks",
            "Git/GitHub"
        ])
    ]
    
    for i, (color, title, items) in enumerate(skills):
        with cols[i]:
            content = "<h4>" + title + "</h4>" + "<br>• ".join([""] + items)
            st.markdown(f"""
            <div style="background-color:#{color};padding:15px;border-radius:10px;height:100%">
            {content}
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Skill Proficiency
    st.subheader("📊 Skill Proficiency")
    skill_levels = {
        "Python (Pandas, NumPy)": 85,
        "Power BI": 90,
        "SQL": 80,
        "Tableau": 75,
        "Excel": 95,
        "Statistics": 85
    }
    
    for skill, level in skill_levels.items():
        st.markdown(f"**{skill}**")
        st.progress(level)
    
    st.markdown("---")
    
    # Personal Brand Statement
    st.markdown("""
    <div style="text-align:center;padding:20px;background-color:#f0f2f6;border-radius:10px">
    <em>"I transform numbers into narratives and data into decisions - bridging the gap between raw information and strategic business value."</em>
    </div>
    """, unsafe_allow_html=True)

# ---------------------- PROJECTS -----------------------
elif page == "📁 Projects":
    st.header("📁 My Data Projects", anchor=False)
    
    st.markdown("""
    <div style="background-color:#f8f9fa;padding:20px;border-radius:10px;margin-bottom:25px;border-left:4px solid #4285f4">
        <h4 style="margin:0;color:#2e4053;">🔍 Explore my Data Analysis Work</h4>
        <p style="margin:0;">Hands-on projects demonstrating my skills in data cleaning, analysis, visualization, and machine learning</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🚀 Featured Projects", anchor=False)

    projects = [
        {
            "title": "📚 Audible Insights: Book Recommendation Engine",
            "desc": "Developed an intelligent recommendation system for audiobooks using machine learning techniques",
            "features": [
                "Used clustering algorithms to group similar books",
                "Implemented sentiment analysis on user reviews",
                "Created personalized recommendations based on user preferences"
            ],
            "tech": "Python Pandas Scikit-learn NLTK Streamlit AWS",
            "links": {
                "Live Demo": "http://51.20.135.71:8501/",
                "GitHub Repo": "https://github.com/priyanka7411/audible-book-recommendations"
            },
            "color": "e3f2fd"
        },
        {
            "title": "📈 DataSpark: Retail Analytics Dashboard",
            "desc": "Comprehensive sales analytics dashboard for global electronics retailer",
            "features": [
                "Identified top-selling products and underperforming categories",
                "Created time-series forecasts for inventory planning",
                "Developed interactive regional performance maps"
            ],
            "tech": "Power BI SQL Python DAX Azure Data Studio",
            "links": {
                "View Dashboard": "#",
                "GitHub Repo": "https://github.com/priyanka7411/DataSpark-Electronics-Retail-Analytics"
            },
            "color": "e8f5e9"
        },
        {
            "title": "😊 Emotion Detection: AI Web App",
            "desc": "Real-time emotion classification from facial images using deep learning",
            "features": [
                "Built CNN model using Keras with TensorFlow backend",
                "Deployed as a web app with Streamlit",
                "Used OpenCV for real-time webcam image capture"
            ],
            "tech": "Python TensorFlow/Keras OpenCV Streamlit",
            "links": {
                "GitHub Repo": "https://github.com/priyanka7411/Emotion-Detection-App"
            },
            "color": "fff8e1"
        },
        {
            "title": "🛒 E-commerce Sales Analysis",
            "desc": "Analyzed Superstore dataset to uncover business trends and opportunities",
            "features": [
                "Performed data cleaning and EDA using Pandas & Seaborn",
                "Uncovered sales insights by segment, region, and category",
                "Built clear visuals for storytelling and decision-making"
            ],
            "tech": "Python Pandas Seaborn Matplotlib",
            "links": {
                "GitHub Repo": "https://github.com/priyanka7411/E-commerce-Sales-Analysis"
            },
            "color": "f3e5f5"
        },
        {
            "title": "🚌 Redbus Data Scraping App",
            "desc": "Web app that scrapes live Redbus data and visualizes insights",
            "features": [
                "Scraped bus names, routes, prices using BeautifulSoup & requests",
                "Filtered and analyzed pricing trends across cities",
                "Built a simple, interactive Streamlit dashboard"
            ],
            "tech": "Python BeautifulSoup Pandas Streamlit",
            "links": {
                "GitHub Repo": "https://github.com/priyanka7411/Redbus-Data-Scraping-Streamlit"
            },
            "color": "ede7f6"
        },
    ]

    for proj in projects:
        with st.container():
            st.markdown(f"""
            <div style="background-color:#{proj['color']};padding:20px;border-radius:12px;margin-bottom:25px;box-shadow: 0 0 10px rgba(0,0,0,0.05)">
                <h4 style="margin-bottom:5px;">{proj['title']}</h4>
                <p style="margin-bottom:10px;">{proj['desc']}</p>
                <ul>
                    {''.join([f"<li>{feature}</li>" for feature in proj['features']])}
                </ul>
                <p><strong>Tech Stack:</strong> {proj['tech']}</p>
                <p>{' | '.join([f"<a href='{url}' target='_blank'>{label}</a>" for label, url in proj['links'].items()])}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style="text-align:center;padding:20px;background-color:#f0f2f6;border-radius:10px">
        <h4 style="margin:0;">Want to know more about any project?</h4>
        <p style="margin:0;">Reach out via the Contact section or connect with me on <a href='https://github.com/priyanka7411' target='_blank'>GitHub</a>!</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------- RESUME -------------------------
elif page == "📄 Resume":
    st.header("My Professional Resume", anchor=False)
    st.markdown("""
    <div style="background-color:#f8f9fa;padding:20px;border-radius:10px;margin-bottom:20px">
    <h4 style="color:#2e4053;margin-top:0;">📌 Current as of {datetime.now().strftime('%B %Y')}</h4>
    <p>Below you can view, download, or print my complete resume</p>
    </div>
    """, unsafe_allow_html=True)

    # Resume display section
    st.markdown("---")
    st.subheader("Resume Preview", anchor=False)

    resume_path = "Priyanka Malavade.pdf"
    if os.path.exists(resume_path):
        try:
            base64_pdf = load_pdf(resume_path)
            if base64_pdf:
                st.markdown(f"""
                <div style="background-color:#e3f2fd;padding:20px;border-radius:10px;overflow:hidden;margin-bottom:25px;">
                <iframe src="data:application/pdf;base64,{base64_pdf}" 
                        width="100%" 
                        height="700px" 
                        style="border:none;">
                </iframe>
                </div>
                """, unsafe_allow_html=True)
            
            # Action buttons
            st.markdown("---")
            st.subheader("Download Options", anchor=False)
            
            col1, col2 = st.columns(2)
            with col1:
                with open(resume_path, "rb") as pdf_file:
                    st.download_button(
                        label="📄 Download PDF Resume",
                        data=pdf_file,
                        file_name="Priyanka_Malavade_Resume.pdf",
                        mime="application/pdf",
                        help="Standard PDF version for printing and sharing"
                    )
            
            with col2:
                if st.button("🖨️ Print Resume"):
                    st.markdown(
                        f'<script>window.open("data:application/pdf;base64,{base64_pdf}").print();</script>',
                        unsafe_allow_html=True
                    )
            
            # Resume highlights
            st.markdown("""
            <div style="background-color:#f0f7ff;padding:20px;border-radius:10px;margin-top:20px">
            <h4>ℹ️ Resume Highlights</h4>
            <ul>
            <li>1-page professional format optimized for ATS systems</li>
            <li>Includes all contact information and portfolio links</li>
            <li>Updated with latest projects and certifications</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error loading resume: {str(e)}")
    else:
        st.error(f"Resume file not found at: {os.path.abspath(resume_path)}")
        st.markdown("""
        <div style="background-color:#fff3e0;padding:15px;border-radius:5px;margin-top:20px">
        In the meantime, you can view my professional background on 
        [LinkedIn](https://www.linkedin.com/in/priyanka-malavade-b34677298/)
        </div>
        """, unsafe_allow_html=True)

    # Call to action
    st.markdown("---")
    st.markdown("""
    <div style="text-align:center;padding:20px;background-color:#f5f5f5;border-radius:10px">
    <h3>Want to discuss opportunities?</h3>
    <p>Feel free to <a href="#contact">contact me</a> after reviewing my qualifications!</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------- CERTIFICATIONS -----------------
elif page == "📜 Certifications":
    st.header("My Certifications", anchor=False)
    st.markdown("""
    <div style="background-color:#f8f9fa;padding:20px;border-radius:10px;margin-bottom:20px">
    <h4 style="color:#2e4053;margin-top:0;">📚 Validated Skills & Qualifications</h4>
    <p>Industry-recognized certifications demonstrating my technical expertise</p>
    </div>
    """, unsafe_allow_html=True)

    # Certifications data
    certs = [
        {
            "title": "Microsoft Power BI Certification",
            "issuer": "GUVI Geek Networks",
            "date": "November 2024",
            "id": "3470Pp3b34EgN461dX",
            "link": "https://www.guvi.in/verify-certificate?id=3470Pp3b34EgN461dX",
            "skills": "Data Visualization, DAX, Power Query, Dashboard Creation",
            "color": "e3f2fd"
        },
        {
            "title": "Oracle SQL Certification",
            "issuer": "GUVI Geek Networks",
            "date": "November 2024",
            "id": "VGl3Tw3s79o90W5318",
            "link": "https://www.guvi.in/verify-certificate?id=VGl3Tw3s79o90W5318",
            "skills": "Database Management, Query Optimization, SQL Joins",
            "color": "e8f5e9"
        },
        {
            "title": "Master Data Science Program",
            "issuer": "GUVI Geek Networks",
            "date": "January 2025",
            "id": "27m16KL0e48v560SFY",
            "link": "https://www.guvi.in/verify-certificate?id=27m16KL0e48v560SFY",
            "skills": "Machine Learning, Python, Statistical Analysis",
            "color": "fff8e1"
        }
    ]

    # Display certifications
    for cert in certs:
        with st.expander(f"📜 {cert['title']}", expanded=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"""
                **Issuing Organization:** {cert['issuer']}  
                **Date Earned:** {cert['date']}  
                **Credential ID:** {cert['id']}  
                **Skills Validated:** {cert['skills']}
                """)
            with col2:
                st.markdown(f"""
                <div style="background-color:#{cert['color']};padding:15px;border-radius:10px;text-align:center">
                <a href="{cert['link']}" target="_blank">
                <button style="background-color:#4285f4;color:white;border:none;padding:8px 16px;border-radius:4px;">
                Verify Credential
                </button>
                </a>
                </div>
                """, unsafe_allow_html=True)
        st.markdown("---")

    # Current pursuits
    st.markdown("""
    <div style="text-align:center;padding:20px;background-color:#f0f2f6;border-radius:10px">
    <h3>Currently pursuing additional certifications in:</h3>
    <p>Tableau | Advanced SQL | Google Data Analytics</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------- CONTACT -----------------------
elif page == "📬 Contact":
    st.header("Let's Connect", anchor=False)
    st.markdown("""
    <div style="background-color:#f8f9fa;padding:20px;border-radius:10px;margin-bottom:20px">
    <h4 style="color:#2e4053;margin-top:0;">💌 Open for opportunities and collaborations</h4>
    <p>Feel free to reach out for projects, job opportunities, or just to say hello!</p>
    </div>
    """, unsafe_allow_html=True)

    # Contact columns
    col1, col2 = st.columns([1, 2])

    with col1:
        # Contact info cards
        contact_info = [
            ("e3f2fd", "📧 Email", "priyasmalavade@gmail.com"),
            ("e8f5e9", "🔗 Professional Profiles", [
                ("LinkedIn", "https://www.linkedin.com/in/priyanka-malavade-b34677298/"),
                ("GitHub", "https://github.com/priyanka7411")
            ]),
            ("fff8e1", "📍 Location", "Bangalore, India<br>Open to remote opportunities")
        ]

        for color, title, content in contact_info:
            if isinstance(content, list):
                content_html = "<br>".join([f'<a href="{url}" target="_blank">{name}</a>' for name, url in content])
            else:
                content_html = content
            
            st.markdown(f"""
            <div style="background-color:#{color};padding:15px;border-radius:10px;margin-bottom:20px">
            <h4>{title}</h4>
            <p>{content_html}</p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        # Enhanced contact form
        with st.form("contact_form", clear_on_submit=True):
            st.subheader("📩 Send Me a Message")
            
            name = st.text_input("Your Name*", placeholder="John Doe")
            email = st.text_input("Your Email*", placeholder="your.email@example.com")
            subject = st.selectbox("Subject*", 
                                 ["Job Opportunity", "Project Collaboration", "General Inquiry", "Feedback"])
            message = st.text_area("Your Message*", 
                                  height=150,
                                  placeholder="I'd like to discuss...")
            
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                if not all([name, email, message]):
                    st.warning("Please fill in all required fields (*)")
                elif not validate_email(email):
                    st.warning("Please enter a valid email address")
                else:
                    st.success("""
                    ✅ Thank you for your message! 
                    I'll get back to you within 24-48 hours.
                    """)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align:center">
    <h4>Connect with me on</h4>
    <p>
    <a href="https://www.linkedin.com/in/priyanka-malavade-b34677298/" target="_blank">LinkedIn</a> | 
    <a href="https://github.com/priyanka7411" target="_blank">GitHub</a> | 
    <a href="https://twitter.com/" target="_blank">Twitter</a>
    </p>
    <p>Thank you for visiting my portfolio! 🙏</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------- FOOTER -----------------------
st.markdown("---")
st.markdown(f"""
<div style="text-align:center; padding:10px;">
    <p>© {datetime.now().year} Priyanka Malavade | 
    <a href="https://www.linkedin.com/in/priyanka-malavade-b34677298/" target="_blank">LinkedIn</a> | 
    <a href="https://github.com/priyanka7411" target="_blank">GitHub</a></p>
</div>
""", unsafe_allow_html=True)