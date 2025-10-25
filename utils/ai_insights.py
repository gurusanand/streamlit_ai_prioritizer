"""
AI Insights Generator - Uses OpenAI to generate insights and recommendations
"""

import os
import json
from openai import OpenAI

def generate_insights(use_case, scores, normalized_score, category_scores):
    """
    Generate AI-powered insights and recommendations
    
    Args:
        use_case: Use case dictionary
        scores: List of score dictionaries
        normalized_score: Overall normalized score (0-100)
        category_scores: Dictionary of category scores
    
    Returns:
        tuple: (insights_text, recommendations_list)
    """
    
    # Check if OpenAI API key is available
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        return get_default_insights(normalized_score, category_scores)
    
    try:
        client = OpenAI(api_key=api_key)
        
        # Prepare data for analysis
        strengths = [s for s in scores if s['score'] >= 4]
        challenges = [s for s in scores if s['score'] <= 2]
        
        # Create prompt
        prompt = f"""Analyze this AI use case assessment and provide insights:

Use Case: {use_case['name']}
Description: {use_case.get('description', 'N/A')}
Normalized Score: {normalized_score}/100

Category Scores:
{chr(10).join([f"- {cat}: {data['normalized']}/100" for cat, data in category_scores.items()])}

Top Strengths (score 4-5):
{chr(10).join([f"- {s['dimension']} ({s['score']}/5)" for s in strengths[:5]])}

Key Challenges (score 1-2):
{chr(10).join([f"- {s['dimension']} ({s['score']}/5)" for s in challenges[:5]])}

Provide:
1. A concise analysis of the overall readiness and viability (2-3 sentences)
2. Top 3 specific, actionable recommendations to improve this use case's score

Format your response as JSON:
{{
  "insights": "your analysis here",
  "recommendations": ["recommendation 1", "recommendation 2", "recommendation 3"]
}}"""
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an AI strategy consultant specializing in enterprise AI implementation."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.7
        )
        
        # Parse response
        result = json.loads(response.choices[0].message.content)
        insights = result.get('insights', '')
        recommendations = result.get('recommendations', [])
        
        return insights, recommendations
        
    except Exception as e:
        print(f"Error generating AI insights: {e}")
        return get_default_insights(normalized_score, category_scores)

def get_default_insights(normalized_score, category_scores):
    """Generate default insights when AI is not available"""
    
    # Determine readiness level
    if normalized_score >= 80:
        readiness = "excellent"
        status = "This use case demonstrates strong readiness across most dimensions and is well-positioned for implementation."
    elif normalized_score >= 60:
        readiness = "good"
        status = "This use case shows good potential with some areas requiring attention before full implementation."
    elif normalized_score >= 40:
        readiness = "moderate"
        status = "This use case has moderate readiness with several significant challenges that need to be addressed."
    else:
        readiness = "challenging"
        status = "This use case faces substantial obstacles and requires significant planning and risk mitigation."
    
    # Find lowest scoring categories
    sorted_categories = sorted(category_scores.items(), key=lambda x: x[1]['normalized'])
    weak_categories = [cat for cat, _ in sorted_categories[:2]]
    
    insights = f"{status} The assessment reveals {readiness} readiness with particular focus needed on {' and '.join(weak_categories)}."
    
    # Generate basic recommendations
    recommendations = [
        f"Focus on improving {weak_categories[0]} dimensions through targeted initiatives and resource allocation.",
        "Conduct a detailed risk assessment and develop mitigation strategies for low-scoring areas.",
        "Engage stakeholders early to build support and address organizational readiness concerns."
    ]
    
    return insights, recommendations

