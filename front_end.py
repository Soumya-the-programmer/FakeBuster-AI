"Importing necessary modules"
import streamlit as st
from fake_news_detect import NewsDetector
import time
import joblib
from pathlib import Path


# creating an instance of NewsDetector class
obj = NewsDetector()

# setting page configuration as wide
st.set_page_config(layout= "wide")


class CorporateNewsValidator:
    
    def __init__(self):
        self._inject_corporate_style()
        self._load_background_image()


    def _load_assets(self, path):
        """Secure asset loading with error handling"""
        try:
            with open(Path(path), 'rb') as f:
                return joblib.load(f)
        except Exception as e:
            st.error(f"Asset loading error: {str(e)}")
            st.stop()

    def _set_page_config(self):
        """Configure professional page settings"""
        st.set_page_config(
            page_title="News Validator AI | AI-powered Misinformation Detection",
            page_icon=":shield:",
            layout="centered",
            initial_sidebar_state="collapsed"
        )


    def _inject_corporate_style(self):
        """Corporate-grade styling with animations"""
        st.markdown(f"""
            <style>
                /* Base styles */
                body {{ 
                    font-family: 'Helvetica Neue', sans-serif;
                    background-color: #f8f9fa;
                }}
                
                /* Professional header */
                .corporate-header {{
                    background: rgba(15, 32, 65, 0.95);
                    padding: 2rem;
                    border-bottom: 4px solid #00c3ff;
                    box-shadow: 0 2px 15px rgba(0,0,0,0.1);
                }}
                
                /* Modern input card */
                .analysis-card {{
                    background: white;
                    border-radius: 15px;
                    padding: 2.5rem;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
                    margin: 2rem auto;
                    max-width: 800px;
                    border-left: 5px solid #00c3ff;
                    transition: transform 0.3s ease;
                }}
                .analysis-card:hover {{ transform: translateY(-5px); }}
                
                /* Result visualization */
                .result-banner {{
                    padding: 1.5rem;
                    border-radius: 8px;
                    color: white;
                    margin: 1.5rem 0;
                    display: flex;
                    align-items: center;
                    animation: fadeIn 0.5s ease;
                }}
                @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
                .real-banner {{ background: linear-gradient(135deg, #00c851, #007e33); }}
                .fake-banner {{ background: linear-gradient(135deg, #ff4444, #cc0000); }}
                
                /* Corporate metrics */
                .metric-card {{
                    background: white;
                    padding: 1.5rem;
                    border-radius: 10px;
                    text-align: center;
                    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
                }}
                
                /* Enhanced text area */
                .custom-textarea {{
                    border: 2px solid #e0e0e0 !important;
                    border-radius: 8px !important;
                    padding: 1rem !important;
                    font-size: 16px !important;
                }}
                
                /* Professional footer */
                .corporate-footer {{
                    background: rgba(15, 32, 65, 0.95);
                    color: white;
                    padding: 2rem;
                    margin-top: 4rem;
                    text-align: center;
                    border-top: 3px solid #00c3ff;
                }}
            </style>
        """, unsafe_allow_html=True)


    def _load_background_image(self):
        """Set a fully responsive background image"""
        
        bg_url = "https://github.com/Soumya-the-programmer/NEWS-VALIDATOR-AI/blob/main/fake_news_banner.jpg?raw=true"

        st.markdown(f"""
            <style>
                .stApp {{
                    background: url("{bg_url}") no-repeat center center fixed;
                    background-size: cover;
                    background-attachment: fixed;
                }}

                /* Adjustments for smaller screens */
                @media (max-width: 768px) {{
                    .stApp {{
                        background-size: 100% 100%; /* Forces full coverage on mobile */
                        background-attachment: scroll; /* Prevents fixed background issues */
                        background-repeat: no-repeat; /* Ensures no tiling */
                    }}
                }}
            </style>
        """, unsafe_allow_html=True)


    def _corporate_header(self):
        """Render enterprise-level header"""
        
        st.markdown("""
        <style>
            .corporate-header {
                max-width: 1200px;
                margin: 0 auto;
                display: flex;
                align-items: center;
                justify-content: space-between;
                flex-wrap: wrap;
            }

            .corporate-header h1 {
                font-size: 2.5rem; /* Default for desktop */
                white-space: nowrap;
            }

            .corporate-header .nav-links {
                display: flex;
                gap: 2rem;
            }

            @media (max-width: 768px) {
                .corporate-header h1 {
                    font-size: 2rem; /* Just a tiny bit bigger */
                }
                .corporate-header .nav-links {
                    gap: 1rem;
                    flex-wrap: wrap;
                    justify-content: center;
                    width: 100%;
                    margin-top: 10px;
                }
            }
        </style>

        <div class="corporate-header">
            <h1 style="color: white; margin: 0; font-weight: 700;">NEWS VALIDATOR AI</h1>
            <div class="nav-links">
                <a href="#text-analysis" class="nav-link" style="color: white; text-decoration: none;">Analysis</a>
                <a href="#about-us" class="nav-link" style="color: white; text-decoration: none;">About Us</a>
            </div>
        </div>
    """, unsafe_allow_html=True)


    def _analysis_section(self):
        """Main analysis interface"""
        
        with st.container():
            st.markdown("""
        <div id="text-analysis" class="analysis-card" style="background: #f5f8ff; 
            padding: 1.5rem; 
            border-radius: 12px; 
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            text-align: center;">
            <h2 style="color: #0f2041; margin-bottom: 1rem; font-size: 1.8rem; font-weight: bold;">
                AI News Authenticity Checker
            </h2>
            <p style="color: #3a3a3a; font-size: 1rem;">
                AI-powered verification system for detecting misinformation and ensuring content authenticity.
            </p>
        </div>
    """, unsafe_allow_html=True)
            
            tab1, = st.tabs(["Text Analysis"])
            
            with tab1:
                text_input = st.text_area("Paste news content:", 
                                        height=250,
                                        placeholder="Enter article text...",
                                        key="text_input",
                                        help="Paste your article here for AI verification.")
                if st.button("Initiate Verification", key="analyze_text"):
                    self._process_input(text_input)
            
            st.markdown("</div>", unsafe_allow_html=True)


    def _process_input(self, text):
        """Handle analysis workflow"""
        
        if len(text) < 100:
            st.warning("Minimum 100 characters required for accurate analysis")
            return
        
        with st.spinner("Executing advanced verification protocols..."):
            progress_bar = st.progress(0)
            for percent in range(100):
                time.sleep(0.02)  # Simulate processing
                progress_bar.progress(percent + 1)
            
            # Replace with actual model prediction
            prediction = obj.predict_news(text = text)
            
            self._display_result(prediction)


    def _display_result(self, prediction):
        """Show professional result banner"""
        
        banner_class = "real-banner" if prediction == "Real" else "fake-banner"
        icon = "✅" if prediction == "Real" else "⚠️"
        
        st.markdown(f"""
            <div class="result-banner {banner_class}">
                <div style="font-size: 24px; margin-right: 1rem;">{icon}</div>
                <div>
                    <h3 style="margin: 0;">{prediction.upper()} CONTENT VERIFIED</h3>
                </div>
            </div>
        """, unsafe_allow_html=True)


    def _corporate_footer(self):
        """Professional footer section with attribution"""
        
        st.markdown(
    """
    <style>
        /* Footer styling */
        .corporate-footer {
            background: #0f2041;
            color: white;
            padding: 2rem 1rem;
            text-align: center;
        }

        .corporate-footer h4 {
            font-size: 1.4rem;
            margin-bottom: 0.5rem;
        }

        .corporate-footer p {
            font-size: 1rem;
            margin-bottom: 0.8rem;
        }

        .corporate-footer a {
            color: rgba(255, 255, 255, 0.8);
            text-decoration: none;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .corporate-footer div {
                display: flex;
                flex-direction: column;
                text-align: center;
                gap: 1.5rem;
            }

            .corporate-footer h4 {
                font-size: 1.2rem;
            }

            .corporate-footer p {
                font-size: 0.9rem;
            }
        }
    </style>

    <div id="about-us" class="corporate-footer">  
        <div style="max-width: 1200px; margin: 0 auto;">
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;">
                <div>
                    <h4>News Validator AI</h4>
                    <p>AI-powered Misinformation Detection</p>
                </div>
                <div>
                    <h4>About Us</h4>
                    <p>News Validator AI is dedicated to fighting misinformation with cutting-edge Machine Learning models.</p>
                </div>
                <div>
                    <h4>Future Updates</h4>
                    <p>We plan to enhance our AI-powered Fake News Detection system with more advanced models.</p>
                </div>
            </div>
            <hr style="margin: 2rem 0; border-color: rgba(255,255,255,0.1);">
            <p style="margin: 0;">© 2025 NewsValidator AI | Developed as an academic project.</p>
            <p style="margin: 0; font-size: 0.9rem; color: rgba(255,255,255,0.7);">
                Background Image: <a href="https://www.freepik.com/">Designed by Freepik</a>
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    def run(self):
        """Main execution flow"""
        self._corporate_header()
        self._analysis_section()
        self._corporate_footer()

if __name__ == "__main__":
    validator = CorporateNewsValidator()
    validator.run()