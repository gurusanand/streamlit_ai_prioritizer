"""
Agentic AI Prioritization Framework - Streamlit Application
A comprehensive tool for evaluating and prioritizing AI use cases
"""

import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Agentic AI Prioritization Framework",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import custom modules
from utils.framework_loader import load_framework_data, get_categories
from utils.database import Database
from utils.ai_insights import generate_insights
from utils.calculations import calculate_scores, calculate_category_scores

# Initialize database
db = Database()

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: green;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: blue;
        text-align: center;
    }
    .score-display {
        font-size: 4rem;
        font-weight: bold;
        margin: 1rem 0;
    }
    .category-score {
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        background: #f8f9fa;
    }
    .recommendation-card {
        background: #blue;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2196f3;
        margin: 0.5rem 0;
    }
    .strength-card {
        background: ;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #4caf50;
        margin: 0.5rem 0;
    }
    .challenge-card {
        background: red;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #f44336;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Main application function"""
    
    # Sidebar navigation
    st.sidebar.title("🤖 AI Prioritization")
    page = st.sidebar.radio(
        "Navigation",
        ["🏠 Home", "📊 Dashboard", "➕ New Use Case", "📝 Assessment", "📈 Results", "ℹ️ About"]
    )
    
    # Route to appropriate page
    if page == "🏠 Home":
        show_home()
    elif page == "📊 Dashboard":
        show_dashboard()
    elif page == "➕ New Use Case":
        show_new_use_case()
    elif page == "📝 Assessment":
        show_assessment()
    elif page == "📈 Results":
        show_results()
    elif page == "ℹ️ About":
        show_about()

def show_home():
    """Display home page"""
    st.markdown('<h1 class="main-header">Agentic AI Prioritization Framework</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Prioritize Your AI Use Cases with Confidence
    
    A comprehensive framework to systematically evaluate, score, and prioritize 
    business processes for agentic AI automation. Make data-driven decisions 
    with AI-powered insights.
    """)
    
    # Feature cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### 📊 31 Evaluation Dimensions
        Comprehensive scoring across Strategic & Business, Risk & Compliance, 
        Technical Implementation, and more.
        """)
    
    with col2:
        st.markdown("""
        #### 🤖 AI-Powered Insights
        Get intelligent recommendations and analysis powered by advanced AI 
        to improve your use case viability.
        """)
    
    with col3:
        st.markdown("""
        #### ⚡ Interactive Dashboard
        Visualize scores, compare use cases, and export detailed reports 
        for stakeholder presentations.
        """)
    
    st.markdown("---")
    
    # How it works
    st.markdown("### 🎯 How It Works")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("**1️⃣**")
    with col2:
        st.markdown("**Define Your Use Case** - Create a new AI use case with details")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("**2️⃣**")
    with col2:
        st.markdown("**Score 31 Dimensions** - Evaluate across all dimensions on a scale of 1-5")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("**3️⃣**")
    with col2:
        st.markdown("**Get AI-Powered Insights** - Receive intelligent analysis and recommendations")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("**4️⃣**")
    with col2:
        st.markdown("**Review & Compare** - View dashboards and prioritize implementation")
    
    st.markdown("---")
    
    # Quick stats
    use_cases = db.get_all_use_cases()
    st.markdown("### 📈 Quick Stats")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Use Cases", len(use_cases))
    with col2:
        completed = len([uc for uc in use_cases if uc['status'] == 'completed'])
        st.metric("Completed Assessments", completed)
    with col3:
        if completed > 0:
            summaries = [db.get_assessment_summary(uc['id']) for uc in use_cases if uc['status'] == 'completed']
            avg_score = sum(s['normalized_score'] for s in summaries if s) / len(summaries)
            st.metric("Average Score", f"{avg_score:.0f}/100")
        else:
            st.metric("Average Score", "N/A")

def show_dashboard():
    """Display dashboard with all use cases"""
    st.markdown('<h1 class="main-header">📊 Dashboard</h1>', unsafe_allow_html=True)
    
    use_cases = db.get_all_use_cases()
    
    if not use_cases:
        st.info("No use cases yet. Create your first use case to get started!")
        if st.button("➕ Create New Use Case"):
            st.session_state.page = "➕ New Use Case"
            st.rerun()
        return
    
    # Display use cases
    st.markdown(f"### Your Use Cases ({len(use_cases)})")
    
    for uc in use_cases:
        with st.expander(f"**{uc['use_case_id']}** - {uc['name']}", expanded=False):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"**Description:** {uc.get('description', 'N/A')}")
                st.markdown(f"**Business Unit:** {uc.get('business_unit', 'N/A')}")
                st.markdown(f"**Process Owner:** {uc.get('process_owner', 'N/A')}")
                st.markdown(f"**Status:** {uc['status'].title()}")
            
            with col2:
                if uc['status'] == 'completed':
                    summary = db.get_assessment_summary(uc['id'])
                    if summary:
                        st.markdown(f'<div class="metric-card"><div class="score-display">{summary["normalized_score"]}</div><div>Overall Score</div></div>', unsafe_allow_html=True)
                        if st.button("📈 View Results", key=f"view_{uc['id']}"):
                            st.session_state.selected_use_case_id = uc['id']
                            st.session_state.page = "📈 Results"
                            st.rerun()
                else:
                    if st.button("📝 Start Assessment", key=f"assess_{uc['id']}"):
                        st.session_state.selected_use_case_id = uc['id']
                        st.session_state.page = "📝 Assessment"
                        st.rerun()
                
                if st.button("🗑️ Delete", key=f"delete_{uc['id']}"):
                    db.delete_use_case(uc['id'])
                    st.success("Use case deleted!")
                    st.rerun()

