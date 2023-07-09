import requests
import json
url = "https://michaelgathara.com/api/python-challenge"
response = requests.get(url)
challenges = response.json()
print(challenges)
results = []

for challenge in challenges:
    problem = challenge['problem']
    # Extract the arithmetic expression by removing the question mark
    expression = problem.rstrip('?')
    
    # Evaluate the arithmetic expression using the eval() function
    result = eval(expression)
    
    # Create a new dictionary with the problem ID and its result
    problem_result = {'id': challenge['id'], 'result': result}
    
    # Append the dictionary to the results list
    results.append(problem_result)

# Print the results
for problem_result in results:
    print(f"Problem ID: {problem_result['id']}, Result: {problem_result['result']}")