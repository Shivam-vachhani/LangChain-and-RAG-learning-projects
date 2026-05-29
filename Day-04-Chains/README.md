# 🦜 LangChain – Day 04: Chains

Day 4 was about **advanced chaining patterns** — moving beyond simple linear chains to parallel execution and conditional branching logic.

---

## ⚡ Parallel Chains
Built a pipeline that runs two tasks **simultaneously** on the same input using `RunnableParallel` — one model generates study notes, another generates quiz questions, both from the same WWII text passage. Once both finish, their outputs merge into a final combined document via a third prompt. Two different models were used in parallel (OpenAI + HuggingFace DeepSeek), which shows how LangChain is model-agnostic within the same chain.

## 🔀 Conditional Chains
Built a feedback classifier that **routes** to different chains based on the result using `RunnableBranch`. First, a structured model classifies the feedback as positive or negative — then the branch picks the matching response template. A fallback `RunnableLambda` handles anything that doesn't match. It's essentially an if-else block wired into a chain.

## 🔍 Chain Visualization
Used `chain.get_graph().print_ascii()` to print a visual map of how the chain is wired — useful for debugging complex multi-step pipelines and understanding the execution flow at a glance.

---

*Stack: LangChain · OpenAI · HuggingFace · Pydantic*