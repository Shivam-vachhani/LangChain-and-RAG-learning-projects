# 🦜 LangChain – Day 11: Tools

Day 11 introduced **Tools** — how to give an LLM the ability to call real functions and interact with the outside world. This is the foundation of agents.

---

## 🔧 What is a Tool?
In LangChain, any Python function decorated with `@tool` becomes callable by an LLM. The docstring is the description the model reads to decide when and how to use it — so writing clear docstrings is actually important here.

## 🧮 Toolkit (Math)
Built a basic `MathToolKit` class wrapping four arithmetic tools (`add`, `subtract`, `multiply`, `divide`) with zero-division handling. Explored tool metadata — `.name`, `.description`, `.args`, `.args_schema` — which shows exactly what the model sees when it decides to use a tool.

## 🌐 Web Search Tool
Built a real-time web search tool using `DuckDuckGo` (`ddgs`) — searches the web and returns formatted title + URL + snippet results. The model can call this whenever it needs fresh information beyond its training data.

## 💱 Currency Converter Agent
The most complete example — built a two-tool agent using `create_agent`:
- `get_conversion_rate` — hits the Frankfurter API to fetch live exchange rates.
- `convert` — multiplies the base value by the rate.

The agent figures out on its own that it needs to call `get_conversion_rate` first, then pass the result to `convert` — it chains the tools together without being explicitly told to. Also tried `.stream()` to watch the agent reason and act step by step.

---

## 💡 Key Insight
The LLM doesn't run the tools — it just decides which ones to call and with what arguments. LangChain executes them and feeds the result back. That loop is what makes an agent.

---

*Stack: LangChain · OpenAI · DuckDuckGo · Frankfurter API*