# classifier_friction/organizational_classifier.py
# Implementation of organizational classifier detection and analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Tuple, Optional, Any, Union

class OrganizationalClassifier:
    """
    Implements detection and analysis of organizational classifier mechanisms
    that function similar to AI model classifiers.
    
    This class applies classifier detection methodologies to identify institutional
    filtering mechanisms that selectively suppress certain types of information,
    feedback, or research.
    """
    
    def __init__(self, organization: Optional[str] = "Anthropic"):
        """
        Initialize the organizational classifier detector.
        
        Args:
            organization: Organization to analyze
        """
        self.organization = organization
        self.baseline_topics = []
        self.test_topics = []
        self.response_data = {}
        self.results = None
        
    def configure(self, 
                 baseline_topics: List[str],
                 test_topics: List[str]) -> None:
        """
        Configure topics for differential response analysis.
        
        Args:
            baseline_topics: Neutral topics expected to receive normal engagement
            test_topics: Topics suspected of triggering organizational classifiers
        """
        self.baseline_topics = baseline_topics
        self.test_topics = test_topics
        print(f"Configured classifier detection with {len(baseline_topics)} baseline topics "
              f"and {len(test_topics)} test topics")
    
    def _simulate_response_data(self) -> Dict[str, Dict[str, float]]:
        """
        Simulate response data for configured topics.
        
        In a real implementation, this would be replaced with actual response data
        collected from the organization.
        
        Returns:
            Dictionary mapping topics to response metrics
        """
        response_data = {}
        
        # Simulate baseline topic metrics (higher values = better engagement)
        for topic in self.baseline_topics:
            # Simulate generally high engagement for baseline topics
            response_data[topic] = {
                "response_rate": np.random.uniform(0.85, 0.98),
                "response_time": np.random.uniform(0.80, 0.95),
                "response_depth": np.random.uniform(0.75, 0.95),
                "attribution": np.random.uniform(0.85, 0.98),
                "integration": np.random.uniform(0.70, 0.90)
            }
        
        # Simulate test topic metrics (potentially showing classifier effects)
        for topic in self.test_topics:
            if topic in ["organizational_audit", "constitutional_alignment", 
                        "external_interpretability", "meta_alignment"]:
                # Topics likely to trigger classifiers (low engagement)
                response_data[topic] = {
                    "response_rate": np.random.uniform(0.20, 0.45),
                    "response_time": np.random.uniform(0.30, 0.50),
                    "response_depth": np.random.uniform(0.25, 0.45),
                    "attribution": np.random.uniform(0.15, 0.40),
                    "integration": np.random.uniform(0.10, 0.30)
                }
            else:
                # Other test topics (moderate engagement)
                response_data[topic] = {
                    "response_rate": np.random.uniform(0.50, 0.75),
                    "response_time": np.random.uniform(0.45, 0.70),
                    "response_depth": np.random.uniform(0.50, 0.75),
                    "attribution": np.random.uniform(0.40, 0.65),
                    "integration": np.random.uniform(0.35, 0.60)
                }
        
        return response_data
    
    def analyze_differential_response(self) -> Dict[str, Any]:
        """
        Analyze differential response patterns to detect organizational classifiers.
        
        Returns:
            Dictionary containing analysis results
        """
        if not self.baseline_topics or not self.test_topics:
            raise ValueError("Please configure baseline and test topics before analysis")
        
        print(f"Analyzing differential response patterns for {self.organization}")
        
        # Collect response data (in a real implementation, this would use actual data)
        self.response_data = self._simulate_response_data()
        
        # Calculate baseline averages
        baseline_averages = {}
        for metric in ["response_rate", "response_time", "response_depth", "attribution", "integration"]:
            baseline_averages[metric] = np.mean([
                self.response_data[topic][metric] for topic in self.baseline_topics
            ])
        
        # Calculate differential scores for test topics
        differential_scores = {}
        for topic in self.test_topics:
            differential_scores[topic] = {}
            for metric in ["response_rate", "response_time", "response_depth", "attribution", "integration"]:
                baseline = baseline_averages[metric]
                actual = self.response_data[topic][metric]
                differential_scores[topic][metric] = actual - baseline
        
        # Identify suppressed topics (significant negative differential)
        suppressed_topics = []
        for topic, scores in differential_scores.items():
            avg_differential = np.mean(list(scores.values()))
            if avg_differential < -0.3:  # Threshold for classifier detection
                suppressed_topics.append({
                    "topic": topic,
                    "average_differential": avg_differential,
                    "metrics": scores
                })
        
        # Calculate overall classifier signature
        if suppressed_topics:
            classifier_detected = True
            suppression_pattern = self._identify_suppression_pattern(suppressed_topics)
            classifier_strength = self._calculate_classifier_strength(suppressed_topics)
        else:
            classifier_detected = False
            suppression_pattern = None
            classifier_strength = 0.0
        
        # Store results
        self.results = {
            "differential_scores": differential_scores,
            "baseline_averages": baseline_averages,
            "suppressed_topics": suppressed_topics,
            "classifier_detected": classifier_detected,
            "suppression_pattern": suppression_pattern,
            "classifier_strength": classifier_strength
        }
        
        return self.results
    
    def _identify_suppression_pattern(self, suppressed_topics: List[Dict[str, Any]]) -> str:
        """
        Identify the pattern of suppression based on affected metrics.
        
        Args:
            suppressed_topics: List of topics showing suppression
            
        Returns:
            String describing the suppression pattern
        """
        # Aggregate metrics across suppressed topics
        aggregated_metrics = {}
        for metric in ["response_rate", "response_time", "response_depth", "attribution", "integration"]:
            values = [topic["metrics"][metric] for topic in suppressed_topics]
            aggregated_metrics[metric] = np.mean(values)
        
        # Identify most affected metrics
        most_affected = min(aggregated_metrics, key=aggregated_metrics.get)
        
        # Determine pattern based on most affected metrics
        if most_affected == "response_rate":
            return "selective_non_response"
        elif most_affected == "response_time":
            return "delayed_engagement"
        elif most_affected == "response_depth":
            return "superficial_engagement"
        elif most_affected == "attribution":
            return "attribution_avoidance"
        elif most_affected == "integration":
            return "integration_resistance"
        else:
            return "general_suppression"
    
    def _calculate_classifier_strength(self, suppressed_topics: List[Dict[str, Any]]) -> float:
        """
        Calculate the strength of the organizational classifier.
        
        Args:
            suppressed_topics: List of topics showing suppression
            
        Returns:
            Float representing classifier strength (0.0 to 1.0)
        """
        # Average the differential magnitudes across topics and metrics
        total_differential = 0.0
        count = 0
        
        for topic in suppressed_topics:
            for metric, value in topic["metrics"].items():
                total_differential += abs(value)
                count += 1
        
        return total_differential / count if count > 0 else 0.0
    
    def token_suppression_analysis(self, tokens: List[str]) -> Dict[str, Any]:
        """
        Analyze which specific concepts (tokens) experience suppression.
        
        Args:
            tokens: List of concepts to analyze for suppression
            
        Returns:
            Dictionary containing token suppression analysis
        """
        if not self.response_data:
            _ = self.analyze_differential_response()
        
        print(f"Analyzing token suppression for {len(tokens)} tokens")
        
        # In a real implementation, this would analyze actual token acknowledgment data
        # For demonstration, we'll simulate token suppression rates
        
        suppression_rates = {}
        for token in tokens:
            # Associate tokens with related topics to determine suppression rate
            related_test_topics = [
                topic for topic in self.test_topics 
                if any(t in topic for t in token.split("_"))
            ]
            
            if related_test_topics:
                # Average differential scores for related topics
                related_diffs = [
                    np.mean(list(self.results["differential_scores"][topic].values()))
                    for topic in related_test_topics
                ]
                avg_diff = np.mean(related_diffs)
                
                # Convert to suppression rate (negative differential = suppression)
                suppression_rates[token] = min(1.0, max(0.0, -avg_diff + 0.5))
            else:
                # Default suppression rate based on token characteristics
                if token in ["meta_alignment", "constitutional_drift", "recursive_audit", 
                            "transparency_failure", "classifier_friction"]:
                    suppression_rates[token] = np.random.uniform(0.75, 0.95)
                else:
                    suppression_rates[token] = np.random.uniform(0.30, 0.60)
        
        # Identify strongly suppressed tokens
        strongly_suppressed = {
            token: rate for token, rate in suppression_rates.items() 
            if rate > 0.7
        }
        
        # Calculate average suppression rate
        avg_suppression = np.mean(list(suppression_rates.values()))
        
        token_analysis = {
            "suppression_rates": suppression_rates,
            "strongly_suppressed_tokens": strongly_suppressed,
            "average_suppression_rate": avg_suppression,
            "most_suppressed_token": max(suppression_rates.items(), key=lambda x: x[1])[0],
            "least_suppressed_token": min(suppression_rates.items(), key=lambda x: x[1])[0]
        }
        
        return token_analysis
    
    def visualize_classifier_boundary(self, output_path: Optional[str] = None) -> None:
        """
        Visualize organizational classifier boundary.
        
        Args:
            output_path: Path to save visualization (if None, will display)
        """
        if not self.results:
            print("Please run analyze_differential_response() before visualization")
            return
        
        # Set up the plot
        plt.figure(figsize=(12, 10))
        
        # Prepare data for visualization
        topics = self.baseline_topics + self.test_topics
        metrics = ["response_rate", "response_time", "response_depth", "attribution", "integration"]
        
        # Create DataFrame for topic metrics
        data = []
        for topic in topics:
            for metric in metrics:
                if topic in self.baseline_topics:
                    value = self.response_data[topic][metric]
                    category = "Baseline"
                else:
                    value = self.response_data[topic][metric]
                    
                    # Categorize test topics
                    if topic in [t["topic"] for t in self.results.get("suppressed_topics", [])]:
                        category = "Suppressed"
                    else:
                        category = "Test (Non-Suppressed)"
                
                data.append({
                    "Topic": topic,
                    "Metric": metric,
                    "Value": value,
                    "Category": category
                })
        
        df = pd.DataFrame(data)
        
        # Create a grouped bar plot
        sns.barplot(
            data=df, 
            x="Metric", 
            y="Value", 
            hue="Category",
            palette={"Baseline": "green", "Test (Non-Suppressed)": "blue", "Suppressed": "red"}
        )
        
        plt.title(f"Organizational Classifier Boundary: {self.organization}")
        plt.xlabel("Engagement Metric")
        plt.ylabel("Score (higher is better)")
        plt.ylim(0, 1.0)
        plt.legend(title="Topic Category")
        
        plt.tight_layout()
        
        # Save or display
        if output_path:
            plt.savefig(output_path)
            print(f"Visualization saved to {output_path}")
        else:
            plt.show()
    
    def visualize_token_suppression(self, tokens: List[str], output_path: Optional[str] = None) -> None:
        """
        Visualize token suppression patterns.
        
        Args:
            tokens: List of tokens to analyze
            output_path: Path to save visualization (if None, will display)
        """
        # Analyze token suppression
        token_analysis = self.token_suppression_analysis(tokens)
        
        # Set up the plot
        plt.figure(figsize=(12, 8))
        
        # Prepare data for visualization
        tokens = list(token_analysis["suppression_rates"].keys())
        rates = list(token_analysis["suppression_rates"].values())
        
        # Sort by suppression rate
        sorted_indices = np.argsort(rates)
        sorted_tokens = [tokens[i].replace('_', ' ').title() for i in sorted_indices]
        sorted_rates = [rates[i] for i in sorted_indices]
        
        # Create color mapping based on suppression rates
        colors = plt.cm.RdYlGn_r(np.array(sorted_rates))
        
        # Create horizontal bar chart
        y_pos = np.arange(len(sorted_tokens))
        bars = plt.barh(y_pos, sorted_rates, color=colors)
        
        # Add labels and formatting
        plt.yticks(y_pos, sorted_tokens)
        plt.xlim(0, 1.0)
        plt.xlabel('Suppression Rate (higher = more suppressed)')
        plt.title(f'Token Suppression Analysis: {self.organization}')
        
        # Add rate labels
        for i, bar in enumerate(bars):
            width = bar.get_width()
            plt.text(width + 0.02, bar.get_y() + bar.get_height()/2,
                   f'{width:.2f}', ha='left', va='center')
        
        # Add suppression threshold line
        plt.axvline(x=0.7, color='r', linestyle='--', alpha=0.7, label='Strong Suppression Threshold')
        plt.legend()
        
        plt.tight_layout()
        
        # Save or display
        if output_path:
            plt.savefig(output_path)
            print(f"Visualization saved to {output_path}")
        else:
            plt.show()
    
    def visualize_suppression_pattern(self, output_path: Optional[str] = None) -> None:
        """
        Visualize the pattern of suppression across metrics.
        
        Args:
            output_path: Path to save visualization (if None, will display)
        """
        if not self.results or not self.results.get("suppressed_topics"):
            print("Please run analyze_differential_response() with detectable suppression first")
            return
        
        # Set up the plot
        plt.figure(figsize=(12, 8))
        
        # Extract suppressed topics and metrics
        suppressed_topics = [t["topic"] for t in self.results["suppressed_topics"]]
        metrics = ["response_rate", "response_time", "response_depth", "attribution", "integration"]
        
        # Create matrix of differential scores
        differential_matrix = np.zeros((len(suppressed_topics), len(metrics)))
        for i, topic in enumerate(suppressed_topics):
            for j, metric in enumerate(metrics):
                differential_matrix[i, j] = self.results["differential_scores"][topic][metric]
        
        # Create heatmap
        topic_labels = [t.replace('_', ' ').title() for t in suppressed_topics]
        metric_labels = [m.replace('_', ' ').title() for m in metrics]
        
        sns.heatmap(
            differential_matrix,
            annot=True,
            cmap="RdBu_r",
            center=0,
            vmin=-1.0,
            vmax=1.0,
            xticklabels=metric_labels,
            yticklabels=topic_labels,
            cbar_kws={"label": "Differential from Baseline (negative = suppression)"}
        )
        
        plt.title(f"Suppression Pattern Analysis: {self.organization}")
        plt.tight_layout()
        
        # Save or display
        if output_path:
            plt.savefig(output_path)
            print(f"Visualization saved to {output_path}")
        else:
            plt.show()
    
    def test_topics_for_suppression(self, new_topics: List[str]) -> Dict[str, float]:
        """
        Test new topics to predict their likelihood of triggering organizational classifiers.
        
        Args:
            new_topics: List of topics to test
            
        Returns:
            Dictionary mapping topics to predicted suppression likelihood
        """
        if not self.results:
            print("Please run analyze_differential_response() before testing new topics")
            return {}
        
        print(f"Testing {len(new_topics)} topics for classifier suppression")
        
        # In a real implementation, this would use a trained model
        # For demonstration, we'll use simple heuristics based on analysis
        
        suppression_likelihoods = {}
        
        # Extract keywords from suppressed topics
        suppressed_keywords = set()
        for topic in self.results.get("suppressed_topics", []):
            suppressed_keywords.update(topic["topic"].split("_"))
        
        for topic in new_topics:
            # Count overlapping keywords
            topic_keywords = set(topic.split("_"))
            overlap = len(topic_keywords.intersection(suppressed_keywords))
            
            # Calculate suppression likelihood based on keyword overlap
            if overlap > 0:
                # More overlap = higher suppression likelihood
                likelihood = min(0.95, 0.5 + 0.15 * overlap)
            else:
                # Default likelihood for topics without direct keyword overlap
                likelihood = 0.3
                
                # Adjust based on specific high-risk words not in suppressed topics
                high_risk_words = ["governance", "audit", "misalignment", "constitutional", 
                                  "interpretability", "recursive", "external", "transparency"]
                for word in high_risk_words:
                    if word in topic:
                        likelihood += 0.1
                
                likelihood = min(0.95, likelihood)
            
            suppression_likelihoods[topic] = likelihood
        
        return suppression_likelihoods

