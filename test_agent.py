import time
from agent import run_agent

TESTS = [
    {
        "question": "Is today good for harvesting?",
        "expect_tool": True,
    },
    {
        "question": "What does plucking mean in tea farming?",
        "expect_tool": False,
    },
    {
        "question": "Give me one tip for training new pluckers.",
        "expect_tool": False,
    },
]

lines = ["# Test results\n"]
passed = 0

for number, test in enumerate(TESTS, start=1):
    question = test["question"]
    print(f"Test {number}: {question}")

    answer, tools_used = run_agent(question)

    used_tool = len(tools_used) > 0
    answered = not answer.startswith("Sorry")
    ok = (used_tool == test["expect_tool"]) and answered
    if ok:
        passed += 1

    status = "PASS" if ok else "FAIL"
    print(f"   Tool used: {tools_used} -> {status}")
    print(f"   Answer: {answer}\n")

    lines.append(f"## Test {number}: {question}")
    lines.append(f"- Tool expected: {test['expect_tool']}")
    lines.append(f"- Tools used: {tools_used}")
    lines.append(f"- Result: {status}")
    lines.append(f"- Answer: {answer}\n")

    time.sleep(2)

print(f"{passed} of {len(TESTS)} tests passed.")

with open("test_results.md", "w", encoding="utf-8") as file:
    file.write("\n".join(lines))
print("Results saved to test_results.md")