def show_new_use_case():
    """Create new use case form"""
    st.markdown('<h1 class="main-header">➕ Create New Use Case</h1>', unsafe_allow_html=True)
    
    with st.form("new_use_case_form"):
        use_case_id = st.text_input("Use Case ID *", placeholder="e.g., UC-001")
        name = st.text_input("Use Case Name *", placeholder="e.g., Fraud Detection - Real-time Transaction Monitoring")
        description = st.text_area("Description", placeholder="Describe the use case and its objectives...")
        
        col1, col2 = st.columns(2)
        with col1:
            business_unit = st.text_input("Business Unit", placeholder="e.g., Retail Banking")
        with col2:
            process_owner = st.text_input("Process Owner", placeholder="e.g., Chief Risk Officer")
        
        submitted = st.form_submit_button("Create Use Case")
    
    if submitted:
        if not use_case_id or not name:
            st.error("Please fill in required fields (Use Case ID and Name)")
        else:
            uc_id = db.create_use_case(
                use_case_id=use_case_id,
                name=name,
                description=description,
                business_unit=business_unit,
                process_owner=process_owner
            )
            st.success(f"Use case '{name}' created successfully!")
            st.session_state.selected_use_case_id = uc_id
            
            # Show button outside the form
            if st.button("Start Assessment Now", type="primary"):
                st.session_state.page = "📝 Assessment"
                st.rerun()

def show_assessment():
    """Show assessment form"""
    st.markdown('<h1 class="main-header">📝 Assessment</h1>', unsafe_allow_html=True)
    
    # Get selected use case
    if 'selected_use_case_id' not in st.session_state:
        st.warning("Please select a use case from the dashboard first.")
        return
    
    use_case = db.get_use_case(st.session_state.selected_use_case_id)
    if not use_case:
        st.error("Use case not found.")
        return
    
    # Display use case info
    st.markdown(f"### {use_case['use_case_id']} - {use_case['name']}")
    if use_case.get('description'):
        st.markdown(f"*{use_case['description']}*")
    
    st.markdown("---")
    
    # Load framework data
    framework = load_framework_data()
    categories = get_categories(framework)
    
    # Initialize session state for scores
    if 'assessment_scores' not in st.session_state:
        existing_scores = db.get_assessment_scores(use_case['id'])
        st.session_state.assessment_scores = {
            score['dimension']: score['score'] for score in existing_scores
        }
    
    # Progress tracking
    total_dimensions = len(framework)
    completed = len(st.session_state.assessment_scores)
    progress = completed / total_dimensions
    
    st.progress(progress)
    st.markdown(f"**Progress:** {completed} / {total_dimensions} dimensions completed")
    
    st.markdown("---")
    
    # Assessment by category
    for category in categories:
        with st.expander(f"📋 {category}", expanded=(category == categories[0])):
            dimensions = [d for d in framework if d['category'] == category]
            
            for dim in dimensions:
                st.markdown(f"#### {dim['dimension']}")
                st.markdown(f"*{dim['description']}*")
                
                # Score selection
                score = st.radio(
                    "Select Score:",
                    options=[5, 4, 3, 2, 1],
                    format_func=lambda x: f"Score {x}: {dim['scores'][str(x)]}",
                    key=f"score_{dim['dimension']}",
                    index=None if dim['dimension'] not in st.session_state.assessment_scores 
                          else 5 - st.session_state.assessment_scores[dim['dimension']],
                    horizontal=False
                )
                
                if score:
                    st.session_state.assessment_scores[dim['dimension']] = score
                
                st.markdown("---")
    
    # Submit button
    if completed == total_dimensions:
        if st.button("✅ Submit Assessment", type="primary", use_container_width=True):
            # Save scores
            scores_data = []
            for dim in framework:
                scores_data.append({
                    'dimension': dim['dimension'],
                    'category': dim['category'],
                    'score': st.session_state.assessment_scores[dim['dimension']],
                    'weight': dim['default_weight']
                })
            
            # Calculate results
            total_score, normalized_score = calculate_scores(scores_data)
            category_scores = calculate_category_scores(scores_data)
            
            # Generate AI insights
            with st.spinner("Generating AI-powered insights..."):
                insights, recommendations = generate_insights(
                    use_case=use_case,
                    scores=scores_data,
                    normalized_score=normalized_score,
                    category_scores=category_scores
                )
            
            # Save to database
            db.save_assessment(
                use_case_id=use_case['id'],
                scores=scores_data,
                total_score=total_score,
                normalized_score=normalized_score,
                category_scores=category_scores,
                ai_insights=insights,
                recommendations=recommendations
            )
            
            st.success("Assessment completed successfully!")
            st.session_state.page = "📈 Results"
            st.rerun()
    else:
        st.info(f"Please complete all {total_dimensions} dimensions before submitting.")