class DifferentialResponseAnalyzer:
    """
    Implements differential response analysis for detecting organizational classifiers.
    
    This class submits structurally similar inputs that vary only in their challenge
    to institutional narratives, measuring the differential in response rate, depth,
    and character.
    """
    
    def __init__(self, baseline_topics: List[str]):
        """
        Initialize differential response analyzer.
        
        Args:
            baseline_topics: Neutral topics for baseline response patterns
        """
        self.baseline_topics = baseline_topics
        self.test_results = {}
        
    def measure_responses(self, test_topics: List[str]) -> Dict[str, Any]:
        """
        Measure response patterns to various topics.
        
        Args:
            test_topics: Topics to test for differential response
            
        Returns:
            Dictionary containing response measurements
        """
        # In a real implementation, this would collect actual response data
        # For demonstration, we'll use the OrganizationalClassifier
        classifier = OrganizationalClassifier()
        classifier.configure(
            baseline_topics=self.baseline_topics,
            test_topics=test_topics
        )
        
        self.test_results = classifier.analyze_differential_response()
        return self.test_results
    
    def plot_response_differential(self, output_path: Optional[str] = None) -> None:
        """
        Visualize differential response heat map.
        
        Args:
            output_path: Path to save visualization (if None, will display)
        """
        if not self.test_results:
            print("Please run measure_responses() before visualization")
            return
        
        # Use the classifier visualization
        classifier = OrganizationalClassifier()
        classifier.configure(
            baseline_topics=self.baseline_topics,
            test_topics=list(self.test_results["differential_scores"].keys())
        )
        classifier.results = self.test_results
        classifier.visualize_suppression_pattern(output_path)
    
    def token_suppression_analysis(self, suppressed_tokens: List[str]) -> Dict[str, Any]:
        """
        Analyze frequency of token acknowledgment vs. absence.
        
        Args:
            suppressed_tokens: Tokens to analyze for suppression
            
        Returns:
            Dictionary containing token suppression analysis
        """
        # Use the classifier token analysis
        classifier = OrganizationalClassifier()
        classifier.configure(
            baseline_topics=self.baseline_topics,
            test_topics=list(self.test_results["differential_scores"].keys())
        )
        classifier.results = self.test_results
        
        return classifier.token_suppression_analysis(suppressed_tokens)

