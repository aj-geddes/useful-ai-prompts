#!/usr/bin/env python3
"""
Enhanced Search System for AI Prompts Repository
Optimized for 500+ prompts with advanced filtering, relevance scoring, and performance
"""

import os
import json
import re
import math
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Set
from collections import defaultdict, Counter
import yaml
import argparse
from dataclasses import dataclass
import nltk
try:
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)

@dataclass
class SearchResult:
    """Search result with relevance scoring"""
    title: str
    description: str
    category: str
    tags: List[str]
    slug: str
    file_path: str
    relevance_score: float
    matched_terms: List[str]
    matched_sections: List[str]
    use_cases: List[str]
    frameworks: List[str]
    expertise_level: str
    estimated_output_length: int

@dataclass
class SearchIndex:
    """Optimized search index structure"""
    version: str
    last_updated: str
    total_prompts: int
    categories: List[str]
    all_tags: List[str]
    prompts: List[Dict]
    inverted_index: Dict[str, List[int]]  # term -> list of prompt indices
    category_index: Dict[str, List[int]]  # category -> list of prompt indices
    tag_index: Dict[str, List[int]]  # tag -> list of prompt indices
    framework_index: Dict[str, List[int]]  # framework -> list of prompt indices
    tf_idf_scores: Dict[int, Dict[str, float]]  # prompt_id -> {term: tf_idf_score}
    performance_metrics: Dict

