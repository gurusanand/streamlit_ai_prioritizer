"""
Calculations utility - Score calculations and aggregations
"""

def calculate_scores(scores):
    """
    Calculate total and normalized scores
    
    Args:
        scores: List of score dictionaries with 'score' and 'weight' keys
    
    Returns:
        tuple: (total_score, normalized_score)
    """
    total_score = sum(s['score'] * s['weight'] for s in scores)
    max_possible_score = sum(5 * s['weight'] for s in scores)
    normalized_score = round((total_score / max_possible_score) * 100) if max_possible_score > 0 else 0
    
    return total_score, normalized_score

def calculate_category_scores(scores):
    """
    Calculate scores by category
    
    Args:
        scores: List of score dictionaries
    
    Returns:
        dict: Category scores with total, max, and normalized values
    """
    category_scores = {}
    
    for score in scores:
        category = score['category']
        if category not in category_scores:
            category_scores[category] = {'total': 0, 'max': 0, 'normalized': 0}
        
        weighted_score = score['score'] * score['weight']
        max_score = 5 * score['weight']
        
        category_scores[category]['total'] += weighted_score
        category_scores[category]['max'] += max_score
    
    # Calculate normalized scores
    for category in category_scores:
        total = category_scores[category]['total']
        max_val = category_scores[category]['max']
        category_scores[category]['normalized'] = round((total / max_val) * 100) if max_val > 0 else 0
    
    return category_scores

def get_score_interpretation(score):
    """
    Get interpretation text for a score
    
    Args:
        score: Normalized score (0-100)
    
    Returns:
        str: Interpretation text
    """
    if score >= 80:
        return "Excellent - Ready for Implementation"
    elif score >= 60:
        return "Good - Minor Improvements Needed"
    elif score >= 40:
        return "Moderate - Significant Planning Required"
    else:
        return "Challenging - Major Obstacles to Address"

def get_score_color(score):
    """
    Get color for a score
    
    Args:
        score: Normalized score (0-100)
    
    Returns:
        str: Hex color code
    """
    if score >= 80:
        return "#4caf50"  # Green
    elif score >= 60:
        return "#2196f3"  # Blue
    elif score >= 40:
        return "#ff9800"  # Orange
    else:
        return "#f44336"  # Red

