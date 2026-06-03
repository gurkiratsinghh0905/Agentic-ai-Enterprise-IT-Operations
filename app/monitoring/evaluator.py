def evaluate_response(response: str) -> dict:
    """Simple quality evaluator — scores response based on length and content."""
    score = min(10, max(1, len(response.split()) // 20))
    return {"quality_score": score}
