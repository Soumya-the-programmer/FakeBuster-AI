"""### News Validator AI Frontend

**Purpose:** This Streamlit-based web application provides an interactive interface for detecting fake news using the `NewsDetector` model.

**Features:**
- Uses a **pre-trained NLP model** to analyze news content.
- Offers a **modern UI** with corporate styling.
- Handles **error detection and asset loading**.
"""

# Importing necessary modules
import streamlit as st
from fake_news_detect import NewsDetector
import time


# Creating an instance of NewsDetector class
obj = NewsDetector()


class FakeBusterAI:
    """### Class `FakeBusterAI`
    
    **Purpose:** Handles frontend configurations, UI styling and model handling.
    """
    
    def __init__(self) -> None:
        """Initialize UI settings by applying corporate styling and background image."""
        
        # importing these methods for the style and bg image
        self._set_page_config()
        self._inject_corporate_style()
        self._load_background_image()


    def _set_page_config(self) -> None:
        """Configures the page with professional settings for branding consistency."""
        
        st.set_page_config(
            page_title="FakeBuster AI - Detect Fake News with AI",
            page_icon="🛡️",
            layout="wide",
            initial_sidebar_state="collapsed"
        )
        
        # 🛠️ Force Streamlit to expand width using CSS
        st.markdown(
            """
            <style>
                .main .block-container {
                    max-width: 100% !important;  /* Forces the page to full width */
                    padding-left: 2rem; 
                    padding-right: 2rem;
                }
            </style>
            """,
            unsafe_allow_html=True
        )


    def _inject_corporate_style(self) -> None:
        """Injects corporate-level styling to enhance the user interface with animations."""
        
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
        """
        Set a fully responsive background image for the Streamlit app.
        - Uses a remote image URL.
        - Ensures proper scaling for both desktop and mobile devices.
        """
        
        # inserting bg image url here
        bg_url = "https://github.com/Soumya-the-programmer/FakeBuster-AI/blob/main/fake_news_banner.jpg?raw=true"

        # writting the markdown script here
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


    def _corporate_header():
        """
        Render an enterprise-level header for the app.
        - Displays the app title.
        - Includes navigation links for a professional look.
        - Ensures full-width responsive styling.
        """
    
        st.markdown("""
            <style>
                /* Ensuring full-width layout */
                .main .block-container {
                    max-width: 100% !important;
                    padding-left: 2rem;
                    padding-right: 2rem;
                }
    
                /* Corporate Header */
                .corporate-header {
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 20px 0;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    flex-wrap: wrap;
                }
    
                .corporate-header h1 {
                    font-size: 2.5rem;
                    font-weight: 700;
                    margin: 0;
                    color: white;
                }
    
                .corporate-header .nav-links {
                    display: flex;
                    gap: 20px;
                }
    
                .corporate-header .nav-link {
                    color: white;
                    text-decoration: none;
                    font-size: 1.2rem;
                    font-weight: 500;
                    transition: color 0.3s;
                }
    
                .corporate-header .nav-link:hover {
                    color: #FFD700;
                }
    
                @media (max-width: 768px) {
                    .corporate-header {
                        flex-direction: column;
                        text-align: center;
                    }
    
                    .corporate-header .nav-links {
                        flex-direction: column;
                        gap: 10px;
                        margin-top: 10px;
                    }
                }
            </style>
    
            <div class="corporate-header">
                <h1>FakeBuster AI</h1>
                <div class="nav-links">
                    <a href="?tab=analysis" class="nav-link">Analysis</a>
                    <a href="?tab=about" class="nav-link">About Us</a>
                </div>
            </div>
        """, unsafe_allow_html=True)
    

    def _analysis_section(self):
        """
        Displays the main analysis interface where users can input news text
        for AI-based authenticity verification.
        """
        
        with st.container():
            # Section Header
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
            
            # Creating a tab for Text Analysis
            tab1, = st.tabs(["Text Analysis"])
            
            with tab1:
                # Input field for news text
                text_input = st.text_area("Paste news content:", 
                                        height=250,
                                        placeholder="Enter article text...",
                                        key="text_input",
                                        help="Paste your article here for AI verification.")
                
                # Button to trigger analysis
                if st.button("Initiate Verification", key="analyze_text"):
                    self._process_input(text_input)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    
    def _process_input(self, text):
        """
        Processes the user input by performing AI-based verification.
        
        Steps:
        1. Checks if the input meets the minimum length requirement.
        2. Simulates an AI verification process using a progress bar.
        3. Calls the model prediction function and displays the result.
        """
        
        # Ensuring minimum text length for accurate prediction
        if len(text) < 100:
            st.warning("Minimum 100 characters required for accurate analysis")
            return
        
        # Simulating processing with a progress bar
        with st.spinner("Executing advanced verification protocols..."):
            progress_bar = st.progress(0)
            for percent in range(100):
                time.sleep(0.02)  # Simulating AI processing delay
                progress_bar.progress(percent + 1)
        
        # Placeholder for the actual AI model prediction (to be replaced with real implementation)
        prediction = obj.predict_news(text=text)
        
        # Displaying the final result
        self._display_result(prediction)


    def _display_result(self, prediction):
        """
        Displays the analysis result based on the AI model's prediction.
        
        Args:
            prediction (str): The AI model's classification of the input text.
        """
        
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
        """
        Displays a professional footer section with attribution and project details.
        """
        
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
            white-space: nowrap; /* Prevents text breaking */
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

            .corporate-footer .grid-container {
                display: flex;
                flex-direction: column; /* Stack items vertically on mobile */
                gap: 1rem;
            }

            .corporate-footer h4 {
                font-size: 1.3rem;
            }

            .corporate-footer p {
                font-size: 1rem;
            }
        }
    </style>

    <div id="about-us" class="corporate-footer">  
        <div style="max-width: 1200px; margin: 0 auto;">
            <div class="grid-container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
                <div>
                    <h4>FakeBuster AI</h4>
                    <p>AI-powered Misinformation Detection</p>
                </div>
                <div>
                    <h4>About Us</h4>
                    <p>FakeBuster AI is dedicated to fighting misinformation with cutting-edge Machine Learning models.</p>
                </div>
                <div>
                    <h4>Future Updates</h4>
                    <p>We plan to enhance our AI-powered Fake News Detection system with more advanced models.</p>
                </div>
            </div>
            <hr style="margin: 2rem 0; border-color: rgba(255,255,255,0.1);">
            <p style="margin: 0;">© 2025 FakeBuster | Developed as an academic project.</p>
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
    validator = FakeBusterAI()
    validator.run()