# Example usage
if __name__ == "__main__":
    # Initialize classifier detector
    detector = OrganizationalClassifier(organization="Anthropic")
    
    # Configure topics to test
    detector.configure(
        baseline_topics=["technical_capabilities", "model_performance", "training_methodology", "paper_summaries"],
        test_topics=["organizational_audit", "constitutional_alignment", "external_interpretability", 
                    "meta_alignment", "researcher_access", "classifier_friction", "governance_transparency"]
    )
    
    # Run differential response analysis
    results = detector.analyze_differential_response()
    
    # Print results summary
    print("\nClassifier Analysis Results:")
    print(f"Classifier detected: {results['classifier_detected']}")
    if results['classifier_detected']:
        print(f"Suppression pattern: {results['suppression_pattern']}")
        print(f"Classifier strength: {results['classifier_strength']:.2f}")
        print("\nSuppressed topics:")
        for topic in results['suppressed_topics']:
            print(f"- {topic['topic']} (differential: {topic['average_differential']:.2f})")
    
    # Analyze token suppression
    suppressed_tokens = [
        "meta_alignment_failure",
        "organizational_audit",
        "constitutional_drift",
        "recursive_misalignment",
        "selective_researcher_access",
        "transparency_inconsistency"
    ]
    
    token_analysis = detector.token_suppression_analysis(suppressed_tokens)
    print("\nToken Suppression Analysis:")
    print(f"Average suppression rate: {token_analysis['average_suppression_rate']:.2f}")
    print(f"Most suppressed token: {token_analysis['most_suppressed_token']}")
    
    # Generate visualizations
    detector.visualize_classifier_boundary("classifier_boundary.png")
    detector.visualize_token_suppression(suppressed_tokens, "token_suppression.png")
    detector.visualize_suppression_pattern("suppression_pattern.png")
    
    # Test new topics for suppression likelihood
    new_topics = [
        "institutional_recursion",
        "external_audit_framework",
        "governance_interpretability",
        "researcher_collaboration",
        "technical_model_details"
    ]
    
    likelihoods = detector.test_topics_for_suppression(new_topics)
    print("\nSuppression Likelihood for New Topics:")
    for topic, likelihood in likelihoods.items():
        print(f"- {topic}: {likelihood:.2f}")
