def get_ai_response(prompt):
    """
    Temporary safe function for testing
    """

    if not prompt:
        raise ValueError("Empty prompt")

    return {
        "response": f"Mock response for: {prompt}"
    }