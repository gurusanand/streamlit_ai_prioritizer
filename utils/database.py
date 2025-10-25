"""
Database utility - SQLite database operations
"""

import sqlite3
import json
from datetime import datetime
from pathlib import Path

class Database:
    def __init__(self, db_path='data/assessments.db'):
        """Initialize database connection"""
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.init_database()
    
    def get_connection(self):
        """Get database connection"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_database(self):
        """Initialize database tables"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Use cases table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS use_cases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                use_case_id TEXT NOT NULL UNIQUE,
                name TEXT NOT NULL,
                description TEXT,
                business_unit TEXT,
                process_owner TEXT,
                status TEXT DEFAULT 'draft',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Assessment scores table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS assessment_scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                use_case_id INTEGER NOT NULL,
                dimension TEXT NOT NULL,
                category TEXT NOT NULL,
                score INTEGER NOT NULL,
                weight INTEGER NOT NULL,
                weighted_score INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (use_case_id) REFERENCES use_cases(id) ON DELETE CASCADE
            )
        ''')
        
        # Assessment summaries table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS assessment_summaries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                use_case_id INTEGER NOT NULL UNIQUE,
                total_score INTEGER NOT NULL,
                normalized_score INTEGER NOT NULL,
                category_scores TEXT NOT NULL,
                ai_insights TEXT,
                recommendations TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (use_case_id) REFERENCES use_cases(id) ON DELETE CASCADE
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def create_use_case(self, use_case_id, name, description='', business_unit='', process_owner=''):
        """Create a new use case"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO use_cases (use_case_id, name, description, business_unit, process_owner)
            VALUES (?, ?, ?, ?, ?)
        ''', (use_case_id, name, description, business_unit, process_owner))
        
        uc_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return uc_id
    
    def get_all_use_cases(self):
        """Get all use cases"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM use_cases ORDER BY created_at DESC')
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def get_use_case(self, use_case_id):
        """Get a specific use case"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM use_cases WHERE id = ?', (use_case_id,))
        row = cursor.fetchone()
        conn.close()
        
        return dict(row) if row else None
    
    def delete_use_case(self, use_case_id):
        """Delete a use case and all related data"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM use_cases WHERE id = ?', (use_case_id,))
        conn.commit()
        conn.close()
    
    def save_assessment(self, use_case_id, scores, total_score, normalized_score, 
                       category_scores, ai_insights='', recommendations=None):
        """Save assessment results"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Delete existing scores
        cursor.execute('DELETE FROM assessment_scores WHERE use_case_id = ?', (use_case_id,))
        
        # Insert new scores
        for score in scores:
            cursor.execute('''
                INSERT INTO assessment_scores 
                (use_case_id, dimension, category, score, weight, weighted_score)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                use_case_id,
                score['dimension'],
                score['category'],
                score['score'],
                score['weight'],
                score['score'] * score['weight']
            ))
        
        # Save or update summary
        category_scores_json = json.dumps(category_scores)
        recommendations_json = json.dumps(recommendations) if recommendations else '[]'
        
        cursor.execute('''
            INSERT OR REPLACE INTO assessment_summaries
            (use_case_id, total_score, normalized_score, category_scores, ai_insights, recommendations)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (use_case_id, total_score, normalized_score, category_scores_json, 
              ai_insights, recommendations_json))
        
        # Update use case status
        cursor.execute('''
            UPDATE use_cases SET status = 'completed', updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (use_case_id,))
        
        conn.commit()
        conn.close()
    
    def get_assessment_scores(self, use_case_id):
        """Get assessment scores for a use case"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM assessment_scores WHERE use_case_id = ?
        ''', (use_case_id,))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def get_assessment_summary(self, use_case_id):
        """Get assessment summary for a use case"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM assessment_summaries WHERE use_case_id = ?
        ''', (use_case_id,))
        
        row = cursor.fetchone()
        conn.close()
        
        if not row:
            return None
        
        summary = dict(row)
        summary['category_scores'] = json.loads(summary['category_scores'])
        summary['recommendations'] = json.loads(summary['recommendations']) if summary['recommendations'] else []
        summary['created_at'] = datetime.fromisoformat(summary['created_at'])
        
        return summary