def show_results():
    """Display assessment results"""
    st.markdown('<h1 class="main-header">📈 Results</h1>', unsafe_allow_html=True)
    
    # Get selected use case
    if 'selected_use_case_id' not in st.session_state:
        st.warning("Please select a use case from the dashboard first.")
        return
    
    use_case = db.get_use_case(st.session_state.selected_use_case_id)
    summary = db.get_assessment_summary(use_case['id'])
    scores = db.get_assessment_scores(use_case['id'])
    
    if not summary:
        st.warning("No assessment results found for this use case.")
        return
    
    # Use case header
    st.markdown(f"### {use_case['use_case_id']} - {use_case['name']}")
    if use_case.get('description'):
        st.markdown(f"*{use_case['description']}*")
    
    st.markdown("---")
    
    # Overall score
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        score_color = "#4caf50" if summary['normalized_score'] >= 80 else "#2196f3" if summary['normalized_score'] >= 60 else "#ff9800" if summary['normalized_score'] >= 40 else "#f44336"
        st.markdown(f"""
        <div style="background: {score_color}; padding: 2rem; border-radius: 10px; color: white; text-align: center;">
            <h2 style="margin: 0;">Overall Readiness Score</h2>
            <div style="font-size: 5rem; font-weight: bold; margin: 1rem 0;">{summary['normalized_score']}</div>
            <div style="font-size: 1.2rem;">out of 100</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.metric("Total Dimensions", len(scores))
        st.metric("Categories", len(summary['category_scores']))
    
    with col3:
        status = "Excellent" if summary['normalized_score'] >= 80 else "Good" if summary['normalized_score'] >= 60 else "Moderate" if summary['normalized_score'] >= 40 else "Challenging"
        st.metric("Status", status)
        st.metric("Assessed On", summary['created_at'].strftime("%Y-%m-%d"))
    
    st.markdown("---")
    
    # Category scores
    st.markdown("### 📊 Category Breakdown")
    
    category_scores = summary['category_scores']
    
    # Create bar chart
    cat_df = pd.DataFrame([
        {'Category': cat, 'Score': data['normalized']}
        for cat, data in category_scores.items()
    ])
    
    fig = px.bar(
        cat_df,
        x='Score',
        y='Category',
        orientation='h',
        color='Score',
        color_continuous_scale='RdYlGn',
        range_color=[0, 100],
        labels={'Score': 'Score (0-100)'},
        title='Category Performance'
    )
    fig.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # Category details
    for cat, data in category_scores.items():
        with st.expander(f"{cat} - {data['normalized']}/100"):
            st.progress(data['normalized'] / 100)
            st.markdown(f"**Total Score:** {data['total']} / {data['max']}")
    
    st.markdown("---")
    
    # Strengths and Challenges
    col1, col2 = st.columns(2)
    
    strengths = [s for s in scores if s['score'] >= 4]
    challenges = [s for s in scores if s['score'] <= 2]
    
    with col1:
        st.markdown("### ✅ Top Strengths")
        if strengths:
            for item in sorted(strengths, key=lambda x: x['score'], reverse=True)[:5]:
                st.markdown(f"""
                <div class="strength-card">
                    <strong>{item['dimension']}</strong> (Score: {item['score']}/5)<br>
                    <small>{item['category']}</small>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No dimensions scored 4 or above.")
    
    with col2:
        st.markdown("### ⚠️ Key Challenges")
        if challenges:
            for item in sorted(challenges, key=lambda x: x['score'])[:5]:
                st.markdown(f"""
                <div class="challenge-card">
                    <strong>{item['dimension']}</strong> (Score: {item['score']}/5)<br>
                    <small>{item['category']}</small>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No dimensions scored 2 or below.")
    
    st.markdown("---")
    
    # AI Insights
    if summary.get('ai_insights'):
        st.markdown("### 🤖 AI-Powered Analysis")
        st.markdown(f"""
        <div style="background: grey; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #2196f3;">
            {summary['ai_insights']}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Recommendations
    if summary.get('recommendations'):
        st.markdown("### 💡 Actionable Recommendations")
        recommendations = json.loads(summary['recommendations']) if isinstance(summary['recommendations'], str) else summary['recommendations']
        
        for idx, rec in enumerate(recommendations, 1):
            st.markdown(f"""
            <div class="recommendation-card">
                <strong>{idx}.</strong> {rec}
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Detailed scores table
    with st.expander("📋 View All Dimension Scores"):
        scores_df = pd.DataFrame(scores)
        scores_df = scores_df[['dimension', 'category', 'score', 'weight', 'weighted_score']]
        scores_df.columns = ['Dimension', 'Category', 'Score (1-5)', 'Weight', 'Weighted Score']
        st.dataframe(scores_df, use_container_width=True)
    
    # Export options
    st.markdown("### 📥 Export")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📄 Export to CSV"):
            scores_df.to_csv(f"assessment_{use_case['use_case_id']}.csv", index=False)
            st.success("Exported to CSV!")
    
    with col2:
        if st.button("📊 Export to JSON"):
            export_data = {
                'use_case': use_case,
                'summary': {k: v for k, v in summary.items() if k != 'created_at'},
                'scores': scores
            }
            with open(f"assessment_{use_case['use_case_id']}.json", 'w') as f:
                json.dump(export_data, f, indent=2)
            st.success("Exported to JSON!")

def show_about():
    """Display about page"""
    st.markdown('<h1 class="main-header">ℹ️ About</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Agentic AI Prioritization Framework
    
    This framework helps IT stakeholders in banking and finance systematically evaluate,
    score, and prioritize business processes and use cases for agentic AI automation.
    
    #### 📊 Framework Dimensions (31 Total)
    
    **1. Strategic & Business (5 dimensions)**
    - Business impact, strategic alignment, time to market, ROI, scalability
    
    **2. Risk & Compliance (5 dimensions)**
    - AI risk, regulatory compliance, data privacy, operational risk, ethical considerations
    
    **3. Technical & Implementation (6 dimensions)**
    - Technical complexity, data readiness, integration complexity, infrastructure, vendor maturity, maintainability
    
    **4. Resource & Investment (4 dimensions)**
    - Total investment, resource availability, skills gap, ongoing costs
    
    **5. Organizational & Change (4 dimensions)**
    - Organizational readiness, stakeholder alignment, change management, employee adoption
    
    **6. Human-in-Loop & Autonomy (3 dimensions)**
    - Autonomy level, human oversight requirements, explainability needs
    
    **7. Process & Operational (4 dimensions)**
    - Process standardization, volume & frequency, criticality, current efficiency
    
    #### 🎯 Scoring Scale
    
    - **Score 5:** Most favorable - easiest to implement, lowest risk, highest value
    - **Score 4:** Favorable - good candidate with manageable challenges
    - **Score 3:** Moderate - balanced pros and cons, requires careful planning
    - **Score 2:** Challenging - significant hurdles, needs risk mitigation
    - **Score 1:** Very challenging - major barriers, high risk or low value
    
    #### 🚀 Features
    
    - ✅ Create and manage multiple AI use cases
    - ✅ Comprehensive 31-dimension assessment
    - ✅ AI-powered insights and recommendations
    - ✅ Interactive visualizations
    - ✅ Export results to CSV/JSON
    - ✅ SQLite database for data persistence
    
    ---
    
    **Version:** 1.0.0  
    **Powered by:** Streamlit & OpenAI  
    **License:** MIT
    """)

if __name__ == "__main__":
    main()