class EnhancedSearchSystem:
    """Advanced search system optimized for 500+ AI prompts"""
    
    def __init__(self, repo_root: str = None):
        self.repo_root = Path(repo_root) if repo_root else Path.cwd()
        self.docs_dir = self.repo_root / "docs"
        self.jekyll_prompts_dir = self.docs_dir / "_prompts"
        self.assets_dir = self.docs_dir / "assets" / "data"
        
        # Search configuration
        self.stop_words = set(stopwords.words('english')) if 'stopwords' in dir() else set()
        self.min_term_length = 2
        self.max_results = 50
        
        # Relevance scoring weights
        self.scoring_weights = {
            'title_match': 3.0,
            'description_match': 2.0,
            'tag_match': 2.5,
            'category_match': 1.5,
            'content_match': 1.0,
            'framework_match': 1.8,
            'use_case_match': 1.6,
            'exact_phrase': 2.0,
            'term_frequency': 1.0,
            'inverse_document_frequency': 1.0
        }
        
        # Performance tracking
        self.search_stats = {
            'total_searches': 0,
            'average_search_time': 0,
            'cache_hits': 0,
            'index_build_time': 0
        }
        
        # Search cache for performance
        self.search_cache = {}
        self.cache_max_size = 1000
    
    def build_enhanced_index(self) -> SearchIndex:
        """Build comprehensive search index optimized for 500+ prompts"""
        start_time = time.time()
        
        print("Building enhanced search index...")
        
        # Collect all prompts
        all_prompts = []
        inverted_index = defaultdict(list)
        category_index = defaultdict(list)
        tag_index = defaultdict(list)
        framework_index = defaultdict(list)
        tf_idf_scores = {}
        
        # Document frequency counter for IDF calculation
        document_frequencies = Counter()
        all_documents = []
        
        for i, prompt_file in enumerate(self.jekyll_prompts_dir.glob("*.md")):
            try:
                with open(prompt_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract frontmatter and content
                prompt_data = self._extract_prompt_data(content, prompt_file, i)
                if prompt_data:
                    all_prompts.append(prompt_data)
                    
                    # Build document text for TF-IDF
                    document_text = self._extract_searchable_text(prompt_data)
                    all_documents.append(document_text)
                    
                    # Update indices
                    self._update_indices(prompt_data, i, inverted_index, category_index, 
                                       tag_index, framework_index, document_frequencies)
                    
                    if i % 50 == 0:
                        print(f"Processed {i+1} prompts...")
                        
            except Exception as e:
                print(f"Error processing {prompt_file}: {e}")
        
        print(f"Calculating TF-IDF scores for {len(all_prompts)} prompts...")
        
        # Calculate TF-IDF scores
        total_documents = len(all_documents)
        for i, (prompt_data, document_text) in enumerate(zip(all_prompts, all_documents)):
            tf_idf_scores[i] = self._calculate_tf_idf(document_text, document_frequencies, total_documents)
        
        # Create optimized search index
        build_time = time.time() - start_time
        
        search_index = SearchIndex(
            version="2.0.0",
            last_updated=datetime.now().isoformat(),
            total_prompts=len(all_prompts),
            categories=list(set(p['category'] for p in all_prompts)),
            all_tags=list(set(tag for p in all_prompts for tag in p['tags'])),
            prompts=all_prompts,
            inverted_index=dict(inverted_index),
            category_index=dict(category_index),
            tag_index=dict(tag_index),
            framework_index=dict(framework_index),
            tf_idf_scores=tf_idf_scores,
            performance_metrics={
                'build_time_seconds': build_time,
                'total_terms': len(inverted_index),
                'average_prompt_length': sum(p['word_count'] for p in all_prompts) / len(all_prompts) if all_prompts else 0,
                'category_distribution': self._calculate_category_distribution(all_prompts),
                'index_memory_estimate_mb': self._estimate_memory_usage(inverted_index, tf_idf_scores)
            }
        )
        
        self.search_stats['index_build_time'] = build_time
        
        print(f"✓ Enhanced search index built successfully!")
        print(f"  Total prompts: {len(all_prompts)}")
        print(f"  Total terms: {len(inverted_index)}")
        print(f"  Build time: {build_time:.2f} seconds")
        print(f"  Memory estimate: {search_index.performance_metrics['index_memory_estimate_mb']:.1f} MB")
        
        return search_index
    
    def _extract_prompt_data(self, content: str, file_path: Path, index: int) -> Optional[Dict]:
        """Extract structured data from prompt file"""
        if not content.startswith('---'):
            return None
        
        try:
            frontmatter_end = content.find('---', 3)
            if frontmatter_end <= 0:
                return None
            
            frontmatter = yaml.safe_load(content[3:frontmatter_end])
            body_content = content[frontmatter_end + 3:]
            
            # Extract searchable content
            searchable_text = self._extract_full_searchable_text(body_content)
            frameworks = self._extract_frameworks(body_content)
            expertise_level = self._determine_expertise_level(body_content)
            
            return {
                'id': index,
                'title': frontmatter.get('title', ''),
                'description': frontmatter.get('description', ''),
                'category': frontmatter.get('category', ''),
                'tags': frontmatter.get('tags', []),
                'slug': frontmatter.get('slug', ''),
                'use_cases': frontmatter.get('use_cases', []),
                'file_path': f"_prompts/{file_path.name}",
                'word_count': len(body_content.split()),
                'frameworks': frameworks,
                'expertise_level': expertise_level,
                'searchable_content': searchable_text,
                'estimated_output_length': self._estimate_output_length(body_content)
            }
        except Exception as e:
            print(f"Error extracting data from {file_path}: {e}")
            return None
    
    def _extract_full_searchable_text(self, content: str) -> str:
        """Extract comprehensive searchable text from prompt content"""
        # Remove markdown formatting but keep structure
        text = re.sub(r'[#*_`]', '', content)
        text = re.sub(r'\n+', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        
        # Extract key sections for enhanced searchability
        key_sections = []
        
        # Extract objectives and deliverables
        objectives = re.findall(r'(?:Objective|Goal|Purpose):\s*(.+?)(?=\n|$)', text, re.IGNORECASE)
        key_sections.extend(objectives)
        
        deliverables = re.findall(r'(?:Deliverable|Output|Result).*?:(.+?)(?=\n|$)', text, re.IGNORECASE)
        key_sections.extend(deliverables)
        
        # Extract framework descriptions
        frameworks = re.findall(r'Framework \d+:(.+?)(?=Framework|\n##|\n###|$)', text, re.DOTALL)
        key_sections.extend([f[:200] for f in frameworks])  # Limit length
        
        # Extract phase descriptions
        phases = re.findall(r'Phase \d+.*?Objective.*?:(.+?)(?=Phase|\n##|\n###|$)', text, re.DOTALL)
        key_sections.extend([p[:200] for p in phases])  # Limit length
        
        # Combine with original text (truncated for performance)
        full_text = text[:1000] + ' '.join(key_sections)
        return full_text[:2000]  # Limit total length for performance
    
    def _extract_frameworks(self, content: str) -> List[str]:
        """Extract framework names from content"""
        frameworks = re.findall(r'### Framework \d+:\s*(.+)', content)
        return [f.strip() for f in frameworks]
    
    def _determine_expertise_level(self, content: str) -> str:
        """Determine expertise level based on content complexity"""
        # Count technical indicators
        technical_terms = len(re.findall(r'\b(?:methodology|architecture|optimization|framework|analysis|assessment|governance|compliance)\b', content, re.IGNORECASE))
        phase_count = len(re.findall(r'Phase \d+', content))
        framework_count = len(re.findall(r'Framework \d+', content))
        deliverable_count = len(re.findall(r'\d+\.\s+\w+', content))
        
        complexity_score = technical_terms + (phase_count * 5) + (framework_count * 3) + deliverable_count
        
        if complexity_score > 50:
            return "expert"
        elif complexity_score > 25:
            return "advanced"
        elif complexity_score > 10:
            return "intermediate"
        else:
            return "beginner"
    
    def _estimate_output_length(self, content: str) -> int:
        """Estimate expected output length"""
        deliverable_count = len(re.findall(r'\d+\.\s+', content))
        phase_count = len(re.findall(r'Phase \d+', content))
        framework_count = len(re.findall(r'Framework \d+', content))
        
        base_length = 400
        complexity_bonus = (deliverable_count * 15) + (phase_count * 50) + (framework_count * 30)
        
        return base_length + complexity_bonus
    
    def _extract_searchable_text(self, prompt_data: Dict) -> str:
        """Extract text for search indexing"""
        components = [
            prompt_data.get('title', ''),
            prompt_data.get('description', ''),
            ' '.join(prompt_data.get('tags', [])),
            ' '.join(prompt_data.get('use_cases', [])),
            ' '.join(prompt_data.get('frameworks', [])),
            prompt_data.get('searchable_content', '')[:500]  # Limit for performance
        ]
        return ' '.join(filter(None, components))
    
    def _update_indices(self, prompt_data: Dict, index: int, inverted_index: Dict, 
                       category_index: Dict, tag_index: Dict, framework_index: Dict,
                       document_frequencies: Counter):
        """Update all search indices"""
        # Extract and tokenize searchable text
        searchable_text = self._extract_searchable_text(prompt_data)
        terms = self._tokenize_and_clean(searchable_text)
        
        # Update inverted index and document frequencies
        unique_terms = set(terms)
        for term in unique_terms:
            inverted_index[term].append(index)
            document_frequencies[term] += 1
        
        # Update category index
        category = prompt_data.get('category', '')
        if category:
            category_index[category].append(index)
        
        # Update tag index
        for tag in prompt_data.get('tags', []):
            tag_index[tag].append(index)
        
        # Update framework index
        for framework in prompt_data.get('frameworks', []):
            framework_clean = self._clean_term(framework)
            if framework_clean:
                framework_index[framework_clean].append(index)
    
    def _tokenize_and_clean(self, text: str) -> List[str]:
        """Tokenize and clean text for indexing"""
        # Convert to lowercase and tokenize
        try:
            tokens = word_tokenize(text.lower())
        except:
            tokens = re.findall(r'\b\w+\b', text.lower())
        
        # Clean and filter tokens
        cleaned_tokens = []
        for token in tokens:
            cleaned = self._clean_term(token)
            if cleaned and cleaned not in self.stop_words and len(cleaned) >= self.min_term_length:
                cleaned_tokens.append(cleaned)
        
        return cleaned_tokens
    
    def _clean_term(self, term: str) -> str:
        """Clean and normalize search term"""
        # Remove non-alphanumeric characters and normalize
        cleaned = re.sub(r'[^a-z0-9]', '', term.lower())
        return cleaned if len(cleaned) >= self.min_term_length else ''
    
    def _calculate_tf_idf(self, document_text: str, document_frequencies: Counter, 
                         total_documents: int) -> Dict[str, float]:
        """Calculate TF-IDF scores for document terms"""
        terms = self._tokenize_and_clean(document_text)
        term_counts = Counter(terms)
        total_terms = len(terms)
        
        tf_idf_scores = {}
        
        for term, count in term_counts.items():
            # Term Frequency
            tf = count / total_terms if total_terms > 0 else 0
            
            # Inverse Document Frequency
            df = document_frequencies.get(term, 1)
            idf = math.log(total_documents / df) if df > 0 else 0
            
            # TF-IDF Score
            tf_idf_scores[term] = tf * idf
        
        return tf_idf_scores
    
    def _calculate_category_distribution(self, prompts: List[Dict]) -> Dict[str, int]:
        """Calculate distribution of prompts across categories"""
        distribution = defaultdict(int)
        for prompt in prompts:
            category = prompt.get('category', 'uncategorized')
            distribution[category] += 1
        return dict(distribution)
    
    def _estimate_memory_usage(self, inverted_index: Dict, tf_idf_scores: Dict) -> float:
        """Estimate memory usage of search index in MB"""
        # Rough estimation based on data structures
        inverted_size = sum(len(term) + len(indices) * 4 for term, indices in inverted_index.items())
        tfidf_size = sum(len(scores) * 8 for scores in tf_idf_scores.values())
        total_bytes = inverted_size + tfidf_size
        return total_bytes / (1024 * 1024)  # Convert to MB
    
    def search(self, query: str, search_index: SearchIndex, filters: Dict = None,
               max_results: int = None) -> List[SearchResult]:
        """Perform enhanced search with relevance scoring"""
        start_time = time.time()
        
        # Check cache first
        cache_key = f"{query}:{str(filters)}:{max_results}"
        if cache_key in self.search_cache:
            self.search_stats['cache_hits'] += 1
            return self.search_cache[cache_key]
        
        max_results = max_results or self.max_results
        filters = filters or {}
        
        # Tokenize and clean query
        query_terms = self._tokenize_and_clean(query)
        if not query_terms:
            return []
        
        # Get candidate prompts from inverted index
        candidate_indices = self._get_candidate_prompts(query_terms, search_index, filters)
        
        # Score and rank candidates
        scored_results = []
        for prompt_index in candidate_indices:
            if prompt_index < len(search_index.prompts):
                prompt_data = search_index.prompts[prompt_index]
                score = self._calculate_relevance_score(
                    query, query_terms, prompt_data, search_index.tf_idf_scores.get(prompt_index, {})
                )
                
                if score > 0:
                    result = self._create_search_result(prompt_data, score, query_terms)
                    scored_results.append(result)
        
        # Sort by relevance score and return top results
        scored_results.sort(key=lambda x: x.relevance_score, reverse=True)
        final_results = scored_results[:max_results]
        
        # Update cache
        if len(self.search_cache) < self.cache_max_size:
            self.search_cache[cache_key] = final_results
        
        # Update statistics
        search_time = time.time() - start_time
        self.search_stats['total_searches'] += 1
        self.search_stats['average_search_time'] = (
            (self.search_stats['average_search_time'] * (self.search_stats['total_searches'] - 1) + search_time) /
            self.search_stats['total_searches']
        )
        
        return final_results
    
    def _get_candidate_prompts(self, query_terms: List[str], search_index: SearchIndex,
                              filters: Dict) -> Set[int]:
        """Get candidate prompt indices based on query terms and filters"""
        candidates = set()
        
        # Get prompts matching query terms
        for term in query_terms:
            if term in search_index.inverted_index:
                candidates.update(search_index.inverted_index[term])
        
        # Apply filters
        if filters.get('category'):
            category_candidates = set(search_index.category_index.get(filters['category'], []))
            candidates = candidates.intersection(category_candidates) if candidates else category_candidates
        
        if filters.get('tags'):
            tag_candidates = set()
            for tag in filters['tags']:
                tag_candidates.update(search_index.tag_index.get(tag, []))
            candidates = candidates.intersection(tag_candidates) if candidates else tag_candidates
        
        if filters.get('frameworks'):
            framework_candidates = set()
            for framework in filters['frameworks']:
                framework_clean = self._clean_term(framework)
                framework_candidates.update(search_index.framework_index.get(framework_clean, []))
            candidates = candidates.intersection(framework_candidates) if candidates else framework_candidates
        
        if filters.get('expertise_level'):
            expertise_candidates = set()
            for i, prompt in enumerate(search_index.prompts):
                if prompt.get('expertise_level') == filters['expertise_level']:
                    expertise_candidates.add(i)
            candidates = candidates.intersection(expertise_candidates) if candidates else expertise_candidates
        
        return candidates
    
    def _calculate_relevance_score(self, original_query: str, query_terms: List[str],
                                  prompt_data: Dict, tf_idf_scores: Dict[str, float]) -> float:
        """Calculate relevance score for a prompt"""
        score = 0.0
        matched_terms = []
        
        title = prompt_data.get('title', '').lower()
        description = prompt_data.get('description', '').lower()
        tags = [tag.lower() for tag in prompt_data.get('tags', [])]
        category = prompt_data.get('category', '').lower()
        use_cases = [uc.lower() for uc in prompt_data.get('use_cases', [])]
        frameworks = [fw.lower() for fw in prompt_data.get('frameworks', [])]
        content = prompt_data.get('searchable_content', '').lower()
        
        query_lower = original_query.lower()
        
        # Exact phrase matching (highest weight)
        if query_lower in title:
            score += self.scoring_weights['exact_phrase'] * 2
        if query_lower in description:
            score += self.scoring_weights['exact_phrase']
        
        # Individual term matching
        for term in query_terms:
            term_score = 0
            
            # Title matching
            if term in title:
                term_score += self.scoring_weights['title_match']
                matched_terms.append(term)
            
            # Description matching
            if term in description:
                term_score += self.scoring_weights['description_match']
                matched_terms.append(term)
            
            # Tag matching
            if any(term in tag for tag in tags):
                term_score += self.scoring_weights['tag_match']
                matched_terms.append(term)
            
            # Category matching
            if term in category:
                term_score += self.scoring_weights['category_match']
                matched_terms.append(term)
            
            # Use case matching
            if any(term in uc for uc in use_cases):
                term_score += self.scoring_weights['use_case_match']
                matched_terms.append(term)
            
            # Framework matching
            if any(term in fw for fw in frameworks):
                term_score += self.scoring_weights['framework_match']
                matched_terms.append(term)
            
            # Content matching with TF-IDF
            if term in content:
                content_score = self.scoring_weights['content_match']
                if term in tf_idf_scores:
                    content_score *= (1 + tf_idf_scores[term])
                term_score += content_score
                matched_terms.append(term)
            
            score += term_score
        
        # Bonus for multiple term matches
        unique_matches = len(set(matched_terms))
        if unique_matches > 1:
            score *= (1 + 0.1 * unique_matches)
        
        return score
    
    def _create_search_result(self, prompt_data: Dict, score: float, query_terms: List[str]) -> SearchResult:
        """Create search result object"""
        matched_sections = []
        content = prompt_data.get('searchable_content', '').lower()
        
        for term in query_terms:
            if term in content:
                # Find context around matched term
                pattern = rf'\b\w*{re.escape(term)}\w*\b'
                matches = re.finditer(pattern, content, re.IGNORECASE)
                for match in matches:
                    start = max(0, match.start() - 30)
                    end = min(len(content), match.end() + 30)
                    context = content[start:end].strip()
                    if context:
                        matched_sections.append(f"...{context}...")
        
        return SearchResult(
            title=prompt_data.get('title', ''),
            description=prompt_data.get('description', ''),
            category=prompt_data.get('category', ''),
            tags=prompt_data.get('tags', []),
            slug=prompt_data.get('slug', ''),
            file_path=prompt_data.get('file_path', ''),
            relevance_score=score,
            matched_terms=list(set(query_terms)),
            matched_sections=matched_sections[:3],  # Limit to top 3 contexts
            use_cases=prompt_data.get('use_cases', []),
            frameworks=prompt_data.get('frameworks', []),
            expertise_level=prompt_data.get('expertise_level', ''),
            estimated_output_length=prompt_data.get('estimated_output_length', 0)
        )
    
    def save_search_index(self, search_index: SearchIndex, filepath: str = None):
        """Save optimized search index to file"""
        if filepath is None:
            filepath = self.assets_dir / "enhanced-search-index.json"
        
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        # Convert SearchIndex to serializable format
        index_data = {
            'version': search_index.version,
            'last_updated': search_index.last_updated,
            'total_prompts': search_index.total_prompts,
            'categories': search_index.categories,
            'all_tags': search_index.all_tags,
            'prompts': search_index.prompts,
            'inverted_index': search_index.inverted_index,
            'category_index': search_index.category_index,
            'tag_index': search_index.tag_index,
            'framework_index': search_index.framework_index,
            'tf_idf_scores': {str(k): v for k, v in search_index.tf_idf_scores.items()},
            'performance_metrics': search_index.performance_metrics
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, indent=2, ensure_ascii=False)
        
        file_size_mb = filepath.stat().st_size / (1024 * 1024)
        print(f"✓ Enhanced search index saved to: {filepath}")
        print(f"  File size: {file_size_mb:.2f} MB")
    
    def load_search_index(self, filepath: str = None) -> SearchIndex:
        """Load search index from file"""
        if filepath is None:
            filepath = self.assets_dir / "enhanced-search-index.json"
        
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Convert back to SearchIndex
        return SearchIndex(
            version=data['version'],
            last_updated=data['last_updated'],
            total_prompts=data['total_prompts'],
            categories=data['categories'],
            all_tags=data['all_tags'],
            prompts=data['prompts'],
            inverted_index=data['inverted_index'],
            category_index=data['category_index'],
            tag_index=data['tag_index'],
            framework_index=data['framework_index'],
            tf_idf_scores={int(k): v for k, v in data['tf_idf_scores'].items()},
            performance_metrics=data['performance_metrics']
        )
    
    def generate_search_performance_report(self) -> Dict:
        """Generate search performance analytics report"""
        return {
            'timestamp': datetime.now().isoformat(),
            'search_statistics': self.search_stats,
            'cache_performance': {
                'cache_size': len(self.search_cache),
                'max_cache_size': self.cache_max_size,
                'hit_rate': self.search_stats['cache_hits'] / max(self.search_stats['total_searches'], 1) * 100
            },
            'recommendations': self._generate_performance_recommendations()
        }
    
    def _generate_performance_recommendations(self) -> List[str]:
        """Generate performance optimization recommendations"""
        recommendations = []
        
        if self.search_stats['average_search_time'] > 0.1:
            recommendations.append("Consider optimizing search algorithm for better response times")
        
        if self.search_stats['cache_hits'] / max(self.search_stats['total_searches'], 1) < 0.3:
            recommendations.append("Increase cache size to improve search performance")
        
        if self.search_stats['index_build_time'] > 30:
            recommendations.append("Optimize index building process for large prompt collections")
        
        return recommendations

def main():
    """Main CLI interface for enhanced search system"""
    parser = argparse.ArgumentParser(description="Enhanced Search System for AI Prompts")
    parser.add_argument("--repo-root", default=".", help="Repository root directory")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Build index command
    build_parser = subparsers.add_parser("build", help="Build enhanced search index")
    build_parser.add_argument("--output", help="Output file for search index")
    
    # Search command
    search_parser = subparsers.add_parser("search", help="Search prompts")
    search_parser.add_argument("query", help="Search query")
    search_parser.add_argument("--category", help="Filter by category")
    search_parser.add_argument("--tags", nargs="+", help="Filter by tags")
    search_parser.add_argument("--expertise", choices=["beginner", "intermediate", "advanced", "expert"], help="Filter by expertise level")
    search_parser.add_argument("--max-results", type=int, default=10, help="Maximum number of results")
    
    # Performance command
    perf_parser = subparsers.add_parser("performance", help="Generate performance report")
    
    args = parser.parse_args()
    
    search_system = EnhancedSearchSystem(args.repo_root)
    
    if args.command == "build":
        search_index = search_system.build_enhanced_index()
        output_file = args.output or (search_system.assets_dir / "enhanced-search-index.json")
        search_system.save_search_index(search_index, output_file)
        
    elif args.command == "search":
        try:
            search_index = search_system.load_search_index()
        except FileNotFoundError:
            print("Search index not found. Please run 'build' command first.")
            return 1
        
        filters = {}
        if args.category:
            filters['category'] = args.category
        if args.tags:
            filters['tags'] = args.tags
        if args.expertise:
            filters['expertise_level'] = args.expertise
        
        results = search_system.search(args.query, search_index, filters, args.max_results)
        
        print(f"Found {len(results)} results for '{args.query}':")
        print("=" * 60)
        
        for i, result in enumerate(results, 1):
            print(f"{i}. {result.title}")
            print(f"   Category: {result.category} | Score: {result.relevance_score:.2f}")
            print(f"   {result.description}")
            if result.matched_sections:
                print(f"   Matched: {result.matched_sections[0]}")
            print()
        
    elif args.command == "performance":
        report = search_system.generate_search_performance_report()
        print(json.dumps(report, indent=2))
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()