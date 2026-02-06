"""
GitHub Tool for searching repositories and fetching information
"""
import os
import requests
from typing import Dict, Any, List
from dotenv import load_dotenv

load_dotenv()


class GitHubTool:
    def __init__(self):
        self.token = os.getenv("GITHUB_TOKEN")
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json"
        }
        if self.token:
            self.headers["Authorization"] = f"token {self.token}"
    
    def search_repositories(
        self, 
        query: str, 
        sort: str = "stars", 
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """
        Search GitHub repositories
        
        Args:
            query: Search query (e.g., "python machine learning")
            sort: Sort by (stars, forks, updated)
            limit: Number of results to return
        
        Returns:
            List of repository information
        """
        try:
            url = f"{self.base_url}/search/repositories"
            params = {
                "q": query,
                "sort": sort,
                "order": "desc",
                "per_page": limit
            }
            
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            repositories = []
            
            for repo in data.get("items", []):
                repositories.append({
                    "name": repo["name"],
                    "full_name": repo["full_name"],
                    "description": repo.get("description", "No description"),
                    "stars": repo["stargazers_count"],
                    "forks": repo["forks_count"],
                    "language": repo.get("language", "Unknown"),
                    "url": repo["html_url"],
                    "updated_at": repo["updated_at"]
                })
            
            return repositories
        
        except requests.exceptions.RequestException as e:
            raise Exception(f"GitHub API Error: {str(e)}")
    
    def get_repository_info(self, owner: str, repo: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific repository
        
        Args:
            owner: Repository owner
            repo: Repository name
        
        Returns:
            Repository details
        """
        try:
            url = f"{self.base_url}/repos/{owner}/{repo}"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            return {
                "name": data["name"],
                "full_name": data["full_name"],
                "description": data.get("description", "No description"),
                "stars": data["stargazers_count"],
                "forks": data["forks_count"],
                "language": data.get("language", "Unknown"),
                "url": data["html_url"],
                "topics": data.get("topics", []),
                "created_at": data["created_at"],
                "updated_at": data["updated_at"]
            }
        
        except requests.exceptions.RequestException as e:
            raise Exception(f"GitHub API Error: {str(e)}")


# Singleton instance
github_tool = GitHubTool()
