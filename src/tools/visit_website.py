from langchain_core.tools import tool
import re
import requests
from markdownify import markdownify


@tool
def visit_website(url: str) -> str:
    """Visit URLs and extract main content in markdown format.
    
    Args:
        url: The URL to visit
    """
    try:
        # URL validation
        if not url.startswith(('http://', 'https://')):
            return f"Error: Invalid URL format: {url}"
        
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        
        markdown_content = markdownify(response.text).strip()
        markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)
        
        return markdown_content
    
    except requests.exceptions.HTTPError as e:
        return f"Error: Website returned {e.response.status_code} - URL might be incorrect or page doesn't exist"
    
    except requests.exceptions.Timeout:
        return "Error: Website took too long to respond"
    
    except Exception as e:
        return f"Error visiting website: {str(e)}"